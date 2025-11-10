import tkinter as tk

class GameGUI:
    def __init__(self, player):
        self.root = tk.Tk()
        self.root.geometry("1280x720")
        self.root.title("EPHEC QUEST")
        self.output_zone = tk.Text(self.root)
        self.input_zone = tk.Entry(self.root)
        self.input_zone.bind("<Return>",self.handle_command)
        self.info_frame = tk.Frame(self.root)
        self.name_player = tk.Label(self.info_frame,text=f"{player.name} ")
        self.health_player = tk.Label(self.info_frame,text=f"{player.health} ")
        self.area_player = tk.Label(self.info_frame,text=f"{player.current_area} ")

        self.output_zone.pack()
        self.input_zone.pack()
        self.info_frame.pack()
        self.name_player.pack()
        self.health_player.pack()
        self.area_player.pack()

    def handle_command(self, event):
        # Récupérer le texte d'input_zone
        # Lancer le traitement du script
        # Afficher le résultat dans output_zone
        pass
