import WifiCheck as WC

location="CESI"

notesTaked = {location : []}

class Note:

    def __init__(self, content, location):
        self.content = content
        self.locaction = location
        
    def takeNote(self):

        self.getNotesTaked()

        self.notesTakedKeys = list(self.notesTaked.keys())

        for i in range(len(self.notesTakedKeys)):
            if self.notesTakedKeys[i] == self.locaction:
                self.notesTaked[self.notesTakedKeys[i]].append(self.content)

    def getNotesTaked(self):
        self.notesTaked = notesTaked



if __name__ == "__main__":

    test = Note("Ceci est un test", "CESI")
    test2 = Note("Test2", "CESI")
    test.takeNote()
    test2.takeNote()
    print(test.notesTaked)
