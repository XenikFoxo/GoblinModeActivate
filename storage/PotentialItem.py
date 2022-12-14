from storage.Item import Item
from storage.ItemList import itemDict

class PotentialItem:
    def __init__(self, name):
        self.name = name

    def generateUniqueItem(self, uniqueName:str) -> Item:
        return itemDict[uniqueName].toItem()

    def generateItem(self, pity = None, uniqueName:str = None, ) -> Item:
        if uniqueName is not None:
            return self.generateUniqueItem(uniqueName)
        else:
            return Item(self.name, rarityModifier=pity)
