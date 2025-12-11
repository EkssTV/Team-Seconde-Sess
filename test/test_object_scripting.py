import pytest

from game.object.object_scripting import load_csv_object
from game.object.object_class import CreaObject
from game.object.object_exceptions import InvalidObjectException



# ---------------------------------------------------------------------------
# Test du chargement du CSV
# ---------------------------------------------------------------------------

def test_load_csv_object():
    objects = load_csv_object()

    # Vérifie que la fonction retourne bien un dict
    assert isinstance(objects, dict)

    # Le dictionnaire ne doit pas être vide
    assert len(objects) > 0

    # Toutes les valeurs doivent être des objets CreaObject
    for obj in objects.values():
        assert isinstance(obj, CreaObject)


# ---------------------------------------------------------------------------
# Test de la classe CreaObject
# ---------------------------------------------------------------------------

def test_creaobject_initialisation():
    obj = CreaObject(
        id="OBJ01",
        nom="Épée Légendaire",
        descri="Une arme très puissante",
        utilite="Combat"
    )

    # L’ID est transformé en liste de caractères upper → on vérifie cela
    assert obj.id == ["O", "B", "J", "0", "1"]

    # Le nom doit être correctement stocké
    assert obj.nom == "Épée Légendaire"


# ---------------------------------------------------------------------------
# Test des erreurs dans le CSV — version simple
# ---------------------------------------------------------------------------

def test_invalid_row(monkeypatch):
    """Simule un CSV avec une ligne trop courte"""

    def fake_open(*args, **kwargs):
        from io import StringIO
        return StringIO(
            "id,nom,descri,utilite,x,y\n"
            "ID1,NomSeulement\n"  # ligne invalide (2 colonnes)
        )

    monkeypatch.setattr("builtins.open", fake_open)

    with pytest.raises(InvalidObjectException):
        load_csv_object()


def test_missing_required_fields(monkeypatch):
    """Simule un CSV avec des champs obligatoires manquants"""

    def fake_open(*args, **kwargs):
        from io import StringIO
        return StringIO(
            "id,nom,descri,utilite,x,y\n"
            ",Nom,Desc,Util,X,Y\n"  # id vide → erreur
        )

    monkeypatch.setattr("builtins.open", fake_open)

    with pytest.raises(InvalidObjectException):
        load_csv_object()
