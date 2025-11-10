"""
===============================================
 EPHEC QUEST - area_class.py
-----------------------------------------------
 Description : création du class area
 Auteur      : Greg
 Date        : 2025
===============================================

"""
#Class area
#pylint: disable=too-many-arguments
class CreaArea:
    """Représentation des Areas"""
    def __init__(self,ident,name,list_npc,near_area,simple_desc,long_desc):
        """
        Initialise un nouvel objet Area

        Args :
        ident (str) : l'identifiant de l'"area"
        name (str) : le nom de l'"area"
        list_npc (list) : liste les identifiants des NPC
        near_area (list) : liste les identifiants des area à côté
        simple_desc : description du "area"
        long_desc : description du "area" mais plus
        """
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
