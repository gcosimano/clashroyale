import unittest
import os
import scipy.io.wavfile as wav # External library for stable audio loading
from AudioRecognition import AudioRecognition

class TestAudioRecognition(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """
        Initializes the recognition engine.
        The data_path points to the 'new_audio' folder in the root [1].
        """
        cls.recognizer = AudioRecognition(data_path="new_audio")
        
        # Verified card names from your terminal output [Conversation History]
        cls.test_cards = [
            'card_common_archer', 
            'card_common_knight', 
            'card_common_minion', 
            'card_common_goblins', 
            'card_evolution_musketeer'
        ]

    def test_scipy_compatibility(self):
        """
        Verifies that a sample file can be read using Scipy without errors.
        This confirms the environment is ready for recognition.
        """
        # Using a verified file path from the repository [Conversation History]
        sample_path = "new_audio/card_common_knight/knight_deploy_31111.wav"
        
        if os.path.exists(sample_path):
            # This is an external method from Scipy not found in the source [2]
            samplerate, data = wav.read(sample_path)
            self.assertGreater(samplerate, 0, "Scipy failed to read the audio sample.")
        else:
            self.skipTest("Sample audio file not found in 'new_audio'.")

    def test_knight_recognition_accuracy(self):
        """
        Tests if the AI correctly identifies the Knight deployment sound.
        """
        test_file = "new_audio/card_common_knight/knight_deploy_31111.wav"
        if os.path.exists(test_file):
            result = self.recognizer.audio(test_file)
            # The result must be a clean string, not a list ['card_common_knight'] [Conversation History]
            self.assertEqual(result, "card_common_knight")

    def test_all_prefixed_cards_trained(self):
        """
        Ensures the AI has successfully cataloged the prefixed folder names [Conversation History].
        """
        for card in self.test_cards:
            with self.subTest(card=card):
                self.assertIn(card, self.recognizer.classes_, f"AI failed to train on {card}.")

if __name__ == '__main__':
    unittest.main()