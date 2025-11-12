from game.player.player_class import Player
from game.gui.gui_class import GameGUI,player
from game.scripts.command_script_magnager import handle_command_from_gui
from game.scripts.script_debut import debut_script

gui = GameGUI(player)
gui.starting_game()
gui.root.mainloop()
