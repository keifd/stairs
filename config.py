WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
TILE_SIZE = 20
FPS = 60
PLAYER_SPEED = 3
DIAG_SPEED = 0.7071

PLAYER_LAYER = 2
GROUND_LAYER = 1

RED = (255, 0 ,0)
BLACK = (0,0,0)


tilemap = []

# 720 / 20
for row in range(36):
    if row == 0 or row == 35:
        # Top and bottom walls
        tilemap.append([1]*64)
    else:
        # Side walls and empty space inside
        tilemap.append([1] + [0]*62 + [1])

print(tilemap)
