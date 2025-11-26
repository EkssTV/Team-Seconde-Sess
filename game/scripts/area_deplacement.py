from ..player.player_class import Player
from ..area.area_class import CreaArea
from ..area.area_scripting import load_csv_area
from ..npc.npc_class import *
from ..npc.npc_scripting import *
from ..object.object_class import *
from ..object.object_scripting import *
from ..question.question_class import *
from ..question.question_scripting import *
from .loading_saves import player
"""
===============================================
 EPHEC QUEST - area_deplacement.py
-----------------------------------------------
 Description : scripting area
 Auteur      : Ekss
 Date        : 2025
===============================================

"""
current_player = player
step = 0
def area_deplacement(gui, command):
    """
            ===============================================
             EPHEC QUEST - area_deplacement
            -----------------------------------------------
             Description : Gère les interactions du joueur
                           dans une zone (Area).
            -----------------------------------------------
             Paramètres :
                gui (GameGUI) :
                    Instance de l'interface graphique utilisée
                    pour afficher les informations au joueur.
                command (str) :
                    La commande saisie par le joueur (ex: "look",
                    "move hal01", "help").

            -----------------------------------------------
             Fonctionnement :
                - Utilise la variable globale `step` pour suivre
                  l'état du script (progression dans la zone).
                - Récupère la zone actuelle du joueur via
                  `player.current_area` et les données chargées
                  par `load_csv_area()`.

                Étape 0 :
                    - Nettoie l'affichage (`gui.clear_output()`).
                    - Affiche la description simple de la zone
                      (`area.simple_desc`).
                    - Passe à l'étape 1.

                Étape 1 :
                    - Si la commande est "look" :
                        → Affiche la description détaillée de la zone
                          (`area.long_desc`).
                        → Liste les zones accessibles depuis la zone
                          actuelle (`area.near_area`) avec leur nom
                          et leur identifiant.
                    - Si la commande commence par "move <zone_id>" :
                        → Vérifie si la zone demandée est dans
                          `area.near_area`.
                        → Si oui :
                            * Déplace le joueur avec `player.move_area()`.
                            * Recharge la nouvelle zone.
                            * Affiche un message de déplacement et la
                              description simple de la nouvelle zone.
                        → Sinon :
                            * Affiche un message d'erreur.
                    - Si la commande est "help" :
                        → Affiche les commandes disponibles ("look",
                          "move ...").
                    - Sinon :
                        → Affiche "Commande inconnue dans ce contexte".

            -----------------------------------------------
             Retour :
                None (les résultats sont affichés via l'objet `gui`).

            -----------------------------------------------
             Notes :
                - La logique repose sur une variable globale `step`
                  pour gérer la progression.
                - `player` est une instance globale de Player,
                  utilisée pour suivre la zone actuelle et les
                  déplacements.
                - `load_csv_area()` recharge les données des zones
                  à chaque appel, ce qui garantit que les infos
                  sont toujours à jour mais peut être optimisé.
            ===============================================
            """

    global step
    area = load_csv_area()[player.current_area]
    if step == 0 :
        gui.clear_output()
        gui.display(area.simple_desc)
        step = 1
        return None
    if step == 1 :
        if command == 'look' :
            gui.display(area.long_desc)
            list_of_next_area_name =" Tu peux aller :\n"
            for el in area.near_area :
                list_of_next_area_name += load_csv_area()[el].name
                list_of_next_area_name += f' [{el}]\n '
            gui.display(list_of_next_area_name)
        elif command.split(' ')[0] == 'move' :
            if command.split(' ')[1] in area.near_area :
                player.move_area(command.split(' ')[1])
                area = load_csv_area()[player.current_area]
                gui.display('TU te déplace')
                gui.display(area.simple_desc)
                gui.update_info(player)
            else :
                gui.display("Tu n'observe pas de lieu portant ce nom")
            return None
        elif command == 'interact':

            if len(area.list_npc) :
                str_of_npc = ""
                for el in area.list_npc:
                    npc = load_csv_npc()[el]
                    str_of_npc += f"[{el}]\n{npc.description}\n"
                gui.display(str_of_npc)
            else :
                gui.display("Tu ne remarque pas de personne ou chose pour lequel tu pourrais intéragir")
        elif command.split(' ')[0] == 'speak' :
            if command.split(' ')[1] in area.list_npc:
                gui.display("Prochain MAJ mais tu peux voir ça en attendant :")
                npc = load_csv_npc()[command.split(' ')[1]]
                gui.display(f'{npc}')
            else:
                gui.display("Tu n'observe pas de personne ou chose portant ce nom")
        elif command == 'save' :
            player.save()
            gui.display('Partie sauvegarder')
            gui.display(f"Voici tes stat actuel : {player} ")
            gui.update_info(player)
        elif command =='quit' :
            gui.quit_game()
        elif command =='clear':
            gui.clear_output()
        elif command == 'who' :
            gui.display(f"Voici tes stat actuel : {player} ")
        elif command == 'help':
            help_text = """
            ===============================================
             EPHEC QUEST - Manuel des Commandes
            -----------------------------------------------

             Commandes générales :
               - look
                   Affiche la description détaillée de la zone
                   et liste les zones accessibles.
               - move <zone_id>
                   Déplace le joueur vers une zone voisine.
               - help
                   Affiche ce manuel des commandes.
               - clear
                   Nettoie l'affichage.
               - quit
                   Quitte le jeu.

             Commandes liées au joueur :
               - who
                   Affiche les statistiques actuelles du joueur.
               - inventory
                   Montre le contenu de l'inventaire.
               - save
                   Sauvegarde la partie et affiche les stats.

             Commandes liées aux PNJ :
               - interact
                   Liste les PNJ présents dans la zone avec leur description.
               - speak <npc_id>
                   Permet de parler à un PNJ (fonctionnalité en cours de dev).

            ===============================================
            """
            gui.display(help_text,500)
        elif command == 'inventory' :
            gui.display(f'Voici ce que tu as dans ton inventaire:\n{player.show_inv()}')
        elif command =='UIA': #code de triche (pour test l'inventory)
            player.add_inv("CARETU")
            player.save()
        else :
            gui.display("Commande inconnue dans ce contexte")
    return None
