import subprocess
import time
import os
import datetime
import search as sch
import files_gestion as fg
import time

LOGICIEL=fg.get_logiciel()
INTERNET_LINK=fg.get_link()
SEQUENCE_CESI=["séquence saisie", "séquence une"]
SEQUENCE_CCTL=["séquence cctl", "séquence une"]

LIEN=[]
LIEN=LOGICIEL+INTERNET_LINK
 


def pathMaker(audio):
    audio_list=audio.split()

    pathBegin=r"C:\Users\arthu\Desktop\Alice Project\executable programs\\"

    for word in audio_list:
        print(word)
        if word in LIEN:
            pathMiddle=word

    if sch.wordSearch(audio, INTERNET_LINK):
        pathEnd=".url"
        execute(pathBegin, pathMiddle, pathEnd)
    elif sch.wordSearch(audio, LOGICIEL):
        pathEnd=".lnk"
        execute(pathBegin, pathMiddle, pathEnd)

    i=0
    while i<len(SEQUENCE_CESI):
        if audio.count(SEQUENCE_CESI[i])>0:
            SEQU_CESI(pathBegin)
        i+=1

    while i<len(SEQUENCE_CCTL):
        if audio.count(SEQUENCE_CCTL[i])>0:
            SEQU_CCTL(pathBegin)
        i+=1

def SEQU_CESI(pathBegin):
    execute(pathBegin, "ent", ".url")
    time.sleep(1)
    execute(pathBegin, "discorde", ".lnk")
    time.sleep(1)
    execute(pathBegin, "moodle", ".url")

def SEQU_CCTL(pathBegin):
    execute(pathBegin, "cctl", ".url")
    time.sleep(1)
    execute(pathBegin, "ent", ".url")
    time.sleep(1)
    execute(pathBegin, "discorde", ".lnk")

def execute(pathBegin, pathMiddle, pathEnd):
    path=pathBegin+pathMiddle+pathEnd
    os.startfile(path)