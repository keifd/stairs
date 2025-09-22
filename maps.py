# ground = .
# wall = W
# player = P
# enemy = E
# healthpot = H
# deathpot = D
# up_stair = U
# down_stair = S
worlds = ['world_1', 'world_2', 'world_3']
stages = ['stage_1', 'stage_2', 'stage_3']

worlds = {
    "world_1": {
        "stage_1": [
            'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
            'W...H...................................W',
            'W...............E.......................W',
            'W....................E..................W',
            'W.......WWWWW................D..........W',
            'W...................E...................W',
            'W...........P..................H........W',
            'W........................E.............SW',
            'W...............E.......................W',
            'W.......................................W',
            'W......................WWWWWW...........W',
            'W.......................................W',
            'W.......................................W',
            'W........H..........................H...W',
            'W.......................................W',
            'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
        ],
        "stage_2": [
            'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
            'W.....................E........HW',
            'W...............E......WWWWWWWWWW',
            'W...............E......W',
            'W...............E......W',
            'W...............E......W',
            'W.........UP....E......W',
            'W...............E......W',
            'W...............E......W',
            'W...D..................W',
            'W......................WWWWWWWWWWWWWWWWWW',
            'W.......................................W',
            'W.......................................W',
            'W.......................................W',
            'W......................................SW',
            'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
        ],
        "stage_3": [
            '                                                  W.',
            'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW.',
            'WUWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW.',
            'WPWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW.W',
            'W.WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW.W',
            'W.......E...........................................W',
            'W...........E............................WWWWWWWWWWWWW',
            'W................E.......................W',
            'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
        ],
    },
    "world_2": {
        "stage_1": [
            # stage map here
        ],
        "stage_2": [
            # stage map here
        ],
    },
    # add more worlds if needed
}
