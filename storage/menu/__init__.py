class MenuItem:
    def __init__(self, option, description, callback):
        self.option = option
        self.description = description
        self.callback = callback

    def run(self, instance):
        self.callback(instance)

    def print(self):
        print(self.option + ": " + self.description)

class Menu:
    def __init__(self, menuItems: dict[str, MenuItem]=None):
        if menuItems is None:
            menuItems = {}
        self.items = menuItems

    def add(self, item: MenuItem):
        self.items[item.option] = item

    def addOption(self, option, description, callback):
        self.items[option] = MenuItem(option, description, callback)

    def option(self, option, instance):
        self.items[option].run(instance)

    def print(self):
        for key in self.items:
            self.items[key].print()