"""
===============================================
 EPHEC QUEST - npc_scripting.py
-----------------------------------------------
 Description : création du class npc
 Auteur      : STEFAN TROCH
 Date        : 2025
===============================================

"""
import os
from game.npc.npc_class  import Npc, InvalidNpcException
import csv
from .npc_logger import logger
def load_csv_npc():

    """
    Charge les données des PNJ (NPC) depuis un fichier CSV
    et retourne un dictionnaire d’objets `Npc`.

    Le fichier CSV doit contenir 6 colonnes :
        - id (str) : identifiant unique du PNJ
        - name (str) : nom du PNJ
        - description (str) : description PNJ
        - idQuestion (str) : liste d’IDs de questions séparées par des virgules

    Returns:
        dict : Dictionnaire dont les clés sont les identifiants des PNJ
               et les valeurs sont des objets `Npc`.
    """

    dico_npc ={}
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "npc_data3.csv")

    try:
        with open(file_path,'r',encoding='utf-8') as file:
            reader =  csv.reader(file, delimiter=';')
            """Skip du header"""
            next(reader)

            """itérer sur chaque ligne du CSV, sert au debut si erreur de data dans le fichier"""
            for line_number, line in enumerate(reader, start=2):
                if len(line) != 6:
                    logger.warning(f"Ligne {line_number} ignorée, format incorrect : {line}")
                    continue

                idQuestion = []
                """Creer la liste des Questions. On split sur les ','"""
                for x in line[3].split(','):
                    try:
                        x = x.strip()
                        x = int(x)
                        idQuestion.append(x)
                    except ValueError:
                        logger.error(f"ligne {line_number}, idQuestion {x} invalide")

                try:
                    npc = Npc(
                        id = line[0],
                        name = line[1],
                        description=line[2],
                        idQuestion=idQuestion,
                        role =line[4],
                        badge=line[5]
                    )


                    dico_npc[line[0]] = npc
                    logger.info(f'NPC [{npc.id}]{npc.name} à été créé avec succes')
                except InvalidNpcException as Invalid:
                    logger.error(f"la ligne {line_number} : Le NPC {Invalid} est incorrect")
    #Gestion des erreurs de fichiers introuvable --> fichier log
    except FileNotFoundError:
        logger.error(f"Fichier CSV introuvable : {file_path}")

    return dico_npc



if __name__ == "__main__":
    d = load_csv_npc()
    for k, v in d.items():
        print(k, v.name,v.idQuestion,v.description,v.badge,v.state)