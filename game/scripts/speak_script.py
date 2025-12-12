from ..npc.npc_scripting import load_csv_npc
#from ..question.question_scripting import load_csv_question

def speak_script(gui, command, npc_id):
    gui.display("tu t'approches de quelqu'un\n [bye] pour finir la discussion \n [look] pour avoir sa description \n [who] pour savoir à qui tu parles")
    parts = command.split()
    cmd = parts[0].lower() if parts else ""
    arg = parts[1].upper() if len(parts) > 1 else None
    npc = load_csv_npc()[npc_id]

    if cmd == "bye" :
        gui.display("SAlem")
        return "area_deplacement"

    if cmd == "look":
        gui.display(npc.description)
    if cmd == "who":
        gui.display(npc.name)
    return f'speak_script {npc_id}'