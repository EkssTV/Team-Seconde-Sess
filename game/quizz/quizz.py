
#param de la classe : question, réponse(liste), la bonne réponse, le npc qui pose la question(j'en ai besoin pour le ask)
class Quizz:
    def __init__(self, question: str, answers: list, correct_response: int, npc: str):
        self.question = question
        self.answers = answers
        self.response = correct_response
        self.npc = npc

#méthod ask()
    def ask(self):
        print(f" Le professeur {self.npc} te pose la question suivante :") #le npc
        print(f"{self.question}")                                          # te pose la question
        for num, reponse in enumerate(self.answers,1):                     # génère n de question + question
            print(f"{num} : {reponse}")                                    # print du for enumerate



# method verify_response()
    def verify_response(self,player_answer):
        if player_answer  == self.response :   # boolean  comparatif réponse entrée par joeur / self.reponse
            return True
        else :
            return False



"""Template
question0 = Quizz("Question",
                  ["1","2","3","4"],
                  3,
                  "npc")

"""