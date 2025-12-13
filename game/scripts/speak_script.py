from ..npc.npc_scripting import load_csv_npc

def speak_script(gui, command, npc_id):
    player = gui.player
    npc =  load_csv_npc()[npc_id]
    npc_name = npc.name
    npc_desc = npc.description

    gui.display("\n========== DIALOGUE ==========")
    gui.display(f"👤 {npc_name}")
    gui.display("------------------------------")

    gui.display(f"{npc_name} : {npc_desc}")

    gui.display("\n(Le dialogue se termine. Tu peux regarder autour de toi avec [look].)\n")

    player.set_npc_state(npc_id, "spoken")
    player.save()
    return "area_deplacement"
