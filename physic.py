#Collission detectino and other physic
from maze import TILE_SIZE


def is_walkable(new_x,new_y,maze):
    tile_x = int(new_x // TILE_SIZE)
    tile_y = int(new_y // TILE_SIZE) # Player coord is different to the maze tile

    if tile_x < 0 or tile_y < 0: #outside the grid is never walkable
        return False
    if tile_y >= len(maze) or tile_x >= len(maze[0]):
        return False

    if maze[tile_y][tile_x] == 0:
        return False
    else:
        return True
