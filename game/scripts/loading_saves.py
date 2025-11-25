from ..player.player_class import Player
from ..area.area_class import CreaArea
from ..area.area_scripting import load_csv_area
from ..npc.npc_class import *
from ..npc.npc_scripting import *
from ..object.object_class import *
from ..object.object_scripting import *
from ..question.question_class import *
from ..question.question_scripting import *
from .saved_player import saved_player


step = 0
player = Player()
def loading_saves(gui, command=None):
    global step

    if command is None:
        # step 0 : choose player
        str_of_saved_player = ""
        for save in saved_player() :
            str_of_saved_player += f'[{save}] '
        gui.clear_output()
        gui.display("=== MENU DE CHARGEMENT ===")
        gui.display("Tape la save que tu choisis ! Sinon [new] pour crée la nouvelle partie")
        gui.display(f'Voici les saves disponibles : {str_of_saved_player}')
        step = 1
        return None
    if step == 1:
        # step 1 : chosen player or new player
        if command == 'new' :
            step = 1.1

        elif command in saved_player() :
            step = 2

        else :
            gui.display("Commande inconnue dans ce contexte.")
    if step == 1.1 :
        gui.display("Bienvenue à l’EPHEC ! Avant de commencer, quel est ton nom ?")
        step = 1.2
        return None

    if step == 1.2 :
        # Étape 1 : réception du nom
        player.name = command
        player.save_path = f'saves/{command}.json'
        player.save()
        player.load(player.save_path)
        gui.update_info(player)
        gui.display(f"Enchanté, {command} ! L’aventure commence maintenant.")
        gui.display(f"Voici tes stat actuel : {player} ")
        gui.display(f"Chargement du script : {player.current_script}")
        step = 2
        return None
    if step == 2:
        if command in saved_player():
            player.name = command
            player.save_path = f'saves/{command}.json'
            player.load(player.save_path)
            gui.update_info(player)
            gui.display(f" Bienvenue dans ta partie sauvegardée {player.name}. Voici tes stat actuel : \n{player} ")
            gui.clear_output()
            player.change_script('area_deplacement')
            gui.display(f"Chargement du script : {player.current_script}",300)
            gui.display("Tape [continue]")
            return 'area_deplacement'
        else :
            gui.display("Commande inconnue dans ce contexte.")
    return None
