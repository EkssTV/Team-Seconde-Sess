from ..npc.npc_scripting import load_csv_npc
from ..question.question_scripting import load_csv_question

def fight_script(gui, command, npc_id):
    player = gui.player
    npc = load_csv_npc()[npc_id]

    idQuestions = npc.idQuestion
    questions = load_csv_question()[idQuestions]

    # Si le joueur a déjà vaincu ce NPC
    if npc.badge in player.badges:
        gui.display(f"Tu as déjà vaincu {npc.name}.")
        return "area_deplacement"




