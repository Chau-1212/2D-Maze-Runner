import random

class enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y

        self.speed = 0
        self.vision = 0

        self.state = "patrol"

        self.path_index = 0
        self.patrol_timer = 0
        self.patrol_direction = []


    def update_state(self,time_states):

        match time_states:

            case "night":
                self.vision = 2
                self.speed = 20

            case "blood moon":
                self.vision = 4
                self.speed = 40

    def get_room(self,stride):
        room_x = (self.x-1) // stride
        room_y = (self.y-1) // stride

        return(room_x,room_y)

    def patrol(self, delta_time, stride):

        current_room = self.get_room(stride)

        if current_room != self.room:

            self.room = current_room

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            self.patrol_direction = random.choice(directions)

        self.x += self.patrol_direction[0] * self.speed * delta_time
        self.y += self.patrol_direction[1] * self.speed * delta_time






    def chasing(self,player_x,player_y):
        pass
