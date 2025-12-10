# 🧙‍♂️ EPHEC QUEST – Spécifications de la classe `CreaObject`

## 📌 Description
La classe `CreaObject` représente un objet dans le jeu **EPHEC QUEST**.  
Elle gère :

- son identité unique (`id`)  
- son nom (`nom`)  
- sa description (`descri`)  
- son utilité dans le jeu (`utilite`)  

Les objets sont chargés depuis un fichier CSV via la fonction `load_csv_object()`.  
Chaque objet constitue un élément du gameplay : inventaire, interactions, progression.

---

## 📦 Attributs

| Attribut | Type | Description |
|---------|------|-------------|
| `__id` | `list[str]` | Identifiant unique de l’objet, stocké en majuscules |
| `__nom` | `str` | Nom de l’objet |
| `descri` | `str` | Description de l’objet |
| `utilite` | `str` | Utilité ou rôle de l’objet |

### ✅ Contraintes
- L’ID est toujours converti en majuscules et stocké sous forme de liste de caractères.
- Le nom ne peut pas être vide.
- Les objets doivent avoir au moins 4 champs valides dans le CSV (`id`, `nom`, `descri`, `utilite`).

---

## ⚙️ Fonctionnalités

### 📂 Chargement d’objets depuis CSV

| Fonction | Description |
|----------|-------------|
| `load_csv_object()` | Charge tous les objets depuis `object_data.csv` et retourne un dictionnaire `id → CreaObject` |

**Règles :**  
- CSV avec moins de 4 colonnes → `InvalidObjectException` levée  
- Champs obligatoires vides → `InvalidObjectException` levée  
- Toutes les valeurs retournées sont des instances de `CreaObject`  

---

### 🏗️ Création d’objet

| Méthode / Attribut | Description |
|------------------|-------------|
| `__init__(id, nom, descri, utilite)` | Initialise un objet avec les champs du CSV |
| `id` (getter) | Retourne l’ID en liste de caractères majuscules |
| `nom` (getter) | Retourne le nom de l’objet |

---

## 🔄 Comportements attendus

### À l’initialisation
- `id` est converti automatiquement en majuscules via regex.  
- `nom`, `descri` et `utilite` sont stockés tels quels.  

### Chargement CSV
- Toutes les lignes valides sont transformées en objets et ajoutées dans le dictionnaire.  
- Les lignes invalides déclenchent `InvalidObjectException` avec message précis.  

---

## ✅ Critères de validation

- `load_csv_object()` retourne un dictionnaire non vide.  
- Chaque entrée du dictionnaire est un `CreaObject`.  
- Les objets ont un `id` en majuscules.  
- Les lignes CSV invalides sont rejetées avec exception.  
- Les champs obligatoires (`id`, `nom`) doivent être présents.
