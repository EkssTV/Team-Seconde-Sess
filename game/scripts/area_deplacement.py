from ..player.player_class import Player
from ..area.area_class import CreaArea
from ..area.area_scripting import load_csv_area
from ..area.exceptions import InvalidAreaException
from ..npc.npc_class import *
from ..npc.npc_scripting import *
from ..object.object_class import *
from ..object.object_scripting import *
from ..question.question_class import *
from ..question.question_scripting import *
from .loading_saves import player
import re
"""
===============================================
 EPHEC QUEST - area_deplacement.py
-----------------------------------------------
 Description : scripting area
 Auteur      : Ekss
 Date        : 2025
===============================================

"""
current_player = player
step = 0
def area_deplacement(gui, command):

    global step
    try:
        #charge dictionnaire de la map
        world = load_csv_area()
        #charge dictionnaire de tous les npc
        people = load_csv_npc()
    except InvalidAreaException as e:
        gui.display(f"[ERREUR CSV] {e}")
        return None

    #pièce actuelle
    area = world[player.current_area]
    npc_id = None
    #si personnage  dans la pièce on récupère tout l'objet du npc
    if area.list_npc and len(area.list_npc) > 0:
        npc_id = area.list_npc[0]
        npc = people.get(npc_id)
    else:
        npc = None
    # Découpage propre de la commande
    parts = command.split()
    cmd = parts[0].lower() if parts else ""
    arg = parts[1].upper() if len(parts) > 1 else None
    if step == 0 :
        gui.clear_output()
        gui.display(area.simple_desc)
        step = 1
    if step == 1 :

        # Regex pour expression régulière (move, go, aller, avancer)
        regex_command = re.match(r"(move|go|aller|avancer?)\s+([A-Za-z0-9]+)", command.lower())

        if regex_command:
            # On récupère la destination trouvée par la regex
            dest = regex_command.group(2).upper()

            if dest in area.near_area:
                player.move_area(dest)
                new_area = world[player.current_area]
                gui.display("Tu te déplaces")
                gui.display(new_area.simple_desc)
                gui.update_info(player)
            else:
                gui.display("Tu n'observes pas de lieu portant ce nom")

            return None

        # LOOK

        if cmd == 'look' :
            gui.display(area.long_desc)

            if npc :
                gui.display(f"Quelqu'un se trouve dans {area.name}")
                if npc.state == 2 :
                    return f"speak_script {npc_id}"
                if npc.state == 1 :
                    return f"fight_script {npc_id}"

            text =" Tu peux aller :\n"
            for el in area.near_area :
                text += f"{world[el].name} [{el}]\n"
            gui.display(text)
            if npc and npc.state == 2 :
                return f"speak_script {npc_id}"
            if npc and npc.state == 1 :
                return f"fight_script {npc_id}"

            return None

        # SAVE
        elif cmd == "save":
            player.save()
            gui.display("Partie sauvegardée")
            gui.display(f"Voici tes stats actuelles : {player}")
            gui.update_info(player)
            return None

        # QUIT
        elif cmd =='quit' :
            gui.quit_game()

        # CLEAR
        elif cmd =='clear':
            gui.clear_output()
        # WHO
        elif cmd == 'who' :
            gui.display(f"Voici tes stats actuelles : {player} ")

        # HELP

        elif cmd == 'help':
            help_text = """
            ===============================================
             EPHEC QUEST - Manuel des Commandes
            -----------------------------------------------

             Commandes générales :
               - look
                   Affiche la description détaillée de la zone
                   et liste les zones accessibles.
               - move <zone_id>
                   Déplace le joueur vers une zone voisine.
               - help
                   Affiche ce manuel des commandes.
               - clear
                   Nettoie l'affichage.
               - quit
                   Quitte le jeu.

             Commandes liées au joueur :
               - who
                   Affiche les statistiques actuelles du joueur.
               - inventory
                   Montre le contenu de l'inventaire.
               - save
                   Sauvegarde la partie et affiche les stats.

             Commandes liées aux PNJ :
               - interact
                   Liste les PNJ présents dans la zone avec leur description.
               - speak <npc_id>
                   Permet de parler à un PNJ (fonctionnalité en cours de dev).

            ===============================================
            """
            gui.display(help_text,1)

        # INVENTORY

        elif command == 'inventory' :
            gui.display(f'Voici ce que tu as dans ton inventaire:\n{player.show_inv()}')
            return None

        # CHEAT

        elif command =='UIA': #code de triche (pour test l'inventory)
            player.add_inv("CARETU")
            player.save()

        # LE RESTE
        else :
            gui.display("Commande inconnue dans ce contexte")
    return None
