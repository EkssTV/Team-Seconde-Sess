# 🧠 EPHEC QUEST – Spécifications du module `script_manager.py`

## 📌 Description générale
Le module `script_manager.py` est le **chef d’orchestre du système de commandes** dans EPHEC QUEST.  
Il gère :

- la réception des commandes venant de l’interface graphique,
- la délégation vers les bons scripts (déplacement, dialogue, chargement…),
- les transitions entre différents “handlers” (états du jeu),
- la gestion des erreurs dans les scripts.

Il constitue le **noyau logique** qui relie l’interface utilisateur au moteur narratif.

---

# ✅ Constantes et variables globales

## `HANDLER_MAP`
Dictionnaire associant des noms de scripts à leurs fonctions :

| Clé                  | Fonction associée  | Rôle                                                      |
|----------------------|--------------------|-----------------------------------------------------------|
| `"area_deplacement"` | `area_deplacement` | Gestion du déplacement et des interactions dans les zones |
| `"speak_script"`     | `speak_script`     | Gestion des dialogues avec les PNJ                        |
| `"loading_saves"`    | `loading_saves`    | Chargement de la sauvegarde au début du jeu               |

Ce mapping permet de **changer dynamiquement de logique de traitement** selon le contexte.

---

## `current_handler`
Variable globale contenant **le script actuellement actif**.

- `None` → aucun script actif (état initial)
- fonction → un script en cours (ex : `area_deplacement`)

---

# ✅ Fonction : `handle_command_from_gui(command: str, gui)`

## 🎯 Objectif
Traiter une commande envoyée par l’interface graphique et :

- soit la déléguer au script actif,
- soit activer un nouveau script,
- soit afficher un message d’erreur.

C’est la **porte d’entrée principale** de toutes les commandes du joueur.

---

## 🧩 Paramètres

| Paramètre | Type | Description |
|----------|------|-------------|
| `command` | `str` | Commande textuelle entrée par le joueur |
| `gui` | `GameGUI` | Interface graphique permettant d’afficher les messages |

---

## 📤 Valeur de retour
La fonction ne retourne rien (`None`).  
Elle agit **par effets de bord** :

- affichage dans l’interface,
- changement du handler actif,
- exécution d’un script.

---

# 🧠 Logique détaillée

## 1. ✅ Si un handler est actif
```
if current_handler:
```

Alors :

1. La commande est envoyée au handler :
   ```
   result = current_handler(gui, command)
   ```

2. Si le handler renvoie une instruction spéciale du type :
   ```
   speak_script <npc_id>
   ```
   → alors un **nouveau handler personnalisé** est créé :
   ```
   current_handler = lambda g, c: speak_script(g, c, npc_id)
   ```

3. Si le handler renvoie un nom présent dans `HANDLER_MAP`  
   → transition vers un autre script :
   ```
   current_handler = HANDLER_MAP[result]
   ```

4. Si une erreur survient :
   - affichage d’un message d’erreur,
   - réinitialisation du handler.

---

## 2. ✅ Si aucun handler n’est actif
Le module gère uniquement **les commandes globales**.

### Commande : `start`
- Active le script `loading_saves`
- Lance immédiatement le chargement :
  ```
  current_handler(gui, None)
  ```

### Commande : `help`
Affiche :
```
Tape 'start' pour commencer
```

### Autre commande
Affiche :
```
Commande inconnue.
```

---

# ✅ Résumé des transitions possibles

| Situation                             | Action                                           |
|---------------------------------------|--------------------------------------------------|
| Handler actif                         | La commande est envoyée au script courant        |
| Handler renvoie `"speak_script <id>"` | Activation d’un handler personnalisé pour ce PNJ |
| Handler renvoie un nom de script      | Transition vers ce script                        |
| Commande `"start"`                    | Activation du script `loading_saves`             |
| Commande `"help"`                     | Affichage d’un message d’aide                    |
| Autre commande                        | Message d’erreur                                 |

---

# ✅ Critères de validation

- Les commandes doivent être correctement routées vers les scripts.
- Les transitions entre scripts doivent fonctionner sans erreur.
- Les dialogues PNJ doivent activer un handler dédié.
- Les erreurs doivent être affichées proprement dans l’interface.
- Le jeu doit démarrer correctement avec la commande `start`.
- Les commandes globales doivent fonctionner même sans handler actif.
