import unittest
import os
# AudioRecognition class as defined in repository structure [1, 2]
from AudioRecognition import AudioRecognition

class TestingAudio(unittest.TestCase):
    # Part c) Tracking variables for the overall accuracy summary
    results = {"passed": 0, "total": 0}
    
    @classmethod
    def setUpClass(cls):
        """Initializes the AI and identifies specific test files in 'new_audio'."""
        # Using the verified 'new_audio' directory [1]
        cls.recognizer = AudioRecognition(data_path="new_audio")
        cls.base_path = "new_audio"
        
        # Folder names verified from previous terminal logs and repository structure [1]
        cls.target_folders = [
            'card_common_knight', 
            'card_common_archer', 
            'card_common_minion', 
            'card_common_goblins', 
            'card_evolution_musketeer'
        ]
        
        cls.test_files = {}
        for folder in cls.target_folders:
            folder_path = os.path.join(cls.base_path, folder)
            if os.path.exists(folder_path):
                # We iterate to find the first .wav and store it as a STRING immediately
                for filename in os.listdir(folder_path):
                    if filename.endswith('.wav'):
                        # MISTAKE FIX: 'filename' is a string. 
                        # This avoids passing a 'list' to os.path.join.
                        cls.test_files[folder] = os.path.join(folder_path, filename)
                        break 

    def run_recognition(self, test_path, expected_label):
        """Helper to process tests and track accuracy for Part c."""
        self.results["total"] += 1
        
        # AudioRecognition must return a string for comparison [History]
        result = self.recognizer.audio(test_path)
        
        if str(result) == expected_label:
            self.results["passed"] += 1
            return True
        return False

    # Part a) recognize and identify audios from new_audio
    def test_known_audio_recognition(self):
        """Tests identifying specific cards from the new_audio folders."""
        for folder, file_path in self.test_files.items():
            with self.subTest(card=folder):
                # Verifies that the AI identifies the folder name correctly
                self.assertTrue(self.run_recognition(file_path, folder))

    # Part b) recognize audios from Clash-Royale-Sound-Effects as unknown
    def test_unknown_audio_recognition(self):
        """Tests that external sound effects are labeled as 'Unknown'."""
        unknown_dir = "Clash-Royale-Sound-Effects"
        if os.path.exists(unknown_dir):
            found_unknown = False
            for filename in os.listdir(unknown_dir):
                if filename.endswith('.wav'):
                    test_path = os.path.join(unknown_dir, filename)
                    self.assertTrue(self.run_recognition(test_path, "Unknown"))
                    found_unknown = True
                    break # Test one sample
            if not found_unknown:
                return False
                self.results["total"] -= 1
                self.skipTest("No .wav files found in Clash-Royale-Sound-Effects.")
        else:
            return False
            self.skipTest("Clash-Royale-Sound-Effects folder not found.")

    # Part c) print a summary of the AI's accuracy
    @classmethod
    def tearDownClass(cls):
        """Calculates and prints the final model performance report [2]."""
        total = cls.results["total"]
        passed = cls.results["passed"]
        accuracy = (passed / total * 100) if total > 0 else 0
        
        print("\n" + "="*40)
        print("FINAL AI ACCURACY REPORT")
        print("="*40)
        print(f"Total Tests Run: {total}")
        print(f"Correct Identifications: {passed}")
        print(f"Overall Model Accuracy: {accuracy:.2f}%")
        print("="*40)

if __name__ == '__main__':
    unittest.main()