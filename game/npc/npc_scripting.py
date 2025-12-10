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

def load_csv_npc():

    """
    Charge les données des PNJ (NPC) depuis un fichier CSV
    et retourne un dictionnaire d’objets `Npc`.

    Le fichier CSV doit contenir 4 colonnes :
        - id (str) : identifiant unique du PNJ
        - name (str) : nom du PNJ
        - description (str) : description du PNJ
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

            next(reader)                                                                # Skip de header line


            for line_number, line in enumerate(reader, start=2):                        #iterer sur chaque line du csv (line_number sert au debug)
                if len(line) != 4:                                                      #Chaque ligne doit contenir 4 colonnes
                    print(f"Ligne {line_number} ignorée, format incorrect : {line}")
                    continue

                idQuestion = []                                                         # Creer liste des id questions

                for x in line[3].split(','):                                            # On split sur les , et on ajoute a la liste
                    x = x.strip()
                    x = int(x)
                    idQuestion.append(x)

                npc = Npc(
                    id = line[0],
                    name = line[1],
                    description=line[2],
                    idQuestion=idQuestion
                )


                dico_npc[line[0]] = npc                                                 # On insère tout dans le dico NPC


    except FileNotFoundError:                                                           # Erreur de fihier introuvable
        print(f"Fichier CSV introuvable : {file_path}")

    return dico_npc



if __name__ == "__main__":
    d = load_csv_npc()
    for k, v in d.items():
        print(k, v.name,v.idQuestion,v.description)