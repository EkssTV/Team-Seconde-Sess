

class Quizz:
    def __init__(self, question: str, answers: list, correct_response: int, npc: str):
        self.question = question
        self.answers = answers
        self.response = correct_response
        self.npc = npc

    def ask(self):
        print(f" Le professeur {self.npc} te pose la question suivante :")
        print(f"{self.question}")
        for num, reponse in enumerate(self.answers,1):
            print(f"{num} : {reponse}")

    def verify_response(self):
        pass
    """def __str__(self):
        return f"{self.question},{self.answers}{self.response},{self.npc}"
    """