"""
===============================================
 EPHEC QUEST - npc_class.py
-----------------------------------------------
 Description : création of the NPC class
 Auteur      : STEFAN TROCH
 Date        : 2025
===============================================

"""
class InvalidNpcException(Exception):
    """Exception levée lorsqu’une entrée PNJ dans le fichier CSV est invalide."""
    pass


#NPC class Definition
class Npc:
    """
   Classe représentant un PNJ (Personnage Non Joueur).

   Attributes:
       id (str) : identifiant unique du PNJ
       name (str) : nom du PNJ
       description (str) : description du PNJ
       idQuestion (list[int]) : liste des IDs de questions associées au PNJ
    """

    def __init__(self,id :str, name: str,description : str,idQuestion:int):
        """
       Initialise un objet PNJ.

       Args:
           id (str) : identifiant du PNJ
           name (str) : nom du PNJ
           description (str) : description du PNJ
           idQuestion (list[int]) : liste des IDs de questions liées au PNJ
        """

        self.id = id
        self.name = name
        self.description = description
        self.idQuestion = idQuestion

    def __str__(self):
        """Retourne une représentation textuelle du PNJ (nom et description)."""
        return f"le NPC a qui tu parles : \n{self.name} {self.description}"