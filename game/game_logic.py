from game.player.player import Player
from game.area.area import Area

class Game:
    def __init__(self):
        self.player = Player()
        self.areas = self.load_areas()

    def load_areas(self):
            # Les zones
            place_de_l_ephec = Area(
                name="Place de L'Ephec ",
                ident="place_de_l_ephec",
                near_places=["hall_d_entree"],
                npc=[],
                objects=["id Etu"],
                description="Tu es à l'entrée de L'Ephec .",
                description_more="L'Ephec se fait grande devant toi."
            )
            hall_d_entree = Area(
                name="Hall d'entrée",
                ident="hall_d_entree",
                near_places=["place_de_l_ephec"],
                npc=[],
                objects=[],
                description="tu es dans le hall de l'ephec il y a le secretariat a ta droite.",
                description_more="flemme decrire la"
            )
            return {
                "place_de_l_ephec": hall_d_entree,
                "hall_d_entree": place_de_l_ephec
            }
    def get_current_area(self):
        return self.areas[self.player.current_area]

    def look(self):
        area = self.get_current_area()
        return f"{area.description}"

    def move(self,next_area):
        current = self.player.current_area
        current = next_area

