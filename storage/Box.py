from storage.PotentialItem import PotentialItem


class Box:
    def __init__(self, boxType, rarityMultiplier, boxKeys, contents: PotentialItem):
        self.type = boxType
        self.multiplier = rarityMultiplier
        self.neededKeys = boxKeys
        self.contents = contents