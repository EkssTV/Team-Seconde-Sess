"""
===============================================
 EPHEC QUEST - question_class.py
-----------------------------------------------
 Description : création du class Questions
 Auteur      : Stéfan (Erreur_504)
 Date        : 01/11/2025
===============================================
"""
import random
class Question:
    def __init__(self,idQuestion: int,question: str,answers : list, correct_answer: int):
        self.id = idQuestion
        self.question = question
        self.answers = answers
        self.correct_answer = int(correct_answer)



    def ask(self):
        bonne_reponse = self.answers[self.correct_answer]
        self.answers.sort(key=lambda x: random.random())
        self.correct_answer = self.answers.index(bonne_reponse)

        print(f'{self.question}')         #print la question
        for num, rep in enumerate(self.answers,1): #boucle print Question + générer n° Question
            print(f'{num} : {rep}')

    def verify(self,input_player):
        if input_player == self.correct_answer:
            return True
        else:
            return False

