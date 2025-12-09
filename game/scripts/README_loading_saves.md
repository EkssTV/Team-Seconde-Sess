# 💾 EPHEC QUEST – Spécifications de la fonction `loading_saves()`

## 📌 Description générale
La fonction `loading_saves()` gère **tout le processus de sélection ou création d’une sauvegarde** au lancement du jeu EPHEC QUEST.

Elle permet :

- d’afficher les sauvegardes existantes,
- de choisir une sauvegarde,
- ou de créer une nouvelle partie,
- de charger les données du joueur,
- de préparer la transition vers le script principal (`area_deplacement`).

Elle fonctionne comme **un mini‑script interactif**, basé sur un système d’étapes (`step`).

---

# ✅ Variables globales

| Variable | Type | Description |
|----------|------|-------------|
| `step` | `float/int` | Indique l’étape actuelle du processus de chargement |
| `player` | `Player` | Instance du joueur utilisée pour charger ou créer une partie |

---

# ✅ Fonction : `loading_saves(gui, command=None)`

## 🎯 Objectif
Gérer l’ensemble du menu de chargement :

- afficher les sauvegardes disponibles,
- permettre la création d’un nouveau joueur,
- charger une sauvegarde existante,
- initialiser les données du joueur,
- préparer la transition vers le script principal.

---

## 🧩 Paramètres

| Paramètre | Type | Description |
|----------|------|-------------|
| `gui` | `GameGUI` | Interface graphique utilisée pour afficher les messages |
| `command` | `str` ou `None` | Commande entrée par le joueur (ou `None` pour l’étape initiale) |

---

## 📤 Valeur de retour

| Retour | Description |
|--------|-------------|
| `None` | Dans la majorité des cas |
| `"area_deplacement"` | Lorsque le chargement est terminé et que le jeu doit commencer |

---

# 🧠 Déroulement par étapes

## ✅ **Étape 0 : affichage du menu de chargement**
Déclenchée lorsque `command is None`.

Actions :

- Efface l’écran.
- Affiche le menu de chargement.
- Liste les sauvegardes disponibles via `saved_player()`.
- Demande au joueur de choisir une sauvegarde ou de taper `new`.

Transition → `step = 1`.

---

## ✅ **Étape 1 : choix du joueur ou création**
Analyse la commande entrée :

### Si `command == "new"` :
→ Transition vers `step = 1.1`.

### Si `command` correspond à une sauvegarde existante :
→ Transition vers `step = 2`.

### Sinon :
→ Message d’erreur :  
```
Commande inconnue dans ce contexte.
```

---

## ✅ **Étape 1.1 : demande du nom du nouveau joueur**
Affiche :
```
Bienvenue à l’EPHEC ! Avant de commencer, quel est ton nom ?
```

Transition → `step = 1.2`.

---

## ✅ **Étape 1.2 : création d’un nouveau joueur**
Actions :

1. Enregistre le nom du joueur.
2. Définit le chemin de sauvegarde.
3. Sauvegarde immédiatement un fichier JSON vide.
4. Recharge les données du joueur.
5. Met à jour l’interface graphique.
6. Affiche un message de bienvenue.
7. Affiche les statistiques du joueur.
8. Efface l’écran.
9. Change le script du joueur vers `area_deplacement`.
10. Affiche un message de chargement.

Retourne :
```
"area_deplacement"
```

---

## ✅ **Étape 2 : chargement d’une sauvegarde existante**
Si `command` correspond à une sauvegarde :

1. Charge les données du joueur.
2. Met à jour l’interface graphique.
3. Affiche un message de bienvenue.
4. Efface l’écran.
5. Change le script vers `area_deplacement`.
6. Affiche un message de chargement.

Retourne :
```
"area_deplacement"
```

Sinon → message d’erreur.

---

# ✅ Résumé des transitions

| Étape | Condition | Action | Transition |
|-------|-----------|--------|------------|
| 0 | `command is None` | Affiche le menu | → 1 |
| 1 | `new` | Demande le nom | → 1.1 |
| 1 | sauvegarde existante | Prépare chargement | → 2 |
| 1 | autre | Erreur | reste en 1 |
| 1.1 | — | Demande le nom | → 1.2 |
| 1.2 | nom entré | Crée joueur + charge | → `area_deplacement` |
| 2 | sauvegarde valide | Charge joueur | → `area_deplacement` |
| 2 | autre | Erreur | reste en 2 |

---

# ✅ Critères de validation

- Le menu de chargement doit s’afficher correctement.
- Les sauvegardes doivent être listées correctement.
- La création d’un nouveau joueur doit fonctionner.
- Le chargement d’une sauvegarde existante doit fonctionner.
- Les informations du joueur doivent être mises à jour dans l’interface.
- La transition vers `area_deplacement` doit être renvoyée correctement.
- Les erreurs doivent être affichées proprement.
