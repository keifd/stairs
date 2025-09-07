import random


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
TILE_SIZE = 20
FPS = 60
PLAYER_SPEED = 3
DIAG_SPEED = 0.7071

PLAYER_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

RED = (255, 0 ,0)
BLACK = (0,0,0)
BLUE = (0,0,255)



tilemap = []

# 720 / 20
for row in range(36):
    if row == 0 or row == 35:
        # Top and bottom walls
        tilemap.append([1]*64)
    else:
        # Side walls and empty space inside
        tilemap.append([1] + [0]*62 + [1])

# Cluster 1
tilemap[2][3] = 1
tilemap[2][4] = 1
tilemap[3][4] = 1
tilemap[3][5] = 1

# Cluster 2
tilemap[6][10] = 1
tilemap[6][11] = 1
tilemap[7][11] = 1
tilemap[8][11] = 1

# Cluster 3
tilemap[12][20] = 1
tilemap[12][21] = 1
tilemap[13][20] = 1
tilemap[13][21] = 1
tilemap[14][21] = 1

# Cluster 4
tilemap[18][5] = 1
tilemap[18][6] = 1
tilemap[19][5] = 1

# Cluster 5
tilemap[25][50] = 1
tilemap[25][51] = 1
tilemap[26][50] = 1
tilemap[26][51] = 1
tilemap[27][50] = 1
tilemap[27][51] = 1

# Set player manually
tilemap[10][10] = 2  # player position
