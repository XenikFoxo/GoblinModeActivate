from storage.Item import Item


class UniqueItem:

    def __init__(self, name: str, rarity: float, itemType: str, damage: int = 0, defense: int = 0, tooltip = "", script = None):
        self.script = script
        self.tooltip = tooltip
        self.defense = defense
        self.damage = damage
        self.itemType = itemType
        self.rarity = rarity
        self.name = name

    def toItem(self) -> Item:
        return Item(self.name, self.rarity, self.itemType, self.tooltip)

# Possible Item Types: weapon, armor, consumable
itemDict: dict[str, UniqueItem] = {
    "testItem": UniqueItem("Test Item", 0.4, "weapon", 5, 10, "This is a test item."),
}
