"""
===============================================
 EPHEC QUEST - npc_class.py
-----------------------------------------------
 Description : création du class npc
 Auteur      : STEFAN TROCH
 Date        : 2025
===============================================

"""



#Class area
class Npc:
    def __init__(self,id :str, nom: str,description : str,idQuestion:int):
        self.id = id
        self.nom = nom
        self.description = description
        self.idQuestion = idQuestion

    def __str__(self):
        return f"le NPC a qui tu parle : \n{self.nom} {self.description}"