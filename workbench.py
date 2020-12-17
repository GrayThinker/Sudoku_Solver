"""
-------------Input---------------
* AR

* Random board generator
-------------Solving-------------

def pre_process():
    temporarily fill all empty cells with all potential 
    numbers that can occupy that cell without collisions.
    (temp filled cell do not cause collisions)

    find permanent cells
    If a cell only has one number filled then that number
    permanently occupies that cell.

    After permanent cells are found repeat until no cell has only
    one potential value.

    check for rows/cols/blocks with only 1 missing value


def dfs():
    test cases where more than one value can occupy a cell
    even after pre_processing.
    Should be called on cells with the least amount of potential
    values.
    The current path being checked is terminated if the board is solved
    or a paradox occurs. 
    A paradox is where adding a permanent value to a cell causes collisions


def no_collision(pos):
    function to check if there are any collisions in the
    matrix

    :param pos: 2 value tuple to the index of the element
    to be check

    :return bool: true if no collision exist else false

-------------Output---------------


-------------Classes---------------
:Board: representation of the board
used to get values in a cell
-should allow temp values
-once a permanent value is added remove all temp values
that cause collisions.

:Block: representation of one of the nine 3x3 blocks

:solver: process for solving a board
"""