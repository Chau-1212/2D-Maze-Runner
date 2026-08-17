class Maze:
    def __init__(self,room,maze,hallway):
        self.room = room
        self.size = maze
        self.hallway = hallway
        self.stride = room + hallway

        self.visited = [ #new 2d list for maze visited
            [False] * self.size #it just set the room cood to false
            for _ in range(self.size)
        ]


        self.maze = [] #the thing that accturally store the list

    def create_grid(self): #it create a empty 2d list

        grid_size = self.stride * (self.size - 1) + self.room + 2 # so we include the final room

        self.maze = [
            [0] * grid_size # one row. It put 0 in every single slot in the gird size
            for _ in range(grid_size) #how many column
        ]

        for row in range(self.size):
            for column in range(self.size):

                x = column * self.stride + 1 #because there is a outter wall
                y = column * self.stride + 1

                for room_y in range(self.room):
                    for room_x in range(self.room):
                        self.maze[y+room_y][x + room_x] = 1 #it change along the maze with x,y
