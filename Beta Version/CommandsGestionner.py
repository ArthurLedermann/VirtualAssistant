import PySimpleGUI as sg
import ListenAndSpeak as las
import os, pickle
 
path=r'C:\Users\arthu\Desktop\Python\Alice Project\Alice Bêta\Donnees\commandsData.txt'

def getCommands():

    with open(path, 'rb') as f:
        myPickler=pickle.Unpickler(f)
        allCommands=myPickler.load()

    return allCommands

def saveCommands(allCommands):
    with open(path, "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(allCommands)


def addCommands(allCommands):

    layout = [  [sg.Text('Sélectionnez une clé :')],
                [sg.Listbox(list(allCommands.keys()), size=(20, 10))],
                [sg.InputText()],
                [sg.Button('Ok'), sg.Button('Exit')]]

    window = sg.Window('Ajouter une commande', layout, element_justification='c')
    events=window.read()
    window.close()

    if events[0]=='Ok':
        """print(events[1])
        print(allCommands[events[1][0][0]])
        print(len(events[1][1]))"""
        allCommands[events[1][0][0]].append(events[1][1].lower())
        saveCommands(allCommands)

def delCommands(allCommands):
    layout = [  [sg.Text('Sélectionnez une clé :')],
                [sg.Listbox(list(allCommands.keys()), size=(20, 10))],
                [sg.Button('Ok'), sg.Button('Exit')]]

    window = sg.Window('Supprimer une commande', layout, element_justification='c')
    events=window.read()
    window.close()

    if events[0]=='Ok':
        key=events[1][0][0]

        layout2 = [ [sg.Text('Choisissez la Commande a supprimer :')],
                    [sg.Listbox(allCommands[key], size=(80, 10))],
                    [sg.Button('Ok'), sg.Button('Exit')]]

        window2 = sg.Window('Supprimer une commande', layout2, element_justification='c')
        events=window2.read()
        window2.close()

        if events[0]=='Ok' and len(events[1][0])>0:
            commandToDel=events[1][0][0]

            i=0
            lenght=1
            while i < lenght:
                if allCommands[key][i] == commandToDel:
                    del allCommands[key][i]
                
                lenght=len(allCommands[key])
                i+=1
            
            saveCommands(allCommands)

def addKey(allCommands):
    layout = [  [sg.Text('Entrez la clé à rajouter:')],
                [sg.Text('Clé : '), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Exit')]]

    window = sg.Window('Rajouter une clé', layout, element_justification='c')
    events = window.read()
    window.close()

    if events[0]=='Ok':
        allCommands[str(events[1][0])]=[]

        saveCommands(allCommands)

def delKey(allCommands):
    layout = [  [sg.Text('Sélectionnez une clé :')],
                [sg.Listbox(list(allCommands.keys()), size=(20, 10))],
                [sg.Button('Ok'), sg.Button('Exit')]]

    window = sg.Window('Supprimer une clé', layout, element_justification='c')
    events=window.read()
    window.close()

    if events[0]=='Ok' and len(events[1][0])>0:
        del allCommands[events[1][0][0]]
        saveCommands(allCommands)


def testMicro():
    layout = [  [sg.Text('J\'écoute...')],
                [sg.Button('Go')]]

    window = sg.Window('Test Micro', layout, element_justification='c')
    events = window.read()
    textSaid = las.listen()
    window.close()

    layout2 = [ [sg.Text('Vous avez dit : '), sg.Text(textSaid)],
                [sg.Button('Ok'), sg.Button('Refaire')]]
    
    window2 = sg.Window('Test Micro', layout2, element_justification='c')
    events = window2.read()
    window2.close()

    if events[0]=='Ok':
        menu()
    else:
        testMicro()
    

def menu():
    layout = [  [sg.Text("Que voulez vous faire ?")], 
                [sg.Checkbox('Commande'), sg.Checkbox('Clé')],
                [sg.Button("Rajouter"), sg.Button("Supprimer"), sg.Button("Test Micro"), sg.Button("Exit")] ]
    
    window = sg.Window('Commands Gestionner', layout)
    events = window.read()
    window.close()

    if events[0] == 'Rajouter' and events[1][0]:
        addCommands(getCommands())
        menu()
    if events[0] == 'Rajouter' and events[1][1]:
        addKey(getCommands())
        menu()
    if events[0] == 'Supprimer' and events[1][0]:
        delCommands(getCommands())
        menu()
    if events[0] == 'Supprimer' and events[1][1]:
        delKey(getCommands())
        menu()
    if events[0] == 'Test Micro':
        testMicro()
