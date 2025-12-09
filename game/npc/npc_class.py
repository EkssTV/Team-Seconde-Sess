"""
===============================================
 EPHEC QUEST - npc_class.py
-----------------------------------------------
 Description : création du class npc
 Auteur      : STEFAN TROCH
 Date        : 2025
===============================================

"""
class InvalidNpcException(Exception):
    """Erreur levée lorsqu'un NPC du fichier CSV est invalide."""
    pass


#Definition de la class Npc
class Npc:

    def __init__(self,id :str, nom: str,description : str,idQuestion:int):
        """
         Initialisation de l'objet NPC.
         Args:
              id(str) :l'identifiant NPC
              nom(str):nom du NPC
              description(stp) :description du npc
              idQuestion(int) : n de question liée au NPC
          """
        self.id = id
        self.nom = nom
        self.description = description
        self.idQuestion = idQuestion

    def __str__(self):
        """Retourne nom + description du NPC"""
        return f"le NPC a qui tu parles : \n{self.nom} {self.description}"