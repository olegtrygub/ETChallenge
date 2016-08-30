import sys

class Result:
    Miss, Hit, Sank, Taken, Win = ["miss", "hit", "sank", "double shot", "win"]

class Field:
    def visit(self, i, j, cnt):
        if self.map[i][j] >= 0:
            return
        self.map[i][j] = cnt
        self.ships[cnt-1].add((i, j))
        if i > 0:
            self.visit(i-1, j, cnt)
        if j > 0:
            self.visit(i, j-1, cnt)
        if i < self.size - 1:
            self.visit(i+1, j, cnt)
        if j < self.size - 1:
            self.visit(i, j+1, cnt)

    def load_map(self):
        cnt = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.map[i][j] == -1:
                    cnt += 1
                    self.ships.append(set([]))
                    self.visit(i, j, cnt)

    def __init__(self, battlemap):
        self.map = battlemap
        self.size = len(battlemap)
        self.ships = []
        self.load_map()
        self.nships = len(self.ships)

    def hit_ship(self, x, y):
        ship = self.ships[self.map[x][y] - 1]
        self.map[x][y] *= -1
        if len(ship) < 2:
            ship.clear()
            self.nships -= 1
            if self.nships == 0:
                return Result.Win
            return Result.Sank

        ship.remove((x, y))
        return Result.Hit

    def hit(self, x, y):
        if self.map[x][y] < 0:
            return Result.Taken
        if self.map[x][y] == 0:
            return Result.Miss

        return self.hit_ship(x, y)

def Field_tests():
    field = Field([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])
    assert len(field.ships) == 3
    field = Field([[0, -1, 0], [0, -1, 0], [0, 0, -1]])
    assert len(field.ships) == 2
    field = Field([[0, 0, -1, 0, -1], [-1, 0, 0, 0, -1], [-1, 0, 0, 0, 0], [-1, 0, -1, 0, -1], [0, 0, -1, 0, 0]])
    assert len(field.ships) == 5
    assert field.hit(1, 0) == Result.Hit
    assert field.hit(1, 1) == Result.Miss
    assert field.hit(2, 0) == Result.Hit
    assert field.hit(3, 0) == Result.Sank
    assert field.nships == 4
    assert field.hit(4, 2) == Result.Hit
    assert field.hit(2, 2) == Result.Miss
    assert field.hit(0, 4) == Result.Hit
    assert field.hit(3, 4) == Result.Sank
    assert field.nships == 3
    assert field.hit(3, 2) == Result.Sank
    assert field.nships == 2
    assert field.hit(0, 2) == Result.Sank
    assert field.nships == 1
    assert field.hit(1, 4) == Result.Win
    assert field.nships == 0
    field = Field([[ 0,  0,  0,-1, -1], \
                   [ 0,  0,  0, 0, -1], \
                   [-1,  0,  0, 0,  0], \
                   [-1,  0, -1, 0,  0], \
                   [-1, -1, -1, 0,  0]])
    assert field.nships == 2

def read_map_from_file(path):
    input_file = open(path, 'r')
    battlemap = []
    size = int(input_file.readline())
    for i in range(size):
        battlemap.append(map(lambda c: 0 if int(c) == 0 else -1, input_file.readline().strip()))
    input_file.close()
    return battlemap

def run(fields):
    turn = 0
    while True:
        print "Player " + str(turn + 1) + " turn:"
        coordinates = raw_input().split(" ")
        y, x = int(coordinates[0]) -  1, int(coordinates[1]) - 1
        print fields[1 - turn].ships
        result = fields[1 - turn].hit(x, y)
        print result
        if result == Result.Win:
            return
        if result == Result.Miss or result == Result.Taken:
            turn = 1 - turn

run(Field(sys.argv[1]), Field(sys.argv[2]))
