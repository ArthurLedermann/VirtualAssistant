from logsClass import logs
import random

class game():

    def __init__(self):
        
        logs("Initialisation de la partie...", "I")
        logs("Selection de l'action de Alice...")

        self.aliceNumberMove = random.randrange(3)

        logs("Alice jouera le numéro "+ str(self.aliceNumberMove))
        logs("Demande au joueur de jouer")

        self.playerNumberMove = input("Qu'allez vous jouer ? \n1-Pierre  2-Papier  3-Ciseaux\n>> ")

        self.playerNumberMove.replace(" ", "")

        if self.playerNumberMove == "1" or "Pierre":
            self.playerNumberMove = 2
        elif self.playerNumberMove == "2" or "Papier":
            self.playerNumberMove = 0
        elif self.playerNumberMove == "3" or "Ciseaux":
            self.playerNumberMove = 1
        else:
            logs("Invalid Number, choosing randomly", "E")
            self.playerNumberMove = random.randrange(3)

        logs("Le joueur a joué le numéro " + str(self.playerNumberMove))
        logs("Traduction en mots...")

        self.aliceMove = move(self.aliceNumberMove)
        self.aliceMove.translate()

        self.playerMove = move(self.playerNumberMove)
        self.playerMove.translate()

        logs("Traduction terminé")
        logs("Affichage de la traduction...")
        
        print("Alice a joué {0}".format(self.aliceMove.playedMove))
        print("Le Joueur a joué {0}".format(self.playerMove.playedMove))

        logs("Calcul du résultat...")

        self.issue = issue(self.aliceNumberMove, self.playerNumberMove)
        self.issue.calculate()

        logs("Résultat calculé")
        logs("Affichage du résultat")

        print(self.issue.issuePlayer)

        logs("Fin de la partie", "I")

class move():

    def __init__(self, numberMove):
        self.numberMove = numberMove

    def translate (self):
        self.playedMove = {
            0 : "Papier",
            1 : "Ciseaux",
            2 : "Pierre"
        }[self.numberMove]

class issue():

    def __init__(self, aliceMove, playerMove):
        self.moves = [aliceMove, playerMove]

        self.issuePossibility = ["You Win", "Equality", "You Lose"]
    
    def calculate(self):        
        if self.moves in [[2, 0], [0, 1], [1, 2]]:
            self.issuePlayer = self.issuePossibility[0]
        elif self.moves[0] == self.moves[1]:
            self.issuePlayer = self.issuePossibility[1]
        else:
            self.issuePlayer = self.issuePossibility[2]


if __name__ == "__main__":
    test = game()