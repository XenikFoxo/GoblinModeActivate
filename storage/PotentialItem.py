from storage.Item import Item


class PotentialItem:
    def __init__(self, name):
        self.name = name

    def generateSeededItem(self, pity = None) -> Item:
        return Item(self.name, rarityModifier=pity)