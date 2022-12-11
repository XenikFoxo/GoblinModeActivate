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
                 damage = 1,
                 defence = 0,
                 dodge = 0
                 ):
        self.money = money
        self.health = health
        self.damage = damage
        self.defence = defence
        self.dodge = dodge
        self.pity: dict[BoxType, int] = {}
        self.inventory: list[Item] = []

    def pull(self, boxType: BoxType):
        if boxType in self.pity.keys():
            pity = self.pity[boxType]
        else:
            pity = 40
            self.pity[boxType] = pity
        item = boxType.getItem().generateSeededItem(pity)
        if item.rarity > 0.95:
            self.pity[boxType] = int(self.pity[boxType] * (randint(5, 40) / 100))
        else:
            self.pity[boxType] += 1
        self.inventory.append(item)
        return item

    def getReduction(self):
        global defenceLimit, defenceTailOff
        overDefence = self.defence - defenceTailOff
        if overDefence > 0:
            defence = min(defenceTailOff + int(overDefence / 10), defenceLimit)
        else:
            defence = self.defence
        return defence

    def hit(self, damage):
        damage = damage - ceil((damage * (self.getReduction() / 100)))
        self.health -= damage