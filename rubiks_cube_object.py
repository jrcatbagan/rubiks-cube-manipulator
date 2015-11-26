#!/usr/bin/python2.7

import numpy as np
import copy

# Color defines
W = 0
G = 1
R = 2
B = 3
O = 4
Y = 5

# Face defines
UP =    0
LEFT =  1
FRONT = 2
RIGHT = 3
BACK =  4
DOWN =  5

# Rotation defines
CW =    12
CCW =   13

# ANSI color code for Rubik's Cube facets
color_code = \
[
    '\033[97m' + u'\u25fc' + '\033[0m',
    '\033[92m' + u'\u25fc' + '\033[0m',
    '\033[91m' + u'\u25fc' + '\033[0m',
    '\033[94m' + u'\u25fc' + '\033[0m',
    '\033[95m' + u'\u25fc' + '\033[0m',
    '\033[93m' + u'\u25fc' + '\033[0m'
]

rubiks_cube_default_state = \
[
    np.array([[W, W, W], [W, W, W], [W, W, W]]),
    np.array([[G, G, G], [G, G, G], [G, G, G]]),
    np.array([[R, R, R], [R, R, R], [R, R, R]]),
    np.array([[B, B, B], [B, B, B], [B, B, B]]),
    np.array([[O, O, O], [O, O, O], [O, O, O]]),
    np.array([[Y, Y, Y], [Y, Y, Y], [Y, Y, Y]])
]

class rubiks_cube_object:
#------------------------------------------------------------------------------

    # Constructor
    def __init__(self, rubiks_cube_initial_state = rubiks_cube_default_state):
        self.__rubiks_cube = rubiks_cube_default_state
        self.__total_moves = 0

#------------------------------------------------------------------------------

    def display(self):
        print ""

        for __row in self.__rubiks_cube[UP]:
            print "       ",
            for __column in __row:
                print color_code[__column],
            print ""

        for __row in range(0, 3):
            print " ",
            for __column in self.__rubiks_cube[LEFT][__row]:
                print color_code[__column],
            for __column in self.__rubiks_cube[FRONT][__row]:
                print color_code[__column],
            for __column in self.__rubiks_cube[RIGHT][__row]:
                print color_code[__column],
            for __column in self.__rubiks_cube[BACK][__row]:
                print color_code[__column],
            print ""

        for __row in self.__rubiks_cube[DOWN]:
            print "       ",
            for __column in __row:
                print color_code[__column],
            print ""

        print ""


#------------------------------------------------------------------------------

    def get_total_moves(self):
        return self.__total_moves

#------------------------------------------------------------------------------

    def __increment_total_moves(self, value):
        self.__total_moves += value

#------------------------------------------------------------------------------

    def __twist_up_cw(self):
        __temp_face = copy.deepcopy(self.__rubiks_cube[UP])

        # Update facets on face
        for i in range(0, 3):
            for j in range(0, 3):
                self.__rubiks_cube[UP][i][j] = __temp_face[2 - j][i]

        # Update adjacent facets of face
        __temp_row = copy.deepcopy(self.__rubiks_cube[FRONT][0])
        self.__rubiks_cube[FRONT][0] = self.__rubiks_cube[RIGHT][0]
        self.__rubiks_cube[RIGHT][0] = self.__rubiks_cube[BACK][0]
        self.__rubiks_cube[BACK][0] = self.__rubiks_cube[LEFT][0]
        self.__rubiks_cube[LEFT][0] = __temp_row

#------------------------------------------------------------------------------

    def __twist_up_ccw(self):
        __temp_face = copy.deepcopy(self.__rubiks_cube[UP])

        # Update facets on face
        for i in range(0, 3):
            for j in range(0, 3):
                self.__rubiks_cube[UP][i][j] = __temp_face[j][2 - i]

        # Update adjacent facets of face
        __temp_row = copy.deepcopy(self.__rubiks_cube[FRONT][0])
        self.__rubiks_cube[FRONT][0] = self.__rubiks_cube[LEFT][0]
        self.__rubiks_cube[LEFT][0] = self.__rubiks_cube[BACK][0]
        self.__rubiks_cube[BACK][0] = self.__rubiks_cube[RIGHT][0]
        self.__rubiks_cube[RIGHT][0] = __temp_row

