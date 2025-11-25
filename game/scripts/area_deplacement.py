from ..player.player_class import Player
from ..area.area_class import CreaArea
from ..area.area_scripting import load_csv_area
from ..npc.npc_class import *
from ..npc.npc_scripting import *
from ..object.object_class import *
from ..object.object_scripting import *
from ..question.question_class import *
from ..question.question_scripting import *
player = Player()

step = 0
def area_deplacement(gui, command):
    global step
    area = load_csv_area()[player.current_area]
    if step == 0 :
        gui.clear_output()
        gui.display(area.simple_desc)
        step = 1
        return None
    if step == 1 :
        if command == 'look' :
            gui.display(area.long_desc)
            list_of_next_area_name =" Tu peux aller :\n"
            for el in area.near_area :
                list_of_next_area_name += load_csv_area()[el].name
                list_of_next_area_name += f' [{el}]\n '
            gui.display(list_of_next_area_name)
        elif command.split(' ')[0] == 'move' :
            if command.split(' ')[1] in area.near_area :
                player.move_area(command.split(' ')[1])
                area = load_csv_area()[player.current_area]
                gui.display('TU te déplace')
                gui.display(area.simple_desc)
            else :
                gui.display("Tu n'observe pas de lieu portant ce nom")
            return None
        elif command == 'help' :
            gui.display("tape [look] pour regarder autour de toi \n tape [move ...] et l'endroit ou tu veux aller ")
        else :
            gui.display("Commande inconnue dans ce contexte")
    return None
