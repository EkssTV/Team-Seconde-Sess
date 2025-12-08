from game.scripts.command_script_magnager import handle_command_from_gui


class ConsoleGUI:
    """
    ===============================================
     EPHEC QUEST - console_main.py
    -----------------------------------------------
     Description :
         Version console du jeu EPHEC QUEST.
         Cette interface remplace la GUI Tkinter et
         permet de jouer entièrement dans le terminal.

     Fonctionnement :
         - Le fichier utilise le même moteur de commandes
           que la version GUI : handle_command_from_gui().
         - Les scripts du jeu (déplacements, objets, NPC,
           chargement de sauvegardes, etc.) appellent des
           méthodes de la classe GameGUI dans la version
           graphique (display(), update_info(), etc.).
         - La classe ConsoleGUI fournie ici imite ces
           méthodes, mais utilise simplement des print()
           pour afficher les informations en console.

     Objectif :
         Offrir une interface texte minimale sans modifier
         la logique interne du jeu.

     Classes :
         ConsoleGUI
             Interface console imitant la GameGUI :
             - display(text)
             - update_info(player)
             - clear_output()
             - quit_game()

     Fonctions :
         run_console()
             Lance la boucle de jeu en console, lit les
             commandes de l'utilisateur via input(), et les
             transmet au moteur de jeu.

     Utilisation :
         python console_main.py

     Auteur :
         Grégory Ly
    ===============================================
    """

    def display(self, text: str, time_to_show: int = 2):
        print(text)

    def update_info(self, player):
        print("\n[INFOS JOUEUR]")
        print(player)
        print()

    def clear_output(self):
        print("\n" + "-" * 60 + "\n")

    def quit_game(self):
        print("Fermeture du jeu.")
        raise SystemExit


def run_console():
    gui = ConsoleGUI()
    gui.display(''' 
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
    
    
        Bienvenue dans EPHEC QUEST

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
        - stefantroch (Stefan Torch)
        - Boureym0 (Benjamin Junion)

        Prépare-toi à vivre une aventure unique… et à prouver que tu es digne de devenir un maître de l’IT !

        Entre [start]''')

    while True:
        cmd = input("> ").strip()
        if cmd in ("quit", "exit"):
            gui.quit_game()
        handle_command_from_gui(cmd, gui)


if __name__ == "__main__":
    run_console()
