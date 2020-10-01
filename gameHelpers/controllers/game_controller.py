from gameHelpers.urban_area import UrbanArea


class GameController:
    def __init__(self, config):
        self.urban1 = UrbanArea(config)

    def render(self):
        self.urban1.render()
