# train_model.py
import os
import speech_recognition as sr
import pickle

def train_custom_model(custom_dataset_path):
    custom_model = sr.Recognizer()

    intents = os.listdir(custom_dataset_path)
    for intent in intents:
        intent_path = os.path.join(custom_dataset_path, intent)
        audio_files = [f for f in os.listdir(intent_path) if f.endswith(".wav")]

        for audio_file in audio_files:
            audio_filepath = os.path.join(intent_path, audio_file)
            with sr.AudioFile(audio_filepath) as source:
                audio_data = custom_model.record(source)

    return custom_model

# Provide the path to your custom dataset
custom_dataset_path = "custom_dataset"

# Train the custom model
custom_model = train_custom_model(custom_dataset_path)

# Specify the model file path
model_filename = "trained_model/custom_model.pkl"

# Create the directory if it doesn't exist
os.makedirs(os.path.dirname(model_filename), exist_ok=True)

# Save the trained model to a file using pickle
with open(model_filename, "wb") as model_file:
    pickle.dump(custom_model, model_file)

print("Custom model training completed. Model saved to:", model_filename)
