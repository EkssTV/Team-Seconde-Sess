from game.player.player_class import Player
from game.gui.gui_class import GameGUI
from game.scripts.command_script_magnager import handle_command_from_gui
player = Player('Ekss')
gui = GameGUI(player)
gui.root.mainloop()
