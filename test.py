import cv2  # Not actually necessary if you just want to create an image.
import numpy as np

blank_image = np.zeros((250, 400, 3), np.uint8)


# hexa = np.array([[200, 109], [234, 129], [234, 170], [200, 190], [165, 170], [165, 129]], np.int32)
# boomerang = np.array([[36, 65], [115, 40], [80, 70], [105, 150]], np.int32)
# # pts = pts.reshape((-1, 1, 2))
# cv2.circle(blank_image, [300, 65], 40, (0, 0, 255), -1)
# cv2.fillPoly(blank_image, [hexa], (0, 0, 255))
# cv2.fillPoly(blank_image, [boomerang], (0, 0, 255))

def boomerang(x, y):
    line_1 = (0.316 * x + 173.608 - y) >= 0
    line_2 = (0.857 * x + 111.429 - y) <= 0
    line_mid = (-0.114 * x + 189.091 - y) <= 0
    line_3 = (-3.2 * x + 436 - y) > 0
    line_4 = (-1.232 * x + 229.348 - y) < 0

    if (line_1 and line_2 and line_mid) or (line_3 and line_4 and not line_mid):
        return True
    else:
        return False


def hexagon(x, y):
    line_1 = (-0.564 * x + 167.821 - y) <= 0
    line_2 = (161 - x) <= 0
    line_3 = (0.590 * x + 27.051 - y) >= 0
    line_4 = (-0.564 * x + 257.821 - y) >= 0
    line_5 = (239 - x) >= 0
    line_6 = (0.590 * x - 62.949 - y) <= 0
    if line_1 and line_2 and line_3 and line_4 and line_5 and line_6:
        return True
    else:
        return False


def circle(x ,y):
    circ_eq = ((x - 300)**2 + (y - 185)**2 - 40*40) <= 0
    if circ_eq:
        return True
    else:
        return False


for x_itr in range(0, blank_image.shape[1]):
    for y_itr in range(0, blank_image.shape[0]):
        if boomerang(x_itr, 249 - y_itr) or hexagon(x_itr, 249 - y_itr) or circle(x_itr, 249 - y_itr):
            blank_image[y_itr][x_itr] = [0, 0, 255]

cv2.imshow('img', blank_image)
# cv2.imwrite('final_map.jpg', blank_image)
cv2.waitKey()