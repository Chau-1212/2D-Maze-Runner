import random

from maze import TILE_SIZE
from physic import is_walkable
import math
from time_state import *

class enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y

        self.speed = 0

        self.vision = 0
        self.buffed_vision = 4

        self.state = "patrol"

        self.path_index = 0
        self.patrol_timer = 0
        self.patrol_direction = []

        self.room = (None,None)


    def update_state(self,time_states):

        match time_states:

            case "day":
                self.vision = 0 #no vision and speed in the day
                self.speed = 0

            case "night":
                self.vision = 2
                self.speed = 20

            case "blood moon":
                self.vision = 4
                self.speed = 40

    def get_room(self,stride:int) -> tuple[int,int]: #it define what is the returning type
        tile_x = int(self.x // TILE_SIZE) #position is in pixels so it convert to tile first
        tile_y = int(self.y // TILE_SIZE)

        room_x = (tile_x - 1) // stride #the -1 remove the outer wall
        room_y = (tile_y - 1) // stride

        return(room_x,room_y)

    def get_available_direction(self,maze,stride,room_size):
        room_x,room_y = self.get_room(stride)
        directions=[]

        x = room_x * stride + 1 #Room x is the room number in x, thes self contain current room coord
        y = room_y * stride + 1 # which turn it in to the tile coord
        # +1 remove the outer wall

        centre_x = x + room_size // 2 #x is top left
        centre_y = y + room_size // 2

        max_row = len(maze) #grid size so the check never go outside
        max_column = len(maze[0])

        if centre_y - 1 >= 0 and maze[centre_y - 1][centre_x] == 1: #check up
            directions.append((0,-1))
        if centre_y + room_size < max_row and maze[centre_y + room_size][centre_x] == 1:# check down
            directions.append((0,+1))
        if centre_x - 1 >= 0 and maze[centre_y][centre_x - 1] == 1: # check left
            directions.append((-1,0))
        if centre_x + room_size < max_column and maze[centre_y][centre_x + room_size] == 1:
            directions.append((+1,0))

        return directions

    def patrol(self, delta_time, stride, maze, room_size):

        current_room = self.get_room(stride)

        if current_room != self.room: #It get a new direction once it in a new room

            self.room = current_room

            directions = self.get_available_direction(
                maze,
                stride,
                room_size
            )

            if directions:
                self.patrol_direction = random.choice(directions)
            elif not self.patrol_direction:
                return #no direction available yet, stay still

        new_x = self.x + self.patrol_direction[0] * self.speed * delta_time
        new_y = self.y + self.patrol_direction[1] * self.speed * delta_time
        #It calculate the new position first before moving
        if is_walkable(new_x,new_y,maze):
            self.x=new_x
            self.y=new_y
        #It will only move if it is walkable






    def chasing(self,player,stride):
        #Player is the player object
        enemy_room = self.get_room(stride)
        player_room = player.get_room(stride)

        #now chekc are they in sam room
        if enemy_room == player_room:
            # directly approach it
            pass
        else:
            # not in the same room, now check if it is within vision range
            room_distance = math.sqrt(
                (enemy_room[0] - player_room[0]) ** 2
                +
                (enemy_room[1] - player_room[1]) ** 2
            )

            if
