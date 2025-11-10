"""
===============================================
 EPHEC QUEST - object_class.py
-----------------------------------------------
 Description : création du class object
 Auteur      : Benjamin
 Date        : 2025
===============================================

"""
#Class objet
class ObjectInventory:
    def __init__(self, id, nom, descri, utilite):
        self.__id = id
        self.__nom = nom
        self.descri = descri
        self.utilite = utilite

    def id(self):
        return self.__id

    def nom(self):
        return self.__nom

    
