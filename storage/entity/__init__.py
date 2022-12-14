class Entity:

    def __init__(self, name: str, health: int = 0, attack: int = 0, defense: int = 0):
        self.name: str = name
        self.health: int = health
        self.attackStat: int = attack
        self.defenseStat: int = defense

    def attack(self, target):
        target.hit(self.attackStat)
    
    def hit(self, amount) -> int:
        self.health -= (amount - self.defenseStat)
        return self.health

    def printHealth(self):
        print(str(self.name) + " has " + str(self.health) + "HP")