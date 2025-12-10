"""
===============================================
 EPHEC QUEST - question_class.py
-----------------------------------------------
 Description : Question class definition
 Auteur      : Stéfan (Erreur_504)
 Date        : 01/11/2025
===============================================
"""
import re
import random


class Question:
    """
    Représente une question à choix multiple.

    Attributes:
        id (int) : identifiant unique de la question
        question (str) : texte de la question
        answers (list[str]) : liste des réponses possibles
        correct_answer (int) : index de la réponse correcte (commence à 1)
    """


    def __init__(self, idQuestion: int, question: str, answers: list, correct_answer: int):
        """
        Initialise un objet Question.

        Args:
            idQuestion (int) : identifiant unique de la question
            question (str) : texte de la question
            answers (list[str]) : liste des réponses possibles
            correct_answer (int) : index de la réponse correcte (commence à 1)
        """

        self.id = idQuestion
        self.question = question
        cleaned_answers = []  # Création d'une liste réponse

        for i in answers:
            cleaned_a = re.sub(r'^\s+|\s+$', '', i)         # Suppression des espaces devant et derrière avec REGEX
            cleaned_answers.append(cleaned_a)

        self.answers = cleaned_answers
        self._correct_answer = int(correct_answer)

    # Getter
    @property
    def correct_answer(self):
        """Retourne l’index de la réponse correcte."""
        return self._correct_answer

    # Setter
    @correct_answer.setter
    def correct_answer(self, value):
        """
        Définit l’index de la réponse correcte avec validation.

        Raises:
            ValueError : si l’index est invalide.
        """
        if value == 0 or value > len(self.answers):
            raise ValueError("Indice de la réponse invalide")
        self._correct_answer = value

    def ask(self):
        """ Affiche la question et mélange les réponses. """

        good_answer_index = self.answers[self.correct_answer]           # On sauvegarde l'index de la bonne réponse avant le shuffle
        self.answers.sort(key=lambda x: random.random())
        self.correct_answer = self.answers.index(good_answer_index)

        print(f'{self.question}')
        for num, rep in enumerate(self.answers, 1):
            print(f'{num} : {rep}')

    def verify(self, input_player):
        """
        Vérifie si la réponse donnée par le joueur est correcte.

        Args:
            input_player (int) : index choisi par le joueur

        Returns:
            bool : True si la réponse est correcte, False sinon.
        """

        if input_player == self.correct_answer:
            return True
        else:
            return False
