#!/usr/bin/python2.7

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
        self.__rubiks_cube_state = rubiks_cube_init_state

    def get_current_state(self):
        return self.__rubiks_cube_state

    def display_visual(self):
        for __layer in range(2, -1, -1):
            print "     ",
            for __cubie in self.__rubiks_cube_state[__layer][0]:
                for __color, __face in __cubie.iteritems():
                    if __face == UP:
                        print color_code[__color],
            print ""

        for __row in range(0, 3):
            for __layer in range(2, -1, -1):
                __cubie = self.__rubiks_cube_state[__layer][__row][0]
                for __color, __face in __cubie.iteritems():
                    if __face == LEFT:
                        print color_code[__color],
            for __column in range(0, 3):
                __cubie = self.__rubiks_cube_state[0][__row][__column]
                for __color, __face in __cubie.iteritems():
                    if __face == FRONT:
                        print color_code[__color],
            for __layer in range(0, 3):
                __cubie = self.__rubiks_cube_state[__layer][__row][2]
                for __color, __face in __cubie.iteritems():
                    if __face == RIGHT:
                        print color_code[__color],
            for __column in range(2, -1, -1):
                __cubie = self.__rubiks_cube_state[2][__row][__column]
                for __color, __face in __cubie.iteritems():
                    if __face == BACK:
                        print color_code[__color],
            print ""

        for __layer in range(0, 3):
            print "     ",
            for __cubie in self.__rubiks_cube_state[__layer][2]:
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

            __temp_cubie = self.__rubiks_cube_state[__layer][0][0]
            self.__rubiks_cube_state[__layer][0][0] = \
                    self.__rubiks_cube_state[__layer][2][0]
            self.__rubiks_cube_state[__layer][2][0] = \
                    self.__rubiks_cube_state[__layer][2][2]
            self.__rubiks_cube_state[__layer][2][2] = \
                    self.__rubiks_cube_state[__layer][0][2]
            self.__rubiks_cube_state[__layer][0][2] = __temp_cubie

            __temp_cubie = self.__rubiks_cube_state[__layer][0][1]
            self.__rubiks_cube_state[__layer][0][1] = \
                    self.__rubiks_cube_state[__layer][1][0]
            self.__rubiks_cube_state[__layer][1][0] = \
                    self.__rubiks_cube_state[__layer][2][1]
            self.__rubiks_cube_state[__layer][2][1] = \
                    self.__rubiks_cube_state[__layer][1][2]
            self.__rubiks_cube_state[__layer][1][2] = \
                    __temp_cubie

            for __row in self.__rubiks_cube_state[__layer]:
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

            __temp_cubie = self.__rubiks_cube_state[__layer][0][0]
            self.__rubiks_cube_state[__layer][0][0] = \
                    self.__rubiks_cube_state[__layer][0][2]
            self.__rubiks_cube_state[__layer][0][2] = \
                    self.__rubiks_cube_state[__layer][2][2]
            self.__rubiks_cube_state[__layer][2][2] = \
                    self.__rubiks_cube_state[__layer][2][0]
            self.__rubiks_cube_state[__layer][2][0] = __temp_cubie

            __temp_cubie = self.__rubiks_cube_state[__layer][0][1]
            self.__rubiks_cube_state[__layer][0][1] = \
                    self.__rubiks_cube_state[__layer][1][2]
            self.__rubiks_cube_state[__layer][1][2] = \
                    self.__rubiks_cube_state[__layer][2][1]
            self.__rubiks_cube_state[__layer][2][1] = \
                    self.__rubiks_cube_state[__layer][1][0]
            self.__rubiks_cube_state[__layer][1][0] = \
                    __temp_cubie

            if face == FRONT:
                for __row in self.__rubiks_cube_state[__layer]:
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
                for __row in self.__rubiks_cube_state[__layer]:
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

            __temp_cubie = self.__rubiks_cube_state[0][0][__column]
            self.__rubiks_cube_state[0][0][__column] = \
                    self.__rubiks_cube_state[0][2][__column]
            self.__rubiks_cube_state[0][2][__column] = \
                    self.__rubiks_cube_state[2][2][__column]
            self.__rubiks_cube_state[2][2][__column] = \
                    self.__rubiks_cube_state[2][0][__column]
            self.__rubiks_cube_state[2][0][__column] = __temp_cubie

            __temp_cubie = self.__rubiks_cube_state[1][0][__column]
            self.__rubiks_cube_state[1][0][__column] = \
                    self.__rubiks_cube_state[0][1][__column]
            self.__rubiks_cube_state[0][1][__column] = \
                    self.__rubiks_cube_state[1][2][__column]
            self.__rubiks_cube_state[1][2][__column] = \
                    self.__rubiks_cube_state[2][1][__column]
            self.__rubiks_cube_state[2][1][__column] = \
                    __temp_cubie

            for __row in range(0, 3):
                for __layer in range(0, 3):
                    __cubie = self.__rubiks_cube_state[__layer][__row][__column]
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

            __temp_cubie = self.__rubiks_cube_state[0][0][__column]
            self.__rubiks_cube_state[0][0][__column] = \
                    self.__rubiks_cube_state[2][0][__column]
            self.__rubiks_cube_state[2][0][__column] = \
                    self.__rubiks_cube_state[2][2][__column]
            self.__rubiks_cube_state[2][2][__column] = \
                    self.__rubiks_cube_state[0][2][__column]
            self.__rubiks_cube_state[0][2][__column] = __temp_cubie

            __temp_cubie = self.__rubiks_cube_state[1][0][__column]
            self.__rubiks_cube_state[1][0][__column] = \
                    self.__rubiks_cube_state[2][1][__column]
            self.__rubiks_cube_state[2][1][__column] = \
                    self.__rubiks_cube_state[1][2][__column]
            self.__rubiks_cube_state[1][2][__column] = \
                    self.__rubiks_cube_state[0][1][__column]
            self.__rubiks_cube_state[0][1][__column] = \
                    __temp_cubie

            for __row in range(0, 3):
                for __layer in range(0, 3):
                    __cubie = self.__rubiks_cube_state[__layer][__row][__column]
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

            __temp_cubie = self.__rubiks_cube_state[0][__row][0]
            self.__rubiks_cube_state[0][__row][0] = \
                    self.__rubiks_cube_state[0][__row][2]
            self.__rubiks_cube_state[0][__row][2] = \
                    self.__rubiks_cube_state[2][__row][2]
            self.__rubiks_cube_state[2][__row][2] = \
                    self.__rubiks_cube_state[2][__row][0]
            self.__rubiks_cube_state[2][__row][0] = \
                    __temp_cubie

            __temp_cubie = self.__rubiks_cube_state[0][__row][1]
            self.__rubiks_cube_state[0][__row][1] = \
                    self.__rubiks_cube_state[1][__row][2]
            self.__rubiks_cube_state[1][__row][2] = \
                    self.__rubiks_cube_state[2][__row][1]
            self.__rubiks_cube_state[2][__row][1] = \
                    self.__rubiks_cube_state[1][__row][0]
            self.__rubiks_cube_state[1][__row][0] = \
                    __temp_cubie

            for __layer in range(0, 3):
                for __cubie in self.__rubiks_cube_state[__layer][__row]:
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

            __temp_cubie = self.__rubiks_cube_state[0][__row][0]
            self.__rubiks_cube_state[0][__row][0] = \
                    self.__rubiks_cube_state[2][__row][0]
            self.__rubiks_cube_state[2][__row][0] = \
                    self.__rubiks_cube_state[2][__row][2]
            self.__rubiks_cube_state[2][__row][2] = \
                    self.__rubiks_cube_state[0][__row][2]
            self.__rubiks_cube_state[0][__row][2] = \
                    __temp_cubie

            __temp_cubie = self.__rubiks_cube_state[0][__row][1]
            self.__rubiks_cube_state[0][__row][1] = \
                    self.__rubiks_cube_state[1][__row][0]
            self.__rubiks_cube_state[1][__row][0] = \
                    self.__rubiks_cube_state[2][__row][1]
            self.__rubiks_cube_state[2][__row][1] = \
                    self.__rubiks_cube_state[1][__row][2]
            self.__rubiks_cube_state[1][__row][2] = \
                    __temp_cubie

            for __layer in range(0, 3):
                for __cubie in self.__rubiks_cube_state[__layer][__row]:
                    for __color, __face in __cubie.iteritems():
                        if __face == FRONT:
                            __cubie[__color] = RIGHT
                        elif __face == RIGHT:
                            __cubie[__color] = BACK
                        elif __face == BACK:
                            __cubie[__color] = LEFT
                        elif __face == LEFT:
                            __cubie[__color] = FRONT

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

        __corner_position = 0

        R = self.twist_face(RIGHT, CW)
        R_ = self.twist_face(RIGHT, CCW)
        L = self.twist_face(LEFT, CW)
        L_ = self.twist_face(LEFT, CCW)
        F  = self.twist_face(FRONT, CW)
        F_ = self.twist_face(FRONT, CCW)
        B = self.twist_face(BACK, CW)
        B_ = self.twist_face(BACK, CCW)
        U = self.twist_face(UP, CW)
        U_ = self.twist_face(UP, CCW)
        D = self.twist_face(DOWN, CW)
        D_ = self.twist_face(DOWN, CCW)

        for __layer in range(0, 3, 2):
            for __row in range(0, 3, 2):
                for __column in range(0, 3, 2):
                    __cubie = self.__rubiks_cube_state[__layer][__row][__column]
                    if GREEN in __cubie and RED in __cubie and \
                              WHITE in __cubie:
                        __cubie_UFL = __corner_position
                    __corner_position += 1

        if __cubie_UFL == CORNER_POS_1:
            if __cubie_UFL[WHITE] == LEFT:
                self.twist_face(LEFT, CW)
                self.twist_face(DOWN, CW)
                self.twist_face(LEFT, CCW)
                self.twist_face(DOWN, CCW)
                self.twist_face(DOWN, CCW)
                self.twist_face(FRONT, CCW)
                self.twist_face(DOWN, CW)
                self.twist_face(FRONT, CW)
            elif __cubie_UFL[WHITE] == FRONT:
                self.twist_face(FRONT, CCW)
                self.twist_face(DOWN, CCW)
                self.twist_face(FRONT, CW)
                self.twist_face(DOWN, CW)
                self.twist_face(DOWN, CW)
                self.twist_face(LEFT, CW)
                self.twist_face(DOWN, CCW)
                self.twist_face(LEFT, CCW)
        elif __cubie_UFL == CORNER_POS_2:
            if __cubie_UFL[WHITE] == RIGHT:
                R_
                L
                D_
                R
                L_
            elif __cubie__UFL[WHITE] == FRONT:
                F
                D
                F_
                D
                F_
                D
                F
            elif __cubie_UFL[WHITE] == UP:
                R_
                D_
                D_
                R
                F_
                D
                F




#        # Using the a    __cubie_UFL = __corner_position         bove diagram indicating the indices corresponding to the
#        # corners of the cube, we search for the positions of the corner cubies
#        # that go on the top layer
#        for __layer in range(0, 3, 2):
#            for __row in range(0, 3, 2):
#                for __column in range(0, 3, 2):
#                    __cubie = self.__rubiks_cube_state[__layer][__row][__column]
#
#                    if GREEN in __cubie and RED in __cubie and \
#                            WHITE in __cubie:
#                        __cubie_UFL = __corner_position
#                    elif BLUE in __cubie and RED in __cubie and \
#                            WHITE in __cubie:
#                        __cubie_UFR = __corner_position
#                    elif GREEN in __cubie and ORANGE in __cubie and \
#                            WHITE in __cubie:
#                        __cubie_UBL = __corner_position
#                    elif BLUE in __cubie and ORANGE in __cubie and \
#                            WHITE in __cubie:
#                        __cubie_UBR = __corner_position
#
#                    __corner_position += 1
#
#        if __cubie_UFL ==  CORNER_POS_1:
#            if __cubie_UFL[WHITE] == FRONT:





