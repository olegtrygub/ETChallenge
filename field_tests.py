from field import Field
from field import Result

def field_tests():
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
    field = Field([[-1, -1,  0,-1, -1], \
                   [ 0, -1,  0, 0, -1], \
                   [-1,  0,  0, 0,  0], \
                   [-1,  0, -1, 0, -1], \
                   [-1, -1, -1, 0,  0]])
    assert field.nships == 4

field_tests()
