"""
===============================================
 EPHEC QUEST - area_class.py
-----------------------------------------------
 Description :
     Ce fichier définit la classe CreaArea, utilisée pour
     représenter une zone du jeu (Area). Une Area contient
     un identifiant, un nom, la liste des PNJ présents, les
     zones adjacentes, ainsi qu'une description simple et
     une description détaillée.

     L'idée de séparer cette classe dans ce module a été
     proposée via une IA afin de rendre la structure du
     projet plus lisible et d'éviter de surcharger le module
     de chargement des zones.

 Rôle de la classe :
     - Modéliser une zone du jeu sous forme d'objet.
     - Faciliter les accès aux attributs (nom, id, voisins…).
     - Servir de structure de base pour les interactions.

 Préconditions :
     - ident, name, simple_desc et long_desc doivent être
       des chaînes non vides.
     - list_npc et near_area doivent être des listes, même
       vides.
     - Les identifiants doivent correspondre à ceux du CSV.

 Postconditions :
     - Une instance valide de CreaArea est créée.
     - Les attributs __ident et __name sont protégés (privés).
     - Les propriétés id et name deviennent accessibles via
       des getters (@property).

 Auteur : Gregory Ly.
 Date   : 2025
===============================================
"""
import re

class CreaArea:
    """Représentation des Areas"""
    def __init__(self,ident : str,name : str,list_npc : str,near_area : str,simple_desc : str,long_desc : str):
        """ Vérifie le format des IDs d'Area"""
        if not re.match(r"^[A-Z0-9]+$", ident):
            raise ValueError(f"ID d'area invalide : {ident}")

        self.__ident = ident
        self.__name = name
        self.list_npc = list_npc
        self.near_area = near_area
        self.simple_desc = simple_desc
        self.long_desc = long_desc

    @property
    def id(self):
        """Retourne l'identifiant de l'area"""
        return self.__ident
    @property
    def name(self):
        """Retourne le nom de l'area"""
        return self.__name
