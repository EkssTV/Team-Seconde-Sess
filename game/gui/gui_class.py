import tkinter as tk
from ..scripts.command_script_magnager import handle_command_from_gui
from ..player.player_class import Player
player = Player()
"""
===============================================
 EPHEC QUEST - gui_class.py
-----------------------------------------------
 Description : Gui for EPHEC QUEST
 Author      : Matthieu
 Date        : 2025
===============================================
"""


class GameGUI:
    """
    GameGUI class handles the graphical user interface for EPHEC QUEST.
    It displays game narration, accepts player commands, and shows player information.
    """

    def __init__(self, player):
        """
        Initializes the main window and all GUI components:
        - Output zone for game narration
        - Input zone for player commands
        - Info panel showing player stats (name, health, area)

        Args:
            player (Player): The player object containing game state
        """
        self.current_text = ""
        self.char_index = 0
        self.display_queue = []
        self.is_displaying = False
        self.root = tk.Tk()
        #self.root.geometry("1280x720")
        self.root.attributes('-fullscreen', True)
        self.root.title("EPHEC QUEST")

        # === MAIN FRAMES ===
        self.output_frame = tk.Frame(self.root, bg="#8c6239")
        self.input_frame = tk.Frame(self.root, bg="#B08d57")
        self.info_frame = tk.Frame(self.root, bg="#3A5F0B")

        # === OUTPUT ZONE ===
        self.output_zone = tk.Text(self.output_frame,bd=5, bg="#EAD7B7", fg="#1a1a1a", font=("Courier", 12), state="disabled")
        self.output_zone.pack(fill="both", expand=True)

        # === INPUT ZONE ===
        self.input_zone = tk.Entry(self.input_frame, bd=5,bg="#EAD7B7", fg="#1a1a1a", font=("Courier", 12))
        self.input_zone.pack(fill="x", padx=10, pady=10)
        self.input_zone.bind("<Return>", self.handle_command)

        # === PLAYER INFO PANEL ===
        self.name_player = tk.Label(self.info_frame, text=f"👤: {player.name}", fg="#f5f5f5", bg="#3A5F0B",
                                    font=("Arial", 12))
        self.health_player = tk.Label(self.info_frame, text=f"❤️: {player.health}", fg="#f5f5f5", bg="#3A5F0B",
                                      font=("Arial", 12))
        self.area_player = tk.Label(self.info_frame, text=f"🏠: {player.current_area}", fg="#f5f5f5", bg="#3A5F0B",
                                    font=("Arial", 12))
        self.inventory = tk.Label(self.info_frame, text=f"====Sac à dos 🎒====\n {'\n '.join(player.inv) if player.inv else 'Empty'}\n", fg="#f5f5f5", bg="#5D7052",
                                    font=("Arial", 12))

        self.name_player.pack(anchor="w", padx=10, pady=5)
        self.health_player.pack(anchor="w", padx=10, pady=5)
        self.area_player.pack(anchor="w", padx=10, pady=5)
        self.inventory.pack(anchor="w", padx=10, pady=5)

        # === FRAME PLACEMENT ===
        self.info_frame.pack(side="left", fill="y",)
        self.output_frame.pack(side="top", fill="both", expand=True)
        self.input_frame.pack(side="bottom", fill="x")

    def _start_next_display(self):
        if self.display_queue:
            self.is_displaying = True
            text, time_to_show = self.display_queue.pop(0)
            self.current_text = text
            self.char_index = 0
            self.text_speed = time_to_show

            self.output_zone.config(state="normal")
            self.output_zone.insert("end", "\n")
            self.output_zone.config(state="disabled")

            self.animate_text()
        else:
            self.is_displaying = False

    def display(self, text,time_to_show=2):
        """
        Displays a string in the output zone with a typewriter effect.
        Disables the input zone during animation.

        Args:
            text (str): The text to display in the output zone
            time_to_show (int) : The time of writing text
        """
        self.display_queue.append((text, time_to_show))
        if not self.is_displaying:
            self._start_next_display()



    def animate_text(self):
        """
        Animates the current text one character at a time.
        Re-enables the input zone once the animation is complete.
        """
        if self.char_index < len(self.current_text):
            self.input_zone.config(state="disabled")
            self.output_zone.config(state="normal")
            self.output_zone.insert("end", self.current_text[self.char_index])
            self.output_zone.config(state="disabled")
            self.output_zone.see("end")
            self.char_index += 1
            self.root.after(self.text_speed, self.animate_text)
        else:
            self.input_zone.config(state="normal")
            self.is_displaying = False
            self._start_next_display()

    def handle_command(self, event):
        """
        Called when the user presses Enter.
        Transfers the entered command to the external script handler.
        """
        command = self.input_zone.get()
        self.input_zone.delete(0, "end")
        handle_command_from_gui(command,self)

    def update_info(self, player):
        """
        Called when the info must be updated
        """
        self.name_player.config(text=f"👤: {player.name}")
        self.health_player.config(text=f"❤️: {player.health}")
        self.area_player.config(text=f"🏠: {player.current_area}")
        self.inventory.config(text=f"====Sac à dos 🎒====\n {'\n'.join(player.inv) if player.inv else 'Empty'}\n")

    def clear_output(self):
        """Called when output must be cleared"""
        self.output_zone.config(state="normal")
        self.output_zone.delete("1.0", "end")
        self.output_zone.config(state="disabled")
    def quit_game(self):
        """Called when game must be quit"""
        self.root.destroy()
    def display_force(self,text):
        self.output_zone.config(state="normal")
        self.output_zone.insert("end", text)
        self.output_zone.config(state="disabled")
    def starting_game(self):
        intro_logo = intro_logo = '''
          ▄████████    ▄███████▄    ▄█    █▄       ▄████████  ▄████████      
          ███    ███   ███    ███   ███    ███     ███    ███ ███    ███      
          ███    █▀    ███    ███   ███    ███     ███    █▀  ███    █▀       
         ▄███▄▄▄       ███    ███  ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███            
        ▀▀███▀▀▀     ▀█████████▀  ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███             
          ███    █▄    ███          ███    ███     ███    █▄  ███    █▄       
          ███    ███   ███          ███    ███     ███    ███ ███    ███      
          ██████████  ▄████▀        ███    █▀      ██████████ ████████▀        
        
         ████████▄   ███    █▄     ▄████████    ▄████████     ███
         ███    ███  ███    ███   ███    ███   ███    ███ ▀█████████▄
         ███    ███  ███    ███   ███    █▀    ███    █▀     ▀███▀▀██
         ███    ███  ███    ███  ▄███▄▄▄       ███            ███   ▀
         ███    ███  ███    ███ ▀▀███▀▀▀     ▀███████████     ███
         ███    ███  ███    ███   ███    █▄           ███     ███
         ███  ▀ ███  ███    ███   ███    ███    ▄█    ███     ███
         ▀██████▀▄█ ████████▀    ██████████  ▄████████▀     ▄████▀
'''
        intro_text = '''
        Bienvenue dans EPHEC QUEST 🎓

        Le projet Ephec Quest propose au joueur d’incarner un étudiant plongé dans une aventure textuelle à travers 
        les bâtiments de la Haute École EPHEC.

        🎯 **Votre mission** : partir à la rencontre des professeurs légendaires de la section IT, 
        résoudre leurs énigmes et percer les secrets du campus.

        🧠 Chaque professeur représente une discipline :
        - Programmation
        - Réseaux
        - Bases de données
        - Et bien plus...

        💡 Le ton du jeu se veut humoristique, immersif et légèrement parodique, tout en rendant hommage à 
        la vie étudiante et à l’apprentissage.

        👨‍💻 Créateurs :
        - Ekss (Matthieu Decreme)
        - GraindeRiz (Gregory Ly)
        - stefantroch (Stefan Troch)
        - Boureym0 (Benjamin Junion)

        Prépare-toi à vivre une aventure unique… et à prouver que tu es digne de devenir un maître de l’IT !
        
        Entre [start]
        '''
        self.display_force(intro_logo + "\n" + intro_text)
