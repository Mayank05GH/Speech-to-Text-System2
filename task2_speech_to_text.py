!pip install SpeechRecognition
from google.colab import files
uploaded = files.upload()

sample voice.mp3(audio/mpeg) - 21213 bytes, last modified: 6/21/2025 - 100% done
Saving sample voice.mp3 to sample voice.mp3

!pip install pydub
!apt-get install ffmpeg
from pydub import AudioSegment

# Load your MP3 file
audio = AudioSegment.from_mp3("sample voice.mp3")

# Export as WAV
audio.export("sample_voice.wav", format="wav")

print("Converted MP3 to WAV successfully!")

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile('sample_voice.wav') as source:
    audio_data = recognizer.record(source)

text = recognizer.recognize_google(audio_data)

print("=== Transcribed Text ===")
print(text)

# Save to file
with open("transcription_output.txt", "w") as f:
    f.write(text)
from google.colab import files

files.download("transcription_output.txt")
