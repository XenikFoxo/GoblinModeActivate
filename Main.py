# Imports
from storage.Box import Box
from storage.BoxType import BoxType
from storage.PotentialItem import PotentialItem

# Defining Variables
debugMode = True  # will be implemented later
notFucked = True  # exit condition
failCount = 0
currentMenu = "Main"

# Defining Dictionaries
boxSets: dict[str, BoxType] = {
    "copper": BoxType((PotentialItem("firstC"), PotentialItem("secondC"), PotentialItem("thirdC"))),
    "iron": BoxType((PotentialItem("firstI"), PotentialItem("secondI"), PotentialItem("thirdI"))),
    "silver": BoxType((PotentialItem("firstS"), PotentialItem("secondS"), PotentialItem("thirdS"))),
    "gold": BoxType((PotentialItem("firstG"), PotentialItem("secondG"), PotentialItem("thirdG")))
}

# Defining Lists
equipmentTypes = ("weapon", "headwear", "chest", "arm", "ring", "leg", "shield", "shoes")
boxInventory = []
keyInventory = []

# Defining Functions
def buildBox(boxType, rarity=1, keys=1):
    contents = boxSets[boxType].getItem()
    newBox = Box(boxType, rarity, keys, contents)
    return newBox

def pull(bType):
    global failCount
    boxType = boxSets[bType]
    item = boxType.getItem().generateSeededItem(failCount)
    if item.rarity is None or item.rarity < 0.95:
        failCount+=1
    else:
        failCount=int(failCount*0.2)
    return item


if __name__ == "__main__":
    # Main Loop
    while notFucked:
        if currentMenu == "Main":
            print("Test Menu Here, disregard")
            print("MENU OPTIONS:\npull: Pull\nstart: Start the damn game.\noptions: This does nothing right now.\nfuck off: Does what it says.")
            select = input(">> ").lower()
            if select == "fuck off" or select == "q":
                notFucked = False
            if select == "pull":
                failCount = 0
                highest = 0
                for x in range(100):
                    i = pull("copper")
                    print("rarity: " + str(i.rarity))
                    print(failCount)
                    if highest < failCount:
                        highest = failCount
                    print("highest " + str(highest))
            if select == "options":
                for item in boxInventory:
                    print(item.contents.generateSeededItem().name)
