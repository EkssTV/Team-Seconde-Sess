"""
===============================================
 EPHEC QUEST - main.py
-----------------------------------------------
 Description :
     Point d'entrée du jeu en version GUI. Ce fichier
     initialise l'interface graphique, charge le joueur,
     puis lance la boucle principale Tkinter.

     L’organisation de ce fichier a été pensée après un
     conseil d’une IA afin de clarifier le rôle du module
     principal et de séparer correctement interface et
     logique métier.

 Fonctionnement :
     - Création d'une instance de GameGUI.
     - Initialisation du joueur.
     - Lancement des scripts d'introduction (starting_game).
     - Exécution de la boucle Tkinter (mainloop).

 Préconditions :
     - GameGUI doit être correctement importé.
     - Le joueur doit être défini dans player_class.
     - handle_command_from_gui doit être disponible.
     - Tkinter doit être fonctionnel.

 Postconditions :
     - La fenêtre du jeu est affichée.
     - Le joueur peut saisir des commandes.
     - Le jeu reste actif jusqu’à la fermeture de la GUI.

 Auteur : Matthieu Decrem
 Date   : 2025
===============================================
"""
from game.player.player_class import Player
from game.gui.gui_class import GameGUI,player
from game.scripts.command_script_magnager import handle_command_from_gui


gui = GameGUI(player)
gui.starting_game()
gui.root.mainloop()
