import sys
from field import Field
from field import Result

def read_map_from_file(path):
    """
    Reads map from its representation in file
    """
    input_file = open(path, 'r')
    battlemap = []
    size = int(input_file.readline())
    for i in range(size):
        battlemap.append(map(lambda c: 0 if int(c) == 0 else -1, input_file.readline().strip()))
    input_file.close()
    return battlemap

def compare_fields(field1, field2):
    """
    Compares two fields and checks that the game is fair.
    method is very naive and just checks that field sizes are the same, not the ships layot
    todo: check ships layout
    """"
    if field1.field_size() == field2.field_size():
        return True
    return False

def read_coordinates(coordinates_input, field_size):
    """
    Reads coordinate from keyboard and checks for input correctness
    """
    coordinates = coordinates_input.strip().split(" ")
    if len(coordinates) != 2:
        print "Please input two coordidates"
        return (-1, -1)
    y, x = int(coordinates[0]) - 1, int(coordinates[1]) - 1
    if y not in range(0, field_size) or x not in range(0, field_size):
        print "Please enter valid coordinates in range 1 .. " + str(field_size)
        return (-1, -1)
    return x, y

def run(fields):
    """
    Main game loop
    """
    turn = 0
    if len(fields) != 2 or not compare_fields(fields[0], fields[1]):
        print "The game should be fair. Enter two eqaully hard fields!"
        return

    while True:
        print "Player " + str(turn + 1) + " turn:"
        x, y = read_coordinates(raw_input(), fields[0].field_size())
        if (x, y) == (-1, -1):
            continue
        result = fields[1 - turn].hit(x, y)
        print result
        if result == Result.Win:
            return
        if result == Result.Miss or result == Result.Taken:
            turn = 1 - turn


if len(sys.argv) != 3:
    print "Run command in the format: python battleship.py pathtomap1 pathtomap2"
else:
    run([Field(read_map_from_file(sys.argv[1])), Field(read_map_from_file(sys.argv[2]))])
