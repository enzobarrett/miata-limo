from gameHelpers.gameElements.bottom_divider import BottomDivider
from gameHelpers.gameElements.center_divider import CenterDivider
from gameHelpers.gameElements.rural_area import RuralArea
from gameHelpers.gameElements.top_divider import TopDivider
from gameHelpers.gameElements.urban_area import UrbanArea


class GameController:
    def __init__(self, config):
        # initialize the urban areas
        self.urbanAreas = []
        self.urbanAreas.append(UrbanArea(config, 17, 0))
        self.urbanAreas.append(UrbanArea(config, 2, 51))

        # initialize the rural area with the urban areas
        self.ruralAreas = []
        self.ruralAreas.append(RuralArea(self.urbanAreas[0]))
        self.ruralAreas.append(RuralArea(self.urbanAreas[1]))

        # initialize the dividers
        self.divider = CenterDivider(config)
        self.bottomDivider = BottomDivider(config)
        self.topDivider = TopDivider(config)

    def render(self):
        # render urban areas
        for urbanArea in self.urbanAreas:
            urbanArea.render()

        # render rural areas
        for ruralArea in self.ruralAreas:
            ruralArea.render()

        # render the dividers
        self.divider.render()
        self.bottomDivider.render()
        self.topDivider.render()
