import PySimpleGUI as sg

def doAliceStart():

    layout = [  [sg.Text('Voulez vous lancer Alice ?')],
                [sg.Button('Yes'), sg.Button('No')]]

    win = sg.Window('Alice Launcher', layout, element_justification='c')
    events = win.read()
    win.close()

    if events[0]=='Yes':
        return True
    else:
        return False

 