#!/usr/bin/python2.7
#
# Copyright (c) 2015, Gerson Ramos

# Import the necessary modules
import cv2
import numpy as np
import copy
import rubiks_cube_object

video_capture = cv2.VideoCapture(0)

def nameColor(index):
    if index == 0:
        return "Red"
    elif index == 1:
        return "Blue"
    elif index == 2:
        return "Green"
    elif index == 3:
        return "Orange"
    elif index == 4:
        return "White"
    elif index == 5:
        return "Yellow"

Prompt = ['Front Face', 'Bottom Face', 'Back Face',
          'Top Face', 'Right Face', 'Left Face']
Cube = []

FS = 0                      #File Select
capturing = 1               #Capturing flag

face = []                   #stores the unsorted face values
Face = []                   #stores the sorted face values
Colors = []                 #stores the sorted colors

row0 = []                   #used to store rows separately
row1 = []
row2 = []

# Color threshold values
ru = [64, 60, 255]
rl = [0, 0, 172]

bu = [255,106, 70]
bl = [90, 31, 0]

gu = [90, 210, 70]
gl = [31, 90, 4]

ou = [48, 255, 255]
ol = [0, 93, 246]

wu = [255, 255, 255]
wl = [200, 200, 200]

yu = [139, 255, 255]
yl = [65, 207, 195]

uppers = [ru, bu, gu, ou, wu, yu]
lowers = [rl, bl, gl, ol, wl, yl]

