from random import randint

pityValue = 40

class Item:
    def __init__(self, name: str=None, rarity: float=None, equipmentType: str="weapon", tooltip: str=None, rarityModifier: float = None):
        global pityValue
        self.equipmentType = equipmentType
        self.tooltip = tooltip
        if rarity is None:
            self.rarity = (randint(0,100)/100)
        else:
            self.rarity = rarity
        if rarityModifier is not None:
            self.rarity = self.rarity * (int((rarityModifier/pityValue))+1)
        if name is None:
            self.name = "Mighty Fuck Off Object"
        else:
            self.name = name