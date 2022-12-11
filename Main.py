# Imports
import sys

from storage.Box import Box
from storage.BoxType import BoxType
from storage.Player import Player
from storage.PotentialItem import PotentialItem
from storage.menu import MenuItem, Menu

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
equipmentTypes = ("weapon", "headgear", "chest", "arm", "ring", "leg", "shield", "shoes")
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

def mm_FuckOff(instance):
    global notFucked
    notFucked = False

def mm_Pull(instance):
    global failCount
    failCount = 0
    highest = 0
    for x in range(100):
        i = pull("copper")
        print("rarity: " + str(i.rarity))
        print(failCount)
        if highest < failCount:
            highest = failCount
        print("highest " + str(highest))

def mm_Hit(instance):
    instance.hit(10)
    print(instance.health)

def generateMainMenu():
    pull = MenuItem("pull", "Pull some random items", mm_Pull)
    hit = MenuItem("hit", "Smack a Bitch", mm_Hit)
    fuckOff = MenuItem("fuck off", "Furry Sex Time", mm_FuckOff)
    menu = Menu()
    menu.add(pull)
    menu.add(hit)
    menu.add(fuckOff)
    return menu


if __name__ == "__main__":
    player = Player(health=50,defence=10)
    mainMenu = generateMainMenu()
    # Main Loop
    while notFucked:
        if currentMenu == "Main":
            print("Test Menu Here, disregard")
            mainMenu.print()
            option = input(">>> ")
            mainMenu.option(option, player)
