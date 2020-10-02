from gameHelpers.gameElements.center_divider import CenterDivider
from gameHelpers.gameElements.urban_area import UrbanArea


class GameController:
    def __init__(self, config):
        # initialize the urban areas
        self.urbanAreas = []
        self.urbanAreas.append(UrbanArea(config, 17, 0))
        self.urbanAreas.append(UrbanArea(config, 2, 51))

        # initialize the divider
        self.divider = CenterDivider(config)

    def render(self):
        # render urban areas
        for urbanArea in self.urbanAreas:
            urbanArea.render()

        # render the center divider
        self.divider.render()
