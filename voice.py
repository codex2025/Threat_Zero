import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import speech_recognition as sr

fs = 44100  # Sample rate
seconds = 5  # Duration

print("Recording for 5 seconds...")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()

write('output.wav', fs, myrecording)
print("Recording saved as output.wav")

# Recognizing speech from recorded file
r = sr.Recognizer()
with sr.AudioFile('output.wav') as source:
    audio = r.record(source)

try:
    print("Converting speech to text...")
    text = r.recognize_google(audio, language='en-IN')
    print("You said:", text)

except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
