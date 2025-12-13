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
        gui.flash_screen()
        gui.display("⚠️ UN DÉFI APPROCHE ⚠️")
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

    # ÉTAT DU COMBAT
    state = gui.fight_state
    q_id = state["question_ids"][state["index"]]
    question = state["questions"][q_id]

    # Vérification réponse joueur
    try:
        answer = int(command)
    except ValueError:
        gui.display("👉 Entre le numéro de ta réponse.")
        return None

    if answer == question.correct_answer:
        gui.display("✅ Bonne réponse !")
        state["score"] += 1
    else:
        gui.display("❌ Mauvaise réponse.")

    state["index"] += 1

    # FIN DU COMBAT
    if state["index"] >= state["total"]:
        gui.display("\n🏁 FIN DU COMBAT")

        if state["score"] >= state["total"] // 2:
            gui.display("🎉 Victoire !")
            player.set_npc_state(npc_id, "defeated")
            if npc.badge:
                player.badges.add(npc.badge)
        else:
            gui.display("💀 Défaite…")

        player.save()
        del gui.fight_state
        return "area_deplacement"

    # QUESTION SUIVANTE
    next_q_id = state["question_ids"][state["index"]]
    next_q = state["questions"][next_q_id]

    gui.display(f"\n❓ {next_q.question}")
    for i, ans in enumerate(next_q.answers, start=1):
        gui.display(f"{i}. {ans}")

    return None
