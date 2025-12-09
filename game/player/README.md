# 🧙‍♂️ EPHEC QUEST – Spécifications de la classe `Player`

## 📌 Description
La classe `Player` représente un joueur dans le jeu **EPHEC QUEST**.  
Elle gère :

- son identité,
- son inventaire,
- ses points de vie,
- sa position dans le monde,
- le script narratif en cours,
- la sauvegarde et le chargement de sa progression.

Elle constitue un élément central du système de jeu.

---

## 📦 Attributs

| Attribut | Type | Description |
|---------|------|-------------|
| `__name` | `str` | Nom privé du joueur (encapsulé) |
| `inv` | `list[str]` | Inventaire contenant les ID des objets |
| `health` | `int` | Points de vie actuels |
| `current_area` | `str` | Zone actuelle du joueur |
| `current_script` | `str` | Script narratif en cours |
| `save_path` | `str` | Chemin du fichier de sauvegarde JSON |

### ✅ Contraintes
- Le nom ne peut pas être vide.
- Les PV ne peuvent pas descendre sous 0.
- L’inventaire contient uniquement des identifiants d’objets valides.

---

## ⚙️ Fonctionnalités

### 🎒 Gestion de l’inventaire

| Méthode | Description |
|--------|-------------|
| `add_inv(id_obj)` | Ajoute un objet à l’inventaire |
| `supp_inv(id_obj)` | Retire un objet si présent |
| `show_inv()` | Retourne une description textuelle des objets |

**Règles :**
- Inventaire vide → message adapté.
- Les objets sont chargés via `load_csv_object()` pour afficher nom, description et utilité.

---

### ❤️ Gestion de la santé

| Méthode | Description |
|--------|-------------|
| `add_health(much)` | Augmente les PV |
| `supp_health(much)` | Diminue les PV |

**Règles :**
- Les PV ne deviennent jamais négatifs.
- Si PV = 0 → message `"player dead"`.

---

### 🗺️ Déplacement et progression

| Méthode | Description |
|--------|-------------|
| `move_area(new_area)` | Change la zone actuelle |
| `change_script(new_script)` | Change le script narratif |

---

### 🧾 Gestion du nom

| Méthode | Description |
|--------|-------------|
| `name` (getter) | Retourne le nom |
| `name` (setter) | Modifie le nom avec validation |

**Règles :**
- Le nom ne peut pas être vide ou composé d’espaces.
- En cas d’erreur → `ValueError`.

---

### 💾 Sauvegarde & Chargement

| Méthode | Description |
|--------|-------------|
| `save()` | Sauvegarde l’état du joueur dans un fichier JSON |
| `load(path)` | Charge un état depuis un fichier JSON |

**Règles de sauvegarde :**
- Le fichier est créé dans `saves/`.
- Données sauvegardées : nom, santé, inventaire, zone, script.

**Règles de chargement :**
- Fichier manquant → message d’erreur.
- JSON invalide → message d’erreur.
- Erreur I/O → message d’erreur.

---

## 🔄 Comportements attendus

### À l’initialisation
- Inventaire vide si non fourni.
- Dossier `saves/` créé automatiquement.
- Valeurs par défaut :
  - `health = 5`
  - `current_area = "PLACEEPHEC"`
  - `current_script = "script_debut"`

### Affichage
La méthode `__str__()` retourne un résumé formaté de l’état du joueur.

---

## ✅ Critères de validation

- Ajouter un objet → inventaire augmente.
- Retirer un objet inexistant → aucune erreur.
- Les PV ne deviennent jamais négatifs.
- Le nom vide est refusé.
- La sauvegarde produit un JSON valide.
- Le chargement restaure correctement l’état.
- `show_inv()` affiche correctement les objets.