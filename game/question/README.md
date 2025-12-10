# EPHEC QUEST - Gestion des Questions

Ce module permet de gérer les **questions à choix multiple** du projet *EPHEC QUEST*.  
Les questions sont définies dans un fichier CSV (`questions_data2.csv`) et chargées en mémoire sous forme d’objets Python.

---

## 📂 Structure du package

- `question_class.py` : définit la classe `Question`.
- `question_scripting.py` : contient la fonction `load_csv_question()` qui lit le fichier CSV et crée les objets Question.
- `questions_data2.csv` : fichier de données contenant la liste des questions.

---

## 📑 Format du fichier CSV

Le fichier `questions_data2.csv` doit contenir les colonnes suivantes (séparées par `;`) :

| id (int) | question (str) | answers (str) | correct_answer (int) |
|----------|----------------|---------------|----------------------|
| Identifiant unique | Texte de la question | Réponses séparées par des virgules | Index de la bonne réponse |

## 📑 Exemple de fichier CSV

Le fichier `questions_data2.csv` doit respecter ce format :

| id | question                                       | answers                                                                        | correct_answer |
|----|------------------------------------------------|--------------------------------------------------------------------------------|----------------|
| 1  | Le potentiomètre est une résistance variable ? |Vrai,Faux                                  | 2              |

---

---

## ⚙️ Utilisation

```python
from game.question.question_scripting import load_csv_question

# Charger les questions depuis le fichier CSV
questions_dict = load_csv_question()

# Afficher les questions
for id, q in questions_dict.items():
    print(q.id, q.question, q.answers, q.correct_answer)
```
## 🚨 Gestion des erreurs
- Si le fichier CSV est introuvable, un message d’erreur est affiché.
- Si une ligne du CSV est invalide (mauvais format), elle est ignorée.


## 👨‍💻 Auteur
Projet développé par Stéfan (Erreur_504) – 2025.
