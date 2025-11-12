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
    def __init__(self,id :int, nom: str,prenom:str,description : str,idQuestion:int):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.description = description
        self.idQuestion = idQuestion

