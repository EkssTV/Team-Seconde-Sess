# EPHEC QUEST - Gestion des PNJ

Ce package permet de gérer les **PNJ (Personnages Non Joueurs)** du projet *EPHEC QUEST*.  
Les PNJ sont définis dans un fichier CSV (`npc_data3.csv`) et chargés en mémoire sous forme d’objets Python.

---

## 📂 Structure du package

- `npc_class.py` : définit la classe `Npc` et l’exception `InvalidNpcException`.
- `npc_scripting.py` : contient la fonction `load_csv_npc()` qui lit le fichier CSV et crée les objets PNJ.
- `npc_data3.csv` : fichier de données contenant la liste des PNJ.

---

## 📑 Format du fichier CSV

Le fichier `npc_data3.csv` doit contenir les colonnes suivantes (séparées par `;`) :

| id (str) | name (str) | description (str) | idQuestion (str) |
|----------|------------|-------------------|------------------|
| Identifiant unique du PNJ | Nom du PNJ | Description du PNJ | Liste d’IDs de questions séparées par des virgules |

## 📑 Exemple de fichier CSV

Le fichier `npc_data3.csv` doit respecter ce format :

| id | name              | description                                                                    | idQuestion |
|----|-------------------|--------------------------------------------------------------------------------|------------|
| PROFANGL  | Bytespeech | Chaque mot qu'elle prononce semble compressé                                   | 1,3,4,5    |
| PROFOHM   | Ohmlette    | On dit qu'il peut allumer une ampoule rien qu'en fronçant les sourcils.(...)". | 7,8,9,10   |

---

## ⚙️ Utilisation

```python
from game.npc.npc_scripting import load_csv_npc

# Charger les PNJ depuis le fichier CSV
pnj_dict = load_csv_npc()

# Afficher les PNJ
for id, npc in pnj_dict.items():
    print(id, npc.name, npc.idQuestion, npc.description)
```

## 🚨 Gestion des erreurs
- Si le fichier CSV est introuvable, un message d’erreur est affiché.
- Si une ligne du CSV est invalide (mauvais format), elle est ignorée.
## 👨‍💻 Auteur

Projet développé par Stefan Troch (2025).
