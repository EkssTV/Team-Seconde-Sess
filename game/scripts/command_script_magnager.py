from .script_debut import debut_script

"""
===============================================
 EPHEC QUEST - script_manager.py
-----------------------------------------------
 Description : Handles game commands and script logic
 Author      : Matthieu
 Date        : 2025
===============================================
"""
current_handler = None

def handle_command_from_gui(command: str, gui):
    """
    Receives a command from the GUI and processes it.
    Sends back a response to be displayed in the GUI.

    Args:
        command (str): The command entered by the player
        gui (GameGUI): The GUI instance to send output to
    """
    global current_handler
    if command == "start":
        current_handler = debut_script
        debut_script(gui,None)
    elif current_handler:
        current_handler(gui, command)
    else:
        gui.display("Commande inconnue.")