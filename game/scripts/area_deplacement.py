from ..area.area_scripting import load_csv_area
from ..area.exceptions import InvalidAreaException
from ..npc.npc_scripting import load_csv_npc
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


def area_deplacement(gui, command):
    global step

    try:
        world = load_csv_area()
        people = load_csv_npc()
    except InvalidAreaException as e:
        gui.display(f"[ERREUR CSV] {e}")
        return None

    # Zone actuelle
    area = world[player.current_area]

    # NPC dans la zone (1 seul pour l’instant)
    npc_id = area.list_npc[0] if area.list_npc else None
    npc = people.get(npc_id) if npc_id else None

    # Découpage commande
    if command:
        parts = command.split()
        cmd = parts[0].lower()
    else:
        cmd = ""

    # --- STEP 0 : affichage automatique à l’entrée ---
    if step == 0:
        gui.clear_output()
        gui.display(area.simple_desc)
        step = 1
        return None

    # =================================================
    # =================== DEPLACEMENT =================
    # =================================================
    regex_command = re.match(r"(move|go|aller|avancer)\s+([A-Za-z0-9]+)", cmd + " " + (command.split()[1] if len(command.split()) > 1 else ""))

    if regex_command:
        dest = regex_command.group(2).upper()
        if dest in area.near_area:
            player.move_area(dest)
            step = 0
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
    if cmd == "look":
        gui.display("\n---")
        gui.display(area.long_desc)
        gui.display("---\n")

        npc_state = player.get_npc_state(npc_id) if npc_id else None

        if npc and npc_state is None and npc.role == "friendly":
            gui.display(f"👤 {npc.name} est ici.")
            gui.display("💬 Tape [talk] pour lui parler.\n")

        if npc and npc_state == "spoken":
            gui.display(f"👋 {npc.name} te salue poliment.\n")

        text = "Tu peux aller :\n"
        for el in area.near_area:
            text += f"- {world[el].name} [{el}]\n"
        gui.display(text)

        return None

    # ==================================================
    # =====================TALK=========================
    # ==================================================
    # ==================================================
    if cmd == "talk":
        if npc and player.get_npc_state(npc_id) is None:
            return f"speak_script {npc_id}"
        else:
            gui.display("Il n’y a personne à qui parler ici.")
        return None

    # =================================================
    # ====================== SAVE =====================
    # =================================================
    if cmd == "save":
        player.save()
        gui.display("Partie sauvegardée.")
        gui.update_info(player)
        return None

    # =================================================
    # ===================== AUTRES ====================
    # =================================================
    if cmd == "who":
        gui.display(str(player))
        return None

    if cmd == "help":
        gui.display("Commandes disponibles : look, move <zone>, save, who, quit")
        return None

    if cmd == "quit":
        gui.quit_game()

    gui.display("Commande inconnue dans ce contexte.")
    return None
