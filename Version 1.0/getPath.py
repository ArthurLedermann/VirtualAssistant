import os

class ExecutablePath():

    def getPath(self):
        self.path = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":

    test = ExecutablePath()
    test.getPath()

    print(test.path)