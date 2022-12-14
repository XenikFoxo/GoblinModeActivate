from storage.Game import Game
from storage.entity import Entity

class CombatInstance:

    def __init__(self, instance: Game, *targets: Entity):
        self.instance = instance
        self.entities: tuple[Entity] = targets

    def loop(self):
        while True:
            while True:
                action = input("Attack (atk) or Run (run)?").lower()
                if action == "atk":
                    self.instance.player.attack(self.entities[0])
                    self.entities[0].printHealth()
                    print()
                    break
                if action == "run":
                    print("pussy")
                    break
            self.entities: tuple[Entity] = tuple(entity for entity in self.entities if entity.health > 0)
            if len(self.entities) == 0:
                print("yay you win")
                break
            for entity in self.entities:
                entity.attack(self.instance.player)
                self.instance.player.printHealth()
            if self.instance.player.health <= 0:
                print("skill issue lol")
                break