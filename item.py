from multiprocessing import parent_process
from time import sleep


class item:
    def __init__(self,name,item_type,p_effect=0,n_effect=0):
        self.name = name
        self.item_type = item_type
        self.p_effect = 0
        self.n_effect = 0


class flash:
    def __init__(self,battery=50):
        self.name = "Flashlight"
        self.on = False
        self.battery = battery
        self.vision = 3
        self.spiked = False #scare away the monster
        self.spike_timer = 0 #how long the spike last

    def turn_on(self):
        self.on = True
    def turn_off(self):
        self.on = False
    def spike(self):
        if self.battery >= 25:
            self.battery -= 25
            self.vision = 5
            self.spiked = True
            self.spike_timer = 20 #the on update process will check this and change after it is 20 -> 0 or whatever numebr

        else:
            pass


bread = item("bread", "hunger", 20)
raw = item("Raw Meat", "hunger", 10, 5)
cooked = item("Cooked Meat", "hunger", 25)
battery = item("Battery", "energy", 25)
