import random


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 704
TILE_SIZE = 32
FPS = 60
PLAYER_SPEED = 2
DIAG_SPEED = 0.7071

PLAYER_LAYER = 3
WALL_LAYER = 2
GROUND_LAYER = 1

RED = (255, 0 ,0)
BLACK = (0,0,0)
BLUE = (0,0,255)


# ground = 0
# wall = 1 - 7
# character = 2
tilemap = []

for row in range(22):  # 22 rows
    if row == 0 or row == 21:  # top & bottom walls
        tilemap.append([1] * 40)
    else:
        # side walls + empty space inside
        tilemap.append([1] + [0] * 38 + [1])


# Top-left rectangle cluster
tilemap[0][0] = 1
tilemap[0][1] = 2
tilemap[0][2] = 3
tilemap[1][0] = 4
tilemap[1][1] = 5
tilemap[1][2] = 6

# Top-right snake cluster
tilemap[0][37] = 1
tilemap[0][38] = 2
tilemap[1][38] = 3
tilemap[1][39] = 4
tilemap[2][39] = 5

# Middle rectangle cluster
tilemap[8][8] = 1
tilemap[8][9] = 2
tilemap[8][10] = 3
tilemap[9][8] = 4
tilemap[9][9] = 5
tilemap[9][10] = 6
tilemap[10][8] = 7
tilemap[10][9] = 1
tilemap[10][10] = 2

# Middle snake cluster
tilemap[11][12] = 3
tilemap[11][13] = 4
tilemap[12][13] = 5
tilemap[12][14] = 6
tilemap[13][14] = 7
tilemap[13][15] = 1

# Bottom-left rectangle cluster
tilemap[17][2] = 2
tilemap[17][3] = 3
tilemap[18][2] = 4
tilemap[18][3] = 5
tilemap[19][2] = 6

# Bottom-right snake cluster
tilemap[15][35] = 7
tilemap[15][36] = 1
tilemap[16][35] = 2
tilemap[16][36] = 3
tilemap[17][36] = 4

# Additional middle clusters (brute force filling)
tilemap[6][15] = 5
tilemap[6][16] = 6
tilemap[7][15] = 7
tilemap[7][16] = 1
tilemap[8][15] = 2
tilemap[8][16] = 3
tilemap[9][15] = 4
tilemap[9][16] = 5
tilemap[10][15] = 6
tilemap[10][16] = 7

# Player spawn
tilemap[10][10] = 90