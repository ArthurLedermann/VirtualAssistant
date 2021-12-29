import ExecutableMaker as Em
import SequencesMaker as Sm
import os

def execute(audio):
    allPrograms=Em.getExecutablesPrograms()
    if 'séquence' in audio:
        sequence(audio)
    else:
        for i in range(len(allPrograms)):
            for program in allPrograms[i]:
                if program in audio:
                    if i == 0:
                        path = 'C:\\Users\\arthu\\Desktop\\Python\\Alice Project\\Alice Bêta\\Executables Programs\\' + program + '.lnk'
                        try:
                            os.startfile(path)
                        except:
                            print('Fichier ', path, ' introuvable')
                    else :
                        path = 'C:\\Users\\arthu\\Desktop\\Python\\Alice Project\\Alice Bêta\\Executables Programs\\' + program + '.url'
                        try:
                            os.startfile(path)
                        except:
                            print('Fichier ', path, ' introuvable')



def sequence(audio):

    allSequences=Sm.getSequences()

    indexOfSequence=0
    if 'une' in audio:
        indexOfSequence=1

    for i in range(len(allSequences)):
        if str(i) in audio:
            indexOfSequence=i

    for executable in allSequences[indexOfSequence-1]:
        execute(executable)