#------------------------------------------------------------------------------

    def __twist_down_cw(self):
        __temp_face = copy.deepcopy(self.__rubiks_cube[DOWN])

        # Update facets on face
        for i in range(0, 3):
            for j in range(0, 3):
                self.__rubiks_cube[DOWN][i][j] = __temp_face[2 - j][i]

        # Update adjacent facets of face
        __temp_row = copy.deepcopy(self.__rubiks_cube[FRONT][2])
        self.__rubiks_cube[FRONT][2] = self.__rubiks_cube[LEFT][2]
        self.__rubiks_cube[LEFT][2] = self.__rubiks_cube[BACK][2]
        self.__rubiks_cube[BACK][2] = self.__rubiks_cube[RIGHT][2]
        self.__rubiks_cube[RIGHT][2] = __temp_row

#------------------------------------------------------------------------------

    def __twist_down_ccw(self):
        __temp_face = copy.deepcopy(self.__rubiks_cube[DOWN])

        # Update facets on face
        for i in range(0, 3):
            for j in range(0, 3):
                self.__rubiks_cube[DOWN][i][j] = __temp_face[j][2 - i]

        # Update adjacent facets of face
        __temp_row = copy.deepcopy(self.__rubiks_cube[FRONT][2])
        self.__rubiks_cube[FRONT][2] = self.__rubiks_cube[RIGHT][2]
        self.__rubiks_cube[RIGHT][2] = self.__rubiks_cube[BACK][2]
        self.__rubiks_cube[BACK][2] = self.__rubiks_cube[LEFT][2]
        self.__rubiks_cube[LEFT][2] = __temp_row

#------------------------------------------------------------------------------

    def __twist_front_cw(self):
        __temp_face = copy.deepcopy(self.__rubiks_cube[FRONT])

        # Update facets on face
        for i in range(0, 3):
            for j in range(0, 3):
                self.__rubiks_cube[FRONT][i][j] = __temp_face[2 - j][i]

        # Update adjacent facets of face
        __temp_row = copy.deepcopy(self.__rubiks_cube[UP][2,:])
        self.__rubiks_cube[UP][2,:] = self.__rubiks_cube[LEFT][:,2][::-1]
        self.__rubiks_cube[LEFT][:,2] = self.__rubiks_cube[DOWN][0]
        self.__rubiks_cube[DOWN][0] = self.__rubiks_cube[RIGHT][:,0][::-1]
        self.__rubiks_cube[RIGHT][:,0] = __temp_row

#------------------------------------------------------------------------------

    def __twist_front_ccw(self):
        __temp_face = copy.deepcopy(self.__rubiks_cube[FRONT])

        # Update facets on face
        for i in range(0, 3):
            for j in range(0, 3):
                self.__rubiks_cube[FRONT][i][j] = __temp_face[j][2 - i]

        # Update adjacent facets of face
        __temp_row = copy.deepcopy(self.__rubiks_cube[UP][2,:][::-1])
        self.__rubiks_cube[UP][2] = self.__rubiks_cube[RIGHT][:,0]
        self.__rubiks_cube[RIGHT][:,0] = self.__rubiks_cube[DOWN][0,:][::-1]
        self.__rubiks_cube[DOWN][0,:] = self.__rubiks_cube[LEFT][:,2]
        self.__rubiks_cube[LEFT][:,2] = __temp_row

