# Motion-Planning-of-a-Point-Robot-using-Dijkstra-Algorithm


This project mainly implements the path planning of a point robot using
Dijkstra Algorithm given obstacle space

## File Structure

```
├── Code
|  ├── dijkstra.py
|  ├── Priority_queue.py
├── Map
|  ├── display_map.png
├── Results
|  |  ├── result.mp4
|  |  ├── result.gif

```
The map can be found in the /Map/map.png

Steps to Run the code 
-> Make sure you have Priority_queue.py file and dijsktra.py in your repository

### Packages used for this project
```
heapq
numpy
opencv
matplotlib
```

```
$ git clone https://github.com/karanamrahul/Motion-Planning-of-a-Point-Robot-using-Dijkstra-Algorithm.git
$ cd Motion-Planning-of-a-Point-Robot-using-Dijkstra-Algorithm
$ python3 dijkstra.py
```

```
--> This will open up the map.
--> Please select two points from the map using your mouse 
--> Starting position and the goal position 
--> If you have selected a position which is inside the obstacle space, 
--> then it will raise an error
--> Please select a different position
```
![](https://github.com/karanamrahul/Motion-Planning-of-a-Point-Robot-using-Dijkstra-Algorithm/blob/main/map/display_map.png)


--> After the selection, the map will pop up showing the 
    exploration path, when the robot reaches the goal point
    , it will show you the best path.

![](https://github.com/karanamrahul/Motion-Planning-of-a-Point-Robot-using-Dijkstra-Algorithm/blob/main/results/result.gif)
--> The video can be found in the /results directory.
    
       
