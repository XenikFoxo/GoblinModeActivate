from storage.BoxType import BoxType
from storage.PotentialItem import PotentialItem


def _generateBoxSets() -> dict[str, BoxType]:
    return {
        "copper": BoxType((PotentialItem("firstC"), PotentialItem("secondC"), PotentialItem("thirdC"))),
        "iron": BoxType((PotentialItem("firstI"), PotentialItem("secondI"), PotentialItem("thirdI"))),
        "silver": BoxType((PotentialItem("firstS"), PotentialItem("secondS"), PotentialItem("thirdS"))),
        "gold": BoxType((PotentialItem("firstG"), PotentialItem("secondG"), PotentialItem("thirdG")))
    }


class Game:

    def __init__(self, player):
        self.player = player
        self.boxes = _generateBoxSets()

    def getBoxType(self, box: str) -> BoxType:
        return self.boxes[box]

