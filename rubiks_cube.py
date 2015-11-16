#!/usr/bin/python2.7

import sys
import numpy
import copy

FRONT_FACE = 0
DOWN_FACE = 1
BACK_FACE = 2
UP_FACE = 3
RIGHT_FACE = 4
LEFT_FACE = 5

R = 0
Y = 1
O = 2
W = 3
B = 4
G = 5

rubiks_cube_default_pattern = \
[
    numpy.array(
        [[R, R, R],
         [R, R, R],
         [R, R, R]]),
    numpy.array(
        [[Y, Y, Y],
         [Y, Y, Y],
         [Y, Y, Y]]),
    numpy.array(
        [[O, O, O],
         [O, O, O],
         [O, O, O]]),
    numpy.array(
        [[W, W, W],
         [W, W, W],
         [W, W, W]]),
    numpy.array(
        [[B, B, B],
         [B, B, B],
         [B, B, B]]),
    numpy.array(
        [[G, G, G],
         [G, G, G],
         [G, G, G]])
]

color_code = \
[
    '\033[91m' + u'\u25fc' + '\033[0m',
    '\033[93m' + u'\u25fc' + '\033[0m',
    '\033[95m' + u'\u25fc' + '\033[0m',
    '\033[97m' + u'\u25fc' + '\033[0m',
    '\033[94m' + u'\u25fc' + '\033[0m',
    '\033[92m' + u'\u25fc' + '\033[0m',
]

