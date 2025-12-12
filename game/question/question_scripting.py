"""
===============================================
 EPHEC QUEST - question_scripting.py
-----------------------------------------------
 Description : Chargement des questions depuis un fichier CSV
 Auteur      : Stéfan (Erreur_504)
 Date        : 01/11/2025
===============================================
"""

from game.question.question_class import Question
import csv
import os
from question_logger import logger

def load_csv_question():
    """
    Charge les questions depuis un fichier CSV et retourne un dictionnaire
    d’objets `Question`.

    Le fichier CSV doit contenir 4 colonnes :
        - id (int) : identifiant unique de la question
        - question (str) : texte de la question
        - answers (str) : liste des réponses séparées par des virgules
        - correct_answer (int) : index de la réponse correcte

    Returns:
        dict : dictionnaire dont les clés sont les identifiants des questions
               et les valeurs sont des objets `Question`.
    """
    dico_questions = {}
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "questions_data2.csv")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  # Ignorer l’en-tête

            for line_number, line in enumerate(reader, start=2):
                if len(line) != 4:
                    logger.warning(f"Ligne {line_number} ignorée, format incorrect : {line}")
                    continue
                try:

                    question_id = int(line[0])
                    question_text = line[1]
                    answers = line[2].split(',')
                    correct_answer = int(line[3])

                    questions = Question(
                        idQuestion=question_id,
                        question=question_text,
                        answers=answers,
                        correct_answer=correct_answer
                    )
                    dico_questions[question_id] = questions
                    logger.info(f"Question {question_id} chargéé avec success")
                except Exception as Error:
                    logger.error(f"Une erreur est survenue lors de la création de la question  à la {line_number}")
    except FileNotFoundError:
        logger.error("Fichier CSV introuvable : {file_path}")

    return dico_questions

if __name__ == "__main__":
    d = load_csv_question()
    for k, q in d.items():
        print(q.id, q.question, q.answers, q.correct_answer)

