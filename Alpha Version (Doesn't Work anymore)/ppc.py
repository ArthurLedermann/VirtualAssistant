import PySimpleGUI as sg
import random
 

def puit():
    layout = [  [sg.Text("Que voulez vous jouer ?")], 
                [sg.Button("Pierre"), sg.Button("Papier"), sg.Button("Ciseaux")] ]

    window = sg.Window('Alice Rock Paper Cisor', layout)
    event = window.read()
    window.close()

    aliceChoose=random.randrange(3)
    if aliceChoose==0:
        alicePlay="Pierre"
    elif aliceChoose==1:
        alicePlay="Papier"
    elif aliceChoose==2:
        alicePlay="Ciseaux"

    if event[0]==alicePlay:
        egalite()
    elif event[0]=="Pierre":
        if alicePlay=="Ciseaux":
            win()
        else:
            lose()
    elif event[0]=="Papier":
        if alicePlay=="Pierre":
            win()
        else:
            lose()
    elif event[0]=="Ciseaux":
        if alicePlay=="Papier":
            win()
        else:
            lose()
        
def egalite():
    layoutEqual = [  [sg.Text("Egalité")], 
                [sg.Button("Ah !"), sg.Button("Okay"), sg.Button("*être blasé*")] ]

    window=sg.Window('Alice Rock Paper Cisor', layoutEqual)
    window.read()
    window.close()

def win():
    layoutWin = [  [sg.Text("VOUS AVEZ GAGNEZ !!!!")], 
                [sg.Button("YES"), sg.Button("YOUPI"), sg.Button("CHEH")] ]

    window=sg.Window('Alice Rock Paper Cisor', layoutWin)
    window.read()
    window.close()

def lose():
    layoutLose = [  [sg.Text("Vous avez perdu, Alice on the top !")], 
                [sg.Button("Ok."), sg.Button("Ftg"), sg.Button("Grognasse")] ]
                
    window=sg.Window('Alice Rock Paper Cisor', layoutLose)
    window.read()
    window.close()

