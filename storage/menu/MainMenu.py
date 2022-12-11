from storage.Box import Box
from storage.Game import Game
from storage.menu import MenuItem, Menu


def buildBox(instance: Game, boxType, rarity=1, keys=1):
    contents = instance.getBoxType(boxType).getItem()
    newBox = Box(boxType, rarity, keys, contents)
    return newBox

def pull(instance: Game, bType: str):
    global failCount
    boxType = instance.getBoxType(bType)
    item = boxType.getItem().generateSeededItem(failCount)
    if item.rarity is None or item.rarity < 0.95:
        failCount+=1
    else:
        failCount=int(failCount*0.2)
    return item

def __mm_FuckOff(instance: Game):
    import sys
    sys.exit(0)

def __mm_Pull(instance: Game):
    failCount = 0
    highest = 0
    for x in range(100):
        i = pull(instance, "copper")
        print("rarity: " + str(i.rarity))
        print(failCount)
        if highest < failCount:
            highest = failCount
        print("highest " + str(highest))

def __mm_Hit(instance: Game):
    instance.player.hit(10)
    print(instance.player.health)

def generateMainMenu():
    pull = MenuItem("pull", "Pull some random items", __mm_Pull)
    hit = MenuItem("hit", "Smack a Bitch", __mm_Hit)
    fuckOff = MenuItem("fuck off", "Furry Sex Time", __mm_FuckOff)
    menu = Menu()
    menu.add(pull)
    menu.add(hit)
    menu.add(fuckOff)
    return menu
