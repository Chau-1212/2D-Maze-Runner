import random

class time_state:
    def __init__(self):
        self.timer = 0
        self.state = "day"

    def update(self,delta_time):
        self.timer += delta_time

        if self.state == "day":
            if self.timer >= 180:
                self.state = "night"
                self.timer = 0

        elif self.state == "night":
            if self.timer >= 120:
                if random.randrange(100) < 20: #randrange is 0-99 so this is a clean 20%
                    self.state = "blood moon"
                else:
                    self.timer = 0

        elif self.state == "blood moon":
            if self.timer >= 30:
                self.state = "day"
                self.timer = 0
