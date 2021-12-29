import os, pickle

Terminal='xfld'

def create(variable, fileName):

    path=r"C:\Users\arthu\Desktop\Python\Alice Project\Alice Bêta\Donnees"
    path += '\\' + fileName + '.txt'
    print(path)

    with open(path, "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(variable)

create(Terminal, 'ShouldOpenTerminalData')