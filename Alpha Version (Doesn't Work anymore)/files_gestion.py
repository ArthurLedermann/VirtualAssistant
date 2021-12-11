import pickle
import os

lienfile = r"c:\Users\arthu\desktop\Alice Project\lien.txt"
logicielfile = r"C:\Users\arthu\desktop\Alice project\logiciel.txt"
adresselienfile = r"C:\Users\arthu\desktop\Alice project\adresse_lien.txt"

def get_link():
    with open(lienfile, "rb") as f:
        myPickler=pickle.Unpickler(f)
        data=myPickler.load()
    return data


def get_logiciel():
    with open(logicielfile, "rb") as f:
        myPickle=pickle.Unpickler(f)
        data=myPickle.load()
    return data


def addLink(ExeName):
    data=get_link()
    data.append(ExeName)
    with open(lienfile, "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(data)


def addLogiciel(ExeName):
    data=get_logiciel()
    data.append(ExeName)
    with open(logicielfile, "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(data)



def supprLink():
    link=get_link()
    print(link)
    loc=input("\nQuel programme doit être supprimé ?  ")
    for i in range(len(link)):
        if loc in link[i]:
            del link[i]
    with open(lienfile, "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(link)
 
def supprLogiciel():
    link=get_logiciel()
    print(link)
    loc=input("\nQuel programme doit être supprimé ?  ")
    for i in range(len(link)):
        if loc in link[i]:
            del link[i]
    with open(logicielfile, "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(link)

def indexSupprLogiciel(i):
    link=get_logiciel()
    print(link)
    del link[i]
    with open(logicielfile, "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(link)
    print(get_logiciel())

def indexSupprLink(i):
    link=get_link()
    print(link)
    del link[i]
    with open(lienfile, "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(link)
    print(get_link())







"""

ADRESSE_LIEN=[]

def create():
    with open("adresse_lien.txt", "wb") as f:
        myPickle=pickle.Pickler(f)
        myPickle.dump(ADRESSE_LIEN)

create()"""