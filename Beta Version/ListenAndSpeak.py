import speech_recognition as sr
import pyttsx3 as pytts
import os

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language="fr")

        except Exception as e:
            pass

    return said.lower()
            
            
def speak(text):
    engine = pytts.init()
    engine.say(text)
    engine.runAndWait()