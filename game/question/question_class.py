"""
===============================================
 EPHEC QUEST - area_class.py
-----------------------------------------------
 Description : création du class Questions
 Auteur      : Stéfan (Erreur_504)
 Date        : 01/11/2025
===============================================
"""

class Question:
    def __init__(self,idNPC : int,question: str,answers : list, correct_answer: int):
        self.idNPC = idNPC
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
