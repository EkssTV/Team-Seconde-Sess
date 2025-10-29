
from game.game_logic import Game

class Command:
    def __init__(self, ui):
        self.ui = ui  # ui = instance de GameUI
        self.game = Game()
    def execute(self, command):
        command = command.strip().lower()

        if command == "help":
            self.ui.output_zone.insert("end", "Commandes disponibles : help,caca,look\n")
        elif command == "start":
            self.ui.output_zone.insert("end", "La Partie va se lancer\n")
        elif command == "caca":
            self.ui.output_zone.insert("end","LE GROS CACA PARTOUT")
        elif command == "look":
            self.ui.output_zone.insert("end",f"{self.game.look()}")
        elif command == "move":

        else:
            self.ui.output_zone.insert("end", f"Commande inconnue : {command}\n")
