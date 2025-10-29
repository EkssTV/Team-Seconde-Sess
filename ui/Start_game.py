from ui.GameUI import GameUI

class StartGame(GameUI):
    def __init__(self):
        super().__init__()  # Initialise GameUI

        # Affiche le message de bienvenue dans output_zone
        self.output_zone.insert("end", "Bienvenue dans Ephec Quest !\n")