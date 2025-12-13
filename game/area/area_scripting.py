"""
===============================================
 EPHEC QUEST - area_scripting.py
-----------------------------------------------
 Description :
     Charge les zones (areas) du jeu depuis le fichier
     CSV area_data.csv. Chaque ligne du fichier est
     transformée en un objet CreaArea, puis stockée
     dans un dictionnaire indexé par l'id de la zone.

     L’idée de séparer ce module dans un fichier dédié
     vient d’un conseil reçu via une IA afin d’améliorer
     la clarté et l’organisation du projet.

 Fonctionnement :
     - Lecture du fichier CSV.
     - Vérification du bon format de chaque ligne.
     - Conversion des champs en structures Python.
     - Création des objets CreaArea.
     - Construction du dictionnaire world.

 Préconditions :
     - Le fichier area_data.csv doit exister dans le
       même dossier que ce script.
     - Chaque ligne du CSV doit contenir au minimum
       6 colonnes valides.
     - Les listes (PNJ, zones voisines) doivent être
       correctement séparées par des virgules.
     - La classe CreaArea doit être importable.

 Postconditions :
     - Retourne un dictionnaire : { id_area : CreaArea }.
     - Chaque élément retourné est une instance valide
       de CreaArea.
     - Une InvalidAreaException est levée si une ligne
       du CSV est invalide.

 Auteur : Gregory Ly
 Date   : 2025
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



