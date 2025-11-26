"""
===============================================
 EPHEC QUEST - question_scripting.py
-----------------------------------------------
 Description : création du script Questions
 Auteur      : Stéfan (Erreur_504)
 Date        : 01/11/2025
===============================================
"""

from .question_class import Question

def get_data_in_file(filename):
    dico_questions={}
    id_question = 1


    with open(filename,'r',encoding='latin-1') as file:
        next(file)# SAUTE L'en-tete (premiere ligne)
        for line in file:                               #boucle itérative sur chaque ligne
            colonnes = line.rstrip().split(";")# je split sur la ;
            colonnes_nettoyees =[]
            for c in colonnes:
                c = c.replace('"', '')
                c = c.strip()
                colonnes_nettoyees.append(c)
            colonnes = colonnes_nettoyees
            answers = []   # je craye une liste pour la colonne réponses
            for rep in colonnes[2:-1]:
                answers.append(rep.strip())

            q = Question(
                idNPC=colonnes[0],
                question=colonnes[1],
                answers=answers,
                correct_answer=colonnes[-1]
            )

            dico_questions[id_question] = q
            id_question += 1

    return dico_questions

if __name__ == "__main__":
    d = get_data_in_file("question_data.csv")
    for k, q in d.items():
        print(k, q.question, q.answers, q.correct_answer)

