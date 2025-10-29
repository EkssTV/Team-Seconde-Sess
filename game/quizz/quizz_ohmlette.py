from quizz import Quizz
#utilisation de la classe QUIZZ pour créer les différentes questions
question1 = Quizz("Quelle est la bonne réponse?",
                  ["la réponse 4","la réponse 4","la réponse 4","la réponse 4"],
                  3,
                  "Ohmlette")











#TEST en LOCAL (je vais supp)
"""print(question1.ask())
reponse = int(input("Donne ta réponse : "))

if question1.verify_response(reponse):
    print('bravo')
else:
    print('faux')"""