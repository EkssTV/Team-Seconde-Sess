"""
===============================================
 EPHEC QUEST - question_scripting.py
-----------------------------------------------
 Description : création du script Questions
 Auteur      : Stéfan (Erreur_504)
 Date        : 01/11/2025
===============================================
"""

from question_class import Question

def get_data_in_file(filename):
    dico_questions={}
    id_question = 1


    with open(filename,'r') as file:
        next(file)                                      # SAUTE L'en-tete (premiere ligne)
        for line in file:                               #boucle itérative sur chaque ligne
            colonnes = line.rstrip().split("\t")        # je split sur la tabulation / saut de ligne
            colonnes[2] = colonnes[2].rstrip().split(";")   # je craye une liste pour la colonne réponses

            q = Question(
                idNPC=colonnes[0],
                question=colonnes[1],
                answers=colonnes[2],
                correct_answer=colonnes[3]
            )

            dico_questions[id_question] = q
            id_question += 1

    return dico_questions



