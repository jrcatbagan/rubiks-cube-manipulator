#!/usr/bin/python2.7

# Copyright (C) 2015, Jarielle Catbagan, Rebecca Grob, Gerson Ramos
#
# The Rubik's Cube is represented in an array of matrices.  The order is
# front, bottom, back, top, right, and then left.

import sys

rubiks_cube_pattern = \
[
        [['r', 'y', 'b'],
         ['w', 'b', 'o'],
         ['r', 'o', 'o']],
        [['y', 'b', 'g'],
         ['w', 'o', 'r'],
         ['y', 'g', 'g']],
        [['r', 'r', 'r'],
         ['y', 'g', 'b'],
         ['o', 'b', 'y']],
        [['y', 'r', 'g'],
         ['b', 'r', 'g'],
         ['b', 'g', 'w']],
        [['o', 'o', 'o'],
         ['y', 'w', 'y'],
         ['w', 'w', 'w']],
        [['b', 'w', 'w'],
         ['r', 'y', 'o'],
         ['b', 'g', 'g']]
]

rubiks_cube_default_pattern = \
[
        [['r', 'r', 'r'],
         ['r', 'r', 'r'],
         ['r', 'r', 'r']],
        [['y', 'y', 'y'],
         ['y', 'y', 'y'],
         ['y', 'y', 'y']],
        [['o', 'o', 'o'],
         ['o', 'o', 'o'],
         ['o', 'o', 'o']],
        [['w', 'w', 'w'],
         ['w', 'w', 'w'],
         ['w', 'w', 'w']],
        [['b', 'b', 'b'],
         ['b', 'b', 'b'],
         ['b', 'b', 'b']],
        [['g', 'g', 'g'],
         ['g', 'g', 'g'],
         ['g', 'g', 'g']]
]

class rubiks_cube:
    __front = 0
    __down = 1
    __back = 2
    __up = 3
    __right = 4
    __left = 5

    # Constructor
    def __init__(self, rubiks_cube_pattern = rubiks_cube_default_pattern):
        self.__rubiks_cube_pattern = rubiks_cube_pattern
    
    # Verify whether the initial pattern of the Rubik's Cube is valid by
    # determining whether all the colors have the same count and are equal
    # to 9.
    #
    # TODO: Need to check if the positions of the colors are correct.
    def verify_init_state(self):
        __r_cnt = 0
        __g_cnt = 0
        __b_cnt = 0
        __y_cnt = 0
        __o_cnt = 0
        __w_cnt = 0

        for __face in self.__rubiks_cube_pattern:
            for __row in __face:
                for __column in __row:
                    if __column == 'r':
                        __r_cnt += 1
                    elif __column == 'g':
                        __g_cnt += 1
                    elif __column == 'b':
                        __b_cnt += 1
                    elif __column == 'y':
                        __y_cnt += 1
                    elif __column == 'o':
                        __o_cnt += 1
                    elif __column == 'w':
                        __w_cnt += 1
        if not (__r_cnt == __g_cnt == __b_cnt == __y_cnt == __w_cnt ==
                __w_cnt == 9):
            print "error"
            sys.exit(-1)
        else:
            print "no error" 

    # Display the current pattern of the Rubik's Cube
    def display(self):
        for __face in self.__rubiks_cube_pattern:
            print __face

rubiks_cube_instance = rubiks_cube(rubiks_cube_pattern)

rubiks_cube_instance.verify_init_state()

rubiks_cube_instance.display()
