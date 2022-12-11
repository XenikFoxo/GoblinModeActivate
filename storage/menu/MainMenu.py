from collections import OrderedDict

from storage.Box import Box
from storage.Game import Game
from storage.Variant import BoxTypeVariant
from storage.menu import MenuItem, Menu


def buildBox(instance: Game, boxType, rarity=1, keys=1):
    contents = instance.getBoxType(boxType).getItem()
    newBox = Box(boxType, contents)
    return newBox

def __mm_FuckOff(instance: Game):
    import sys
    instance.save()
    sys.exit(0)

def __mm_Pull(instance: Game):
    highest = 0
    avg = []
    failCount = 0
    for x in range(100):
        i = instance.player.pull(BoxTypeVariant.COPPER.value)
        if i.rarity > 0.95:
            if highest < failCount:
                highest = failCount
            avg.append(failCount)
            failCount = 0
        else:
            failCount+=1
    print("highest " + str(highest))
    average = 0
    freq: dict[int, int] = {}
    for x in avg:
        average += x
        if x not in freq.keys():
            freq[x] = 1
        else:
            freq[x] += 1
    print("average " + str(average/len(avg)))
    print("inventory size " + str(len(instance.player.inventory)))
    instance.save()

def __mm_Hit(instance: Game):
    instance.player.hit(10)
    print(instance.player.health)
    instance.save()

def generateMainMenu():
    pull = MenuItem("pull", "Pull some random items", __mm_Pull)
    hit = MenuItem("hit", "Smack a Bitch", __mm_Hit)
    fuckOff = MenuItem("fuck off", "Furry Sex Time", __mm_FuckOff)
    menu = Menu()
    menu.add(pull)
    menu.add(hit)
    menu.add(fuckOff)
    return menu
