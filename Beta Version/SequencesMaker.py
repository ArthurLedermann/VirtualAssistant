import PySimpleGUI as sg
import ExecutableMaker as Em
import os, pickle

path=r'C:\Users\arthu\Desktop\Python\Alice Project\Alice Bêta\Donnees\SequencesExecutables.txt'

def getSequences():
    with open(path, 'rb') as f:
        myPickler=pickle.Unpickler(f)
        allExecutablesPrograms=myPickler.load()

    return allExecutablesPrograms

def saveSequences(allSequences):
    with open(path, "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(allSequences)


def addSequences(allSequences):

    allExecutablesPrograms=Em.getExecutablesPrograms()
    allExecutablesPrograms=allExecutablesPrograms[0]+allExecutablesPrograms[1]
    
    layout = [  [sg.Text('Rajouter une Séquence')],
                [sg.Listbox(allExecutablesPrograms, select_mode='multiple', size=(20, 10))],
                [sg.Text('Il y a '), sg.Text(len(allSequences)), sg.Text('Séquences')],
                [sg.Button('Ok'), sg.Button('Exit')]]

    window = sg.Window('Sequences Maker', layout, element_justification='c')
    events = window.read()
    window.close()

    if events[0]=='Ok':
        programsInSequences=[]
        for program in events[1][0]:
            programsInSequences.append(program)
        allSequences.append(programsInSequences)
        saveSequences(allSequences)

def modSequences(allSequences):

    allExecutablesPrograms=Em.getExecutablesPrograms()
    allExecutablesPrograms=allExecutablesPrograms[0]+allExecutablesPrograms[1]

    listOfSequences=[]
    for i in range(len(allSequences)):
        listOfSequences.append('Séquence ' + str(i+1))

    layout = [  [sg.Text('Quelle séquence voulez vous modifier ?')],
                [sg.Listbox(listOfSequences, size=(20, 10))],
                [sg.Button('Ok'), sg.Button('Exit')]]
    
    window = sg.Window('Sequences Maker', layout, element_justification='c')
    events = window.read()
    window.close()

    if events[0] == 'Ok' and events[1][0]!=[]:
        index=int(events[1][0][0][9:])
        
        layout2 = [ [sg.Text('Quelles modifications voulait vous apportez ?')],
                    [sg.Listbox(allSequences[index-1], select_mode='multiple', size=(20, 10)), sg.Listbox(allExecutablesPrograms, select_mode='multiple', size=(20, 10))],
                    [sg.Checkbox('Ajouter'), sg.Checkbox('Supprimer')],
                    [sg.Button('Ok'), sg.Button('Exit')]]

        window2 = sg.Window('Sequences Maker', layout2, element_justification='c')
        events2 = window2.read()
        window2.close()

        if events2[0] == "Ok":
            if events2[1][2] and events2[1][1]!=[]:
                for i in range(len(events2[1][1])):
                    allSequences[index-1].append(events2[1][1][i])
            if events2[1][3] and events2[1][0]!=[]:
                for executable in events2[1][0]:
                    while i < len(allSequences[index-1]):
                        if executable in allSequences[index-1][i]:
                            del allSequences[index-1][i]
                        else:
                            i+=1
            
            saveSequences(allSequences)

def delSequences(allSequences):
    
    listOfSequences=[]
    for i in range(len(allSequences)):
        listOfSequences.append('Séquence ' + str(i+1))

    layout = [  [sg.Text('Supprimer une Séquence')],
                [sg.Listbox(listOfSequences, size=(20, 10))],
                [sg.Button('Ok'), sg.Button('Exit')]]

    window = sg.Window('Sequences Maker', layout, element_justification='c')
    events = window.read()
    window.close()

    if events[0]=='Ok':
        index=int(events[1][0][0][9:])
        del allSequences[index-1]
        saveSequences(allSequences)

def menu():
    layout = [  [sg.Text("Que voulez vous faire ?")],
                [sg.Button("Rajouter"), sg.Button("Supprimer"), sg.Button('Modifier'), sg.Button("Exit")] ]
    
    window = sg.Window('Sequences Maker', layout)
    events = window.read()
    window.close()

    if events[0] == 'Rajouter':
        addSequences(getSequences())
        menu()
    if events[0] == 'Supprimer':
        delSequences(getSequences())
        menu()
    if events[0] == 'Modifier':
        modSequences(getSequences())
        menu()