#main loop
while True:
    face = []
    Face = []
    Colors = []

    # Capture an image from the camera
    ret, image = video_capture.read()

    image_mod = cv2.rectangle(copy.deepcopy(image), (280,50), (360, 130),
            (255, 255, 255), 2)
    cv2.rectangle(image_mod, (280, 190), (360, 270), (255, 255, 255), 2)
    cv2.rectangle(image_mod, (280, 330), (360, 410), (255, 255, 255), 2)
    cv2.rectangle(image_mod, (420, 50), (500, 130), (255, 255, 255), 2)
    cv2.rectangle(image_mod, (420, 190), (500, 270), (255, 255, 255), 2)
    cv2.rectangle(image_mod, (420, 330), (500, 410), (255, 255, 255), 2)
    cv2.rectangle(image_mod, (140, 50), (220, 130), (255, 255, 255), 2)
    cv2.rectangle(image_mod, (140, 190), (220, 270), (255, 255, 255), 2)
    cv2.rectangle(image_mod, (140, 330), (220, 410), (255, 255, 255), 2)

    _, mask = cv2.threshold(copy.deepcopy(image), 255, 255, cv2.THRESH_BINARY)
    mask = cv2.rectangle(mask, (280,50), (360, 130), (255, 255, 255), -1)
    cv2.rectangle(mask, (280, 190), (360, 270), (255, 255, 255), -1)
    cv2.rectangle(mask, (280, 330), (360, 410), (255, 255, 255), -1)
    cv2.rectangle(mask, (420, 50), (500, 130), (255, 255, 255), -1)
    cv2.rectangle(mask, (420, 190), (500, 270), (255, 255, 255), -1)
    cv2.rectangle(mask, (420, 330), (500, 410), (255, 255, 255), -1)
    cv2.rectangle(mask, (140, 50), (220, 130), (255, 255, 255), -1)
    cv2.rectangle(mask, (140, 190), (220, 270), (255, 255, 255), -1)
    cv2.rectangle(mask, (140, 330), (220, 410), (255, 255, 255), -1)

    res = cv2.bitwise_and(image, mask)
    blur = cv2.blur(res, (1, 1))

    # Goes through all the colors that we are looking for
    for i in range(0, 6):
        upper = np.array(uppers[i],dtype="uint8")
        lower = np.array(lowers[i],dtype="uint8")

        # Creates an image based on the color thresholds
        thresh = cv2.inRange(blur, lower, upper)
        temp = thresh.copy()

        # Finds the contours of the objects of the specified color
        image, contours, hierarchy = \
                cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        max_area = 0
        best_cnt = 1

        # Looks for squares of the specified color that are of a relatively
        # specific size
        for cnt in contours:
            area = cv2.contourArea(cnt)
            x, y, w, h = cv2.boundingRect(cnt)
            if (abs(w - h) < 10) and (w + h > 120) and (w + h < 300):
                cv2.rectangle(image_mod, (x, y), (x + w, y + h), lowers[i], 10)
                cv2.putText(image_mod, nameColor(i), (x, y + h / 2),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, [0, 0, 0], thickness = 2)
                face.append([x, y, nameColor(i)])
            if area > max_area:
                max_area = area
                best_cnt = cnt

    # Sorts the squares found to form the face of the cube
    face.sort(key = lambda x: x[1])
    row0 = face[0:3]
    row0.sort()
    row1 = face[3:6]
    row1.sort()
    row2 = face[6:9]
    row2.sort()

    Face = [row0, row1, row2]

    for r in Face:
        for e in r:
            Colors.append(e[2])
    if capturing == 1:
        if len(Colors) == 9:
            cv2.putText(image_mod, 'READY', (250,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, [0, 255, 0], thickness = 2)
        cv2.putText(image_mod, Prompt[FS], (10,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, [0, 0, 0], thickness = 2)
    else:
        cv2.putText(image_mod, 'Press 'r' to reset', (10,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, [0, 0, 0], thickness = 2)

    cv2.imshow("Frame", image_mod)

    cnts = []

    # User input
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if key == ord("c"):
        if len(Colors) == 9:
            Cube.append(Colors)
            if FS < 5:
                FS = FS + 1
            else:
                for c in Cube:
                    print(c)
                capturing = 0
    if key == ord("r"):
        FS = 0
        capturing = 1

video_capture.release()
cv2.destroyAllWindows()

FRONT = 0
LEFT = 1
BACK = 2
RIGHT = 3
UP = 4
DOWN = 5

RED = 0
GREEN = 1
ORANGE = 2
BLUE = 3
WHITE = 4
YELLOW = 5

color = \
    {'Red':RED, 'Green':GREEN, 'Orange':ORANGE,
     'Blue':BLUE, 'White':WHITE, 'Yellow':YELLOW}

rubiks_cube_initial_state = \
[
    [
        [
            {color[Cube[5][2]]:LEFT, color[Cube[0][0]]:FRONT, color[Cube[3][6]]:UP},
            {color[Cube[0][1]]:FRONT, color[Cube[3][7]]:UP},
            {color[Cube[4][0]]:RIGHT, color[Cube[0][2]]:FRONT, color[Cube[3][8]]:UP}
        ],
        [
            {color[Cube[5][5]]:LEFT, color[Cube[0][3]]:FRONT},
            {color[Cube[0][4]]:FRONT},
            {color[Cube[4][3]]:RIGHT, color[Cube[0][5]]:FRONT}
        ],
        [
            {color[Cube[5][8]]:LEFT, color[Cube[0][6]]:FRONT, color[Cube[1][0]]:DOWN},
            {color[Cube[0][7]]:FRONT, color[Cube[1][1]]:DOWN},
            {color[Cube[4][6]]:RIGHT, color[Cube[0][8]]:FRONT, color[Cube[1][2]]:DOWN}
        ],
    ],
    [
        [
            {color[Cube[5][1]]:LEFT, color[Cube[3][3]]:UP},
            {color[Cube[3][4]]:UP},
            {color[Cube[4][1]]:RIGHT, color[Cube[3][5]]:UP}
        ],
        [
            {color[Cube[5][4]]:LEFT},
            {},
            {color[Cube[4][4]]:RIGHT}
        ],
        [
            {color[Cube[5][7]]:LEFT, color[Cube[1][3]]:DOWN},
            {color[Cube[1][4]]:DOWN},
            {color[Cube[4][7]]:RIGHT, color[Cube[1][5]]:DOWN}
        ]
    ],
    [
        [
            {color[Cube[5][0]]:LEFT, color[Cube[2][2]]:BACK, color[Cube[3][0]]:UP},
            {color[Cube[2][1]]:BACK, color[Cube[3][1]]:UP},
            {color[Cube[4][2]]:RIGHT, color[Cube[2][0]]:BACK, color[Cube[3][2]]:UP}
        ],
        [
            {color[Cube[5][3]]:LEFT, color[Cube[2][5]]:BACK},
            {color[Cube[2][4]]:BACK},
            {color[Cube[4][5]]:RIGHT, color[Cube[2][3]]:BACK}
        ],
        [
            {color[Cube[5][6]]:LEFT, color[Cube[2][8]]:BACK, color[Cube[1][6]]:DOWN},
            {color[Cube[2][7]]:BACK, color[Cube[1][7]]:DOWN},
            {color[Cube[4][8]]:RIGHT, color[Cube[2][6]]:BACK, color[Cube[1][8]]:DOWN}
        ]
    ]
]

rubiks_cube = rubiks_cube_object.rubiks_cube_object(rubiks_cube_initial_state)
rubiks_cube.display_visual()
rubiks_cube.solve_top_edges()
rubiks_cube.solve_top_corners()
rubiks_cube.solve_middle_layer()
rubiks_cube.solve_top_layer()
rubiks_cube.display_visual()
print "Total moves: ",
print rubiks_cube.get_total_moves()