#------------------------------------------------------------------------------

    def __twist_back_cw(self):
        __temp_face = copy.deepcopy(self.__rubiks_cube[BACK])

        # Update facets on face
        for i in range(0, 3):
            for j in range(0, 3):
                self.__rubiks_cube[BACK][i][j] = __temp_face[2 - j][i]

        # Update adjacent facets of face
        __temp_row = copy.deepcopy(self.__rubiks_cube[UP][0,:][::-1])
        self.__rubiks_cube[UP][0,:] = self.__rubiks_cube[RIGHT][:,2]
        self.__rubiks_cube[RIGHT][:,2] = self.__rubiks_cube[DOWN][2,:][::-1]
        self.__rubiks_cube[DOWN][2,:] = self.__rubiks_cube[LEFT][:,0]
        self.__rubiks_cube[LEFT][:,0] = __temp_row

#------------------------------------------------------------------------------

    def __twist_back_ccw(self):
        __temp_face = copy.deepcopy(self.__rubiks_cube[BACK])

        # Update facets on face
        for i in range(0, 3):
            for j in range(0, 3):
                self.__rubiks_cube[BACK][i][j] = __temp_face[j][2 - i]

        # Update adjacent facets of face
        __temp_row = copy.deepcopy(self.__rubiks_cube[UP][0,:])
        self.__rubiks_cube[UP][0,:] = self.__rubiks_cube[LEFT][:,0][::-1]
        self.__rubiks_cube[LEFT][:,0] = self.__rubiks_cube[DOWN][2,:]
        self.__rubiks_cube[DOWN][2,:] = self.__rubiks_cube[RIGHT][:,2][::-1]
        self.__rubiks_cube[RIGHT][:,2] = __temp_row

#------------------------------------------------------------------------------

    def __twist_right_cw(self):
        __temp_face = copy.deepcopy(self.__rubiks_cube[RIGHT])

        # Update facets on face
        for i in range(0, 3):
            for j in range(0, 3):
                self.__rubiks_cube[RIGHT][i][j] = __temp_face[2 - j][i]

        # Update adjacent facets of face
        __temp_row = copy.deepcopy(self.__rubiks_cube[UP][:,2][::-1])
        self.__rubiks_cube[UP][:,2] = self.__rubiks_cube[FRONT][:,2]
        self.__rubiks_cube[FRONT][:,2] = self.__rubiks_cube[DOWN][:,2]
        self.__rubiks_cube[DOWN][:,2] = self.__rubiks_cube[BACK][:,0][::-1]
        self.__rubiks_cube[BACK][:,0] = __temp_row

#------------------------------------------------------------------------------

    def __twist_right_ccw(self):
        __temp_face = copy.deepcopy(self.__rubiks_cube[RIGHT])

        # Update facets on face
        for i in range(0, 3):
            for j in range(0, 3):
                self.__rubiks_cube[RIGHT][i][j] = __temp_face[j][2 - i]

        # Update adjacent facets of face
        __temp_row = copy.deepcopy(self.__rubiks_cube[UP][:,2])
        self.__rubiks_cube[UP][:,2] = self.__rubiks_cube[BACK][:,0][::-1]
        self.__rubiks_cube[BACK][:,0] = self.__rubiks_cube[DOWN][:,2][::-1]
        self.__rubiks_cube[DOWN][:,2] = self.__rubiks_cube[FRONT][:,2]
        self.__rubiks_cube[FRONT][:,2] = __temp_row

#------------------------------------------------------------------------------

    def __twist_left_cw(self):
        __temp_face = copy.deepcopy(self.__rubiks_cube[LEFT])

        # Update facets on face
        for i in range(0, 3):
            for j in range(0, 3):
                self.__rubiks_cube[LEFT][i][j] = __temp_face[2 - j][i]

        # Update adjacent facets of face
        __temp_row = copy.deepcopy(self.__rubiks_cube[UP][:,0])
        self.__rubiks_cube[UP][:,0] = self.__rubiks_cube[BACK][:,2][::-1]
        self.__rubiks_cube[BACK][:,2] = self.__rubiks_cube[DOWN][:,0][::-1]
        self.__rubiks_cube[DOWN][:,0] = self.__rubiks_cube[FRONT][:,0]
        self.__rubiks_cube[FRONT][:,0] = __temp_row

