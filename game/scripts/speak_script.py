from ..npc.npc_scripting import load_csv_npc
from ..scripts.area_deplacement import player,people,world

def speak_script(gui, command, npc_id):
    npc =  people[npc_id]
    gui.display("\n========== DIALOGUE ==========")
    gui.display(f"👤 {npc.name}")
    gui.display("------------------------------")
    if npc.role == 'neutral' :
        if npc.id == 'CAFE' :
            gui.display("Tu as reçu du café")
            player.add_inv("CAFE")
        gui.display(f"{npc.name} : {npc.description}")
    if npc.role == 'friendly':
        gui.display(" Salut c'est jhonny \n")
    if npc.role =='hostile' :
        return f"fight_script {npc_id}"

    gui.display("\n(Le dialogue se termine. Tu peux regarder autour de toi avec [look].)\n")
    return "area_deplacement"
