

from .area_deplacement import area_deplacement
from .loading_saves import loading_saves, step
from .speak_script import speak_script
from .fight_script import fight_script

"""
===============================================
 EPHEC QUEST - script_manager.py
-----------------------------------------------
 Description : Handles game commands and script logic
 Author      : Matthieu
 Date        : 2025
===============================================
"""

# Mapping des transitions possibles
HANDLER_MAP = {
    "area_deplacement": area_deplacement,
    "loading_saves": loading_saves,
}

current_handler = None


def handle_command_from_gui(command: str, gui):
    global current_handler

    # Si un handler est actif → on lui délègue la commande
    if current_handler:
        try:

            result = current_handler(gui, command)

            # Si le result est speak
            if result and result.startswith("speak_script"):
                _, npc_id = result.split()
                current_handler = lambda g, c: speak_script(g, c, npc_id)

            if result and result.startswith("fight_script"):

                _, npc_id = result.split()
                current_handler = lambda g, c: fight_script(g, c, npc_id)


            # Si le handler renvoie une transition valide
            if result in HANDLER_MAP:
                current_handler = HANDLER_MAP[result]

        except Exception as e:
            gui.display(f"Erreur dans le script : {e}")
            current_handler = None

        return

    # Aucun handler actif → commandes globales
    if command == "start":
        current_handler = loading_saves
        current_handler(gui, None)
        return



    if command == "help":
        gui.display("Tape 'start' pour commencer")
        return

    gui.display("Commande inconnue.")