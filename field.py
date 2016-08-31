"""
Class that represents enum for game turn Result
"""
class Result:
    Miss, Hit, Sank, Taken, Win = ["miss", "hit", "sank", "double shot", "win"]

"""
Class that represents battle field
"""
class Field:
    def __init__(self, battlemap):
        self.map = battlemap
        self.size = len(battlemap)
        self.ships = []
        self.load_map()
        self.nships = len(self.ships)

    def visit(self, i, j, cnt):
        """
        Visit ship's node as part of DFS when discovering ships in the map
        """
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
        """
        Loads map from file, discovers ships and builds ships array
        """
        cnt = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.map[i][j] == -1:
                    cnt += 1
                    self.ships.append(set([]))
                    self.visit(i, j, cnt)

    def hit_ship(self, x, y):
        """
        Hits ship part at specified coordinates
        """
        ship = self.ships[self.map[x][y] - 1]
        self.map[x][y] = -1
        if len(ship) == 1:
            ship.clear()
            self.nships -= 1
            if self.nships == 0:
                return Result.Win
            return Result.Sank

        ship.remove((x, y))
        return Result.Hit

    def hit(self, x, y):
        """
        Hits the map at specified coordinates
        """
        if self.map[x][y] < 0:
            return Result.Taken
        if self.map[x][y] == 0:
            return Result.Miss

        return self.hit_ship(x, y)

    def field_size(self):
        """
        Returns field size
        """
        return self.size
