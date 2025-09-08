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



tilemap = []

for row in range(22):  # 22 rows
    if row == 0 or row == 21:  # top & bottom walls
        tilemap.append([1] * 40)
    else:
        # side walls + empty space inside
        tilemap.append([1] + [0] * 38 + [1])


# Cluster 1 (top-left corner)
tilemap[2][3] = 1
tilemap[2][4] = 1
tilemap[3][4] = 1
tilemap[3][5] = 1

# Cluster 2 (upper-middle)
tilemap[6][10] = 1
tilemap[6][11] = 1
tilemap[7][11] = 1
tilemap[8][11] = 1

# Cluster 3 (middle-right)
tilemap[10][30] = 1
tilemap[10][31] = 1
tilemap[11][30] = 1
tilemap[11][31] = 1
tilemap[12][31] = 1

# Cluster 4 (bottom-left)
tilemap[17][5] = 1
tilemap[17][6] = 1
tilemap[18][5] = 1

# Cluster 5 (bottom-right)
tilemap[15][35] = 1
tilemap[15][36] = 1
tilemap[16][35] = 1
tilemap[16][36] = 1
tilemap[17][35] = 1
tilemap[17][36] = 1


# Set player manually
tilemap[10][10] = 2  # player position
