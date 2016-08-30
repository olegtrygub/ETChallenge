import sys
import field

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


run([field.Field(read_map_from_file(sys.argv[1])), field.Field(read_map_from_file(sys.argv[2]))])
