
"""
===============================================
 EPHEC QUEST - script_manager.py
-----------------------------------------------
 Description : Handles game commands and script logic
 Author      : Matthieu
 Date        : 2025
===============================================
"""


def handle_command_from_gui(command: str, gui):
    """
    Receives a command from the GUI and processes it.
    Sends back a response to be displayed in the GUI.

    Args:
        command (str): The command entered by the player
        gui (GameGUI): The GUI instance to send output to
    """
#exemple de test
    response = f"> {command}\nYou said: {command}"
    gui.display(response)
