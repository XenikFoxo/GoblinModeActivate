from math import ceil
from random import randint

from storage.BoxType import BoxType
from storage.Item import Item

defenceTailOff = 50
defenceLimit = 70
class Player:
    def __init__(self,
                 money = 0,
                 health = 20,
                 ):
        self.money = money
        self.health = health
        self.pity: dict[BoxType, int] = {}
        self.inventory: list[Item] = []

    def pull(self, boxType: BoxType):
        if boxType.name in self.pity.keys():
            pity = self.pity[boxType.name]
        else:
            pity = 40
            self.pity[boxType.name] = pity
        item = boxType.getItem().generateItem(pity)
        if item.rarity > 0.95:
            self.pity[boxType.name] = int(self.pity[boxType.name] * (randint(5, 40) / 100))
        else:
            self.pity[boxType.name] += 1
        self.inventory.append(item)
        return item

    def getReduction(self):
        global defenceLimit, defenceTailOff
        overDefence = 1 - defenceTailOff
        if overDefence > 0:
            defence = min(defenceTailOff + int(overDefence / 10), defenceLimit)
        else:
            defence = 1
        return defence

    def hit(self, damage):
        damage = damage - ceil((damage * (self.getReduction() / 100)))
        self.health -= damage

    def serialize(self):
        pity = {}
        for key,value in self.pity.items():
            pity[key] = value
        inventory = []
        for item in self.inventory:
            inventory.append(item.serialize())
        return repr({
            'money': self.money,
            'health': self.health,
            'pity': pity,
            'inventory': inventory,
        })

    @staticmethod
    def deserialize(string):
        data = eval(string)
        player = Player(data['money'], data['health'])
        player.pity = data['pity']
        for item in data['inventory']:
            player.inventory.append(Item.deserialize(item))
        return player