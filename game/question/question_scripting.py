"""
===============================================
 EPHEC QUEST - question_scripting.py
-----------------------------------------------
 Description : création du script Questions
 Auteur      : Stéfan (Erreur_504)
 Date        : 01/11/2025
===============================================
"""

from game.question.question_class import Question
import csv
import os

def load_csv_question():
    dico_questions={}
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "questions_data2.csv")

    try:
        with open(file_path,'r',encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)

            for line_number, line in enumerate(reader,start=2):
                if len(line) != 4:
                    print(f"Ligne {line_number} ignorée, format incorrect : {line}")
                    continue
                question_id = int(line[0])
                question_text = line[1]
                answers = line[2].split(',')  # transformer la chaîne en liste
                correct_answer = int(line[3])

                questions = Question(
                    idQuestion = question_id,
                    question = question_text,
                    answers=answers,
                    correct_answer=correct_answer
                )
                dico_questions[question_id] = questions
    except FileNotFoundError:
        print(f"Fichier CSV introuvable : {file_path}")

    return dico_questions

if __name__ == "__main__":
    d = load_csv_question()
    for k,q in d.items():
        print(q.id, q.question, q.answers, q.correct_answer)