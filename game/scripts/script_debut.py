
from ..player.player_class import Player
from ..area.area_class import CreaArea
from ..area.area_scripting import load_csv_area
from ..npc.npc_class import *
from ..npc.npc_scripting import *
from ..object.object_class import *
from ..object.object_scripting import *
from ..question.question_class import *
from ..question.question_scripting import *
step = 0
player = Player()
def debut_script(gui, command=None):
    global step

    if command is None:
        # Étape 0 : intro
        gui.display("Bienvenue à l’EPHEC ! Avant de commencer, quel est ton nom ?")
        step = 1
        return

    if step == 1:
        # Étape 1 : réception du nom
        player.name = command
        player.save_path = f'saves/{command}.json'
        player.save()
        player.load()
        gui.update_info(player)
        gui.display(f"Enchanté, {command} ! L’aventure commence maintenant.")
        step = 2
        return

    if step == 2:
        # Étape 2 : suite du jeu
        if command == "entrer":
            gui.display("Tu entres dans le hall lumineux de l’EPHEC.")
        elif command == "regarder":
            gui.display("Tu observes les étudiants autour de toi.")
        else:
            gui.display("Commande inconnue dans ce contexte.")
