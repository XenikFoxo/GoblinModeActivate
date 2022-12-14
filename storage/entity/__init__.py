class Entity:

    def __init__(self, name: str, health: int = 0, attack: int = 0, defense: int = 0):
        self.name: str = name
        self.health: int = health
        self.attack: int = attack
        self.defense: int = defense

    def attack(self, target):
        target.hit(self.attack)
    
    def hit(self, amount) -> int:
        self.health -= (amount - self.defense)
        return self.health