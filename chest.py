import random

from item import item, items

class chest:
    def __init__(self):
        self.loot = []
        self.open = False #So it doesn't generate loot more than once

    def gen_loot(self,loot_table): #the loot_table.json
        self.loot =[]

        for x in range(3):
            roll = random.randint(1,100)

            current_rate = 0

            for loot in loot_table: #loot is item inside JSON
                current_rate += loot["drop_rate"]

                if roll <= current_rate:
                    if loot["item"] != "nothing":

                        item_object = items[loot["item"]] #it look up to the currently exist object to add it
                        self.loot.append(item_object)

                    break
