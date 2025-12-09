import pytest
from game.player.player_class import Player
import json

def test_add_inv():
    player = Player(name="test")
    player.add_inv("KEY01")

    assert "KEY01" in player.inv
    assert len(player.inv) == 1


def test_move_area():
    player = Player(name="test", current_area="PLACEEPHEC")

    player.move_area("BIBLIOTHEQUE")

    assert player.current_area == "BIBLIOTHEQUE"


def test_save(tmp_path, monkeypatch):
    # On force le chemin de sauvegarde dans un dossier temporaire
    fake_save = tmp_path / "test_save.json"

    player = Player(name="testplayer")
    player.save_path = str(fake_save)  # on remplace le chemin réel

    player.save()

    # Vérifie que le fichier existe
    assert fake_save.exists()

    # Vérifie le contenu JSON
    with open(fake_save, "r") as f:
        data = json.load(f)

    assert data["name"] == "testplayer"
    assert data["health"] == player.health
    assert data["inv"] == player.inv
    assert data["current_area"] == player.current_area
    assert data["current_script"] == player.current_script

def test_load(tmp_path):
    fake_save = tmp_path / "load_test.json"

    # On crée un faux fichier JSON
    data = {
        "name": "loaded_player",
        "health": 10,
        "inv": ["KEY01", "POTION"],
        "current_area": "BIBLIOTHEQUE",
        "current_script": "script_test"
    }

    with open(fake_save, "w") as f:
        json.dump(data, f)

    player = Player(name="temp")
    player.load(fake_save)

    assert player.name == "loaded_player"
    assert player.health == 10
    assert player.inv == ["KEY01", "POTION"]
    assert player.current_area == "BIBLIOTHEQUE"
    assert player.current_script == "script_test"

def test_show_inv(monkeypatch):
    # Fake object class
    class FakeObj:
        def __init__(self, id,nom, descri, utilite):
            self.__id = id
            self.nom = nom
            self.descri = descri
            self.utilite = utilite

    # Fake load_csv_object()
    def fake_loader():
        return {
            "KEY01": FakeObj("KEY01","Clé", "Une clé", "Ouvre une porte"),
        }

    # On remplace load_csv_object par notre version fake
    monkeypatch.setattr("game.player.player_class.load_csv_object", fake_loader)

    player = Player(name="test")
    player.inv = ["KEY01"]

    result = player.show_inv()
    assert "KEY01" in result
    assert "Clé" in result
    assert "Une clé" in result
    assert "Ouvre une porte" in result
