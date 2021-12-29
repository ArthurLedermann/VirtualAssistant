import ListenAndSpeak as las
import CommandsGestionner as Cg
import ExecutableMaker as Em
import CommandChecker as Cc
import Execute as exe
import PierrePapierCiseau as Ppc
import InternetResearch as Ir
import GiveInformations as Gi
import os, time, sys, pickle, AliceTerminal, Greetings
import DoAliceStart as Das

def startAlice():
    print('Lancement...')

    Greetings.greetings()
    Terminal=False

    las.speak('Je suis prête !')

    audio=''

    while (audio != 'alice coloquinte') and (audio != 'alice asperges'):

        if AliceTerminal.getInTerminal()=='xfld':
            Terminal=False
            audio=las.listen()
        else:
            Terminal=True
            audio=AliceTerminal.getInTerminal()

        print(audio)
        
        if 'alice' in audio:

            command=Cc.findCommandLabel(audio)

            if " gestionnaire de commande" in audio:
                Cg.menu()
            elif " gestionnaire des programme" in audio:
                Em.menu()

            #-------------------------------------

            elif command=='execute':
                exe.execute(audio)
            elif command=='PierrePapierCiseau':
                Ppc.play()
            elif command=='InternetResearch':
                Ir.research(audio)
            elif command=='GiveInformations':
                Gi.whatToSay(audio)
            
            #-------------------------------------
            
            elif audio == "alice coloquinte":
                las.speak('Mise en arrêt...')
            else:
                print('Pas compris :', audio)


            if Terminal==True:
                AliceTerminal.menu()


if Das.doAliceStart():
    startAlice()