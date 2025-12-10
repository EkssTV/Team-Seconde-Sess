# 🏰 EPHEC QUEST – Spécifications de la classe `CreaArea`

## 📌 Description
La classe `CreaArea` représente une zone (area) dans le jeu **EPHEC QUEST**.  
Chaque zone possède :

- un identifiant unique (`id`)  
- un nom (`name`)  
- une liste de PNJ présents (`list_npc`)  
- une liste de zones adjacentes (`near_area`)  
- une description simple (`simple_desc`)  
- une description détaillée (`long_desc`)  

Les zones sont chargées depuis un fichier CSV via la fonction `load_csv_area()`.  
Chaque zone constitue un élément central du monde du jeu, permettant la navigation et les interactions.

---

## 📦 Attributs

| Attribut | Type | Description |
|----------|------|-------------|
| `__ident` | `str` | Identifiant privé de la zone |
| `__name` | `str` | Nom privé de la zone |
| `list_npc` | `list[str]` | Liste des PNJ présents dans la zone |
| `near_area` | `list[str]` | Liste des identifiants des zones adjacentes |
| `simple_desc` | `str` | Description courte de la zone |
| `long_desc` | `str` | Description détaillée de la zone |

### ✅ Contraintes
- `__ident` et `__name` sont protégés (privés) et accessibles via getters.  
- `list_npc` et `near_area` doivent toujours être des listes, même vides.  
- Chaque ligne CSV doit contenir au moins 6 colonnes valides.  

---

## ⚙️ Fonctionnalités

### 📂 Chargement des zones depuis CSV

| Fonction | Description |
|----------|-------------|
| `load_csv_area()` | Charge toutes les zones depuis `area_data.csv` et retourne un dictionnaire `id → CreaArea` |

**Règles :**  
- CSV avec moins de 6 colonnes → `InvalidAreaException` levée  
- Les listes de PNJ et de zones voisines sont séparées par des virgules et nettoyées des espaces  
- Toutes les valeurs retournées sont des instances de `CreaArea`  

---

### 🏗️ Création d’une zone

| Méthode / Attribut | Description |
|------------------|-------------|
| `__init__(ident, name, list_npc, near_area, simple_desc, long_desc)` | Initialise une zone avec les champs du CSV |
| `id` (getter) | Retourne l’identifiant de la zone |
| `name` (getter) | Retourne le nom de la zone |

---

## 🔄 Comportements attendus

### À l’initialisation
- Les listes `list_npc` et `near_area` sont toujours des listes Python.  
- `__ident` et `__name` sont protégés et accessibles via getters.  

### Chargement CSV
- Toutes les lignes valides sont transformées en zones et ajoutées dans le dictionnaire `world`.  
- Les lignes invalides déclenchent `InvalidAreaException` avec message précis.  

---

## ✅ Critères de validation

- `load_csv_area()` retourne un dictionnaire non vide.  
- Chaque entrée du dictionnaire est une instance de `CreaArea`.  
- Les identifiants (`id`) correspondent aux clés du dictionnaire.  
- Les listes de PNJ et de zones adjacentes sont correctement traitées.  
- Les lignes CSV invalides sont rejetées avec exception.