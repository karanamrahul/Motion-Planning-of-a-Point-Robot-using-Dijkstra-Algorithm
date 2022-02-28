import numpy as np
import cv2
import matplotlib.pyplot as plt


# Creating the Map using opencv

# Creating a Black image of size (450 , 250 )
map = np.zeros((250,400,3), np.uint8)


# Drawing a Circle in the map with a radius of 65
cv2.circle(map,(300,65), 40, (0,255,255), -1)


# Drawing a Hexagon (200 , 100)
pts = np.array([[200, 109], [234, 129], [234, 170], [200, 190], [165, 170], [165, 129]], np.int32)
cv2.fillPoly(map,[pts],(0,255,255))


# Drawing a polygon
pts = np.array([[36, 65], [115, 40], [80, 70], [105, 150]], np.int32)
cv2.fillPoly(map,[pts],(0,255,255))



def is_polygon(x, y):
    line_1 = (0.316 * x + 173.608 - y) >= 0
    line_2 = (0.857 * x + 111.429 - y) <= 0
    line_mid = (-0.114 * x + 189.091 - y) <= 0
    line_3 = (-3.2 * x + 436 - y) > 0
    line_4 = (-1.232 * x + 229.348 - y) < 0

    if (line_1 and line_2 and line_mid) or (line_3 and line_4 and not line_mid):
        return True
    else:
        return False


def is_hexagon(x, y):
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


def is_circle(x ,y):
    circ_eq = ((x - 300)**2 + (y - 185)**2 - 40*40) <= 0
    if circ_eq:
        return True
    else:
        return False


def is_obstacle(x,y):
    if  is_circle(x,249 - y) or is_hexagon(x,249-y) or is_polygon(x,249-y):
        return True
    else: return False

#To check the origin
cv2.circle(map, [0, 0], 10, (0, 0, 255), -1)

# for i in range(0,10):
#         x=200
#         y=80
#         if not is_obstacle(x,y):
#             map[y-i][x-i] = [255,0,255]
         
        
# Flipping the y-axis
#map = map[::-1,:,:]








cv2.imshow('map',map)
cv2.waitKey(0)
cv2.destroyAllWindows()