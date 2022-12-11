from random import choice

from storage.PotentialItem import PotentialItem


class BoxType:
    def __init__(self, potentialItems):
        self.potentialItems = potentialItems

    def getItem(self) -> PotentialItem:
        return choice(self.potentialItems)