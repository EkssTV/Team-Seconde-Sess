"""
===============================================
 EPHEC QUEST - npc_scription.py
-----------------------------------------------
 Description : création du class npc
 Auteur      : STEFAN TROCH
 Date        : 2025
===============================================

"""

from .npc_class import Npc


def get_data_in_file(filename):
    dico_npc ={}
    with open(filename,'r',encoding='utf-8') as file:
        next(file)  # SAUTE L'en-tete (premiere ligne)
        for line in file:  # boucle itérative sur chaque ligne
            colonnes = line.rstrip().split("\t")  # je split sur la tabulation / saut de ligne
            colonnes[4] = colonnes[4].rstrip().split(";")

            npc = Npc(
                id = colonnes[0],
                nom = colonnes[1],
                prenom=colonnes[2],
                description=colonnes[3],
                idQuestion=colonnes[4]

            )
            dico_npc[colonnes[0]] = npc

    return dico_npc




