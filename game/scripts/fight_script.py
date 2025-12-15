import random

from ..scripts.speak_script import people,player,world
from ..question.question_scripting import load_csv_question

step = 0
correct_answer = 0

def fight_script(gui, command, npc_id):
    global step,question,question_ans,correct_answer
    if player.health == 0 :
        gui.display("HAHAHAHAH tu n'as plus assez d'énergie pour me battre\nRetourne d'ou tu viens")
        step = 0
        return "area_deplacement"

    cmd = command
    prof = people[npc_id]
    questions = load_csv_question()
    profs_question = prof.idQuestion

    if step == 0 :
        gui.display("⚔️ Que Quizz commence !")
        gui.display(f"{prof.name} te barre la route !")
        gui.display("🔥 LE Quizz COMMENCE 🔥\n")

        step = 1
        gui.display("[Enter]")
        return None
    if step == 1:

        quest = random.choice(profs_question)
        question = questions[quest]
        question_ans = question.answers
        gui.display(question.question)
        gui.display(" Choisis entre : \n ")
        gui.display(f" la bonne c'est {question.correct_answer}")
        for index,el in enumerate(question_ans) :
            gui.display(f"{index + 1 } {el}")
        step = 1.1
        return None
    if step == 1.1 :
        if int(cmd) == question.correct_answer :
            correct_answer += 1
            step = 1
            gui.display(f"Bonne réponse, tu as :{correct_answer} de bonnes réponses")
            gui.display("[ENTER] pour la prochaine question")
            if correct_answer == 5 :
                gui.display("[ENTER]")
                step = 5
            return None
        elif not cmd in question_ans :
            gui.display("Mauvaise réponse")
            player.supp_health(1)
            #gui.update_info()
            return None

    if step == 5:
        gui.display("Bien joué tu as reussi a répondre a mes question voici pour toi")
        if prof.id == "PROFSUDO":
            player.add_inv("BADGSUDO")
            gui.display("Tu as reçu le badge du Prof SUDO ! ")
        step = 0
        gui.display("[ENTER] pour revenir a la map !")
    return "area_deplacement"
