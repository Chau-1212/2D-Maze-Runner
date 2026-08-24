import random

TILE_SIZE = 32


class Maze:
    def __init__(self,room,size,hallway):
        self.room = room #room size
        self.size = size
        self.hallway = hallway
        self.stride = room + hallway

        self.visited = [ #new 2d list for maze visited. is a ROOM 2d list
            [False] * self.size #it just set the room cood to false. Thing we put inside the list
            for _ in range(self.size) #using _ becuase we don care about the number. we create self.size amount of row
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
                y = row * self.stride + 1

                for room_y in range(self.room):
                    for room_x in range(self.room):
                        self.maze[y+room_y][x + room_x] = 1 #it change along the maze with x,y

    def dfs(self,row,column):
        directions= [
            (-1,0), #up
            (1,0), #down
            (0,-1), #left
            (0,1) #right
        ]

        stack = [(row,column)] #explicit stack instead of recursion so big maze can not crash the recursion limit
        self.visited[row][column] = True

        while stack:
            row,column = stack.pop()

            random.shuffle(directions)

            for dir_row, dir_column in directions:
                new_row = row + dir_row #New column coord for room
                new_column = column + dir_column #New row coord for room

                if (
                    0 <= new_row < self.size#that is how many room are there
                    and
                    0 <= new_column < self.size
                    and not
                    self.visited[new_row][new_column]
                ):
                    x = column * self.stride + 1
                    y = row * self.stride + 1
                    # this point to the top left tile of the room

                    new_x = new_column * self.stride + 1
                    new_y = new_row * self.stride + 1
                    #the new top left tile of the new room from the directoin

                    if dir_row == 1: #go down
                        passage_x = x + self.room // 2 #make sure it is in the middle of the room
                        passage_y = y + self.room

                        for i in range(self.hallway):
                            self.maze[passage_y + i][passage_x] = 1 #it make that tile become 1 which is floor

                    elif dir_row == -1: #go up
                        passage_x = x + self.room // 2
                        passage_y = y - 1

                        for i in range(self.hallway):
                            self.maze[passage_y - i][passage_x] = 1

                    elif dir_column == 1: #go right
                        passage_x = x + self.room
                        passage_y = y + self.room //2

                        for i in range(self.hallway):
                            self.maze[passage_y][passage_x + i] = 1

                    elif dir_column == -1: #go left
                        passage_x = x - 1
                        passage_y = y + self.room // 2

                        for i in range(self.hallway):
                            self.maze[passage_y][passage_x - i] = 1

                    # When we create the maze we fill it with wall so when we carve out room there is already
                    # wall around it so we can do the hallway outside of the room which is the wall.

                    self.visited[new_row][new_column] = True
                    stack.append((new_row,new_column))

    def gen_maze(self):
        self.create_grid()
        self.dfs((self.size//2),(self.size//2))

        return self.maze
