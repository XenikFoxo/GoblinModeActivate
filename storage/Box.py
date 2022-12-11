from storage.PotentialItem import PotentialItem
from storage.Variant import BoxTypeVariant


class Box:
    def __init__(self, boxType: BoxTypeVariant, contents: PotentialItem):
        self.type = boxType
        self.contents = contents