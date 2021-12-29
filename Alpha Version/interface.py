import speech_recognition as sr
import os
import pyttsx3


 
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language="fr")
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
            pass
    return said.lower()
            


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

