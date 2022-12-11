from math import ceil

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