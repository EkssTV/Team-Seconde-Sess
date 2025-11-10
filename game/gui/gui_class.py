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
        self.root = tk.Tk()
        self.root.geometry("1280x720")
        self.root.title("EPHEC QUEST")

        # === MAIN FRAMES ===
        self.output_frame = tk.Frame(self.root, bg="black")
        self.input_frame = tk.Frame(self.root, bg="gray20")
        self.info_frame = tk.Frame(self.root, bg="gray15")

        # === OUTPUT ZONE ===
        self.output_zone = tk.Text(self.output_frame, bg="black", fg="white", font=("Courier", 12), state="disabled")
        self.output_zone.pack(fill="both", expand=True)

        # === INPUT ZONE ===
        self.input_zone = tk.Entry(self.input_frame, bg="white", fg="black", font=("Courier", 12))
        self.input_zone.pack(fill="x", padx=10, pady=10)
        self.input_zone.bind("<Return>", self.handle_command)

        # === PLAYER INFO PANEL ===
        self.name_player = tk.Label(self.info_frame, text=f"Name: {player.name}", fg="white", bg="gray15",
                                    font=("Arial", 12))
        self.health_player = tk.Label(self.info_frame, text=f"Health: {player.health}", fg="white", bg="gray15",
                                      font=("Arial", 12))
        self.area_player = tk.Label(self.info_frame, text=f"Area: {player.current_area}", fg="white", bg="gray15",
                                    font=("Arial", 12))

        self.name_player.pack(anchor="w", padx=10, pady=5)
        self.health_player.pack(anchor="w", padx=10, pady=5)
        self.area_player.pack(anchor="w", padx=10, pady=5)

        # === FRAME PLACEMENT ===
        self.info_frame.pack(side="left", fill="y")
        self.output_frame.pack(side="top", fill="both", expand=True)
        self.input_frame.pack(side="bottom", fill="x")

    def display(self, text):
        """
        Displays a string in the output zone with a typewriter effect.
        Disables the input zone during animation.

        Args:
            text (str): The text to display in the output zone
        """
        self.input_zone.config(state="disabled")
        self.current_text = text
        self.char_index = 0

        self.output_zone.config(state="normal")
        self.output_zone.insert("end", "\n")
        self.output_zone.config(state="disabled")

        self.animate_text()

    def animate_text(self):
        """
        Animates the current text one character at a time.
        Re-enables the input zone once the animation is complete.
        """
        if self.char_index < len(self.current_text):
            self.output_zone.config(state="normal")
            self.output_zone.insert("end", self.current_text[self.char_index])
            self.output_zone.config(state="disabled")
            self.output_zone.see("end")
            self.char_index += 1
            self.root.after(30, self.animate_text)
        else:
            self.input_zone.config(state="normal")

    def handle_command(self, event):
        """
        Called when the user presses Enter.
        Transfers the entered command to the external script handler.
        """
        command = self.input_zone.get()
        self.input_zone.delete(0, "end")
        handle_command_from_gui(command,self)
