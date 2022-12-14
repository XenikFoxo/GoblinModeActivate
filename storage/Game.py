from storage.Item.BoxType import BoxType
from storage.entity.Player import Player
from storage.Item.PotentialItem import PotentialItem


def _generateBoxSets() -> dict[str, BoxType]:
    return {
        "copper": BoxType("copper", (PotentialItem("firstC"), PotentialItem("secondC"), PotentialItem("thirdC"))),
        "iron": BoxType("iron", (PotentialItem("firstI"), PotentialItem("secondI"), PotentialItem("thirdI"))),
        "silver": BoxType("silver", (PotentialItem("firstS"), PotentialItem("secondS"), PotentialItem("thirdS"))),
        "gold": BoxType("gold", (PotentialItem("firstG"), PotentialItem("secondG"), PotentialItem("thirdG")))
    }


class Game:

    def __init__(self, player: Player):
        self.player = player
        self.boxes = _generateBoxSets()

    def getBoxType(self, box: str) -> BoxType:
        return self.boxes[box]

    def save(self):
        try:
            with open("save.json", "w") as f:
                f.write(self.player.serialize())
        except Exception:
            print('Error in Save Function')

    def load(self):
        try:
            with open("save.json", "r") as f:
                player = Player.deserialize(f.read())
            self.player = player
        except Exception:
            print('Error in Load Function')
