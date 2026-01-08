import unittest
import os
from AudioRecognition import AudioRecognition

class TestAudioRecognition(unittest.TestCase):
    # Tracking for overall accuracy summary
    results = {"passed": 0, "total": 0}
    
    @classmethod
    def setUpClass(cls):
        """Initializes AI and maps card folders to the first available .wav file."""
        cls.recognizer = AudioRecognition(data_path="new_audio")
        cls.base_path = "new_audio"
        
        # Verified prefixes from your repository history [5, Conversation History]
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
                files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]
                if files:
                    # FIX: Access the first element of the list (files) to get a string
                    cls.test_files[folder] = os.path.join(folder_path, files)

    def run_recognition(self, folder_name):
        """Helper to execute the test and log results for accuracy summary."""
        if folder_name not in self.test_files:
            self.skipTest(f"No .wav file found for {folder_name} in new_audio.")
            
        self.results["total"] += 1
        file_to_test = self.test_files[folder_name]
        result = self.recognizer.audio(file_to_test)
        
        if result == folder_name:
            self.results["passed"] += 1
            return True
        return False

    def test_knight_recognition(self):
        self.assertTrue(self.run_recognition('card_common_knight'))

    def test_archer_recognition(self):
        self.assertTrue(self.run_recognition('card_common_archer'))

    def test_minion_recognition(self):
        self.assertTrue(self.run_recognition('card_common_minion'))

    def test_musketeer_recognition(self):
        self.assertTrue(self.run_recognition('card_evolution_musketeer'))

    def test_unknown_rejection(self):
        """Ensures non-training sounds from Clash-Royale-Sound-Effects return 'Unknown'."""
        self.results["total"] += 1
        unknown_dir = "Clash-Royale-Sound-Effects"
        if os.path.exists(unknown_dir):
            files = [f for f in os.listdir(unknown_dir) if f.endswith('.wav')]
            if files:
                # FIX: Also ensure this uses index  to avoid the same TypeError
                result = self.recognizer.audio(os.path.join(unknown_dir, files))
                if result == "Unknown":
                    self.results["passed"] += 1
                self.assertEqual(result, "Unknown")
        else:
            self.results["total"] -= 1
            self.skipTest("Clash-Royale-Sound-Effects folder not found.")

    @classmethod
    def tearDownClass(cls):
        """Prints the accuracy report after all tests are completed."""
        total = cls.results["total"]
        passed = cls.results["passed"]
        accuracy = (passed / total * 100) if total > 0 else 0
        
        print("\n" + "="*40)
        print("SUMMARY OF OVERALL ACCURACY")
        print("="*40)
        print(f"Final Score: {accuracy:.2f}%")
        print(f"Correct: {passed} | Total Tests: {total}")
        print("="*40)

if __name__ == '__main__':
    unittest.main()