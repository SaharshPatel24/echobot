import speech_recognition as sr
import os

def capture_and_save_audio(intent, attempt):
    recognizer = sr.Recognizer()

    print(f"Attempt {attempt}: Please say '{intent}'.")
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)

        # Create the directory if it doesn't exist
        directory_path = os.path.join("custom_dataset", intent)
        os.makedirs(directory_path, exist_ok=True)

        # Save the captured audio as a WAV file
        wav_filename = f"{intent}_{attempt}.wav"
        wav_filepath = os.path.join(directory_path, wav_filename)
        with open(wav_filepath, "wb") as wav_file:
            wav_file.write(audio.get_wav_data())

        print(f"Audio file '{wav_filepath}' saved successfully.")

    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Words or phrases you want to capture
intents = ["move_forward", "turn_left", "turn_right", "stop"]

# Number of attempts for each word
attempts = 2

# Generate audio samples for each intent
for intent in intents:
    for attempt in range(1, attempts + 1):
        capture_and_save_audio(intent, attempt)

        # Listen for confirmation
        confirmation = input("Did you say the correct word? (yes/no): ")
        if confirmation.lower() != "yes":
            print("Please try again.")

print("Audio samples captured successfully.")
