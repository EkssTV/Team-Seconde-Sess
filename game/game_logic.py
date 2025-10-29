from game.player.player import Player
from game.area.area import Area
from game.area.world import map
class Game:
    def __init__(self):
        self.player = Player()
        self.areas = self.load_areas()

    def load_areas(self):
            # Les zones
        return map
    def get_current_area(self):
        return self.areas[self.player.current_area]

    def look(self):
        area = self.get_current_area()
        return f"{area.description}"

    def move(self,next_area):
        current = self.player.current_area
        current = next_area

