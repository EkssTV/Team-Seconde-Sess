from quizz import Quizz
"""
===============================================
 EPHEC QUEST - quizz_elec.py
-----------------------------------------------
 Description : quizz anglais
 Auteur      : Stefan
 Date        : 2025-10-30
 noms NPC    : Ohmlette : se leve tjs du bon courant
===============================================
"""

schema1= """
Voici le schéma n1 
+----------------------+  LEGENDE :
|   (+) ──[ R ]──┐     |    (+) borne positive
|                │     |    (-) borne négative
|               (⏚)    |    [ R ] Résistance
|                │     |    (⏚) terre
|   (−)──────────┘     |
+----------------------+
"""
schema2 ="""
Donne moi la résistance équivalente dans ce schéma :

+----------------------+  LEGENDE :
|        3 Ohms        |
|     ┌───[ R ]──┐     |    (+) borne positive
|     |          |     |    [ R ] Résistance
|     └───[ R ]──┘     |  
|        6 Ohms        |
+----------------------+


"""

#Template
"""question0 = Quizz("Question",
                  ["1","2","3","4"],
                  3,
                  "npc")
"""
#Question niveau 1

question1 = Quizz("Donne moi la résistance nécéssaire pour faire fonctionne ce schéma :" + schema1,
                  ["350Ohm","1kOhm","10A","4V"],
                  2,
                  "Ohmlette")

question2= Quizz(" Defini moi La loi d'Ohm :",
                 ["donne la relation entre la différence de potentiel aux bornes d'une résistance et le courant la traversant. La différence de potentiel est proportionnelle au courant.",
                          "donne la relation entre la différence de potentiel aux bornes d'une résistance et le courant la traversant. La différence de potentiel est inversement proportionnelle au courant",
                          "donne la relation entre la différence de potentiel aux bornes de n'importe quel dipôle électrique et le courant le traversant. La différence de potentiel est inversement proportionnelle au courant.",
                          "donne la relation entre la différence de potentiel aux bornes de n'importe quel dipôle électrique et le courant le traversant. La différence de potentiel est proportionnelle au courant."],
                1,
                 "Ohmlette"
                 )

question3= Quizz(schema2,["3 Ohms","6 Ohms","9 Ohms","12 Ohms"],3,"Ohmlette")
#question3.ask()
#print(question2.verify_response(1))