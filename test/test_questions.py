import pytest
from game.question.question_scripting import  load_csv_question
from game.question.question_class import Question

def test_load_csv_question():
    question = load_csv_question()
    assert isinstance(question,dict)
    assert len(question) > 0
    for q in  question.values():
        assert isinstance(q,Question)


#Test de la méthode correct Answer

def test_verify_correct_answer():
    q1 = Question(
        idQuestion=1,
        question="La réponse est la Réponse 1",
        answers=["Réponse1","Réponse2","Réponse3","Réponse4"],
        correct_answer=1
    )
    # Je teste ça ( une fois false, une fois true) j'ai volontairement fait +1 car dans le CSV 1ere reponse =1
    assert q1.verify(1) is True

    assert q1.verify(2) is False
    assert q1.verify(3) is False
    assert q1.verify(4) is False

    # Test du setter correct_answer
    q1.correct_answer = 2
    assert q1.correct_answer == 2  # setter fonctionne

    # Setter doit lever ValueError si indice invalide
    with pytest.raises(ValueError):
        q1.correct_answer = 5  # trop grand
