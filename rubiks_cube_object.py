#!/usr/bin/python2.7

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

    def get_current_state(self):
        return self.__rubiks_cube

    def display_visual(self):
        for __layer in range(2, -1, -1):
            print "     ",
            for __cubie in self.__rubiks_cube[__layer][0]:
                for __color, __face in __cubie.iteritems():
                    if __face == UP:
                        print color_code[__color],
            print ""

        for __row in range(0, 3):
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
            print "     ",
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
        elif (face == FRONT and direction == CCW) or \
                (face == BACK and direction == CW):
            self.twist_face(FRONT, CCW)
            self.twist_middle_layer(MIDDLE_FB, CCW)
            self.twist_face(BACK, CW)
        elif (face == RIGHT and direction == CW) or \
                (face == LEFT and direction == CCW):
            self.twist_face(RIGHT, CW)
            self.twist_middle_layer(MIDDLE_RL, CW)
            self.twist_face(LEFT, CCW)
        elif (face == RIGHT and direction == CCW) or \
                (face == LEFT and direction == CW):
            self.twist_face(RIGHT, CCW)
            self.twist_middle_layer(MIDDLE_RL, CCW)
            self.twist_face(LEFT, CW)
        elif (face == UP and direction == CW) or \
                (face == DOWN and direction == CCW):
            self.twist_face(UP, CW)
            self.twist_middle_layer(MIDDLE_UD, CW)
            self.twist_face(DOWN, CCW)
        elif (face == UP and direction == CCW) or \
                (face == DOWN and direction == CW):
            self.twist_face(UP, CCW)
            self.twist_middle_layer(MIDDLE_UD, CCW)
            self.twist_face(DOWN, CW)

    def algorithm(self, sequence):
        __operation = ""
        for i in range(0, len(sequence)):
            if sequence[i] != ' ':
                __operation += sequence[i]

            if sequence[i] == ' ' or i == len(sequence) - 1:
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
