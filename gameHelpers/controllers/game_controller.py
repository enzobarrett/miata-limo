from gameHelpers.urban_area import UrbanArea


class GameController:
    def __init__(self, config):
        self.urbanAreas = []
        self.urbanAreas.append(UrbanArea(config, 17, 0))
        self.urbanAreas.append(UrbanArea(config, 2, 51))

    def render(self):
        for urbanArea in self.urbanAreas:
            urbanArea.render()
