import json
import random

from item import item, items

with open("data/loot_table.json") as f:
    _LOOT_TABLES = json.load(f)

class chest:
    def __init__(self):
        self.loot = []
        self.open = False #So it doesn't generate loot more than once

    def gen_loot(self, is_night=False): #night gives better loot — 3-5 items and a doubled flashlight rate
        self.loot = []

        table_name = "night_chest_loot" if is_night else "normal_chest_loot"
        loot_table = _LOOT_TABLES[table_name]

        item_count = random.randint(3, 5) if is_night else random.randint(2, 4)

        for x in range(item_count):
            roll = random.randint(1,100)

            current_rate = 0

            for loot in loot_table: #loot is item inside JSON
                current_rate += loot["drop_rate"]

                if roll <= current_rate:
                    if loot["item"] != "nothing":

                        item_object = items[loot["item"]] #it look up to the currently exist object to add it
                        self.loot.append(item_object)

                    break