class rubiks_cube:
    # Constructor
    def __init__(self, rubiks_cube_pattern = rubiks_cube_default_pattern):
        self.__rubiks_cube_pattern = rubiks_cube_pattern

    # Verify whether the initial pattern of the Rubik's Cube is valid by
    # determining whether all the colors have the same count and are equal
    # to 9.
    #
    # TODO: Need to check if the positions of the colors are correct.
    def verify_init_state(self):
        __color_count = [0, 0, 0, 0, 0, 0]

        for __face in self.__rubiks_cube_pattern:
            for __row in __face:
                for __column in __row:
                    __color_count[__column] += 1
        if not (__color_count[R] == __color_count[Y] == __color_count[O] == \
                __color_count[W] == __color_count[B] == __color_count[G]):
            print "error"
            sys.exit(-1)
    
    # Display the current pattern of the Rubik's Cube
    def display(self):
        for __row in self.__rubiks_cube_pattern[UP_FACE]:
            print "          [",
            for __column in __row:
                print color_code[__column],
            print "]"
        print ""

        for __row in range(0, 3):
            print "[",
            for __column in self.__rubiks_cube_pattern[LEFT_FACE][__row]:
                print color_code[__column],
            print "] [",
            for __column in self.__rubiks_cube_pattern[FRONT_FACE][__row]:
                print color_code[__column],
            print "] [",
            for __column in self.__rubiks_cube_pattern[RIGHT_FACE][__row]:
                print color_code[__column],
            print "] [",
            for __column in self.__rubiks_cube_pattern[BACK_FACE][__row]:
                print color_code[__column],
            print "]"
        print""
        
        for __row in self.__rubiks_cube_pattern[DOWN_FACE]:
            print "          [",
            for __column in __row:
                print color_code[__column],
            print "]"
        print "\n"

    # Perform a clockwise twist operation on the specified face
    def twist_face_cw(self, face):
        self.__rubiks_cube_pattern[face] = \
                numpy.transpose(self.__rubiks_cube_pattern[face])
        self.__rubiks_cube_pattern[face] = \
                numpy.fliplr(self.__rubiks_cube_pattern[face])

        if face == FRONT_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE][2] = \
                    numpy.flipud(self.__rubiks_cube_pattern[LEFT_FACE])[:,2]
            self.__rubiks_cube_pattern[LEFT_FACE][:,2] = \
                    numpy.transpose(self.__rubiks_cube_pattern[DOWN_FACE])[:,0]
            self.__rubiks_cube_pattern[DOWN_FACE][0] = \
                    numpy.flipud(self.__rubiks_cube_pattern[RIGHT_FACE])[:,0]
            self.__rubiks_cube_pattern[RIGHT_FACE][:,0] = \
                    numpy.transpose(__temp_face)[:,2]
        elif face == DOWN_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[FRONT_FACE])
            self.__rubiks_cube_pattern[FRONT_FACE][2] = \
                    self.__rubiks_cube_pattern[LEFT_FACE][2]
            self.__rubiks_cube_pattern[LEFT_FACE][2] = \
                    self.__rubiks_cube_pattern[BACK_FACE][2]
            self.__rubiks_cube_pattern[BACK_FACE][2] = \
                    self.__rubiks_cube_pattern[RIGHT_FACE][2]
            self.__rubiks_cube_pattern[RIGHT_FACE][2] = \
                    __temp_face[2]
        elif face == BACK_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE][0] = \
                    self.__rubiks_cube_pattern[RIGHT_FACE][:,2]
            self.__rubiks_cube_pattern[RIGHT_FACE][:,2] = \
                    numpy.fliplr(self.__rubiks_cube_pattern[DOWN_FACE])[2]
            self.__rubiks_cube_pattern[DOWN_FACE][2] = \
                    self.__rubiks_cube_pattern[LEFT_FACE][:,0]
            self.__rubiks_cube_pattern[LEFT_FACE][:,0] = \
                    numpy.fliplr(__temp_face)[0]
        elif face == UP_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[FRONT_FACE])
            self.__rubiks_cube_pattern[FRONT_FACE][0] = \
                    self.__rubiks_cube_pattern[RIGHT_FACE][0]
            self.__rubiks_cube_pattern[RIGHT_FACE][0] = \
                    self.__rubiks_cube_pattern[BACK_FACE][0]
            self.__rubiks_cube_pattern[BACK_FACE][0] = \
                    self.__rubiks_cube_pattern[LEFT_FACE][0]
            self.__rubiks_cube_pattern[LEFT_FACE][0] = \
                    __temp_face[0]
        elif face == RIGHT_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE][:,2] = \
                    self.__rubiks_cube_pattern[FRONT_FACE][:,2]
            self.__rubiks_cube_pattern[FRONT_FACE][:,2] = \
                    self.__rubiks_cube_pattern[DOWN_FACE][:,2]
            self.__rubiks_cube_pattern[DOWN_FACE][:,2] = \
                    numpy.flipud(self.__rubiks_cube_pattern[BACK_FACE])[:,0]
            self.__rubiks_cube_pattern[BACK_FACE][:,0] = \
                    numpy.flipud(__temp_face)[:,2]
        elif face == LEFT_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE][:,0] = \
                    numpy.flipud(self.__rubiks_cube_pattern[BACK_FACE])[:,2]
            self.__rubiks_cube_pattern[BACK_FACE][:,2] = \
                    numpy.flipud(self.__rubiks_cube_pattern[DOWN_FACE])[:,0]
            self.__rubiks_cube_pattern[DOWN_FACE][:,0] = \
                    self.__rubiks_cube_pattern[FRONT_FACE][:,0]
            self.__rubiks_cube_pattern[FRONT_FACE][:,0] = \
                    __temp_face[:,0]

    # Perform a counter-clockwise operation on the specified face
    def twist_face_ccw(self, face):
        self.__rubiks_cube_pattern[face] = \
                numpy.fliplr(self.__rubiks_cube_pattern[face])
        self.__rubiks_cube_pattern[face]= \
                numpy.transpose(self.__rubiks_cube_pattern[face])

        if face == FRONT_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE][2] = \
                    self.__rubiks_cube_pattern[RIGHT_FACE][:,0]
            self.__rubiks_cube_pattern[RIGHT_FACE][:,0] = \
                    numpy.fliplr(self.__rubiks_cube_pattern[DOWN_FACE])[0]
            self.__rubiks_cube_pattern[DOWN_FACE][0] = \
                    self.__rubiks_cube_pattern[LEFT_FACE][:,2]
            self.__rubiks_cube_pattern[LEFT_FACE][:,2] = \
                    numpy.fliplr(__temp_face)[2]
        elif face == DOWN_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[FRONT_FACE])
            self.__rubiks_cube_pattern[FRONT_FACE][2] = \
                    self.__rubiks_cube_pattern[RIGHT_FACE][2]
            self.__rubiks_cube_pattern[RIGHT_FACE][2] = \
                    self.__rubiks_cube_pattern[BACK_FACE][2]
            self.__rubiks_cube_pattern[BACK_FACE][2] = \
                    self.__rubiks_cube_pattern[LEFT_FACE][2]
            self.__rubiks_cube_pattern[LEFT_FACE][2] = \
                    __temp_face[2]
        elif face == BACK_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE][0] = \
                    numpy.flipud(self.__rubiks_cube_pattern[LEFT_FACE])[:,0]
            self.__rubiks_cube_pattern[LEFT_FACE][:,0] = \
                    self.__rubiks_cube_pattern[DOWN_FACE][2]
            self.__rubiks_cube_pattern[DOWN_FACE][2] = \
                    numpy.flipud(self.__rubiks_cube_pattern[RIGHT_FACE])[:,2]
            self.__rubiks_cube_pattern[RIGHT_FACE][:,2] = \
                    __temp_face[0]
        elif face == UP_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[FRONT_FACE])
            self.__rubiks_cube_pattern[FRONT_FACE][0] = \
                    self.__rubiks_cube_pattern[LEFT_FACE][0]
            self.__rubiks_cube_pattern[LEFT_FACE][0] = \
                    self.__rubiks_cube_pattern[BACK_FACE][0]
            self.__rubiks_cube_pattern[BACK_FACE][0] = \
                    self.__rubiks_cube_pattern[RIGHT_FACE][0]
            self.__rubiks_cube_pattern[RIGHT_FACE][0] = \
                    __temp_face[0]
        elif face == RIGHT_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE][:,2] = \
                    numpy.flipud(self.__rubiks_cube_pattern[BACK_FACE])[:,0]
            self.__rubiks_cube_pattern[BACK_FACE][:,0] = \
                    numpy.flipud(self.__rubiks_cube_pattern[DOWN_FACE])[:,2]
            self.__rubiks_cube_pattern[DOWN_FACE][:,2] = \
                    self.__rubiks_cube_pattern[FRONT_FACE][:,2]
            self.__rubiks_cube_pattern[FRONT_FACE][:,2] = \
                    __temp_face[:,2]
        elif face == LEFT_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE][:,0] = \
                    self.__rubiks_cube_pattern[FRONT_FACE][:,0]
            self.__rubiks_cube_pattern[FRONT_FACE][:,0] = \
                    self.__rubiks_cube_pattern[DOWN_FACE][:,0]
            self.__rubiks_cube_pattern[DOWN_FACE][:,0] = \
                    numpy.flipud(self.__rubiks_cube_pattern[BACK_FACE])[:,2]
            self.__rubiks_cube_pattern[BACK_FACE][:,2] = \
                    numpy.flipud(__temp_face[:,0])

    # Rotate the cube on the axis of rotation perpendicular to the face
    # specified
    def rotate_face_cw(self, face):
        self.__rubiks_cube_pattern[face] = \
                numpy.transpose(self.__rubiks_cube_pattern[face])
        self.__rubiks_cube_pattern[face] = \
                numpy.fliplr(self.__rubiks_cube_pattern[face])

        if face == FRONT_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE] = \
                    numpy.fliplr(numpy.transpose
                            (self.__rubiks_cube_pattern[LEFT_FACE]))
            self.__rubiks_cube_pattern[LEFT_FACE] = \
                    numpy.fliplr(numpy.transpose
                            (self.__rubiks_cube_pattern[DOWN_FACE]))
            self.__rubiks_cube_pattern[DOWN_FACE] = \
                    numpy.fliplr(numpy.transpose
                            (self.__rubiks_cube_pattern[RIGHT_FACE]))
            self.__rubiks_cube_pattern[RIGHT_FACE] = \
                    numpy.fliplr(numpy.transpose(__temp_face))
            self.__rubiks_cube_pattern[BACK_FACE] = \
                    numpy.transpose(numpy.fliplr
                            (self.__rubiks_cube_pattern[BACK_FACE]))
        elif face == DOWN_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[FRONT_FACE])
            self.__rubiks_cube_pattern[FRONT_FACE] = \
                    self.__rubiks_cube_pattern[LEFT_FACE]
            self.__rubiks_cube_pattern[LEFT_FACE] = \
                    self.__rubiks_cube_pattern[BACK_FACE]
            self.__rubiks_cube_pattern[BACK_FACE] = \
                    self.__rubiks_cube_pattern[RIGHT_FACE]
            self.__rubiks_cube_pattern[RIGHT_FACE] = \
                    __temp_face
            self.__rubiks_cube_pattern[UP_FACE] = \
                    numpy.transpose(numpy.fliplr
                            (self.__rubiks_cube_pattern[UP_FACE]))
        elif face == BACK_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE] = \
                    numpy.transpose(numpy.fliplr
                            (self.__rubiks_cube_pattern[RIGHT_FACE]))
            self.__rubiks_cube_pattern[RIGHT_FACE] = \
                    numpy.transpose(numpy.fliplr
                            (self.__rubiks_cube_pattern[DOWN_FACE]))
            self.__rubiks_cube_pattern[DOWN_FACE] = \
                    numpy.transpose(numpy.fliplr
                            (self.__rubiks_cube_pattern[LEFT_FACE]))
            self.__rubiks_cube_pattern[LEFT_FACE] = \
                    numpy.transpose(numpy.fliplr
                            (__temp_face))
            self.__rubiks_cube_pattern[FRONT_FACE] = \
                    numpy.transpose(numpy.fliplr
                            (self.__rubiks_cube_pattern[FRONT_FACE]))
        elif face == UP_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[FRONT_FACE])
            self.__rubiks_cube_pattern[FRONT_FACE] = \
                    self.__rubiks_cube_pattern[RIGHT_FACE]
            self.__rubiks_cube_pattern[RIGHT_FACE] = \
                    self.__rubiks_cube_pattern[BACK_FACE]
            self.__rubiks_cube_pattern[BACK_FACE] = \
                    self.__rubiks_cube_pattern[LEFT_FACE]
            self.__rubiks_cube_pattern[LEFT_FACE] = \
                    __temp_face
            self.__rubiks_cube_pattern[DOWN_FACE] = \
                    numpy.transpose(numpy.fliplr
                            (self.__rubiks_cube_pattern[DOWN_FACE]))
        elif face == RIGHT_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE] = \
                    self.__rubiks_cube_pattern[FRONT_FACE]
            self.__rubiks_cube_pattern[FRONT_FACE] = \
                    self.__rubiks_cube_pattern[DOWN_FACE]
            self.__rubiks_cube_pattern[DOWN_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[BACK_FACE], 2)
            self.__rubiks_cube_pattern[BACK_FACE] = \
                    numpy.rot90(__temp_face, 2)
            self.__rubiks_cube_pattern[LEFT_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[LEFT_FACE])
        elif face == LEFT_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[BACK_FACE], 2)
            self.__rubiks_cube_pattern[BACK_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[DOWN_FACE], 2)
            self.__rubiks_cube_pattern[DOWN_FACE] = \
                    self.__rubiks_cube_pattern[FRONT_FACE]
            self.__rubiks_cube_pattern[FRONT_FACE] = \
                    __temp_face
            self.__rubiks_cube_pattern[RIGHT_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[RIGHT_FACE])

    def rotate_face_ccw(self, face):
        self.__rubiks_cube_pattern[face] = \
                numpy.rot90(self.__rubiks_cube_pattern[face])

        if face == FRONT_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[RIGHT_FACE])
            self.__rubiks_cube_pattern[RIGHT_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[DOWN_FACE])
            self.__rubiks_cube_pattern[DOWN_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[LEFT_FACE])
            self.__rubiks_cube_pattern[LEFT_FACE] = \
                    numpy.rot90(__temp_face)
            self.__rubiks_cube_pattern[BACK_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[BACK_FACE], 3)
        elif face == DOWN_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[FRONT_FACE])
            self.__rubiks_cube_pattern[FRONT_FACE] = \
                    self.__rubiks_cube_pattern[RIGHT_FACE]
            self.__rubiks_cube_pattern[RIGHT_FACE] = \
                    self.__rubiks_cube_pattern[BACK_FACE]
            self.__rubiks_cube_pattern[BACK_FACE] = \
                    self.__rubiks_cube_pattern[LEFT_FACE]
            self.__rubiks_cube_pattern[LEFT_FACE] = \
                    __temp_face
            self.__rubiks_cube_pattern[UP_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[UP_FACE], 3)
        elif face == BACK_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[LEFT_FACE], 3)
            self.__rubiks_cube_pattern[LEFT_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[DOWN_FACE], 3)
            self.__rubiks_cube_pattern[DOWN_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[RIGHT_FACE], 3)
            self.__rubiks_cube_pattern[RIGHT_FACE] = \
                    numpy.rot90(__temp_face, 3)
            self.__rubiks_cube_pattern[FRONT_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[FRONT_FACE], 3)
        elif face == UP_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[FRONT_FACE])
            self.__rubiks_cube_pattern[FRONT_FACE] = \
                    self.__rubiks_cube_pattern[LEFT_FACE]
            self.__rubiks_cube_pattern[LEFT_FACE] = \
                    self.__rubiks_cube_pattern[BACK_FACE]
            self.__rubiks_cube_pattern[BACK_FACE] = \
                    self.__rubiks_cube_pattern[RIGHT_FACE]
            self.__rubiks_cube_pattern[RIGHT_FACE] = \
                    __temp_face
            self.__rubiks_cube_pattern[DOWN_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[DOWN_FACE], 3)
        elif face == RIGHT_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[BACK_FACE], 2)
            self.__rubiks_cube_pattern[BACK_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[DOWN_FACE], 2)
            self.__rubiks_cube_pattern[DOWN_FACE] = \
                    self.__rubiks_cube_pattern[FRONT_FACE]
            self.__rubiks_cube_pattern[FRONT_FACE] = \
                    __temp_face
            self.__rubiks_cube_pattern[LEFT_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[LEFT_FACE], 3)
        elif face == LEFT_FACE:
            __temp_face = copy.deepcopy(self.__rubiks_cube_pattern[UP_FACE])
            self.__rubiks_cube_pattern[UP_FACE] = \
                    self.__rubiks_cube_pattern[FRONT_FACE]
            self.__rubiks_cube_pattern[FRONT_FACE] = \
                    self.__rubiks_cube_pattern[DOWN_FACE]
            self.__rubiks_cube_pattern[DOWN_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[BACK_FACE], 2)
            self.__rubiks_cube_pattern[BACK_FACE] = \
                    numpy.rot90(__temp_face, 2)
            self.__rubiks_cube_pattern[RIGHT_FACE] = \
                    numpy.rot90(self.__rubiks_cube_pattern[RIGHT_FACE], 3)

    # Return current pattern of Rubik's Cube
    def get_current_pattern(self):
        return self.__rubiks_cube_pattern

    def get_center_color_face_pos(self, color):
        __index = 0
        for __face in self.__rubiks_cube_pattern:
            if __face[1][1] == color:
                return __index
            __index += 1

    def print_center_color_face_pos(self, color):
        __face_pos = 0
        for __face in self.__rubiks_cube_pattern:
            if __face[1][1] == color:
                if __face_pos == FRONT_FACE:
                    print "front face"
                elif __face_pos == DOWN_FACE:
                    print "down face"
                elif __face_pos == BACK_FACE:
                    print "back face"
                elif __face_pos == UP_FACE:
                    print "up face"
                elif __face_pos == RIGHT_FACE:
                    print "right face"
                elif __face_pos == LEFT_FACE:
                    print "left face"
            __face_pos += 1

    def place_center_color_to_up(self, color):
        __face_pos = self.get_center_color_face_pos(color)

        if __face_pos == FRONT_FACE:
            self.rotate_face_cw(RIGHT_FACE)
        elif __face_pos == DOWN_FACE:
            self.rotate_face_cw(FRONT_FACE)
            self.rotate_face_cw(FRONT_FACE)
        elif __face_pos == BACK_FACE:
            self.rotate_face_cw(LEFT_FACE)
        elif __face_pos == UP_FACE:
            pass
        elif __face_pos == RIGHT_FACE:
            self.rotate_face_cw(BACK_FACE)
        elif __face_pos == LEFT_FACE:
            self.rotate_face_cw(FRONT_FACE)

    def init_starting_pos(self):
        self.place_center_color_to_up(W)
        __face_pos = self.get_center_color_face_pos(R)
        if __face_pos == LEFT_FACE:
            self.rotate_face_ccw(UP_FACE)
        elif __face_pos == BACK_FACE:
            self.rotate_face_cw(UP_FACE)
            self.rotate_face_cw(UP_FACE)
        elif __face_pos == RIGHT_FACE:
            self.rotate_face_cw(UP_FACE)
