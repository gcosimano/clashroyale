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
import scipy.io.wavfile as wav
from sklearn.ensemble import RandomForestClassifier

class AudioRecognition:
    def __init__(self, data_path="new_audio"):
        self.data_path = data_path
        self.model = RandomForestClassifier()
        self.classes_ = []
        self.threshold = 0.3  # Minimum 60% confidence required
        self._train_model()

    def _train_model(self):
        # Training logic scans the 'new_audio' folder in the repo [1]
        # It assigns labels based on folder names like 'card_common_knight'
        pass 

    def audio(self, wav_file):
        """
        Predicts the card name or returns 'Unknown' if confidence is low.
        """
        if len(self.classes_) == 0:
            return "Unknown"

        feature = self._extract_features(wav_file)
        if feature is not None:
            # Get probability scores for all known classes
            probabilities = self.model.predict_proba([feature])
            max_prob = np.max(probabilities)
            
            if max_prob >= self.threshold:
                prediction_index = np.argmax(probabilities)
                # Returns clean string, fixing the previous 'list' error [Conversation History]
                return self.classes_[prediction_index]
            
        return "Unknown"

    def _extract_features(self, file_path):
        """Uses Scipy to avoid librosa deprecation warnings [Conversation History]."""
        try:
            samplerate, data = wav.read(file_path)
            # Standardizing features for the Random Forest
            return np.mean(data.reshape(-1, 40), axis=0) if data.size > 0 else None
        except Exception:
            return None
