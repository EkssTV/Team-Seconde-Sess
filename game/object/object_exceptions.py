"""
===============================================
 EPHEC QUEST - object_exceptions.py
-----------------------------------------------
 Description :
     Module contenant les exceptions personnalisées
     utilisées dans le module Object du jeu.

     L’idée de placer ces exceptions dans un fichier
     séparé vient d’un conseil reçu via une IA, afin de
     mieux structurer le projet et d’isoler les erreurs
     liées au chargement des objets.

 Exception principale :
     - InvalidObjectException :
         Levée lorsqu’un objet lue dans le CSV est
         invalide ou impossible à construire.

 Préconditions :
     - Aucune : les exceptions peuvent être importées
       librement par les autres modules.

 Postconditions :
     - Lorsqu’une exception est levée, le programme
       interrompt le chargement courant et redirige
       l’erreur vers l'appelant.

 Auteur : JUNION Benjamin
 Date   : 2025
===============================================
"""

class InvalidObjectException(Exception):
    """Erreur levée lorsqu'un objet du fichier CSV est invalide."""
    pass
