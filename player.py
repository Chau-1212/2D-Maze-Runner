import arcade

class Player:
    def __init__(self):
        #postision and speed
        self.x = 100
        self.y = 100
        self.speed = 300

        # Stat
        self.health = 100
        self.hunger = 100

        # Invetory
        self.invetory = [] #2d list for item name and number of item
        self.max_item_types = 3

    def add_item(self, item, number):
        for invetory_item in self.invetory:
            if invetory_item[0] == item:
                invetory_item[1] += number
                return

            if len(self.invetory) >= self.max_item_types:
                return #if you have too much type of item in the invetory you can't take it
        self.invetory.append([item,number]) #If item don exist in player invetory
