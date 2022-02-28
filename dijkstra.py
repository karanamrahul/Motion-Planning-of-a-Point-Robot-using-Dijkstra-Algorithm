import numpy as np
from Priority_queue import PriorityQueue
import matplotlib.pyplot as plt
import cv2



def cost(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

actions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1,1)
}

def is_legal_pos(input_state,i,j):
        num_rows = len(input_state)
        num_cols = len(input_state[0])
        return 0 <= i < num_rows and 0 <= j < num_cols 



def ActionMove(currentNode,state,predecessors):
        result=[]
        i,j=get_blank_pos(state)
        for action in ["up", "right", "down", "left","up_left", "up_right", "down_left", "down_right"]:

                new_state=state.copy()
                row_offset, col_offset = actions[action]

                if is_legal_pos(state,i + row_offset, j + col_offset):
                    newNode = new_state[i + row_offset][ j + col_offset]
                    new_state[i,j],new_state[i + row_offset][ j + col_offset] = newNode,currentNode
                    if  list(new_state.flatten()) not in predecessors:
                        result.append((new_state))
        return result


def get_path(dict_path, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = dict_path[current]
    path.append(start)
    path.reverse()
    return path



def dijkstra(map, start, goal):
    pq = PriorityQueue() # OpenList
    pq.put(start, 0)
    predecessors = {start: None} # Closed List
    cost_to_come = {start: 0} # To store the cost2come values

    while not pq.is_empty():
        current_cell = pq.get()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left","up_left", "up_right", "down_left", "down_right"]:
            row_offset, col_offset = actions[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(map, neighbour) and neighbour not in cost_to_come:
                if direction not in ["up_left", "up_right", "down_left", "down_right"]:
                  new_cost = cost_to_come[current_cell] + 1 
                else:
                    new_cost = cost_to_come[current_cell] + 1.4
                cost_to_come[neighbour] = new_cost
                f_value = new_cost + cost(current_cell, neighbour)
                pq.put(neighbour, f_value)
                predecessors[neighbour] = current_cell
    return None