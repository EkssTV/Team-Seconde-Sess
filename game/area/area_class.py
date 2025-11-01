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
class CreaArea:
    def __init__(self,ident,name,list_npc,near_area,simple_desc,long_desc):
        self.__ident = ident
        self.__name = name
        self.list_npc = list_npc
        self.near_area = near_area
        self.simple_desc = simple_desc
        self.long_desc = long_desc

    @property
    def id(self):
        return self.__ident

    @property
    def name(self):
        return self.__name


