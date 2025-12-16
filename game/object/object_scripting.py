"""
===============================================
 EPHEC QUEST - object_scripting.py
-----------------------------------------------
 Description : scripting objects
 Auteur      : Benjamin
 Date        : 2025
===============================================

"""
import csv
import os
from game.object.object_exceptions import InvalidObjectException
from game.object.object_class import CreaObject
from ..object.object_logger import  logger

def load_csv_object():
    base_path = os.path.dirname(__file__) #dossier courant
    file_path = os.path.join(base_path,"object_data.csv") #vient chercher le dossier

    objects = {} #dictionnaire objects
    try:

        with open(file_path,'r',encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file,delimiter=";")

            next(reader) #saute la première ligne

            #remplissage du dictionnaire
            for row in reader:
                if len(row) < 4:
                    logger.warning(f"Ligne CSV invalide : {row}")
                try:
                    if not row[0] or not row[1]:
                        raise ValueError("Champs obligatoires manquants")

                    objet = CreaObject(row[0],row[1],row[2],row[3]) #Création de l'objet
                    objects[row[0]] = objet #Remplissage du dictionnaire objects
                    logger.info(f"Objet [{row[0]}] créé avec succès")
                except InvalidObjectException as Invalid:
                    logger.error(f"Erreur lors de la création de l'objet {row[0]} : {Invalid}")
    except FileNotFoundError:
        logger.error(f'le fichier CSV : {file_path} est introuvable')
    return objects



if __name__ == "__main__":
    d = load_csv_object()
    for k, v in d.items():
        print(k, v.nom,v.utilite,v.id)

