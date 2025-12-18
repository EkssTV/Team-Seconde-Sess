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
import re

class CreaObject:
    def __init__(self, id, nom, descri, utilite):
        self.__id = [re.sub(r'(.*)', lambda m: m.group(1).upper(), a) for a in id]
        self.__nom = nom
        self.descri = descri
        self.utilite = utilite

    @property
    def id(self):
        return self.__id



    @property
    def nom(self):
        return self.__nom


    def nom(self, new_nom):
        if not new_nom or not new_nom.strip():
            raise ValueError("Le nom de l'objet ne peut pas être vide.")
        self.__nom = new_nom
    
