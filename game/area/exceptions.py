"""
===============================================
 EPHEC QUEST - exceptions.py
-----------------------------------------------
 Description :
     Module contenant les exceptions personnalisées
     utilisées dans le module Area du jeu.

     L’idée de placer ces exceptions dans un fichier
     séparé vient d’un conseil reçu via une IA, afin de
     mieux structurer le projet et d’isoler les erreurs
     liées au chargement des zones.

 Exception principale :
     - InvalidAreaException :
         Levée lorsqu’une zone lue dans le CSV est
         invalide ou impossible à construire.

 Préconditions :
     - Aucune : les exceptions peuvent être importées
       librement par les autres modules.

 Postconditions :
     - Lorsqu’une exception est levée, le programme
       interrompt le chargement courant et redirige
       l’erreur vers l'appelant.

 Auteur : Gregory Ly
 Date   : 2025
===============================================
"""

class InvalidAreaException(Exception):
    """Erreur levée lorsqu'une zone du fichier CSV est invalide."""
    pass
