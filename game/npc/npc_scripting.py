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
from .npc_class import Npc


def load_csv():
    dico_npc ={}
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "npc_data.csv")
    with open(file_path,'r',encoding='latin-1') as file:
        next(file)  # SAUTE L'en-tete (premiere ligne)
        for line in file:  # boucle itérative sur chaque ligne
            colonnes = line.rstrip().split(";")  # je split sur ;
            colonnes = [c.strip().replace('"', '') for c in colonnes]
            colonnes[3] = colonnes[3].rstrip().split(",")


            npc = Npc(
                id = colonnes[0],
                nom = colonnes[1],
                description=colonnes[2],
                idQuestion=colonnes[3],


            )
            dico_npc[colonnes[0]] = npc
    return dico_npc



if __name__ == "__main__":
    d = get_data_in_file("npc_data.csv")
    for k, v in d.items():
        print(k, v.nom,v.idQuestion,v.description)