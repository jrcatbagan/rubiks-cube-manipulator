#!/usr/bin/python2.7
#
# Copyright (c) 2015, Jarielle Catbagan

import copy

#-----------------------------------------------------------------------------
# Some constants to aid in indexing and manipulating the Rubik's Cube
# data structure

# Face defines
FRONT = 0
LEFT = 1
BACK = 2
RIGHT = 3
UP = 4
DOWN = 5
MIDDLE_FB = 6
MIDDLE_RL = 7
MIDDLE_UD = 8

# Color defines
RED = 0
GREEN = 1
ORANGE = 2
BLUE = 3
WHITE = 4
YELLOW = 5

# Rotation defines
CW = 0
CCW = 1

# Default state of Rubik's Cube
_rubiks_cube_default_state = \
[
    [
        [
            {GREEN:LEFT, RED:FRONT, WHITE:UP},
            {RED:FRONT, WHITE:UP},
            {BLUE:RIGHT, RED:FRONT, WHITE:UP}
        ],
        [
            {GREEN:LEFT, RED:FRONT},
            {RED:FRONT},
            {BLUE:RIGHT, RED:FRONT}
        ],
        [
            {GREEN:LEFT, RED:FRONT, YELLOW:DOWN},
            {RED:FRONT, YELLOW:DOWN},
            {BLUE:RIGHT, RED:FRONT, YELLOW:DOWN}
        ]
    ],
    [
        [
            {GREEN:LEFT, WHITE:UP},
            {WHITE:UP},
            {BLUE:RIGHT, WHITE:UP}
        ],
        [
            {GREEN:LEFT},
            {},
            {BLUE:RIGHT}
        ],
        [
            {GREEN:LEFT, YELLOW:DOWN},
            {YELLOW:DOWN},
            {BLUE:RIGHT, YELLOW:DOWN}
        ],
    ],
    [
        [
            {GREEN:LEFT, ORANGE:BACK, WHITE:UP},
            {ORANGE:BACK, WHITE:UP},
            {BLUE:RIGHT, ORANGE:BACK, WHITE:UP}
        ],
        [
            {GREEN:LEFT, ORANGE:BACK},
            {ORANGE:BACK},
            {BLUE:RIGHT, ORANGE:BACK}
        ],
        [
            {GREEN:LEFT, ORANGE:BACK, YELLOW:DOWN},
            {ORANGE:BACK, YELLOW:DOWN},
            {BLUE:RIGHT, ORANGE:BACK, YELLOW:DOWN}
        ]
    ]

]

# ANSI code
color_code = \
[
    '\033[91m' + u'\u25fc' + '\033[0m',
    '\033[92m' + u'\u25fc' + '\033[0m',
    '\033[95m' + u'\u25fc' + '\033[0m',
    '\033[94m' + u'\u25fc' + '\033[0m',
    '\033[97m' + u'\u25fc' + '\033[0m',
    '\033[93m' + u'\u25fc' + '\033[0m'
]

