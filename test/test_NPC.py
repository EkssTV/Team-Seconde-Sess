import pytest
from game.npc.npc_scripting import load_csv_npc
from game.npc.npc_class import Npc

# Charger le CSV et renvoyer un dictionnaire
def test_load_csv_npc():
    npcs = load_csv_npc()
    assert isinstance(npcs, dict)        # doit renvoyer un dict
    assert len(npcs) > 0                 # il doit y avoir au moins un NPC

    # Verification des values (attributs)
    for npc in npcs.values():
        assert isinstance(npc, Npc)
        assert hasattr(npc, "id")
        assert hasattr(npc, "name")
        assert hasattr(npc, "description")
        assert hasattr(npc, "idQuestion")
        assert isinstance(npc.idQuestion, list)  # liste d'IDs
        # ID des questions = entiers ?
        for qid in npc.idQuestion:
            assert isinstance(qid, int)

# Creation NPC
def test_npc_str_and_attributes():
    npc = Npc(
        id="npc1",
        name="PNJ Test",
        description="Description du PNJ",
        idQuestion=[1,2,3]
    )

    assert npc.id == "npc1"
    assert npc.name == "PNJ Test"
    assert npc.description == "Description du PNJ"
    assert npc.idQuestion == [1,2,3]

    # Vérifie le __str__, qu'il n'y ai pas d'erreurs
    s = str(npc)
    assert "PNJ Test" in s
    assert "Description du PNJ" in s
