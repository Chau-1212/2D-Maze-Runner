

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
        self.hunger_decay = 10/60 #10% per min

        self.sprint_speed = 500
        self.sprinting = False
        self.sprinting_hunger_decay = 30/60 #30% per min

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

    def moving(self,keys,delta_time):
        #change in directoin
        dx = 0
        dy = 0

        #This just check the directoin
        if arcade.key.W in keys:
            dy += 1

        if arcade.key.S in keys:
            dy -= 1

        if arcade.key.A in keys:
            dx -= 1

        if arcade.key.D in keys:
            dx += 1

        #This check is it "sprinting"
        if arcade.key.LSHIFT in keys:
            Current_Speed = self.sprint_speed
            self.sprinting = True
        else:
            Current_Speed = self.speed
            self.sprinting = False

        #This accturally move it
        self.x += dx * Current_Speed * delta_time
        self.y += dy * Current_Speed * delta_time

        #if i just use W,A,S,D arcade won't handle it as W,A,S,D but binary of that verison

    def hunger_update(self ,delta_time):

        if self.sprint:
            decay = self.sprinting_hunger_decay
        else:
            decay = self.hunger_decay

        self.hunger -= decay * delta_time

    def take_damage(self,damage):

        self.health -= damage

        if self.health <= 0:
            self.lost = True


    def get_room(self,stride):
        tile_x = int(self.x // TILE_SIZE) #position is in pixels so it convert to tile first
        tile_y = int(self.y // TILE_SIZE)

        room_x = (tile_x - 1) // stride #the -1 remove the outer wall
        room_y = (tile_y - 1) // stride

        return(room_x,room_y)
