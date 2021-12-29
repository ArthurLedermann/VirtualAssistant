
class logs():

    def __init__(self, message, importance="N"):

        self.color = {
            "I" : "\033[33m",
            "E" : "\033[91m",
            "N" : "\033[96m"
        }[importance]

        print(self.color + "Logs : " + str(message) + '\033[0m')