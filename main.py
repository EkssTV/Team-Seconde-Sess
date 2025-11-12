from game.player.player_class import Player
from game.gui.gui_class import GameGUI,player
from game.scripts.command_script_magnager import handle_command_from_gui


gui = GameGUI(player)
gui.starting_game()
gui.root.mainloop()
