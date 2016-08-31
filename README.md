# ETChallenge
##Overview
Due to time concerns I implemented relatively basic version of battleship, except that
it supports maps with ships of any form (i.e not only vertical/horizontal, but also snake-like)
and also various sizes of map.

Game is relatively small, so I used combination of object-oriented and procedural style. Where state should be maintained
I defined a class. For main game loop with couple of utilities I used plain functions.
Due to time concerns I wrote unit-tests only for main piece of the game - field class.

##Structure
field.py - contains class Field that represents battleship field for a single user

field_test.py - contains field class tests

battleship.py - contains game implementation like turns, main game loop, etc.

examples - contains map examples that can be input into game

##Running
battleship.py "filewithmap1" "filewithmap2"

Coordinates are in traditional layout for battleship - (x, y), where x, y belong to 1..size. Left upper corner is (1, 1),
right bottom - (size, size)
 

##Implementation of the field abstraction
Field is created from a map that is loaded from input file. After that, program runs DFS to discover ships
using map itself to track visited points. While doing this map is converted into the form
where 0 represents empty spot; and number 1..n - ship index in the ships array. Ships array contains ships in the form of 
set of coordidates/
