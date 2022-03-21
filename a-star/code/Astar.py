
import numpy as np
import cv2
import matplotlib.pyplot as plt
from Priority_queue import PriorityQueue
from scipy.spatial import distance


"""_summary_

This project mainly implements the path planning of a point robot using
A-star Algorithm given obstacle space

The map can be found in the /docs/map.png

Steps to Run the code 
-> Make sure you have Priority_queue.py file and dijsktra.py in your repository
```
$ git clone https://github.com/karanamrahul/Motion-Planning-of-a-Point-Robot-using-Dijkstra-Algorithm.git
$ cd A-star
$ python3 Astar.py
```
--> This will open up the map.
--> Please select two points from the map
--> Starting position and the goal position
--> If you have selected a position which is inside the obstacle space, 
--> then it will raise an error
--> Please select a different position

--> After the selection, the map will pop up showing the 
    exploration path, when the robot reaches the goal point
    , it will show you the best path.


--> The video can be found in the /results directory.
    
       
"""

# Creating the Map using opencv
def gen_map():
    """_summary_ Generating the Map considering the obstacle space

    Returns:
        _type_: _map with obstacles_
    """
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
    

    return map

output= cv2.VideoWriter('result.mp4', cv2.VideoWriter_fourcc(*'mp4v'),10, (400, 250))

# We can also use the below function to generate our map
def generate_map():
    """Generating Map using the obstacle space

    Returns:
        [np.narray]: [It is the updated map with obstacle space]
    """
    map = np.zeros((250, 400, 3), np.uint8)


    for x in range(0, map.shape[1]):
     for y in range(0, map.shape[0]):
        if is_polygon(x,  y) or is_hexagon(x,  y) or is_circle(x, y):
            map[y][x] = [0, 130, 190]

    return map

def is_polygon(x, y):
    l1 = (0.316 * x + 173.608 - y) >= 0
    l2 = (0.857 * x + 111.429 - y) <= 0
    lm = (-0.114 * x + 189.091 - y) <= 0
    l3 = (-3.2 * x + 436 - y) >= 0
    l4 = (-1.232 * x + 229.348 - y) <= 0

    if (l1 and l2 and lm) or (l3 and l4 and not lm):
         return True
    else:
        return False



def is_hexagon(x, y):
    l1 = (-0.571 * x + 174.286 - y) <= 0
    l2 = (165 - x) <= 0
    l3 = (0.571 * x + 25.714 - y) >= 0
    l4 = (-0.571 * x + 254.286 - y) >= 0
    l5 = (235 - x) >= 0
    l6 = (0.571 * x - 54.286 - y) <= 0

    if l1 and l2 and l3 and l4 and l5 and l6:
        return True
    else:
        return False




def is_circle(x ,y):
    circ_eq = ((x - 300)**2 + (y - 185)**2 - 40*40) <= 0
    if circ_eq:
        return True
    else:
        return False

def polygon_space(x, y):
    l1 = (0.316 * x + 178.608 - y) >= 0
    l2 = (0.857 * x + 106.429 - 10 - y) <= 0
    lmid = (-0.114 * x + 189.091 - y) <= 0
    l3 = (-3.2 * x + 450 - y) >= 0
    l4 = (-1.232 * x + 220.348 - y) <= 0

    return ((l1 and l2 and lmid) or (l3 and l4 and not lmid)) 


def hexagon_space(x, y):
    l1 = (-0.575 * x + 169+10 - y) <= 0
    l2 = (160-10 - x) <= 0
    l3 = (0.575 * x + 31+10 - y) >= 0
    l4 = (-0.575 * x + 261+10 - y) >= 0
    l5 = (240+10 - x) >= 0
    l6 = (0.575 * x - 61-10 - y) <= 0

    return l1 and l2 and l3 and l4 and l5 and l6

def circle_space(x, y):
    circ = ((x - 300) ** 2 + (y - 185) ** 2 - 55 * 55) <= 0
    
    return circ

