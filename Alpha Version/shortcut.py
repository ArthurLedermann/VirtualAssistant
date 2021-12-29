import PySimpleGUI as sg
import files_gestion as fg
import interface as ihm
import os




def executableMaker():
    layout = [  [sg.Text("Rajouter un executable")], 
                [sg.Text("Commande:"), sg.Input()],
                [sg.Checkbox("Link"), sg.Checkbox("Logiciel")],
                [sg.Button("Ajouter"), sg.Cancel(), sg.Button("Test d'écoute")] ]

    window = sg.Window('Alice Executable Maker', layout)
    event, values = window.read()
    print(values)
    if event=="Test d'écoute":
        window.close()
        audio=""
        while audio!="alice c'est bon":
            audio=ihm.listen()
        executableMaker()
    if event=="Ajouter":
        if values[1]==True:
            fg.addLink(str(values[0]))
            os.startfile(r"c:\Users\arthu\Desktop\Alice Project\executable_programs.lnk")
        elif values[2]==True:
            fg.addLogiciel(str(values[0]))
            os.startfile(r"c:\Users\arthu\Desktop\Alice Project\executable_programs.lnk")
        else:
            print("Erreur 404 Maggle")
        window.close()

    else:
        window.close()          

