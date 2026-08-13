import arcade

class furance:
    def __init__(self):
        self.fuel = 0
        self.cooking = False
        self.content = 0
        self.cook_timer = 0
        self.product = 0

    def add_coal(self): #we have the minus the coal from the player inveotry
        self.fuel += 15

    def add_meat(self):
        self.content += 1

    def cook(self,delta_time):

        if self.content > 0 and self.fuel > 0: #It check before it start cooking that it have mroe than 20
            self.cooking = True

            if self.cooking:
                self.cook_timer += delta_time

                if self.cook_timer >= 20:
                    self.cook_timer = 0
                    self.content -= 1
                    self.product += 1
                    self.cooking = False #process are saved becuase the cook timer isn't reset to zero

        else:
            self.cooking = False
