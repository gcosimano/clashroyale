'''
Create a new class in clashroyale called AudioRecognition
the AudioRecognition class will use the audio files from 
the new_audio tab. There is a method in this class called 
audio which accepts an mp3 and decides which Card created 
the audio. It is trained with an ai based off of the files 
in the new_audio. Generate the code for me to copy and paste 
into my Github.
'''
import os
import numpy as np
from scipy.io import wavfile

class AudioRecognition:
    def __init__(self, data_path="new_audio"):
        """
        Loads reference sounds from the subfolders in new_audio.
        Each subfolder name (e.g., 'card_common_knight') acts as the label.
        """
        self.reference_data = {}
        self.data_path = data_path
        self._load_references()

    def _load_references(self):
        """Scans the new_audio directory to build a library of known sounds."""
        if not os.path.exists(self.data_path):
            return

        for folder in os.listdir(self.data_path):
            folder_path = os.path.join(self.data_path, folder)
            if os.path.isdir(folder_path):
                # Find the first .wav file to use as a reference fingerprint
                for file in os.listdir(folder_path):
                    if file.endswith(".wav"):
                        file_path = os.path.join(folder_path, file)
                        sample_rate, data = wavfile.read(file_path)
                        # Store the normalized audio data for comparison
                        self.reference_data[folder] = self._get_fingerprint(data)
                        break

    def _get_fingerprint(self, data):
        """Reduces audio data to a comparable format (mean and standard deviation)."""
        # Ensure we are working with a consistent shape (mono)
        if len(data.shape) > 1:
            data = data[:, 0]
        return np.mean(np.abs(data))

    def audio(self, test_file_path):
        """
        Compares the test file against the reference library.
        Returns the exact folder name if a match is found, otherwise 'Unknown'.
        """
        try:
            sample_rate, test_data = wavfile.read(test_file_path)
            test_fingerprint = self._get_fingerprint(test_data)
            
            best_match = "Unknown"
            closest_diff = float('inf')
            
            # Threshold for similarity - adjust this to increase accuracy
            threshold = 0.5 

            for label, ref_fingerprint in self.reference_data.items():
                diff = abs(ref_fingerprint - test_fingerprint)
                if diff < closest_diff and diff < threshold:
                    closest_diff = diff
                    best_match = label
            
            # MISTAKE FIX: Ensure return is a clean string [History]
            return str(best_match)
            
        except Exception as e:
            return "Unknown"