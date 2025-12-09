from game.area.area_scripting import load_csv_area
from game.area.area_class import CreaArea

def test_load_csv_area():
    world = load_csv_area()

    # Vérifie que la fonction retourne bien un dictionnaire
    assert isinstance(world, dict)
    assert len(world) > 0  # Au moins une zone doit exister

    # On récupère une zone au hasard
    first_key = next(iter(world))
    area = world[first_key]

    # Vérification des postconditions
    assert isinstance(first_key, str)
    assert isinstance(area, CreaArea)
    assert isinstance(area.name, str)
    assert isinstance(area.simple_desc, str)
    assert isinstance(area.near_area, list)