#------------------------------------------------------------------------------

    def __twist_left_ccw(self):
        __temp_face = copy.deepcopy(self.__rubiks_cube[LEFT])

        # Update facets on face
        for i in range(0, 3):
            for j in range(0, 3):
                self.__rubiks_cube[LEFT][i][j] = __temp_face[j][2 - i]

        # Update adjacent facets of face
        __temp_row = copy.deepcopy(self.__rubiks_cube[UP][:,0][::-1])
        self.__rubiks_cube[UP][:,0] = self.__rubiks_cube[FRONT][:,0]
        self.__rubiks_cube[FRONT][:,0] = self.__rubiks_cube[DOWN][:,0]
        self.__rubiks_cube[DOWN][:,0] = self.__rubiks_cube[BACK][:,2][::-1]
        self.__rubiks_cube[BACK][:,2] = __temp_row

#------------------------------------------------------------------------------

    def __twist_mud_cw(self):
        __temp_row = copy.deepcopy(self.__rubiks_cube[FRONT][1,:])
        self.__rubiks_cube[FRONT][1,:] = self.__rubiks_cube[RIGHT][1,:]
        self.__rubiks_cube[RIGHT][1,:] = self.__rubiks_cube[BACK][1,:]
        self.__rubiks_cube[BACK][1,:] = self.__rubiks_cube[LEFT][1,:]
        self.__rubiks_cube[LEFT][1,:] = __temp_row

#------------------------------------------------------------------------------

    def __twist_mud_ccw(self):
        __temp_row = copy.deepcopy(self.__rubiks_cube[FRONT][1,:])
        self.__rubiks_cube[FRONT][1,:] = self.__rubiks_cube[LEFT][1,:]
        self.__rubiks_cube[LEFT][1,:] = self.__rubiks_cube[BACK][1,:]
        self.__rubiks_cube[BACK][1,:] = self.__rubiks_cube[RIGHT][1,:]
        self.__rubiks_cube[RIGHT][1,:] = __temp_row

#------------------------------------------------------------------------------

    def __twist_mfb_cw(self):
        __temp_row = copy.deepcopy(self.__rubiks_cube[UP][1,:])
        self.__rubiks_cube[UP][1,:] = self.__rubiks_cube[LEFT][:,1][::-1]
        self.__rubiks_cube[LEFT][:,1] = self.__rubiks_cube[DOWN][1,:]
        self.__rubiks_cube[DOWN][1,:] = self.__rubiks_cube[RIGHT][:,1][::-1]
        self.__rubiks_cube[RIGHT][:,1] = __temp_row

#------------------------------------------------------------------------------

    def __twist_mfb_ccw(self):
        __temp_row = copy.deepcopy(self.__rubiks_cube[UP][1,:][::-1])
        self.__rubiks_cube[UP][1,:] = self.__rubiks_cube[RIGHT][:,1]
        self.__rubiks_cube[RIGHT][:,1] = self.__rubiks_cube[DOWN][1,:][::-1]
        self.__rubiks_cube[DOWN][1,:] = self.__rubiks_cube[LEFT][:,1]
        self.__rubiks_cube[LEFT][:,1] = __temp_row

#------------------------------------------------------------------------------

    def __twist_mrl_cw(self):
        __temp_row = copy.deepcopy(self.__rubiks_cube[UP][:,1][::-1])
        self.__rubiks_cube[UP][:,1] = self.__rubiks_cube[FRONT][:,1]
        self.__rubiks_cube[FRONT][:,1] = self.__rubiks_cube[DOWN][:,1]
        self.__rubiks_cube[DOWN][:,1] = self.__rubiks_cube[BACK][:,1][::-1]
        self.__rubiks_cube[BACK][:,1] = __temp_row

