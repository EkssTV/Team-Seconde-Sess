"""
===============================================
 EPHEC QUEST - area_class.py
-----------------------------------------------
 Description : scripting area
 Auteur      : Greg
 Date        : 2025
===============================================

"""
import csv
import os
from game.area.area_class import CreaArea

def load_csv_area():
    base_path = os.path.dirname(__file__) #dossier courant
    file_path = os.path.join(base_path,"area_data.csv") #vient chercher le dossier

    world = {} #dictionnaire area

    with open(file_path,'r',encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file,delimiter=";")

        next(reader) #saute la première ligne

        #remplissage du dictionnaire
        for row in reader:
            area = CreaArea(row[0],row[1],row[2],row[3],row[4],row[5]) #Création de l'objet
            world[row[0]] = area #Remplissage du dictionnaire world

    return world


load_csv_area()





