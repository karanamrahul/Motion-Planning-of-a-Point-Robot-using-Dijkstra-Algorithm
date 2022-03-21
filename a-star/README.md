# Motion-Planning-of-a-Point-Robot-using-Dijkstra-Algorithm


Github Repository : https://github.com/karanamrahul/Motion-Planning-of-a-Point-Robot-using-Dijkstra-and-Astar-Algorithm

This project mainly implements the path planning of a point robot using A-star Algorithm given obstacle space

## File Structure

```
├── Code
|  ├── Astar.py
|  ├── Priority_queue.py
├── Map
|  ├── output_map.png
├── Results
|  |  ├── result.mp4
|  |  ├── test_output_1.mp4

```
The map can be found in the /Map/map.png

Steps to Run the code 
-> Make sure you have Priority_queue.py file and dijsktra.py in your repository


```
$ git clone Motion-Planning-of-a-Point-Robot-using-Dijkstra-and-Astar-Algorithm
$ cd Motion-Planning-of-a-Point-Robot-using-Dijkstra-and-Astar-Algorithm
$ python3 Astar.py
```

```
--> Please enter your start and goal coordinates in this format (x,y,theta ) for both start and goal.
--> If you have selected a position which is inside the obstacle space, 
--> then it will raise an error
--> Please select a different position
```

### Test case - 1
![](https://github.com/karanamrahul/Motion-Planning-of-a-Point-Robot-using-Dijkstra-and-Astar-Algorithm/blob/main/a-star/results/test_1.jpg)

![](https://github.com/karanamrahul/Motion-Planning-of-a-Point-Robot-using-Dijkstra-and-Astar-Algorithm/blob/main/a-star/results/test_1_output.gif)


--> After the selection, the map will pop up showing the 
    exploration path, when the robot reaches the goal point
    , it will show you the best path.
    
    
### Test Case - 2

![](https://github.com/karanamrahul/Motion-Planning-of-a-Point-Robot-using-Dijkstra-and-Astar-Algorithm/blob/main/a-star/results/fig.jpg)

![](https://github.com/karanamrahul/Motion-Planning-of-a-Point-Robot-using-Dijkstra-and-Astar-Algorithm/blob/main/a-star/results/1.gif)

--> The video can be found in the /results directory.


    
       

