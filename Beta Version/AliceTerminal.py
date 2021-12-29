import PySimpleGUI as sg
import pickle

path=r"C:\Users\arthu\Desktop\Python\Alice Project\Alice Bêta\Donnees"
path += '\\' + 'ShouldOpenTerminalData' + '.txt'

def getInTerminal(): 

    with open(path, 'rb') as f:
        myPickler=pickle.Unpickler(f)
        textInTerminal=myPickler.load()

    return textInTerminal.lower()

def resetTerminal():
    reset='xfld'

    with open(path, "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(reset)

def modifyTerminal(text='xfld'):
    with open(path, "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(text)

def menu():
    layout = [  [sg.Text('Entrez une commande :')],
                [sg.Input()],
                [sg.Button('Ok'), sg.Button('Exit')]]

    window = sg.Window('Terminal', layout, element_justification='c')
    events=window.read()
    window.close()

    if events[0]=='Ok':
        if events[1][0]=='t exit':
            resetTerminal()
        else:
            modifyTerminal(events[1][0])