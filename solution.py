
CONST_MISS = 0
CONST_HIT = 1
CONST_SANK = 2
CONST_TAKEN = 3
CONST_WIN = 4

import sys

class Field:
    def __init__(self, data = , ships = None):
        self.ships = ships
        self.nships = len(ships)

    def hit(self, x, y):
        if self.map[x][y] < 0:
            return CONST_TAKEN
        if self.map[x][y] == 0:
            return CONST_MISS

        ship = ships[self.map[x][y] - 1]
        self.map[x][y] *= -1
        if len(ship) < 2:
            ship.clear()
            self.nships -= 1
            if self.nships != 0:
                return CONST_SANK
            return CONST_WIN
        else:
            ship.remove((x, y))
            return CONST_HIT

def is_coordinate(s, m = None):
    try:
        val = int(s)
        return val > 0 and (m == None or val <= m)
    except ValueError:
        return False


def run(fields):
    turn = 0
    while True:
        status = "Player " + str(turn + 1) + " "
        print status + " turn:"
        coordinates = raw_input().split(" ")
        if len(coordinates) < 2:

        x, y = int(coordinates[0]), int(coordinates[1])
        result = fields[1 - turn].hit(x, y)
        if result == CONST_WIN:
            print status + "wins"
            return
        if result == CONST_SANK:
            print status + "sank a ship"
        elif result == CONST_HIT:
            print status + "hit a ship"
        elif result == CONST_MISS:
            turn = 1 - turn
            print status + "misses"
        elif result == CONST_TAKEN:
            turn = 1 - turn
            print status + "misses, double shot"


field = [[0, 0, 2, 0, 4], \
          [1, 0, 0, 0, 4], \
          [1, 0, 0, 0, 0], \
          [1, 0, 3, 0, 5], \
          [0, 0, 3, 0, 0]]
ships = [[(1, 1), (1, 2), (1, 3)], [(0, 2)], [(3, 2), (4, 2)], [(0, 4), (1, 4)]]
