from ..npc.npc_scripting import load_csv_npc
#from ..question.question_scripting import load_csv_question

def speak_script(gui, command, npc_id):
    npc =  load_csv_npc()[npc_id]
    npc_name = npc.name
    npc_desc = npc.description

    if command is None :
        gui.display(f"Tu t'approches de {npc_name}")

    gui.display(npc_desc)
    return "area_deplacement"