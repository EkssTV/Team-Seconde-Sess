"""
===============================================
 EPHEC QUEST - object_class.py
-----------------------------------------------
 Description : scripting objects
 Auteur      : Benjamin
 Date        : 2025
===============================================

"""
import csv
import os
from game.object.object_class import CreaObject

def load_csv_object():
    base_path = os.path.dirname(__file__) #dossier courant
    file_path = os.path.join(base_path,"object_data.csv") #vient chercher le dossier

    objects = {} #dictionnaire objects

    with open(file_path,'r',encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file,delimiter=",")

        next(reader) #saute la première ligne

        #remplissage du dictionnaire
        for row in reader:
            objet = CreaObject(row[0],row[1],row[2],row[3]) #Création de l'objet
            objects[row[0]] = objet #Remplissage du dictionnaire objects

    return objects

print(load_csv_object())




