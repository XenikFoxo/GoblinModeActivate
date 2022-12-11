from enum import Enum

from storage.BoxType import BoxType
from storage.PotentialItem import PotentialItem


class BoxTypeVariant(Enum):
    COPPER = BoxType("copper", (PotentialItem("firstC"), PotentialItem("secondC"), PotentialItem("thirdC")))
    IRON = BoxType("iron", (PotentialItem("firstI"), PotentialItem("secondI"), PotentialItem("thirdI"))),
    SILVER = BoxType("silver", (PotentialItem("firstS"), PotentialItem("secondS"), PotentialItem("thirdS"))),
    GOLD = BoxType("gold", (PotentialItem("firstG"), PotentialItem("secondG"), PotentialItem("thirdG")))