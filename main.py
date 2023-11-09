# recognize_audio.py
import speech_recognition as sr
import io
import sounddevice as sd
import numpy as np
import pickle

def recognize_audio(model, audio_data, sample_rate):
    recognizer = sr.Recognizer()

    try:
        audio_data = audio_data.tobytes()
        audio = sr.AudioData(audio_data, sample_rate=sample_rate, sample_width=2)  # Assuming 16-bit audio
        text = model.recognize_google(audio, language="en-US", show_all=False)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Load the trained model using pickle
model_filename = "trained_model/custom_model.pkl"
with open(model_filename, "rb") as model_file:
    custom_model = pickle.load(model_file)

# Capture audio from the microphone
sample_rate = 44100  # Adjust as needed
duration = 5  # seconds

print("Recording... Speak now.")
audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype=np.int16)
sd.wait()

# Use the trained model for recognition
recognized_text = recognize_audio(custom_model, audio_data, sample_rate)

if recognized_text:
    print(f"Recognized Text: {recognized_text}")
else:
    print("Recognition failed.")
