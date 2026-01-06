import os
import librosa
import numpy as np 
from sklearn.ensemble import RandomForestClassifier

class AudioRecognition:
    """
    A class to recognize Clash Royale card sounds using AI.
    Trained on audio files located in the 'new_audio' directory.
    """
    
    def __init__(self, data_path="new_audio"):
        # The new_audio folder is located in the root directory [1]
        self.data_path = data_path
        self.model = RandomForestClassifier(n_estimators=100)
        self.classes_ = []
        self._train_from_repository()

    def _extract_features(self, file_path):
        """
        External Knowledge: Uses librosa to extract Mel-frequency 
        cepstral coefficients (MFCCs) as features for the AI model.
        """
        try:
            # Load the audio file (supports mp3, ogg, wav)
            audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
            mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
            # Flatten features into a 1D array for the classifier
            return np.mean(mfccs.T, axis=0)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None

    def _train_from_repository(self):
        """
        Scans the new_audio directory for training data [1].
        Assumes subfolders are named after the Cards (e.g., 'Giant', 'Minions').
        """
        features = []
        labels = []
        
        if not os.path.exists(self.data_path):
            print(f"Directory {self.data_path} not found.")
            return

        for card_name in os.listdir(self.data_path):
            card_folder = os.path.join(self.data_path, card_name)
            if os.path.isdir(card_folder):
                for file_name in os.listdir(card_folder):
                    file_path = os.path.join(card_folder, file_name)
                    data = self._extract_features(file_path)
                    if data is not None:
                        features.append(data)
                        labels.append(card_name)
        
        if features:
            self.model.fit(X=np.array(features), y=np.array(labels))
            self.classes_ = self.model.classes_
            print(f"AI Training Complete. Identified cards: {list(self.classes_)}")

    def audio(self, mp3_file):
        """
        Accepts an mp3 file and returns the name of the Card that created it.
        """
        if not self.classes_:
            return "Model not trained. Please check the new_audio directory."
            
        feature = self._extract_features(mp3_file)
        if feature is not None:
            # External Knowledge: Predict the class with the highest probability
            prediction = self.model.predict([feature])
            return prediction
        return "Audio file could not be processed."

# Example of how this integrates with the existing Python environment [2]:
# recognizer = AudioRecognition()
# result = recognizer.audio("path_to_unknown_card_sound.mp3")
# print(f"Card identified: {result}")