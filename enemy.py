import random

from pyglet.window.key import _0
from collections import deque
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

    def get_available_direction(self,room,maze,stride,room_size):
        room_x,room_y = room
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

    def bfs(self, start, target, maze, stride, room_size):
        #It guarantte the shortest route
        queue = deque([start]) #It is more effeicnet than a normal list for removing thing in both end unlike list you have to move everything if you move the first item
        visited = {start} #Is a python data structrue call set that is faster look up
        previous = {start: None} # this create a dictionary. Start: previous value

        while queue: #when it is not empty
            current = queue.popleft() #take the enxt room from queue

            if current == target: #have we find the player yet
                break

            directions = self.get_available_direction(
                current,
                maze,
                stride,
                room_size
            ) #search which neighbouring room can we enter

            for directoin in directions:
                next_room = (
                    current[0] + directions[0], #x
                    current[1] + directions[1] #y
                ) # calculate the neighbouring room coord

                #because we are using set we don have to use for loop
                if next_room not in visited:
                    visited.add(next_room) # make it visited
                    previous[next_room] = current #remember where we come from
                    queue.append(next_room)

        if target not in previous:
            return [] # There is no path to the player

        path = []
        current = target

        while current != start: # keep going back ward
            path.append(current)
            current = previous[current] # loop through the dcionary key

        path.reverse() #from target -> self to sekf -> target

        return path


    def patrol(self, delta_time, stride, maze, room_size):

        current_room = self.get_room(stride)

        if current_room != self.room: #It get a new direction once it in a new room

            self.room = current_room

            directions = self.get_available_direction(
                current_room,
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


    def chasing(self,player,stride,current_time_state, delta_time, maze):
        #Player is the player object
        enemy_room = self.get_room(stride)
        player_room = player.get_room(stride)

        #Determine vision
        if current_time_state == "night":
            vision = self.vision

        elif current_time_state == "blood moon":
            vision = self.buffed_vision



        #Same room -> diret chase
        if enemy_room == player_room:
            # directly approach it

            #Find the difference between themn first
            dx = player.x - self.x
            dy = player.y - self.y

            # A^2 + B^2 = C^2
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance == 0:
                return

            #normalise the factor so it don change base on distance
            dx /= distance
            dy /= distance


            new_x= self.x + dx * self.speed * delta_time
            new_y = self.y + dy * self.speed * delta_time

            if is_walkable(new_x, new_y,maze):
                self.x = new_x
                self.y = new_y


        else:
            # not in the same room, now check if it is within vision range
            room_distance = math.sqrt(
                (enemy_room[0] - player_room[0]) ** 2
                +
                (enemy_room[1] - player_room[1]) ** 2
            )

            if room_distance > vision:
                self.state = "patrol"
                return #end the function becuase it is no longer in spider vision

            else: #player in vision BFS mechanic
