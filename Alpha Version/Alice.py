import os
import interface as ihm
import execute as exe
import search as sch
import research as rsch
import close
import files_gestion as fg
import shortcut as sc
import ppc
import he_ho as hh
import AsciiPictures as Asci

pathClub=r"C:\Users\arthu\Desktop\Alice Project\ClubBall.jpg"
pathKawaii=r"C:\Users\arthu\Desktop\Alice Project\Kawaii.jpg"


WAKE="alice"

ouverture=["lance", "lances", "lancer", "ouvre", "ouvre", "ouvrir", "éxecute", "éxecutes", "éxcuter"]
recherche=["recherche", "recherches", "rechercher", "regarde", "regarder"]
creer=["raccourci", "shortcut", "lien"]

COMMANDS=[]
COMMANDS.append(ouverture)
COMMANDS.append(recherche)
COMMANDS.append(creer)


def run():
    hh.eh_oh()
    while True:
        os.system("cls")
        Asci.AsciiClub(pathKawaii)
        audio = ihm.listen()

        close.wait(audio)
        close.close(audio)
        close.reload(audio)
        close.startAlice(audio)
        
        c=sch.commandFinding(audio, COMMANDS, WAKE)
        if c!=None:
            print(c)

        if c in ouverture:
            exe.pathMaker(audio)
        if c in recherche:
            rsch.research(audio, c)
        if c in creer:
            sc.executableMaker()

        if audio=="alice écoute":
            while audio!="alice c'est bon":
                audio=ihm.listen()
        
        if audio=="alice pierre papier ciseau":
            ppc.puit()
        
        close.stopComputer(audio)



run()
