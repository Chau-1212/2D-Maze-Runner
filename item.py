class item:
    def __init__(self,name,item_type,p_effect=0,n_effect=0):
        self.name = name
        self.item_type = item_type
        self.p_effect = p_effect
        self.n_effect = n_effect


class flash:
    def __init__(self,battery=50):
        self.name = "flashlight"
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

bread = item("bread", "hunger", 25)
raw_meat = item("raw_meat", "health", 5, 0)
cooked_meat = item("cooked_meat", "health", 40)
coal = item("coal", "fuel", 1)
battery = item("battery", "energy", 40)
flashlight = flash()

items = {
    "flashlight": flashlight,
    "bread": bread, #it use the string to find the object
    "raw_meat": raw_meat,
    "cooked_meat": cooked_meat,
    "coal": coal,
    "battery": battery
}
