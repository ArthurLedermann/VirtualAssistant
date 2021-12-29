import os
import sys
import interface as ihm
import he_ho as hh


def reload(audio):
    if audio == "recharge alice" or audio == "alice recharge":
        os.startfile(r"C:\Users\arthu\Desktop\Alice Project\executable programs\Alice.lnk")
        sys.exit(1)

def close(audio):
    if audio == "stoppe alice" or audio == "alice stop":
        hh.pompom()
        sys.exit(1)

def wait(audio):
    if audio == "attends alice" or audio == "alice attend":
            ihm.speak("mise en veille")
            while audio != "alice réveil" and audio!= "réveil alice":
                os.system("cls")
                print("Zzz... Zzz... Zzzz...")
                audio=ihm.listen()

def stopComputer(audio):
    if audio == "alice code coloquinte":
        hh.pompom()
        os.system("shutdown /s /t 1")

def startAlice(audio):
    if audio == "alice start":
        os.startfile(r"C:\Users\arthu\Desktop\Alice Project\executable programs\Alice.lnk")

