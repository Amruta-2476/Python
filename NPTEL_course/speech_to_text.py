# to install write in terminal:
# pip install SpeechRecognition
# then create an audio file with microphone and convert it to .wav extension

import speech_recognition as sr
AUDIO_FILE = ("amruta_speek.wav")
# use the audio file as the audio source
# initialize the recognizer
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    # reads the audio file
try :
    print("The audio file contains: " + r.recognize_google(audio))  # print the text
except sr.UnknownValueError:
    #not recognize the audio
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print("Could not get results from Google Speech Recognition")