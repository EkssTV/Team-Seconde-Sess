from game.area.area_class import CreaArea

def test_CreaArea():
    area = CreaArea(
        ident="HALL01",
        name="Hall d'entrée",
        list_npc=["NPC01", "NPC02"],
        near_area=["PARK", "ROOM1"],
        simple_desc="Une grande entrée",
        long_desc="Une entrée spacieuse avec des colonnes anciennes"
    )

    assert area.id == "HALL01"
    assert area.name == "Hall d'entrée"
    assert area.list_npc == ["NPC01", "NPC02"]
    assert area.near_area == ["PARK", "ROOM1"]
    assert area.simple_desc == "Une grande entrée"
    assert area.long_desc == "Une entrée spacieuse avec des colonnes anciennes"
