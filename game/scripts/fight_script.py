import random

from ..scripts.speak_script import people,player,world,objs
from ..question.question_scripting import load_csv_question

step = 0
correct_answer = 0
BADGES = {
    "PROFSUDO": "BADGSUDO",
    "PROFOHM": "BADGELEC",
    "PROFDISTRO": "BADGDISTRO",
    "PROFTECH": "BADGTECH",
    "PROFWEB": "BADGWEB",
    "PROFANGL": "BADGANG",
    "PROFSQL": "BADGSQL",
    "PROFSIGN": "BADGSIGN",
    "PROFMATH": "BADGMATH",
    "PROFLEG": "BADGLEG",
}
for_leg = {  "BADGSUDO","BADGELEC","BADGDISTRO","BADGTECH","BADGWEB","BADGANG","BADGSQL","BADGSIGN","BADGMATH"}
def fight_script(gui, command, npc_id):
    global step,question,question_ans,correct_answer,BADGES
    if "CARTEETU" not in player.inv :
        gui.display("🚫 Tu n'as pas de carte étudiante et tu oses me défier ? Quelle honte...")
        gui.display("➡️ Retourne d’où tu viens !")
        step = 0
        return "area_deplacement"
    if player.health == 0:
        gui.display("💀 Tu n’as plus assez d’énergie pour me battre...")
        gui.display("➡️ Retourne d’où tu viens !")
        step = 0
        return "area_deplacement"

    if npc_id == "PROFLEG" and not for_leg.issubset(player.inv):
        gui.display(" ❌ Tu n’as pas assez aquis de badge pour me deffier...")
        gui.display("➡️ Retourne d’où tu viens !")
        step = 0
        return "area_deplacement"
    cmd = command
    prof = people[npc_id]
    questions = load_csv_question()
    profs_question = prof.idQuestion


    # --- Début du quiz ---
    if step == 0:
        gui.display("═══════════════════════════════")
        gui.display(" ⚔️  LE QUIZZ COMMENCE ! ⚔️ ")
        gui.display("═══════════════════════════════")
        gui.display(f"👨‍🏫 {prof.name} te barre la route !")
        gui.display("🔥 Réponds correctement pour avancer 🔥\n")
        step = 1
        gui.display("👉 [Appuie sur ENTER]")
        return None

    # --- Affichage des questions ---
    if step == 1:
        quest = random.choice(profs_question)
        question = questions[quest]
        question_ans = question.answers

        gui.display("📜 Question :")
        gui.display(f"❓ {question.question}\n")
        gui.display("Choisis ta réponse :\n")
        for index, el in enumerate(question_ans):
            gui.display(f"   {index + 1}. {el}")
        step = 1.1
        return None

    # --- Bonne réponse ---
    if step == 1.1:
        if int(cmd) == question.correct_answer:
            correct_answer += 1
            step = 1
            gui.display("✅ Bonne réponse !")
            gui.display(f"🏆 Score actuel : {correct_answer} / 5")
            gui.display("👉 [ENTER] pour la prochaine question")
            if correct_answer == 5:
                gui.display("🎉 Tu as répondu correctement à toutes les questions !")
                gui.display("👉 [ENTER]")
                step = 5
            return None
        else:
            gui.display("❌ Mauvaise réponse...")
            gui.display("💔 Tu perds 1 point de vie")
            player.supp_health(1)
            gui.update_info(player)
            return None

    # --- Fin du quiz ---
    if step == 5:
        gui.display("✨ Bien joué ! Tu as réussi le défi ✨")
        if prof.id in BADGES :
            badge = BADGES[prof.id]
            if badge not in player.inv :
                player.add_inv(badge)
                gui.display("🎖️ Tu as reçu le badge du Prof !")
                gui.update_info(player)
            else :
                gui.display("🎖️ Tu as déja reçu le badge du Prof !")
        if npc_id == "PROFLEG" :
            gui.display("👑 Tu as vaincu tous les professeurs, y compris moi...")
            gui.display("🏆 Ta quête est terminée, félicitations !")
        step = 0
        gui.display("👉 [ENTER] pour revenir à la carte")
    return "area_deplacement"
