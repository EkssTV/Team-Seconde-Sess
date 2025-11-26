"""
===============================================
 EPHEC QUEST - npc_scription.py
-----------------------------------------------
 Description : création du class npc
 Auteur      : STEFAN TROCH
 Date        : 2025
===============================================

"""

from game.npc.npc_class  import Npc
import os

def load_csv_npc():
    dico_npc ={}
    base_path = os.path.dirname(__file__)  # dossier courant
    file_path = os.path.join(base_path, "npc_data.csv")  # vient chercher le dossier
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
print(load_csv_npc())