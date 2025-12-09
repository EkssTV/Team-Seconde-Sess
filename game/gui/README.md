# 🖥️ EPHEC QUEST – Spécifications de la classe `GameGUI`

## 📌 Description
La classe `GameGUI` gère l’interface graphique du jeu **EPHEC QUEST**.  
Elle permet :

- d’afficher la narration du jeu,
- de saisir les commandes du joueur,
- de montrer les informations du joueur (nom, santé, zone),
- d’animer le texte avec un effet "machine à écrire",
- de gérer l’affichage séquentiel des messages,
- de lancer l’introduction du jeu.

Elle constitue la couche d’interaction visuelle entre le joueur et le moteur du jeu.

---

## 🧩 Attributs principaux

| Attribut | Type | Description |
|---------|------|-------------|
| `root` | `tk.Tk` | Fenêtre principale du jeu |
| `output_frame` | `tk.Frame` | Zone contenant la narration |
| `input_frame` | `tk.Frame` | Zone contenant l’entrée utilisateur |
| `info_frame` | `tk.Frame` | Panneau d’informations du joueur |
| `output_zone` | `tk.Text` | Zone d’affichage du texte narratif |
| `input_zone` | `tk.Entry` | Champ de saisie des commandes |
| `name_player` | `tk.Label` | Affiche le nom du joueur |
| `health_player` | `tk.Label` | Affiche les PV du joueur |
| `area_player` | `tk.Label` | Affiche la zone actuelle |
| `display_queue` | `list` | File d’attente des textes à afficher |
| `current_text` | `str` | Texte en cours d’animation |
| `char_index` | `int` | Position actuelle dans l’animation |
| `is_displaying` | `bool` | Indique si une animation est en cours |
| `text_speed` | `int` | Vitesse d’affichage des caractères |

---

## ✅ Fonctionnalités

### 🖼️ Initialisation de l’interface (`__init__`)
- Création de la fenêtre principale en plein écran.
- Création des trois zones :
  - **Output** : narration du jeu.
  - **Input** : saisie des commandes.
  - **Info** : informations du joueur.
- Liaison de la touche **Entrée** à la méthode `handle_command`.
- Affichage initial des informations du joueur.

---

### 📝 Affichage du texte

#### `display(text, time_to_show=2)`
Ajoute un texte à la file d’attente et lance son affichage si aucune animation n’est en cours.

#### `_start_next_display()`
Démarre l’affichage du prochain texte dans la file.

#### `animate_text()`
Affiche le texte **caractère par caractère** (effet machine à écrire).

**Règles :**
- L’entrée utilisateur est désactivée pendant l’animation.
- Une fois le texte terminé, l’entrée est réactivée.
- Si plusieurs textes sont en file, ils s’affichent dans l’ordre.

---

### ⌨️ Gestion des commandes

#### `handle_command(event)`
- Récupère la commande entrée par le joueur.
- Efface le champ de saisie.
- Transmet la commande au gestionnaire externe `handle_command_from_gui`.

---

### 🧾 Mise à jour des informations du joueur

#### `update_info(player)`
Met à jour :
- le nom,
- les points de vie,
- la zone actuelle.

---

### 🧹 Gestion de l’affichage

#### `clear_output()`
Efface entièrement la zone de narration.

---

### ❌ Quitter le jeu

#### `quit_game()`
Ferme proprement la fenêtre Tkinter.

---

### 🚀 Introduction du jeu

#### `starting_game()`
Affiche :
- un **logo ASCII** du jeu,
- un **texte d’introduction** immersif,
- les crédits des créateurs,
- une invitation à commencer (`[start]`).

Le tout est affiché via la méthode `display()` avec animation.

---

## 🔄 Comportements attendus

- L’interface doit toujours rester responsive.
- Les commandes ne doivent être acceptées **que lorsque l’animation est terminée**.
- Les informations du joueur doivent être mises à jour en temps réel.
- Les messages doivent s’afficher dans l’ordre d’arrivée.
- L’introduction doit se lancer correctement au démarrage.

---

## ✅ Critères de validation

- L’interface s’ouvre en plein écran sans erreur.
- Le texte s’affiche correctement avec l’effet machine à écrire.
- Les commandes sont envoyées au gestionnaire externe.
- Les informations du joueur se mettent à jour correctement.
- La file d’affichage fonctionne sans bloquer l’interface.
- Le bouton Entrée déclenche bien `handle_command`.
- L’introduction s’affiche correctement.
