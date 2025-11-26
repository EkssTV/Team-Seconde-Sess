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
from game.area.exceptions import InvalidAreaException
from game.area.area_class import CreaArea

def load_csv_area():
    base_path = os.path.dirname(__file__) #dossier courant
    file_path = os.path.join(base_path,"area_data.csv") #vient chercher le dossier

    world = {} #dictionnaire area

    with open(file_path,'r',encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file,delimiter=";")

        next(reader) #saute la première ligne

        #lecture des données du reader
        for row in reader:
            if len(row) < 6:
                raise InvalidAreaException(f"Ligne CSV invalide : {row}")

            try:
                list_near_area = list(map(lambda x: x.strip(), row[3].split(",")))
                list_npc = list(map(lambda x: x.strip(), row[2].split(",")))

                area = CreaArea(
                    row[0], row[1], list_npc, list_near_area, row[4], row[5])
                world[row[0]] = area
            except Exception as e:
                raise InvalidAreaException(f"Erreur lors de la création de l'area {row[0]} : {e}")

    return world






