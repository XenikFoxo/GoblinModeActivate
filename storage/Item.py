from random import randint

pityValue = 100

class Item:
    def __init__(self, name: str=None, rarity: float=None, equipmentType: str="weapon", tooltip: str=None, rarityModifier: float = None):
        global pityValue
        self.equipmentType = equipmentType
        self.tooltip = tooltip
        if rarity is None:
            rarity = (randint(40,60)/100)
            if rarityModifier is not None:
                self.rarity = rarity + (((1.09**(rarityModifier-20))-2)/100)
            else:
                self.rarity = (randint(0,100)/100)
        else:
            self.rarity = rarity
        if name is None:
            self.name = "Mighty Fuck Off Object"
        else:
            self.name = name

    def serialize(self):
        return repr({
            'name': self.name,
            'equipmentType': self.equipmentType,
            'tooltip': self.tooltip,
            'rarity': self.rarity,
        })

    @staticmethod
    def deserialize(string):
        data = eval(string)
        return Item(data['name'], data['rarity'], data['equipmentType'], data['tooltip'])
