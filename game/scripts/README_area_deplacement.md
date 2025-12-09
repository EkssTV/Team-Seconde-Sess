# 🧭 EPHEC QUEST – Spécifications des fonctions du module `area_deplacement.py`

## 📌 Description générale
Ce module gère **la logique de déplacement et d’interaction du joueur dans les zones** du jeu EPHEC QUEST.  
Il interprète les commandes textuelles du joueur et déclenche les actions correspondantes :

- déplacement entre zones,
- observation,
- interaction avec les PNJ,
- gestion de l’inventaire,
- sauvegarde,
- aide,
- etc.

Il s’agit du **cœur du gameplay textuel**.

---

# ✅ Fonction : `area_deplacement(gui, command)`

## 🎯 Objectif
Interpréter une commande utilisateur et exécuter l’action correspondante dans le contexte de la zone actuelle.

Cette fonction :

- charge les zones depuis le CSV,
- récupère la zone actuelle du joueur,
- analyse la commande,
- exécute l’action (déplacement, look, interact, speak, save…),
- met à jour l’interface graphique,
- renvoie éventuellement une instruction spéciale (ex : `speak_script <npc_id>`).

---

## 🧩 Paramètres

| Paramètre | Type | Description |
|----------|------|-------------|
| `gui` | `GameGUI` | Interface graphique utilisée pour afficher les messages et mettre à jour les infos |
| `command` | `str` | Commande textuelle entrée par le joueur |

---

## 📤 Valeur de retour

| Retour | Description |
|--------|-------------|
| `None` | Dans la majorité des cas |
| `"speak_script <npc_id>"` | Si le joueur utilise la commande `speak <id>` |

---

## 🧠 Déroulement général

1. **Chargement du monde** via `load_csv_area()`.
2. **Récupération de la zone actuelle** du joueur.
3. **Découpage de la commande** (`cmd`, `arg`).
4. **Gestion d’un système d’étapes** (`step`) :
   - `step == 0` → affichage de la description simple de la zone.
   - `step == 1` → interprétation des commandes.
5. **Analyse de la commande** :
   - déplacement,
   - observation,
   - interaction,
   - inventaire,
   - sauvegarde,
   - aide,
   - etc.

---

# 🧭 Détail des commandes gérées

## 🚶 Commande : déplacement (`move`, `go`, `aller`, `avancer`)
### Syntaxe :
```
move <zone_id>
go <zone_id>
aller <zone_id>
avancer <zone_id>
```

### Fonctionnement :
- Analyse via **regex**.
- Vérifie si la destination est dans `area.near_area`.
- Si oui :
  - met à jour la zone du joueur,
  - affiche la nouvelle description,
  - met à jour le panneau d’informations.
- Sinon :
  - affiche un message d’erreur.

---

## 👀 Commande : `look`
Affiche :

- la description longue de la zone,
- la liste des zones accessibles.

---

## 🗣️ Commande : `interact`
Liste les PNJ présents dans la zone :

- charge les PNJ via `load_csv_npc()`,
- affiche leur description.

Si aucun PNJ → message adapté.

---

## 💬 Commande : `speak <npc_id>`
Si le PNJ existe dans la zone :

✅ retourne :  
```
speak_script <npc_id>
```

Sinon → message d’erreur.

---

## 💾 Commande : `save`
- Sauvegarde la partie via `player.save()`.
- Affiche les stats du joueur.
- Met à jour le panneau d’informations.

---

## ❌ Commande : `quit`
Ferme le jeu via `gui.quit_game()`.

---

## 🧹 Commande : `clear`
Efface la zone d’affichage.

---

## 👤 Commande : `who`
Affiche les statistiques actuelles du joueur.

---

## 📚 Commande : `help`
Affiche un manuel complet des commandes disponibles.

---

## 🎒 Commande : `inventory`
Affiche le contenu de l’inventaire du joueur.

---

## 🧪 Commande : `UIA` (cheat code)
Ajoute un objet de test dans l’inventaire.

---

## ❓ Commande inconnue
Affiche :
```
Commande inconnue dans ce contexte
```

---

# ✅ Critères de validation

- Le chargement des zones doit fonctionner sans erreur.
- Les commandes doivent être correctement interprétées.
- Les déplacements doivent respecter les zones accessibles.
- Les PNJ doivent être correctement listés et identifiés.
- Les sauvegardes doivent fonctionner.
- L’interface doit être mise à jour après chaque action.
- Les erreurs doivent être affichées proprement.
