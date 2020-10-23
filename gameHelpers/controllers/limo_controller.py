import random
from gameHelpers.gameElements.limo import Limo

# define probability for a limo to spawn every 10sec
ONE_IN_EIGHTY = 1 / 80


class LimoController:
    def __init__(self, config, entranceScanner):
        # init config
        self.config = config

        # initialize limo array
        self.limos = []

        # store entranceScanner
        self.scanner = entranceScanner

        # one limo should be spawned immediately
        self.first = True

    # called every game tick, limos will be randomly generated
    def tick(self):
        if self.first:
            self.limos.append(Limo(self.config, random.choice(self.scanner.entrances), '1'))
            self.first = False

        # TODO: generation frequency should depend on game level
        # maybe store level in WinConfig?
        if self.decision(ONE_IN_EIGHTY):
            self.limos.append(Limo(self.config, random.choice(self.scanner.entrances), '1'))

        return

    # render will call tick to update limos, then render limos
    def render(self):
        self.tick()

        for limo in self.limos:
            limo.render()

    def decision(self, prob):
        return random.random() < prob
