"""
===============================================
 EPHEC QUEST - npc_scription.py
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
    dico_npc ={}
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "npc_data3.csv")
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            reader =  csv.reader(file, delimiter=';')
            next(reader)  # SAUTE L'en-tete (premiere ligne)

            for line_number, line in enumerate(reader, start=2):  # compte les lignes
                # vérifier que la ligne a exactement 4 colonnes
                if len(line) != 4:
                    print(f"Ligne {line_number} ignorée, format incorrect : {line}")
                    continue


                npc = Npc(
                    id = line[0],
                    nom = line[1],
                    description=line[2],
                    idQuestion=[int(x.strip()) for x in line[3].split(',')]


                )
                dico_npc[line[0]] = npc
    except FileNotFoundError:
        print(f"Fichier CSV introuvable : {file_path}")


    return dico_npc



if __name__ == "__main__":
    d = load_csv_npc()
    for k, v in d.items():
        print(k, v.nom,v.idQuestion,v.description)