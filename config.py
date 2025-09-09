import random


WINDOW_WIDTH = 960
WINDOW_HEIGHT = 512
TILE_SIZE = 32
FPS = 60
PLAYER_SPEED = 2
ENEMY_SPEED = 1
DIAG_SPEED = PLAYER_SPEED * 0.7071

PLAYER_LAYER = 3
WALL_LAYER = 2
GROUND_LAYER = 1
ENEMY_LAYER = 3

RED = (255, 0 ,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)


# ground = 0
# wall = 1 - 7
# player = 90
# enemy = 200
tilemap = []

# Create empty map with walls
for row in range(16):  # 16 rows
    if row == 0 or row == 15:  # top & bottom walls
        tilemap.append([1] * 30)
    else:
        tilemap.append([1] + [0] * 28 + [1])

# Top-left rectangle cluster
tilemap[0][0] = 1
tilemap[0][1] = 2
tilemap[0][2] = 3
tilemap[1][0] = 4
tilemap[1][1] = 5
tilemap[1][2] = 6

# Top-right snake cluster
tilemap[0][27] = 1
tilemap[0][28] = 2
tilemap[1][28] = 3
tilemap[1][29] = 4
tilemap[2][29] = 5

# Middle rectangle cluster
tilemap[6][6] = 1
tilemap[6][7] = 2
tilemap[6][8] = 3
tilemap[7][6] = 4
tilemap[7][7] = 5
tilemap[7][8] = 6
tilemap[8][6] = 7
tilemap[8][7] = 1
tilemap[8][8] = 2

# Middle snake cluster
tilemap[9][9] = 3
tilemap[9][10] = 4
tilemap[10][10] = 5
tilemap[10][11] = 6
tilemap[11][11] = 7
tilemap[11][12] = 1

# Bottom-left rectangle cluster
tilemap[12][2] = 2
tilemap[12][3] = 3
tilemap[13][2] = 4
tilemap[13][3] = 5
tilemap[14][2] = 6

# Bottom-right snake cluster
tilemap[11][25] = 7
tilemap[11][26] = 1
tilemap[12][25] = 2
tilemap[12][26] = 3
tilemap[13][26] = 4

# Additional middle clusters
tilemap[5][12] = 5
tilemap[5][13] = 6
tilemap[6][12] = 7
tilemap[6][13] = 1
tilemap[7][12] = 2
tilemap[7][13] = 3
tilemap[8][12] = 4
tilemap[8][13] = 5
tilemap[9][12] = 6
tilemap[9][13] = 7

# Player spawn
tilemap[8][8] = 90

# Enemy spawn
tilemap[14][6] = 200
tilemap[3][14] = 200