def is_obstacle(y,x):
    if  is_circle(x, y) or is_hexagon(x,y) or is_polygon(x,y):
        return True
    else: return False


def check_obs_space(y_pos, x_pos):
    return polygon_space(x_pos, y_pos) or hexagon_space(x_pos, y_pos) or circle_space(x_pos, y_pos) \
        or (maze.shape[1] - 15 <= x_pos) or x_pos <= 14 or (maze.shape[0] - 15 <= y_pos) or y_pos <= 14





# This finds the cost between the nodes
def cost(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


# This represent all the actions needed in a 8-action space
actions = {
    "-pi/3": (np.cos(np.deg2rad(-60)),np.sin(np.deg2rad(-60))),
    "-pi/6": (np.cos(np.deg2rad(-30)),np.sin(np.deg2rad(-30))),
    "0": (np.cos(np.deg2rad(0)),np.sin(np.deg2rad(0))),
    "pi/6": (np.cos(np.deg2rad(30)),np.sin(np.deg2rad(30))),
    "pi/3":(np.cos(np.deg2rad(60)),np.sin(np.deg2rad(60)))
}


# This function is used to check whether a position is a legal position or not 
# considering the obstacle space and checking the tolerance of the robot with respect 
# to the obstacle space
def is_legal_pos(map, pos):
    i, j = pos
    num_rows = len(map)
    num_cols = len(map[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and not is_obstacle(i,j) and not check_obs_space(i,j)

def heuristicEuclidean(now, goal):
    cost=0.0
    
    if now is not None:
        cost=np.sqrt((now[0]-goal[0])**2 + (now[1]-goal[1])**2)
    return cost
    
"""
This function is used to generate the path a.k.a back-tracing
It returns two variables 
[path] - Shortest path found using the algorithm
[dict_path] - This dictionary contains all the explored nodes in the map used.
"""
def get_path(dict_path, start, goal):
    current = goal
    path = [current]
    #print(cost(current,start))
    print(dict_path.items())
    while  current != start:
        current = dict_path[current]
        path.append(current)
        
    path.append(start)
    path.reverse()
    #print(dict_path)
    return path,dict_path



def theta2val(theta):
    if theta == "-pi/3":
        return 0
    if theta == "-pi/6":
        return 1
    if theta == "0":
        return 2
    if theta == "pi/6":
        return 3
    if theta == "pi/3":
        return 4

def chk_duplicate(V,pos,theta,thres):
    return V[int(pos[0]/thres)][int(pos[1]/thres)][theta] != 1
        
def pos2coords(pos,step_size):
    x,y,theta=pos
    x_new = int(round((step_size*np.cos(np.deg2rad(theta)) + x),2))
    y_new = int(round((step_size*np.sin(np.deg2rad(theta)) + y),2))
    return (x_new,y_new)


"""
[fn] dijkstra

[in] - map
[in] - start
[in] - goal

This function takes the above inputs and find the shortest path using the dijkstra algorithm.


[out] returns the shortest path
"""
def astar(map, start, goal,step_size,threshold):
    #start = 
    #goal = 
    pq = PriorityQueue() # OpenList
    pq.put(start, 0) # We add the start to our priority_queue
    predecessors = {start: None} # Closed List
    cost_to_come = {start: 0} # To store the cost2come values
    V = np.zeros((int(map.shape[0]/threshold),int(map.shape[1]/threshold),5))

    while not pq.is_empty(): # Checking all the explored nodes
        current_cell = pq.get() # Popping the element based upon priority(cost)
        if  heuristicEuclidean(current_cell,goal) < 1.5: # if this is goal we return the shortest path
            predecessors[goal]=current_cell
            return get_path(predecessors, start, goal)
        for direction in ["-pi/3","-pi/6","0","pi/6","pi/3"]:
            row_offset, col_offset = actions[direction] # We check for all the direction in the path using the above for loop
            neighbour = (int(round((current_cell[0] + step_size*row_offset),2)), int(round((current_cell[1] + step_size*col_offset),2)))
            
            if is_legal_pos(map, neighbour) and neighbour not in cost_to_come and chk_duplicate(V,neighbour,theta2val(direction),threshold):
                # Here we check whether the selected direction or action is a legal move
                # if yes we assign new cost and add it to the priority_queue based
                # upon the cost.
                new_cost = cost_to_come[current_cell] + 1
                V[int(neighbour[0]/threshold)][int(neighbour[1]/threshold)][theta2val(direction)] = 1
                #print(direction)
                cost_to_come[neighbour] = new_cost
                f_value = new_cost + int(heuristicEuclidean(goal, neighbour))
                pq.put(neighbour, f_value)
                predecessors[neighbour] = current_cell  
                #print(neighbour)  
    print("[ERROR] Please enter different start_pos and goal_pos away from the obstacle space")
           
    return None


if __name__ == "__main__":
    
    # # Here we call all our function calls in order to generate the shortest path
    global maze
    maze = generate_map()
    # fig, ax=plt.subplots()
    # ax.imshow(maze[::-1,:,:])

    # #select point from the given map output

    # start_pos,goal_pos = plt.ginput(2)
    # start_pos=(249- int(start_pos[1]),int(start_pos[0]))
    # goal_pos=(249 - int(goal_pos[1]),int(goal_pos[0]))
    # start = (start_pos[0],start_pos[1],-30)
    # goal = (goal_pos[0],goal_pos[1],-30)
    # test case-1 
    #start=(35,30,-60)
    # test case -1 
    #goal=(230,224,0)
    x_s = int(input("Enter x coordinate  "))
    y_s = int(input("Enter y coordinate ")) 
    theta_s = int(input("Enter Initial Angle: "))
    x_g = int(input("Enter x coordinate  "))
    y_g = int(input("Enter y coordinate ")) 
    theta_g = int(input("Enter Initial Angle: "))
    start=(y_s,x_s,theta_s)
    goal=(y_g,x_g,theta_g)
    start_pos=pos2coords(start,5)
    goal_pos = pos2coords(goal,5)
    print("***      A-Star   ***")
    print("You have selected the start position as:",start_pos)
    print("You have selected the goal position as:",goal_pos)

    
    if is_obstacle(goal_pos[0],goal_pos[1]) or is_obstacle(start_pos[0],start_pos[1]) or check_obs_space(start_pos[0],start_pos[1]): 
         print("Please enter different start_pos and goal_pos away from the obstacle space")
    else:
        result,predec= astar(maze, start_pos, goal_pos,5,0.5)
        predec.pop(start_pos,None)
        for key,val in predec.items():
            #for k,val in disp.items():
            
            if not is_obstacle(key[0],key[1]):
                #To check the origin
                #cv2.circle(maze, [224, 230], 8, (0, 0, 255), -1)
                cv2.arrowedLine(maze,(val[1],val[0]),(key[1],key[0]),(0,0,255), 1)
                #maze[key[0]][key[1]] = [255,255,255]
                cv2.imshow('map',maze[::-1,:,:])
                output.write(maze[::-1,:,:])
                keyCode = cv2.waitKey(1)
                if (keyCode & 0xFF) == ord("q"):
                 cv2.destroyAllWindows()
                 break
        for i in result:
            maze[i[0]][i[1]] = [255,0,255]
            cv2.circle(maze, (i[1],i[0]),2,(125,0,255),-1)
            output.write(maze[::-1,:,:])
            cv2.imshow('map',maze[::-1,:,:])
            keyCode = cv2.waitKey(1)
            if (keyCode & 0xFF) == ord("q"):
                 cv2.destroyAllWindows()
                 break
        output.release()
        cv2.imwrite("fig.jpg",maze[::-1,:,:])
        # imageio.mimsave(res, result,fps=60)
          
    





