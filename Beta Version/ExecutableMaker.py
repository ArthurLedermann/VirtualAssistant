import PySimpleGUI as sg
import ListenAndSpeak as las
import os, pickle
 
path=r'C:\Users\arthu\Desktop\Python\Alice Project\Alice Bêta\Donnees\ExecutableProgramsNames.txt'

def getExecutablesPrograms():
    with open(path, 'rb') as f:
        myPickler=pickle.Unpickler(f)
        allExecutablesPrograms=myPickler.load()

    return allExecutablesPrograms

def saveExecutablesPrograms(allExecutablesPrograms):
    with open(path, "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(allExecutablesPrograms)


def addExecutablesPrograms(allExecutablesPrograms):
    layout = [  [sg.Text('Rajouter un executable:')],
                [sg.Checkbox('Logiciel'), sg.Checkbox('Lien Internet')],
                [sg.Listbox(allExecutablesPrograms[0], size=(20, 10)), sg.Listbox(allExecutablesPrograms[1], size=(20, 10))],
                [sg.Input()],
                [sg.Button('Ok'), sg.Button('Exit')]]

    window = sg.Window('Executable Maker', layout, element_justification='c')
    events = window.read()
    window.close()

    if events[0]=='Ok':
        if events[1][0]:
            allExecutablesPrograms[0].append(events[1][4])
            saveExecutablesPrograms(allExecutablesPrograms)
        if events[1][1]:
            allExecutablesPrograms[1].append(events[1][4])
            saveExecutablesPrograms(allExecutablesPrograms)

def delExecutablesPrograms(allExecutablesPrograms):
    layout = [  [sg.Text('Supprimer un executable:')],
                [sg.Listbox(allExecutablesPrograms[0], size=(20, 10)), sg.Listbox(allExecutablesPrograms[1], size=(20, 10))],
                [sg.Button('Ok'), sg.Button('Exit')]]

    window = sg.Window('Executable Maker', layout, element_justification='c')
    events = window.read()
    window.close()

    if events[0]=='Ok':
        if events[1][0] != []:
            for i in range(len(allExecutablesPrograms[0])):
                if events[1][0][0]==allExecutablesPrograms[0][i]:
                    del allExecutablesPrograms[0][i]
        if events[1][1] != []:
            for i in range(len(allExecutablesPrograms[1])):
                if events[1][1][0]==allExecutablesPrograms[1][i]:
                    del allExecutablesPrograms[1][i]

    saveExecutablesPrograms(allExecutablesPrograms)


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
                [sg.Button("Rajouter"), sg.Button("Supprimer"), sg.Button('File'), sg.Button("Test Micro"), sg.Button("Exit")] ]
    
    window = sg.Window('Executable Maker', layout)
    events = window.read()
    window.close()

    if events[0] == 'Rajouter':
        addExecutablesPrograms(getExecutablesPrograms())
        menu()
    if events[0] == 'Supprimer':
        delExecutablesPrograms(getExecutablesPrograms())
        menu()
    if events[0] == 'Test Micro':
        testMicro()
    if events[0] == 'File':
        os.startfile(r'C:\Users\arthu\Desktop\Python\Alice Project\Alice Bêta\Executables Programs')

    