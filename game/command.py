
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
            txt = ''
            for i in self.game.areas[self.game.player.current_area].near_places:
               txt += str(i) + ' '

            self.ui.output_zone.insert("end",f"{self.game.look()}\n tu peux aller {txt}")
        elif command.startswith("move"):
            direction = command.split(" ")[1]
            result = self.game.move(self.game.areas[direction])
            self.ui.output_zone.insert("end", self.game.player.current_area + "\n")
        else:
            self.ui.output_zone.insert("end", f"Commande inconnue : {command}\n")
