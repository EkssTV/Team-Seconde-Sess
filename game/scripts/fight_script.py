from ..npc.npc_scripting import load_csv_npc
from ..question.question_scripting import load_csv_question

def fight_script(gui, command, npc_id):
    player = gui.player
    npc = load_csv_npc()[npc_id]

    # Si déjà vaincu → retour direct
    if player.get_npc_state(npc_id) == "defeated":
        gui.display(f"Tu as déjà vaincu {npc.name}.")
        return "area_deplacement"

    # INITIALISATION DU COMBAT
    if command is None:
        gui.flash_screen(flashes=2, color="darkred")
        gui.display("⚔️ Le combat commence !")
        gui.display(f"{npc.name} te barre la route !")
        gui.display("🔥 LE COMBAT COMMENCE 🔥\n")

        questions = load_csv_question()

        gui.fight_state = {
            "npc_id": npc_id,
            "question_ids": list(npc.idQuestion),
            "index": 0,
            "score": 0,
            "total": len(npc.idQuestion),
            "questions": questions
        }


    return None
