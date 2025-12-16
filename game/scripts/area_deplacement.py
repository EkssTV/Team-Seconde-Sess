from ..area.area_scripting import load_csv_area
from ..area.exceptions import InvalidAreaException
from ..npc.npc_scripting import load_csv_npc
from ..object.object_scripting import load_csv_object
from .loading_saves import player
import re

"""
===============================================
 EPHEC QUEST - area_deplacement.py
-----------------------------------------------
 Description : Gestion des déplacements et LOOK
 Auteur      : Ekss / corrigé
 Date        : 2025
===============================================
"""

step = 0

try:
    world = load_csv_area()
    people = load_csv_npc()
    objs = load_csv_object()
except InvalidAreaException as e:
    print(f"[ERREUR CSV] {e}")


def area_deplacement(gui, command):
    global step


    # Zone actuel

    area = world[player.current_area]
    # NPC Actuel
    npcs = area.list_npc

    # Découpage commande
    if command == '':
        gui.display("N'oublie pas d'écrire une commande")
        return None
    parts = command.split()
    cmd = parts[0].lower()
    if len(parts)>1 :
        param = parts[1].upper()
    # --- STEP 0 : affichage automatique à l’entrée ---
    if step == 0:
        gui.clear_output()
        gui.display(area.simple_desc)
        step = 1
        return None

    # =================================================
    # =================== DEPLACEMENT =================
    # =================================================
    regex_command = re.match(r"(move|go|aller|avancer)\s+([A-Za-z0-9]+)", cmd + " " + (param if len(command.split()) > 1 else ""))

    if regex_command:
        dest = regex_command.group(2).upper()
        if dest in area.near_area:
            player.move_area(dest)
            new_area = world[player.current_area]
            gui.display("Tu te déplaces...\n")
            gui.display(new_area.simple_desc)
            gui.update_info(player)
            return None
        else:
            gui.display("Tu n'observes pas de lieu portant ce nom.")
            return None

    # =================================================
    # ====================== LOOK =====================
    # =================================================
    elif cmd == "look":
        gui.display("\n---")
        gui.display(area.long_desc)
        gui.display("---\n")

        for npc in npcs:
            gui.display(f"👤 {people[npc].name} est ici. [{people[npc].id}]\n")
        gui.display("💬 Tape [talk] [ID] pour lui parler.\n")


        #affiche les destination possible depuis la pièce actuelle
        text = "Tu peux aller :\n"
        for el in area.near_area:
            text += f"- {world[el].name} [{el}]\n"
        gui.display(text)

        return None

    # ==================================================
    # =====================TALK=========================
    # ==================================================
    # ==================================================
    elif cmd == "talk":
        if not npcs:
            gui.display("Il n’y a personne à qui parler ici.")
            return None
        if param in npcs :
            return f"speak_script {param}"
        else :
            gui.display("Il n'y a personne avec ce nom ici")
            return None

    elif cmd == "use":
        obj = param

        if not obj in player.inv :
            gui.display("Tu n'as pas ceci dans ton sac ! ")
            return None
        else :
            thing = objs[obj]
            if thing.utilite == "Aucune" :
                gui.display(f"======Tu regardes ton objet : {thing.nom} =======")
            else :
                gui.display("======Tu utilise un object ! =======")
                if obj == "CAFE" or obj == "MARMOUT" :
                    gui.display(thing.utilite)
                    player.add_health(1)
                    player.supp_inv(obj)
                    gui.update_info(player)

            return None

    # =================================================
    # ====================== SAVE =====================
    # =================================================
    elif cmd == "save":
        player.save()
        gui.display("Partie sauvegardée.")
        gui.update_info(player)
        return None

    # =================================================
    # ===================== AUTRES ====================
    # =================================================
    elif cmd == "who":
        gui.display(str(player))
        return None

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
        return None

    # INVENTORY

    elif cmd == 'inventory' :
        gui.display(f'Voici ce que tu as dans ton inventaire:\n{player.show_inv()}')
        return None

    # CHEAT
    elif cmd =='uia': #code de triche (pour test l'inventory)
        gui.display("Tu as rentré un code de triche honte a toi")
        for i in objs:
            player.add_inv(i)
        player.save()
        return None
    #clear
    elif cmd == "clear" :
        gui.clear_output()
        return None
    #quit
    elif cmd == "quit":
        gui.quit_game()
        return None
    else :
        gui.display("Commande inconnue dans ce contexte.")
    return None