#------------------------------------------------------------------------------

    def __twist_mrl_ccw(self):
        __temp_row = copy.deepcopy(self.__rubiks_cube[UP][:,1])
        self.__rubiks_cube[UP][:,1] = self.__rubiks_cube[BACK][:,1][::-1]
        self.__rubiks_cube[BACK][:,1] = self.__rubiks_cube[DOWN][:,1][::-1]
        self.__rubiks_cube[DOWN][:,1] = self.__rubiks_cube[FRONT][:,1]
        self.__rubiks_cube[FRONT][:,1] = __temp_row

#------------------------------------------------------------------------------

    def __rotate_x_cw(self):
        self.__twist_front_cw()
        self.__twist_mfb_cw()
        self.__twist_back_ccw()

#------------------------------------------------------------------------------

    def __rotate_x_ccw(self):
        self.__twist_front_ccw()
        self.__twist_mfb_ccw()
        self.__twist_back_cw()

#------------------------------------------------------------------------------

    def __rotate_y_cw(self):
        self.__twist_right_cw()
        self.__twist_mrl_cw()
        self.__twist_left_ccw()

#------------------------------------------------------------------------------

    def __rotate_y_ccw(self):
        self.__twist_right_ccw()
        self.__twist_mrl_ccw()
        self.__twist_left_cw()

#------------------------------------------------------------------------------

    def __rotate_z_cw(self):
        self.__twist_up_cw()
        self.__twist_mud_cw()
        self.__twist_down_ccw()

#------------------------------------------------------------------------------

    def __rotate_z_ccw(self):
        self.__twist_up_ccw()
        self.__twist_mud_ccw()
        self.__twist_down_cw()

#------------------------------------------------------------------------------

    def maneuver(self, move_sequence):
        MOVE_UNDEFINED = 0
        MOVE_INVALID = 1
        MOVE_VALID = 2

        __move_validity = MOVE_UNDEFINED

        __move_operation = ""
        for i in range(0, len(move_sequence)):
            if move_sequence[i] != ' ':
                __move_operation += move_sequence[i]

            if move_sequence[i] == ' ' or i == len(move_sequence) - 1:
                __move_validity = MOVE_VALID

                if __move_operation == "U":
                    self.__twist_up_cw()
                elif __move_operation == "U'":
                    self.__twist_up_ccw()
                elif __move_operation == "D":
                    self.__twist_down_cw()
                elif __move_operation == "D'":
                    self.__twist_down_ccw()
                elif __move_operation == "F":
                    self.__twist_front_cw()
                elif __move_operation == "F'":
                    self.__twist_front_ccw()
                elif __move_operation == "B":
                    self.__twist_back_cw()
                elif __move_operation == "B'":
                    self.__twist_back_ccw()
                elif __move_operation == "R":
                    self.__twist_right_cw()
                elif __move_operation == "R'":
                    self.__twist_right_ccw()
                elif __move_operation == "L":
                    self.__twist_left_cw()
                elif __move_operation == "L'":
                    self.__twist_left_ccw()
                elif __move_operation == "E":
                    self.__twist_mud_cw()
                elif __move_operation == "E'":
                    self.__twist_mud_ccw()
                elif __move_operation == "S":
                    self.__twist_mfb_cw()
                elif __move_operation == "S'":
                    self.__twist_mfb_ccw()
                elif __move_operation == "M":
                    self.__twist_mrl_cw()
                elif __move_operation == "M'":
                    self.__twist_mrl_ccw()
                elif __move_operation == "X":
                    self.__rotate_x_cw()
                elif __move_operation == "X'":
                    self.__rotate_x_ccw()
                elif __move_operation == "Y":
                    self.__rotate_y_cw()
                elif __move_operation == "Y'":
                    self.__rotate_y_ccw()
                elif __move_operation == "Z":
                    self.__rotate_z_cw()
                elif __move_operation == "Z'":
                    self.__rotate_z_ccw()
                else:
                    print "error: invalid move operation"
                    __move_validity = MOVE_INVALID

                if __move_validity == MOVE_VALID:
                    self.__increment_total_moves(1)
                else:
                    pass

                __move_operation == ""

#------------------------------------------------------------------------------
