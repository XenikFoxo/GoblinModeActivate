from random import choice

from storage.Item.PotentialItem import PotentialItem


class BoxType:
    def __init__(self, name, potentialItems):
        self.name = name
        self.potentialItems = potentialItems

    def getItem(self) -> PotentialItem:
        return choice(self.potentialItems)