from curses import flash
import numbers

import arcade
from item import battery, flash

class Player:
    def __init__(self):
        #postision and speed
        self.x = 100
        self.y = 100
        self.speed = 300

        # Stat
        self.health = 100
        self.hunger = 100
        self.lost = False
        self.win = False

        # inventory
        self.inventory = [] #2d list for item name and number of item
        self.selected_slot = 0
        self.max_item_types = 3
        self.flashlight = None #So i can check can we use battery

    def pick_up_item(self, item, number): #Pick up item from the floor
        if isinstance(item, flash): #flashlight is equipped, not stored in the hotbar
            self.flashlight = item
            return

        for inventory_item in self.inventory:
            if inventory_item[0] == item:
                inventory_item[1] += number
                return

        if len(self.inventory) >= self.max_item_types:
            return

        self.inventory.append([item, number])

    def loot_chest(self,chest,num): # player can press 1,2,3 to select the itme and press e to take it
            pass


    def use_item(self):

        if self.selected_slot >= len(self.inventory):
            return

        inventory_item = self.inventory[self.selected_slot]
        item = inventory_item[0]

        match item.item_type:

            case "hunger":
                self.hunger += item.p_effect
                self.health -= item.n_effect

            case "health":
                self.health += item.p_effect

            case "energy":
                if self.flashlight is not None:
                    self.flashlight.battery += item.p_effect
                else:
                    return

            case _:
                return

        inventory_item[1] -= 1

        if inventory_item[1] <= 0:
            self.inventory.remove(inventory_item)

    def drop_item(self,item):
        for inventory_item in self.inventory:

            if inventory_item[0] == item:
                inventory_item[1] -= 1

                if inventory_item[1] <= 0:
                    self.inventory.remove(inventory_item)
                return

    def hot_bar(self,number):
        match number:
            case 1:
                self.selected_slot = 0
            case 2:
                self.selected_slot = 1
            case 3:
                self.selected_slot = 2
