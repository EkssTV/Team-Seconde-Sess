
#param de la classe : question, réponse(liste), la bonne réponse, le npc qui pose la question(j'en ai besoin pour le ask)
class Quizz:
    def __init__(self, question: str, answers: list, correct_response: int, npc: str):
        self.question = question
        self.answers = answers
        self.response = correct_response
        self.npc = npc

#méthod poser la question : for enumerate pour générer des numéros de questions / et on démarre a 1
    def ask(self):
        print(f" Le professeur {self.npc} te pose la question suivante :")
        print(f"{self.question}")
        for num, reponse in enumerate(self.answers,1):
            print(f"{num} : {reponse}")
# vérification de la question (in progress)
    def verify_response(self):
        pass








#test perso / sera supprimé par ma part
    """def __str__(self):
        return f"{self.question},{self.answers}{self.response},{self.npc}"
    """