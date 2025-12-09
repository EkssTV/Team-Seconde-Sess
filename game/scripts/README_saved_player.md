# 📁 EPHEC QUEST – Spécifications de la fonction `saved_player()`

## 📌 Description générale
La fonction `saved_player()` permet de **récupérer la liste des sauvegardes existantes** dans le dossier `saves/`.  
Elle est utilisée dans le menu de chargement pour afficher les parties disponibles.

Elle retourne uniquement **les noms des fichiers sans extension**, afin de représenter directement les noms des joueurs.

---

# ✅ Fonction : `saved_player()`

## 🎯 Objectif
Lister toutes les sauvegardes présentes dans le dossier `saves/`, en renvoyant une liste triée des noms de joueurs.

---

## 🧩 Paramètres
La fonction **ne prend aucun paramètre**.

---

## 📤 Valeur de retour

| Type | Description |
|------|-------------|
| `list[str]` | Liste triée des noms de sauvegardes (sans extension) |

Exemple de retour :
```
["benjamin", "gregory", "matthieu"]
```

---

# 🧠 Déroulement détaillé

## ✅ 1. Définition du chemin du dossier
```
path_to_saves = "saves"
```

---

## ✅ 2. Vérification de l’existence du dossier
Si le dossier n’existe pas :

- une exception `SaveDirectoryError` est levée,
- avec un message explicite.

Cela évite de continuer avec un chemin invalide.

---

## ✅ 3. Lecture du contenu du dossier
La fonction tente de lister les fichiers :

```
files = os.listdir(path_to_saves)
```

Si une erreur survient (permissions, corruption…) :

- une exception `SaveDirectoryError` est levée,
- contenant la cause exacte.

---

## ✅ 4. Filtrage des fichiers valides
Pour chaque fichier trouvé :

1. Construction du chemin complet.
2. Vérification qu’il s’agit bien d’un fichier (et non d’un dossier).
3. Extraction du nom **sans extension** via :
   ```
   os.path.splitext(file)[0]
   ```
4. Ajout du nom dans une liste temporaire.

---

## ✅ 5. Tri alphabétique
La liste est triée **sans tenir compte de la casse** :

```
sorted_list = sorted(list_saved_player_cleared, key=lambda x: x.lower())
```

Cela garantit un affichage propre et cohérent dans le menu de chargement.

---

## ✅ 6. Retour de la liste triée
La fonction renvoie la liste finale.

---

# ✅ Critères de validation

- Le dossier `saves/` doit exister.
- La fonction doit lever une exception claire si le dossier est introuvable.
- La fonction doit lever une exception claire si le dossier ne peut pas être lu.
- Seuls les fichiers doivent être pris en compte (pas les dossiers).
- Les noms doivent être retournés **sans extension**.
- La liste doit être triée alphabétiquement, insensible à la casse.

---

# ✅ Exemple d’utilisation

```
for save in saved_player():
    print(save)
```

Sortie possible :
```
alex
benjamin
matthieu
```