class rubiks_cube_object:
    def __init__(self, rubiks_cube_init_state = _rubiks_cube_default_state):
        self.__rubiks_cube = rubiks_cube_init_state
        self.__total_moves = 0

    def get_current_state(self):
        return self.__rubiks_cube

    def display_visual(self):
        for __layer in range(2, -1, -1):
            print "       ",
            for __cubie in self.__rubiks_cube[__layer][0]:
                for __color, __face in __cubie.iteritems():
                    if __face == UP:
                        print color_code[__color],
            print ""

        for __row in range(0, 3):
            print " ",
            for __layer in range(2, -1, -1):
                __cubie = self.__rubiks_cube[__layer][__row][0]
                for __color, __face in __cubie.iteritems():
                    if __face == LEFT:
                        print color_code[__color],
            for __column in range(0, 3):
                __cubie = self.__rubiks_cube[0][__row][__column]
                for __color, __face in __cubie.iteritems():
                    if __face == FRONT:
                        print color_code[__color],
            for __layer in range(0, 3):
                __cubie = self.__rubiks_cube[__layer][__row][2]
                for __color, __face in __cubie.iteritems():
                    if __face == RIGHT:
                        print color_code[__color],
            for __column in range(2, -1, -1):
                __cubie = self.__rubiks_cube[2][__row][__column]
                for __color, __face in __cubie.iteritems():
                    if __face == BACK:
                        print color_code[__color],
            print ""

        for __layer in range(0, 3):
            print "       ",
            for __cubie in self.__rubiks_cube[__layer][2]:
                for __color, __face in __cubie.iteritems():
                    if __face == DOWN:
                        print color_code[__color],
            print ""

        print ""

    def twist_face(self, face, direction):
        if (face == FRONT and direction == CW) or \
                (face == BACK and direction == CCW):

            if face == FRONT:
                __layer = 0
            elif face == BACK:
                __layer = 2

            __temp_cubie = copy.deepcopy(self.__rubiks_cube[__layer][0][0])
            self.__rubiks_cube[__layer][0][0] = \
                    self.__rubiks_cube[__layer][2][0]
            self.__rubiks_cube[__layer][2][0] = \
                    self.__rubiks_cube[__layer][2][2]
            self.__rubiks_cube[__layer][2][2] = \
                    self.__rubiks_cube[__layer][0][2]
            self.__rubiks_cube[__layer][0][2] = __temp_cubie

            __temp_cubie = copy.deepcopy(self.__rubiks_cube[__layer][0][1])
            self.__rubiks_cube[__layer][0][1] = \
                    self.__rubiks_cube[__layer][1][0]
            self.__rubiks_cube[__layer][1][0] = \
                    self.__rubiks_cube[__layer][2][1]
            self.__rubiks_cube[__layer][2][1] = \
                    self.__rubiks_cube[__layer][1][2]
            self.__rubiks_cube[__layer][1][2] = \
                    __temp_cubie

            for __row in self.__rubiks_cube[__layer]:
                for __cubie in __row:
                    for __color, __face in __cubie.iteritems():
                        if __face == UP:
                            __cubie[__color] = RIGHT
                        elif __face == RIGHT:
                            __cubie[__color] = DOWN
                        elif __face == DOWN:
                            __cubie[__color] = LEFT
                        elif __face == LEFT:
                            __cubie[__color] = UP
        elif (face == FRONT and direction == CCW) or \
                (face == BACK and direction == CW):

            if face == FRONT:
                __layer = 0
            elif face == BACK:
                __layer = 2

            __temp_cubie = copy.deepcopy(self.__rubiks_cube[__layer][0][0])
            self.__rubiks_cube[__layer][0][0] = \
                    self.__rubiks_cube[__layer][0][2]
            self.__rubiks_cube[__layer][0][2] = \
                    self.__rubiks_cube[__layer][2][2]
            self.__rubiks_cube[__layer][2][2] = \
                    self.__rubiks_cube[__layer][2][0]
            self.__rubiks_cube[__layer][2][0] = __temp_cubie

            __temp_cubie = copy.deepcopy(self.__rubiks_cube[__layer][0][1])
            self.__rubiks_cube[__layer][0][1] = \
                    self.__rubiks_cube[__layer][1][2]
            self.__rubiks_cube[__layer][1][2] = \
                    self.__rubiks_cube[__layer][2][1]
            self.__rubiks_cube[__layer][2][1] = \
                    self.__rubiks_cube[__layer][1][0]
            self.__rubiks_cube[__layer][1][0] = \
                    __temp_cubie

            if face == FRONT:
                for __row in self.__rubiks_cube[__layer]:
                    for __cubie in __row:
                        for __color, __face in __cubie.iteritems():
                            if __face == UP:
                                __cubie[__color] = LEFT
                            elif __face == LEFT:
                                __cubie[__color] = DOWN
                            elif __face == DOWN:
                                __cubie[__color] = RIGHT
                            elif __face == RIGHT:
                                __cubie[__color] = UP
            elif face == BACK:
                for __row in self.__rubiks_cube[__layer]:
                    for __cubie in __row:
                        for __color, __face in __cubie.iteritems():
                            if __face == UP:
                                __cubie[__color] = LEFT
                            elif __face == LEFT:
                                __cubie[__color] = DOWN
                            elif __face == DOWN:
                                __cubie[__color] = RIGHT
                            elif __face == RIGHT:
                                __cubie[__color] = UP

        elif (face == RIGHT and direction == CW) or \
               (face == LEFT and direction == CCW):

            if face == RIGHT:
                __column = 2
            elif face == LEFT:
                __column = 0

            __temp_cubie = copy.deepcopy(self.__rubiks_cube[0][0][__column])
            self.__rubiks_cube[0][0][__column] = \
                    self.__rubiks_cube[0][2][__column]
            self.__rubiks_cube[0][2][__column] = \
                    self.__rubiks_cube[2][2][__column]
            self.__rubiks_cube[2][2][__column] = \
                    self.__rubiks_cube[2][0][__column]
            self.__rubiks_cube[2][0][__column] = __temp_cubie

            __temp_cubie = copy.deepcopy(self.__rubiks_cube[1][0][__column])
            self.__rubiks_cube[1][0][__column] = \
                    self.__rubiks_cube[0][1][__column]
            self.__rubiks_cube[0][1][__column] = \
                    self.__rubiks_cube[1][2][__column]
            self.__rubiks_cube[1][2][__column] = \
                    self.__rubiks_cube[2][1][__column]
            self.__rubiks_cube[2][1][__column] = \
                    __temp_cubie

            for __row in range(0, 3):
                for __layer in range(0, 3):
                    __cubie = self.__rubiks_cube[__layer][__row][__column]
                    for __color, __face in __cubie.iteritems():
                        if __face == UP:
                            __cubie[__color] = BACK
                        elif __face == BACK:
                            __cubie[__color] = DOWN
                        elif __face == DOWN:
                            __cubie[__color] = FRONT
                        elif __face == FRONT:
                            __cubie[__color] = UP

        elif (face == RIGHT and direction == CCW) or \
               (face == LEFT and direction == CW):

            if face == RIGHT:
                __column = 2
            elif face == LEFT:
                __column = 0

            __temp_cubie = copy.deepcopy(self.__rubiks_cube[0][0][__column])
            self.__rubiks_cube[0][0][__column] = \
                    self.__rubiks_cube[2][0][__column]
            self.__rubiks_cube[2][0][__column] = \
                    self.__rubiks_cube[2][2][__column]
            self.__rubiks_cube[2][2][__column] = \
                    self.__rubiks_cube[0][2][__column]
            self.__rubiks_cube[0][2][__column] = __temp_cubie

            __temp_cubie = copy.deepcopy(self.__rubiks_cube[1][0][__column])
            self.__rubiks_cube[1][0][__column] = \
                    self.__rubiks_cube[2][1][__column]
            self.__rubiks_cube[2][1][__column] = \
                    self.__rubiks_cube[1][2][__column]
            self.__rubiks_cube[1][2][__column] = \
                    self.__rubiks_cube[0][1][__column]
            self.__rubiks_cube[0][1][__column] = \
                    __temp_cubie

            for __row in range(0, 3):
                for __layer in range(0, 3):
                    __cubie = self.__rubiks_cube[__layer][__row][__column]
                    for __color, __face in __cubie.iteritems():
                        if __face == UP:
                            __cubie[__color] = FRONT
                        elif __face == FRONT:
                            __cubie[__color] = DOWN
                        elif __face == DOWN:
                            __cubie[__color] = BACK
                        elif __face == BACK:
                            __cubie[__color] = UP

        elif (face == UP and direction == CW) or \
                (face == DOWN and direction == CCW):

            if face == UP:
                __row = 0
            elif face == DOWN:
                __row = 2

            __temp_cubie = copy.deepcopy(self.__rubiks_cube[0][__row][0])
            self.__rubiks_cube[0][__row][0] = \
                    self.__rubiks_cube[0][__row][2]
            self.__rubiks_cube[0][__row][2] = \
                    self.__rubiks_cube[2][__row][2]
            self.__rubiks_cube[2][__row][2] = \
                    self.__rubiks_cube[2][__row][0]
            self.__rubiks_cube[2][__row][0] = \
                    __temp_cubie

            __temp_cubie = copy.deepcopy(self.__rubiks_cube[0][__row][1])
            self.__rubiks_cube[0][__row][1] = \
                    self.__rubiks_cube[1][__row][2]
            self.__rubiks_cube[1][__row][2] = \
                    self.__rubiks_cube[2][__row][1]
            self.__rubiks_cube[2][__row][1] = \
                    self.__rubiks_cube[1][__row][0]
            self.__rubiks_cube[1][__row][0] = \
                    __temp_cubie

            for __layer in range(0, 3):
                for __cubie in self.__rubiks_cube[__layer][__row]:
                    for __color, __face in __cubie.iteritems():
                        if __face == FRONT:
                            __cubie[__color] = LEFT
                        elif __face == LEFT:
                            __cubie[__color] = BACK
                        elif __face == BACK:
                            __cubie[__color] = RIGHT
                        elif __face == RIGHT:
                            __cubie[__color] = FRONT
        elif (face == UP and direction == CCW) or \
                (face == DOWN and direction == CW):

            if face == UP:
                __row = 0
            elif face == DOWN:
                __row = 2

            __temp_cubie = copy.deepcopy(self.__rubiks_cube[0][__row][0])
            self.__rubiks_cube[0][__row][0] = \
                    self.__rubiks_cube[2][__row][0]
            self.__rubiks_cube[2][__row][0] = \
                    self.__rubiks_cube[2][__row][2]
            self.__rubiks_cube[2][__row][2] = \
                    self.__rubiks_cube[0][__row][2]
            self.__rubiks_cube[0][__row][2] = \
                    __temp_cubie

            __temp_cubie = copy.deepcopy(self.__rubiks_cube[0][__row][1])
            self.__rubiks_cube[0][__row][1] = \
                    self.__rubiks_cube[1][__row][0]
            self.__rubiks_cube[1][__row][0] = \
                    self.__rubiks_cube[2][__row][1]
            self.__rubiks_cube[2][__row][1] = \
                    self.__rubiks_cube[1][__row][2]
            self.__rubiks_cube[1][__row][2] = \
                    __temp_cubie

            for __layer in range(0, 3):
                for __cubie in self.__rubiks_cube[__layer][__row]:
                    for __color, __face in __cubie.iteritems():
                        if __face == FRONT:
                            __cubie[__color] = RIGHT
                        elif __face == RIGHT:
                            __cubie[__color] = BACK
                        elif __face == BACK:
                            __cubie[__color] = LEFT
                        elif __face == LEFT:
                            __cubie[__color] = FRONT

    def twist_middle_layer(self, middle_layer, direction):
        if middle_layer == MIDDLE_FB and direction == CW:
            __temp_cubie = copy.deepcopy(self.__rubiks_cube[1][0][0])
            self.__rubiks_cube[1][0][0] = self.__rubiks_cube[1][2][0]
            self.__rubiks_cube[1][2][0] = self.__rubiks_cube[1][2][2]
            self.__rubiks_cube[1][2][2] = self.__rubiks_cube[1][0][2]
            self.__rubiks_cube[1][0][2] = __temp_cubie
            __temp_cubie = copy.deepcopy(self.__rubiks_cube[1][0][1])
            self.__rubiks_cube[1][0][1] = self.__rubiks_cube[1][1][0]
            self.__rubiks_cube[1][1][0] = self.__rubiks_cube[1][2][1]
            self.__rubiks_cube[1][2][1] = self.__rubiks_cube[1][1][2]
            self.__rubiks_cube[1][1][2] = __temp_cubie
            for __row in range(0, 3):
                for __cubie in self.__rubiks_cube[1][__row]:
                    for __color, __face in __cubie.iteritems():
                        if __face == UP:
                            __cubie[__color] = RIGHT
                        elif __face == RIGHT:
                            __cubie[__color] = DOWN
                        elif __face == DOWN:
                            __cubie[__color] = LEFT
                        elif __face == LEFT:
                            __cubie[__color] = UP
        elif middle_layer == MIDDLE_FB and direction == CCW:
            __temp_cubie = copy.deepcopy(self.__rubiks_cube[1][0][0])
            self.__rubiks_cube[1][0][0] = self.__rubiks_cube[1][0][2]
            self.__rubiks_cube[1][0][2] = self.__rubiks_cube[1][2][2]
            self.__rubiks_cube[1][2][2] = self.__rubiks_cube[1][2][0]
            self.__rubiks_cube[1][2][0] = __temp_cubie
            __temp_cubie = copy.deepcopy(self.__rubiks_cube[1][0][1])
            self.__rubiks_cube[1][0][1] = self.__rubiks_cube[1][1][2]
            self.__rubiks_cube[1][1][2] = self.__rubiks_cube[1][2][1]
            self.__rubiks_cube[1][2][1] = self.__rubiks_cube[1][1][0]
            self.__rubiks_cube[1][1][0] = __temp_cubie
            for __row in range(0, 3):
                for __cubie in self.__rubiks_cube[1][__row]:
                    for __color, __face in __cubie.iteritems():
                        if __face == UP:
                            __cubie[__color] = LEFT
                        elif __face == LEFT:
                            __cubie[__color] = DOWN
                        elif __face == DOWN:
                            __cubie[__color] = RIGHT
                        elif __face == RIGHT:
                            __cubie[__color] = UP
        elif middle_layer == MIDDLE_RL and direction == CW:
            __temp_cubie = copy.deepcopy(self.__rubiks_cube[0][0][1])
            self.__rubiks_cube[0][0][1] = self.__rubiks_cube[0][2][1]
            self.__rubiks_cube[0][2][1] = self.__rubiks_cube[2][2][1]
            self.__rubiks_cube[2][2][1] = self.__rubiks_cube[2][0][1]
            self.__rubiks_cube[2][0][1] = __temp_cubie
            __temp_cubie = copy.deepcopy(self.__rubiks_cube[1][0][1])
            self.__rubiks_cube[1][0][1] = self.__rubiks_cube[0][1][1]
            self.__rubiks_cube[0][1][1] = self.__rubiks_cube[1][2][1]
            self.__rubiks_cube[1][2][1] = self.__rubiks_cube[2][1][1]
            self.__rubiks_cube[2][1][1] = __temp_cubie
            for __layer in range(0, 3):
                for __row in range(0, 3):
                    __cubie = self.__rubiks_cube[__layer][__row][1]
                    for __color, __face in __cubie.iteritems():
                        if __face == UP:
                            __cubie[__color] = BACK
                        elif __face == BACK:
                            __cubie[__color] = DOWN
                        elif __face == DOWN:
                            __cubie[__color] = FRONT
                        elif __face == FRONT:
                            __cubie[__color] = UP
        elif middle_layer == MIDDLE_RL and direction == CCW:
            __temp_cubie = copy.deepcopy(self.__rubiks_cube[0][0][1])
            self.__rubiks_cube[0][0][1] = self.__rubiks_cube[2][0][1]
            self.__rubiks_cube[2][0][1] = self.__rubiks_cube[2][2][1]
            self.__rubiks_cube[2][2][1] = self.__rubiks_cube[0][2][1]
            self.__rubiks_cube[0][2][1] = __temp_cubie
            __temp_cubie = copy.deepcopy(self.__rubiks_cube[1][0][1])
            self.__rubiks_cube[1][0][1] = self.__rubiks_cube[2][1][1]
            self.__rubiks_cube[2][1][1] = self.__rubiks_cube[1][2][1]
            self.__rubiks_cube[1][2][1] = self.__rubiks_cube[0][1][1]
            self.__rubiks_cube[0][1][1] = __temp_cubie
            for __layer in range(0, 3):
                for __row in range(0, 3):
                    __cubie = self.__rubiks_cube[__layer][__row][1]
                    for __color, __face in __cubie.iteritems():
                        if __face == UP:
                            __cubie[__color] = FRONT
                        elif __face == FRONT:
                            __cubie[__color] = DOWN
                        elif __face == DOWN:
                            __cubie[__color] = BACK
                        elif __face == BACK:
                            __cubie[__color] = UP
        elif middle_layer == MIDDLE_UD and direction == CW:
            __temp_cubie = copy.deepcopy(self.__rubiks_cube[0][1][0])
            self.__rubiks_cube[0][1][0] = self.__rubiks_cube[0][1][2]
            self.__rubiks_cube[0][1][2] = self.__rubiks_cube[2][1][2]
            self.__rubiks_cube[2][1][2] = self.__rubiks_cube[2][1][0]
            self.__rubiks_cube[2][1][0] = __temp_cubie
            __temp_cubie = copy.deepcopy(self.__rubiks_cube[0][1][1])
            self.__rubiks_cube[0][1][1] = self.__rubiks_cube[1][1][2]
            self.__rubiks_cube[1][1][2] = self.__rubiks_cube[2][1][1]
            self.__rubiks_cube[2][1][1] = self.__rubiks_cube[1][1][0]
            self.__rubiks_cube[1][1][0] = __temp_cubie
            for __layer in range(0, 3):
                for __column in range(0, 3):
                    __cubie = self.__rubiks_cube[__layer][1][__column]
                    for __color, __face in __cubie.iteritems():
                        if __face == FRONT:
                            __cubie[__color] = LEFT
                        elif __face == LEFT:
                            __cubie[__color] = BACK
                        elif __face == BACK:
                            __cubie[__color] = RIGHT
                        elif __face == RIGHT:
                            __cubie[__color] = FRONT
        elif middle_layer == MIDDLE_UD and direction == CCW:
            __temp_cubie = copy.deepcopy(self.__rubiks_cube[0][1][0])
            self.__rubiks_cube[0][1][0] = self.__rubiks_cube[2][1][0]
            self.__rubiks_cube[2][1][0] = self.__rubiks_cube[2][1][2]
            self.__rubiks_cube[2][1][2] = self.__rubiks_cube[0][1][2]
            self.__rubiks_cube[0][1][2] = __temp_cubie
            __temp_cubie = copy.deepcopy(self.__rubiks_cube[0][1][1])
            self.__rubiks_cube[0][1][1] = self.__rubiks_cube[1][1][0]
            self.__rubiks_cube[1][1][0] = self.__rubiks_cube[2][1][1]
            self.__rubiks_cube[2][1][1] = self.__rubiks_cube[1][1][2]
            self.__rubiks_cube[1][1][2] = __temp_cubie
            for __layer in range(0, 3):
                for __column in range(0, 3):
                    __cubie = self.__rubiks_cube[__layer][1][__column]
                    for __color, __face in __cubie.iteritems():
                        if __face == FRONT:
                            __cubie[__color] = RIGHT
                        elif __face == RIGHT:
                            __cubie[__color] = BACK
                        elif __face == BACK:
                            __cubie[__color] = LEFT
                        elif __face == LEFT:
                            __cubie[__color] = FRONT

    def rotate_cube(self, face, direction):
        if (face == FRONT and direction == CW) or \
                (face == BACK and direction == CCW):
            self.twist_face(FRONT, CW)
            self.twist_middle_layer(MIDDLE_FB, CW)
            self.twist_face(BACK, CCW)
            print "X"
        elif (face == FRONT and direction == CCW) or \
                (face == BACK and direction == CW):
            self.twist_face(FRONT, CCW)
            self.twist_middle_layer(MIDDLE_FB, CCW)
            self.twist_face(BACK, CW)
            print "X'"
        elif (face == RIGHT and direction == CW) or \
                (face == LEFT and direction == CCW):
            self.twist_face(RIGHT, CW)
            self.twist_middle_layer(MIDDLE_RL, CW)
            self.twist_face(LEFT, CCW)
            print "Y"
        elif (face == RIGHT and direction == CCW) or \
                (face == LEFT and direction == CW):
            self.twist_face(RIGHT, CCW)
            self.twist_middle_layer(MIDDLE_RL, CCW)
            self.twist_face(LEFT, CW)
            print "Y'"
        elif (face == UP and direction == CW) or \
                (face == DOWN and direction == CCW):
            self.twist_face(UP, CW)
            self.twist_middle_layer(MIDDLE_UD, CW)
            self.twist_face(DOWN, CCW)
            print "Z"
        elif (face == UP and direction == CCW) or \
                (face == DOWN and direction == CW):
            self.twist_face(UP, CCW)
            self.twist_middle_layer(MIDDLE_UD, CCW)
            self.twist_face(DOWN, CW)
            print "Z'"

    def algorithm(self, sequence):
        __operation = ""
        for i in range(0, len(sequence)):
            if sequence[i] != ' ':
                __operation += sequence[i]

            if sequence[i] == ' ' or i == len(sequence) - 1:
                self.__total_moves += 1
                if __operation == "R":
                    self.twist_face(RIGHT, CW)
                    print "R",
                elif __operation == "R'":
                    self.twist_face(RIGHT, CCW)
                    print "R'",
                elif __operation == "L":
                    self.twist_face(LEFT, CW)
                    print "L",
                elif __operation == "L'":
                    self.twist_face(LEFT, CCW)
                    print "L'",
                elif __operation == "F":
                    self.twist_face(FRONT, CW)
                    print "F",
                elif __operation == "F'":
                    self.twist_face(FRONT, CCW)
                    print "F'",
                elif __operation == "B":
                    self.twist_face(BACK, CW)
                    print "B",
                elif __operation == "B'":
                    self.twist_face(BACK, CCW)
                    print "B'",
                elif __operation == "U":
                    self.twist_face(UP, CW)
                    print "U",
                elif __operation == "U'":
                    self.twist_face(UP, CCW)
                    print "U'",
                elif __operation == "D":
                    self.twist_face(DOWN, CW)
                    print "D",
                elif __operation == "D'":
                    self.twist_face(DOWN, CCW)
                    print "D'",

                __operation = ""

        print ""

    def solve_top_corners(self):

       #          5-----------6
       #         /|          /|
       #        / |         / |
       #       /  |        /  |
       #      1-----------2   |
       #      |   |       |   |
       #      |   7-------|---8
       #      |  /        |  /
       #      | /         | /
       #      |/          |/
       #      3-----------4

        CORNER_POS_1 = 0
        CORNER_POS_2 = 1
        CORNER_POS_3 = 2
        CORNER_POS_4 = 3
        CORNER_POS_5 = 4
        CORNER_POS_6 = 5
        CORNER_POS_7 = 6
        CORNER_POS_8 = 7

        CUBIE_LFU = 0
        CUBIE_RFU = 1
        CUBIE_LBU = 2
        CUBIE_RBU = 3

        __cubie_color = \
        [
            [GREEN, RED, WHITE],
            [BLUE, RED, WHITE],
            [BLUE, ORANGE, WHITE],
            [GREEN, ORANGE, WHITE]
        ]

        # Resolve the top layer corners cubie by cubie
        for cubie_index in range(0, 4):
            __corner_position = 0

            # Locate for the top layer corner cubie at interest
            for __layer in range(0, 3, 2):
                for __row in range(0, 3, 2):
                    for __column in range(0, 3, 2):
                        __cubie = self.__rubiks_cube[__layer][__row][__column]

                        if __cubie_color[cubie_index][0] in __cubie and \
                                __cubie_color[cubie_index][1] in __cubie and \
                                __cubie_color[cubie_index][2] in __cubie:
                            __cubie_position = __corner_position

                        __corner_position += 1

            if __cubie_position == CORNER_POS_1:
                if self.__rubiks_cube[0][0][0][WHITE] == LEFT:
                    self.algorithm("L D L' D' D' F' D F")
                elif self.__rubiks_cube[0][0][0][WHITE] == FRONT:
                    self.algorithm("F' D' F D D L D' L'")
            elif __cubie_position == CORNER_POS_2:
                if self.__rubiks_cube[0][0][2][WHITE] == RIGHT:
                    self.algorithm("R' L D' R L'")
                elif self.__rubiks_cube[0][0][2][WHITE] == FRONT:
                    self.algorithm("F D F' D F' D F")
                elif self.__rubiks_cube[0][0][2][WHITE] == UP:
                    self.algorithm("R' D' D' R F' D F")
            elif __cubie_position == CORNER_POS_3:
                if self.__rubiks_cube[0][2][0][WHITE] == LEFT:
                    self.algorithm("D' F' D F")
                elif self.__rubiks_cube[0][2][0][WHITE] == FRONT:
                    self.algorithm("D L D' L'")
                elif self.__rubiks_cube[0][2][0][WHITE] == DOWN:
                    self.algorithm("L D' L' D F' D F")
            elif __cubie_position == CORNER_POS_4:
                if self.__rubiks_cube[0][2][2][WHITE] == RIGHT:
                    self.algorithm("L D' L'")
                elif self.__rubiks_cube[0][2][2][WHITE] == FRONT:
                    self.algorithm("D' D' F' D F")
                elif self.__rubiks_cube[0][2][2][WHITE] == DOWN:
                    self.algorithm("D' F' D F L D' D' L'")
            elif __cubie_position == CORNER_POS_5:
                if self.__rubiks_cube[2][0][0][WHITE] == LEFT:
                    self.algorithm("L' D' D' L L D' L'")
                elif self.__rubiks_cube[2][0][0][WHITE] == BACK:
                    self.algorithm("B F' D' B' F")
                elif self.__rubiks_cube[2][0][0][WHITE] == UP:
                    self.algorithm("B D' D' B' L D' L'")
            elif __cubie_position == CORNER_POS_6:
                if self.__rubiks_cube[2][0][2][WHITE] == RIGHT:
                    self.algorithm("R D R' F' D F")
                elif self.__rubiks_cube[2][0][2][WHITE] == BACK:
                    self.algorithm("B' D' B L D' L'")
                elif self.__rubiks_cube[2][0][2][WHITE] == UP:
                    self.algorithm("B' D' B D' D' F' D F")
            elif __cubie_position == CORNER_POS_7:
                if self.__rubiks_cube[2][2][0][WHITE] == LEFT:
                    self.algorithm("D D L D' L'")
                elif self.__rubiks_cube[2][2][0][WHITE] == BACK:
                    self.algorithm("F' D F")
                elif self.__rubiks_cube[2][2][0][WHITE] == DOWN:
                    self.algorithm("D F' D F D' L D' L'")
            elif __cubie_position == CORNER_POS_8:
                if self.__rubiks_cube[2][2][2][WHITE] == RIGHT:
                    self.algorithm("F' D D F")
                elif self.__rubiks_cube[2][2][2][WHITE] == BACK:
                    self.algorithm("L D' D' L'")
                elif self.__rubiks_cube[2][2][2][WHITE] == DOWN:
                    self.algorithm("D D F' D F D' L D' L'")

            self.rotate_cube(UP, CW)

    def solve_top_edges(self):
        #     -----9-----
        #    /|        /|
        #   5 |       6 |
        #  /  10     /  11
        # -----1-----   |
        # |   |     |   |
        # |   ----12|---|
        # 2  /      3  /
        # | 7       | 8
        # |/        |/
        # -----4-----

        EDGE_POS_UNDEFINED = -1
        EDGE_POS1 = 0
        EDGE_POS2 = 1
        EDGE_POS3 = 2
        EDGE_POS4 = 3
        EDGE_POS5 = 4
        EDGE_POS6 = 5
        EDGE_POS7 = 6
        EDGE_POS8 = 7
        EDGE_POS9 = 8
        EDGE_POS10 = 9
        EDGE_POS11 = 10
        EDGE_POS12 = 11

        __cubie_color = \
        [
            [RED, WHITE],
            [BLUE, WHITE],
            [ORANGE, WHITE],
            [GREEN, WHITE]
        ]

        # Resolve the top layer edges cubie by cubie
        for __cubie_index in range(0, 4):
            __edge_position = 0

            # Locate for the top layer edge cubie at interest
            for __layer in range(0, 3):
                if __layer == 1:
                    for __row in range(0, 3, 2):
                        for __column in range(0, 3, 2):
                            __cubie = self.__rubiks_cube[__layer][__row][__column]
                            if __cubie_color[__cubie_index][0] in __cubie and \
                                    __cubie_color[__cubie_index][1] in __cubie:
                                __cubie_position = __edge_position
                                __edge_cubie = __cubie
                            else:
                                __edge_position += 1
                else:
                    for __row in range(0, 3):
                        if __row == 1:
                            for __column in range(0, 3, 2):
                                __cubie = self.__rubiks_cube[__layer][__row][__column]
                                if __cubie_color[__cubie_index][0] in __cubie and \
                                        __cubie_color[__cubie_index][1] in __cubie:
                                    __cubie_position = __edge_position
                                    __edge_cubie = __cubie
                                else:
                                    __edge_position += 1
                        else:
                            __cubie = self.__rubiks_cube[__layer][__row][1]
                            if __cubie_color[__cubie_index][0] in __cubie and \
                                    __cubie_color[__cubie_index][1] in __cubie:
                                __cubie_position = __edge_position
                                __edge_cubie = __cubie
                            else:
                                __edge_position += 1

            if __cubie_position == EDGE_POS1:
                if __edge_cubie[WHITE] == FRONT:
                    self.algorithm("F F D R F' R'")
            elif __cubie_position == EDGE_POS2:
                if __edge_cubie[WHITE] == LEFT:
                    self.algorithm("F")
                elif __edge_cubie[WHITE] == FRONT:
                    self.algorithm("F' D R F' R'")
            elif __cubie_position == EDGE_POS3:
                if __edge_cubie[WHITE] == RIGHT:
                    self.algorithm("F'")
                elif __edge_cubie[WHITE] == FRONT:
                    self.algorithm("F D R F' R'")
            elif __cubie_position == EDGE_POS4:
                if __edge_cubie[WHITE] == FRONT:
                    self.algorithm("D R F' R'")
                elif __edge_cubie[WHITE] == DOWN:
                    self.algorithm("F F")
            elif __cubie_position == EDGE_POS5:
                if __edge_cubie[WHITE] == LEFT:
                    self.algorithm("L F")
                elif __edge_cubie[WHITE] == UP:
                    self.algorithm("L L D F F")
            elif __cubie_position == EDGE_POS6:
                if __edge_cubie[WHITE] == RIGHT:
                    self.algorithm("R' F'")
                elif __edge_cubie[WHITE] == UP:
                    self.algorithm("R' R' D' F' F'")
            elif __cubie_position == EDGE_POS7:
                if __edge_cubie[WHITE] == LEFT:
                    self.algorithm("D D R F' R'")
                elif __edge_cubie[WHITE] == DOWN:
                    self.algorithm("D F F")
            elif __cubie_position == EDGE_POS8:
                if __edge_cubie[WHITE] == RIGHT:
                    self.algorithm("R F' R")
                elif __edge_cubie[WHITE] == DOWN:
                    self.algorithm("D' F' F'")
            elif __cubie_position == EDGE_POS9:
                if __edge_cubie[WHITE] == BACK:
                    self.algorithm("B' B' D' R F' R'")
                elif __edge_cubie[WHITE] == UP:
                    self.algorithm("B' B' D' D' F' F'")
            elif __cubie_position == EDGE_POS10:
                if __edge_cubie[WHITE] == LEFT:
                    self.algorithm("B D' D' B' F' F'")
                elif __edge_cubie[WHITE] == BACK:
                    self.algorithm("B' D' B R F' R'")
            elif __cubie_position == EDGE_POS11:
                if __edge_cubie[WHITE] == RIGHT:
                    self.algorithm("B' D' D' B F' F'")
                elif __edge_cubie[WHITE] == BACK:
                    self.algorithm("B' D' B R F' R'")
            elif __cubie_position == EDGE_POS12:
                if __edge_cubie[WHITE] == BACK:
                    self.algorithm("D' R F' R'")
                elif __edge_cubie[WHITE] == DOWN:
                    self.algorithm("D' D' F' F'")

            self.rotate_cube(UP, CW)

    def get_total_moves(self):
        return self.__total_moves

    def solve_middle_layer(self):
        self.rotate_cube(FRONT, CW)
        self.rotate_cube(FRONT, CW)

        EDGE_POS_UNDEFINED = -1
        EDGE_POS1 = 0
        EDGE_POS2 = 1
        EDGE_POS3 = 2
        EDGE_POS4 = 3
        EDGE_POS5 = 4
        EDGE_POS6 = 5
        EDGE_POS7 = 6
        EDGE_POS8 = 7
        EDGE_POS9 = 8
        EDGE_POS10 = 9
        EDGE_POS11 = 10
        EDGE_POS12 = 11

        __cubie_color = \
        [
            [BLUE, RED],
            [RED, GREEN],
            [GREEN, ORANGE],
            [ORANGE, BLUE]
        ]

        # First remove all the middle layer edge pieces at interest if they
        # are not in the right place to the top layer
        for __cubie_index in range(0, 4):
            __cubie = self.__rubiks_cube[0][1][0]
            if __cubie_color[__cubie_index][0] in __cubie and \
                    __cubie_color[__cubie_index][1] in __cubie:
                if __cubie[__cubie_color[__cubie_index][1]] == FRONT:
                    pass
                else:
                    if YELLOW in self.__rubiks_cube[0][0][1].keys():
                        self.algorithm("U' L' U L U F U' F'")
                    elif YELLOW in self.__rubiks_cube[1][0][0].keys():
                        self.algorithm("U' U' L' U L U F U' F'")
                    elif YELLOW in self.__rubiks_cube[1][0][2].keys():
                        self.algorithm("L' U L U F U' F'")
                    elif YELLOW in self.__rubiks_cube[2][0][1].keys():
                        self.algorithm("U L' U L U F U' F'")
            else:
                if YELLOW in __cubie.keys():
                    pass
                else:
                    if YELLOW in self.__rubiks_cube[0][0][1].keys():
                        self.algorithm("U' L' U L U F U' F'")
                    elif YELLOW in self.__rubiks_cube[1][0][0].keys():
                        self.algorithm("U' U' L' U L U F U' F'")
                    elif YELLOW in self.__rubiks_cube[1][0][2].keys():
                        self.algorithm("L' U L U F U' F'")
                    elif YELLOW in self.__rubiks_cube[2][0][1].keys():
                        self.algorithm("U L' U L U F U' F'")
            self.rotate_cube(UP, CW)

        # Now place the middle layer edge pieces from the top layer to the
        # right locations
        for __cubie_index in range(0, 4):
            for __layer in range(0, 3):
                if __layer == 0:
                    __cubie = self.__rubiks_cube[__layer][0][1]
                    if __cubie_color[__cubie_index][0] in __cubie and \
                            __cubie_color[__cubie_index][1] in __cubie:
                        if __cubie[__cubie_color[__cubie_index][1]] == FRONT:
                            self.algorithm("U' L' U L U F U' F'")
                        else:
                            self.algorithm("U U F U' F' U' L' U L")
                elif __layer == 1:
                    for __column in range(0, 3, 2):
                        __cubie = self.__rubiks_cube[__layer][0][__column]
                        if __cubie_color[__cubie_index][0] in __cubie and \
                                __cubie_color[__cubie_index][1] in __cubie:
                            if __column == 0:
                                if __cubie[__cubie_color[__cubie_index][1]] == \
                                        LEFT:
                                    self.algorithm("U' U' L' U L U F U' F'")
                                elif __cubie[__cubie_color[__cubie_index][1]] == \
                                        UP:
                                    self.algorithm("U F U' F' U' L' U L")
                            elif __column == 2:
                                if __cubie[__cubie_color[__cubie_index][1]] == \
                                        RIGHT:
                                    self.algorithm("L' U L U F U' F'")
                                elif __cubie[__cubie_color[__cubie_index][1]] == \
                                        UP:
                                    self.algorithm("U' F U' F' U' L' U L")
                elif __layer == 2:
                    __cubie = self.__rubiks_cube[__layer][0][1]
                    if __cubie_color[__cubie_index][0] in __cubie and \
                            __cubie_color[__cubie_index][1] in __cubie:
                        if __cubie[__cubie_color[__cubie_index][1]] == BACK:
                            self.algorithm("U L' U L U F U' F'")
                        elif __cubie[__cubie_color[__cubie_index][1]] == UP:
                            self.algorithm("F U' F' U' L' U L")
            self.rotate_cube(UP, CW)

    def solve_top_layer(self):
        # Orient all edges with yellow side facing up
        while 1:
            if self.__rubiks_cube[0][0][1][YELLOW] == UP and \
                    self.__rubiks_cube[1][0][0][YELLOW] == UP and \
                    self.__rubiks_cube[1][0][2][YELLOW] == UP and \
                    self.__rubiks_cube[2][0][1][YELLOW] == UP:
                break
            elif self.__rubiks_cube[0][0][1][YELLOW] == UP and \
                    self.__rubiks_cube[1][0][0][YELLOW] != UP and \
                    self.__rubiks_cube[1][0][2][YELLOW] != UP and \
                    self.__rubiks_cube[2][0][1][YELLOW] == UP:
                self.algorithm("U F R U R' U' F'")
            elif self.__rubiks_cube[0][0][1][YELLOW] != UP and \
                    self.__rubiks_cube[1][0][0][YELLOW] == UP and \
                    self.__rubiks_cube[1][0][2][YELLOW] == UP and \
                    self.__rubiks_cube[2][0][1][YELLOW] != UP:
                self.algorithm("F R U R' U' F'")
            elif self.__rubiks_cube[0][0][1][YELLOW] == UP and \
                    self.__rubiks_cube[1][0][0][YELLOW] == UP and \
                    self.__rubiks_cube[1][0][2][YELLOW] != UP and \
                    self.__rubiks_cube[2][0][1][YELLOW] != UP:
                self.algorithm("U F U R U' R' F'")
            elif self.__rubiks_cube[0][0][1][YELLOW] != UP and \
                    self.__rubiks_cube[1][0][0][YELLOW] == UP and \
                    self.__rubiks_cube[1][0][2][YELLOW] != UP and \
                    self.__rubiks_cube[2][0][1][YELLOW] == UP:
                self.algorithm("F U R U' R' F'")
            elif self.__rubiks_cube[0][0][1][YELLOW] != UP and \
                    self.__rubiks_cube[1][0][0][YELLOW] != UP and \
                    self.__rubiks_cube[1][0][2][YELLOW] == UP and \
                    self.__rubiks_cube[2][0][1][YELLOW] == UP:
                self.algorithm("U' F U R U' R' F'")
            elif self.__rubiks_cube[0][0][1][YELLOW] == UP and \
                    self.__rubiks_cube[1][0][0][YELLOW] != UP and \
                    self.__rubiks_cube[1][0][2][YELLOW] == UP and \
                    self.__rubiks_cube[2][0][1][YELLOW] != UP:
                self.algorithm("U U F U R U' R' F'")
            else:
                self.algorithm("F U R U' R' F'")

        # Orient all corners with yellow side facing up
        while 1:
            # All yellow corners facing up
            if self.__rubiks_cube[0][0][0][YELLOW] == UP and \
                    self.__rubiks_cube[0][0][2][YELLOW] == UP and \
                    self.__rubiks_cube[2][0][0][YELLOW] == UP and \
                    self.__rubiks_cube[2][0][2][YELLOW] == UP:
                break
            # No yellow corners facing up
            elif self.__rubiks_cube[0][0][0][YELLOW] != UP and \
                    self.__rubiks_cube[0][0][2][YELLOW] != UP and \
                    self.__rubiks_cube[2][0][0][YELLOW] != UP and \
                    self.__rubiks_cube[2][0][2][YELLOW] != UP:
                while 1:
                    if self.__rubiks_cube[0][0][0][YELLOW] == LEFT:
                        break
                    else:
                        self.rotate_cube(UP, CW)
                self.algorithm("R U R' U R U U R'")
            # One yellow corner facing up
            elif self.__rubiks_cube[0][0][0][YELLOW] == UP and \
                    self.__rubiks_cube[0][0][2][YELLOW] != UP and \
                    self.__rubiks_cube[2][0][0][YELLOW] != UP and \
                    self.__rubiks_cube[2][0][2][YELLOW] != UP:
                self.algorithm("R U R' U R U U R'")
            elif self.__rubiks_cube[0][0][0][YELLOW] != UP and \
                    self.__rubiks_cube[0][0][2][YELLOW] == UP and \
                    self.__rubiks_cube[2][0][0][YELLOW] != UP and \
                    self.__rubiks_cube[2][0][2][YELLOW] != UP:
                self.algorithm("U R U R' U R U U R'")
            elif self.__rubiks_cube[0][0][0][YELLOW] != UP and \
                    self.__rubiks_cube[0][0][2][YELLOW] != UP and \
                    self.__rubiks_cube[2][0][0][YELLOW] == UP and \
                    self.__rubiks_cube[2][0][2][YELLOW] != UP:
                self.algorithm("U' R U R' U R U U R'")
            elif self.__rubiks_cube[0][0][0][YELLOW] != UP and \
                    self.__rubiks_cube[0][0][2][YELLOW] != UP and \
                    self.__rubiks_cube[2][0][0][YELLOW] != UP and \
                    self.__rubiks_cube[2][0][2][YELLOW] == UP:
                self.algorithm("U U R U R' U R U U R'")
            # More than one yellow corner facing up
            else:
                while 1:
                    if self.__rubiks_cube[0][0][0][YELLOW] == FRONT:
                        break
                    else:
                        self.rotate_cube(UP, CW)
                self.algorithm("R U R' U R U U R'")

        INCOMPLETE = 0
        COMPLETE = 1

        __corner_init_state = INCOMPLETE

        while 1:
            for __index in range(0, 4):
                if __corner_init_state == INCOMPLETE:
                    for __color, __face in \
                            self.__rubiks_cube[0][0][0].iteritems():
                        if __face == FRONT:
                            __color1 = __color
                    for __color, __face in \
                            self.__rubiks_cube[0][0][2].iteritems():
                        if __face == FRONT:
                            __color2 = __color

                    if __color1 == __color2:
                        if __color1 == __color2 == \
                                self.__rubiks_cube[0][1][1].keys()[0]:
                            self.rotate_cube(UP, CCW)
                            self.rotate_cube(UP, CCW)
                        elif __color1 == __color2 == \
                                self.__rubiks_cube[1][1][0].keys()[0]:
                            self.algorithm("U")
                            self.rotate_cube(UP, CW)
                        elif __color1 == __color2 == \
                                self.__rubiks_cube[1][1][2].keys()[0]:
                            self.algorithm("U'")
                            self.rotate_cube(UP, CCW)
                        elif __color1 == __color2 == \
                                self.__rubiks_cube[2][1][1].keys()[0]:
                            self.algorithm("U U")

                        __corner_init_state = COMPLETE
                    else:
                        self.rotate_cube(UP, CW)

            if __corner_init_state == INCOMPLETE:
                self.algorithm("R' F R' B B R F' R' B B R R U'")
            else:
                STATE0A = -1
                STATE1A = 0
                STATE2A = 1
                STATE3A = 2
                STATE4A = 3
                STATE5A = 4
                STATE6A = 5

                STATE0B = -1
                STATE1B = 6
                STATE2B = 7

                __rotation_state1 = STATE0A
                __rotation_state2 = STATE0B


                if RED in self.__rubiks_cube[0][1][1].keys():
                    pass
                elif RED in self.__rubiks_cube[1][1][0].keys():
                    __rotation_state1 = STATE1A
                    self.rotate_cube(UP, CCW)
                elif RED in self.__rubiks_cube[1][1][2].keys():
                    __rotation_state1 = STATE2A
                    self.rotate_cube(UP, CW)
                elif RED in self.__rubiks_cube[2][1][1].keys():
                    __rotation_state1 = STATE3A
                    self.rotate_cube(UP, CW)
                    self.rotate_cube(UP, CW)
                elif RED in self.__rubiks_cube[1][0][1].keys():
                    __rotation_state1 = STATE4A
                    self.rotate_cube(RIGHT, CCW)
                else: # RED in self.__rubiks_cube[1][2][1].keys():
                    __rotation_state1 = STATE5A
                    self.rotate_cube(RIGHT, CW)

                if WHITE in self.__rubiks_cube[1][0][1].keys():
                    pass
                elif WHITE in self.__rubiks_cube[1][2][1].keys():
                    # TODO: Fix this,
                    __rotation_state2 = STATE1B
                    self.rotate_cube(FRONT, CW)
                    self.rotate_cube(FRONT, CW)
                else:
                    pass

                if self.__rubiks_cube != _rubiks_cube_default_state:
                    if __rotation_state2 == STATE1B:
                        self.rotate_cube(FRONT, CCW)
                        self.rotate_cube(FRONT, CCW)

                    if __rotation_state1 == STATE1A:
                        self.rotate_cube(UP, CW)
                    elif __rotation_state1 == STATE2A:
                        self.rotate_cube(UP, CCW)
                    elif __rotation_state1 == STATE3A:
                        self.rotate_cube(UP, CCW)
                        self.rotate_cube(UP, CCW)
                    elif __rotation_state1 == STATE4A:
                        self.rotate_cube(RIGHT, CW)
                    elif __rotation_state1 == STATE5A:
                        self.rotate_cube(RIGHT, CCW)

                    self.algorithm("R' F R' B B R F' R' B B R R U'")
                break

        __edge_init_state = INCOMPLETE

        for __color, __face in self.__rubiks_cube[0][0][1].iteritems():
            if __face == FRONT:
                __edge1_color = __color
        for __color, __face in self.__rubiks_cube[1][0][0].iteritems():
            if __face == LEFT:
                __edge2_color = __color
        for __color, __face in self.__rubiks_cube[1][0][2].iteritems():
            if __face == RIGHT:
                __edge3_color = __color
        for __color, __face in self.__rubiks_cube[2][0][1].iteritems():
            if __face == BACK:
                __edge4_color = __color

        # Perform the following if no top layer edges are correct
        if __edge1_color != self.__rubiks_cube[0][1][1].keys()[0] and \
                __edge2_color != self.__rubiks_cube[1][1][0].keys()[0] and \
                __edge3_color != self.__rubiks_cube[1][1][2].keys()[0] and \
                __edge4_color != self.__rubiks_cube[2][1][1].keys()[0]:
            self.algorithm("F F U L R' F F L' R U F F")

            for __color, __face in self.__rubiks_cube[0][0][1].iteritems():
                if __face == FRONT:
                    __edge1_color = __color
            for __color, __face in self.__rubiks_cube[1][0][0].iteritems():
                if __face == LEFT:
                    __edge2_color = __color
            for __color, __face in self.__rubiks_cube[1][0][2].iteritems():
                if __face == RIGHT:
                    __edge3_color = __color
            for __color, __face in self.__rubiks_cube[2][0][1].iteritems():
                if __face == BACK:
                    __edge4_color = __color

            # Position the right edge to the back face
            if __edge1_color == self.__rubiks_cube[0][1][1].keys()[0]:
                self.rotate_cube(UP, CW)
                self.rotate_cube(UP, CW)
                __temp_edge_color = copy.deepcopy(__edge1_color)
                __edge1_color = __edge4_color
                __edge4_color = __temp_edge_color
                __temp_edge_color = __edge2_color
                __edge2_color = __edge3_color
                __edge3_color = __temp_edge_color
            elif __edge2_color == self.__rubiks_cube[1][1][0].keys()[0]:
                self.rotate_cube(UP, CW)
                __temp_edge_color = copy.deepcopy(__edge1_color)
                __edge1_color = __edge3_color
                __edge3_color = __edge4_color
                __edge4_color = __edge2_color
                __edge2_color = __temp_edge_color
            elif __edge3_color == self.__rubiks_cube[1][1][2].keys()[0]:
                self.rotate_cube(UP, CCW)
                __temp_edge_color = copy.deepcopy(__edge1_color)
                __edge1_color = __edge2_color
                __edge2_color = __edge4_color
                __edge4_color = __edge3_color
                __edge3_color = __temp_edge_color

            if __edge1_color == self.__rubiks_cube[1][1][0].keys()[0]:
                self.algorithm("F F U L R' F F L' R U F F")
            elif __edge1_color == self.__rubiks_cube[1][1][2].keys()[0]:
                self.algorithm("F F U' L R' F F L' R U' F F")

        elif __edge1_color == self.__rubiks_cube[0][1][1].keys()[0] and \
                __edge2_color == self.__rubiks_cube[1][1][0].keys()[0] and \
                __edge3_color == self.__rubiks_cube[1][1][2].keys()[0] and \
                __edge4_color == self.__rubiks_cube[2][1][1].keys()[0]:
            pass
        else:
            # Position the right edge to the back face
            if __edge1_color == self.__rubiks_cube[0][1][1].keys()[0]:
                self.rotate_cube(UP, CW)
                self.rotate_cube(UP, CW)
                __temp_edge_color = copy.deepcopy(__edge1_color)
                __edge1_color = __edge4_color
                __edge4_color = __temp_edge_color
                __temp_edge_color = __edge2_color
                __edge2_color = __edge3_color
                __edge3_color = __temp_edge_color
            elif __edge2_color == self.__rubiks_cube[1][1][0].keys()[0]:
                self.rotate_cube(UP, CW)
                __temp_edge_color = copy.deepcopy(__edge1_color)
                __edge1_color = __edge3_color
                __edge3_color = __edge4_color
                __edge4_color = __edge2_color
                __edge2_color = __temp_edge_color
            elif __edge3_color == self.__rubiks_cube[1][1][2].keys()[0]:
                self.rotate_cube(UP, CCW)
                __temp_edge_color = copy.deepcopy(__edge1_color)
                __edge1_color = __edge2_color
                __edge2_color = __edge4_color
                __edge4_color = __edge3_color
                __edge3_color = __temp_edge_color

            if __edge1_color == self.__rubiks_cube[1][1][0].keys()[0]:
                self.algorithm("F F U L R' F F L' R U F F")
            elif __edge1_color == self.__rubiks_cube[1][1][2].keys()[0]:
                self.algorithm("F F U' L R' F F L' R U' F F")
