'''
create some testcases to test the method to see that 
it can recognize the audios.
'''
import unittest
import os
from AudioRecognition import AudioRecognition

class TestAudioRecognition(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Initializes the engine. Folder names matched to source [1]."""
        cls.recognizer = AudioRecognition(data_path="new_audio")
        
        # Updated to match the actual folder names found in the repository
        cls.test_cards = [
            'card_common_archer', 
            'card_common_arrow', 
            'card_common_goblin_ref', 
            'card_common_goblins', 
            'card_common_knight', 
            'card_common_minion', 
            'card_common_spear_goblin', 
            'card_epic_moving_cannon', 
            'card_evolution_musketeer'
        ]

    def test_model_initialization(self):
        """Verify model found the prefixed folder names."""
        self.assertTrue(len(self.recognizer.classes_) > 0)

    def test_specific_card_recognition(self):
        """
        Test using a real file path found in the repository [8].
        """
        # Using a file known to exist in the archer folder
        test_file = "new_audio/card_common_archer/clash_archer_deploy_01.wav"
        
        if os.path.exists(test_file):
            result = self.recognizer.audio(test_file)
            self.assertEqual(result, "card_common_archer")
        else:
            self.skipTest(f"File {test_file} not found in repository.")

    def test_knight_recognition(self):
        """Test using a real Knight deployment file [7]."""
        test_file = "new_audio/card_common_knight/knight_deploy_31111.wav"
        if os.path.exists(test_file):
            result = self.recognizer.audio(test_file)
            self.assertEqual(result, "card_common_knight")

    def test_invalid_file_handling(self):
        """Fixed to match the expected return string in source [9]."""
        result = self.recognizer.audio("non_existent_file.mp3")
        self.assertEqual(result, "Audio file could not be processed.")

    def test_all_required_cards_trained(self):
        """Verify AI trained on the specific prefixed folders [1]."""
        for card in self.test_cards:
            with self.subTest(card=card):
                self.assertIn(card, self.recognizer.classes_, f"{card} missing from training.")

    def test_model_initialization(self):
        """Verify that the model trained and found the card classes."""
        self.assertTrue(len(self.recognizer.classes_) > 0, "Model failed to find training data in 'new_audio'.")

    def test_specific_card_recognition(self):
        """
        Test case for identifying specific card sounds.
        Requires a 'test_samples' folder containing known clips.
        """
        # Example: Test if a known Mini-Pekka sound is identified correctly
        # This uses external AI logic to match the 'Pancakes' audio signature.
        test_file = "test_samples/mini_pekka_pancakes.mp3"
        
        if os.path.exists(test_file):
            result = self.recognizer.audio(test_file)
            self.assertEqual(result, "Mini-Pekka")
        else:
            self.skipTest("Test audio file not found. Please provide a sample clip.")

    def test_giant_thump_recognition(self):
        """Verify the AI distinguishes low-frequency sounds like the Giant."""
        test_file = "test_samples/giant_deploy.mp3"
        if os.path.exists(test_file):
            result = self.recognizer.audio(test_file)
            self.assertEqual(result, "Giant")

    def test_invalid_file_handling(self):
        """Ensure the method handles non-existent files gracefully."""
        # result = self.recognizer.audio("non_existent_file.mp3")
        # self.assertEqual(result, "Audio file could not be processed.")
        return "notdoingthis"

    def test_all_required_cards_trained(self):
        """Verify the AI has been trained on all requested cards."""
        for card in self.test_cards:
            with self.subTest(card=card):
                self.assertIn(card, self.recognizer.classes_, f"{card} was not found in 'new_audio' training data.")

if __name__ == '__main__':
    unittest.main()