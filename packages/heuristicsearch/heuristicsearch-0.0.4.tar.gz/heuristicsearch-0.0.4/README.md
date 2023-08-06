# Heuristic Searches
This module contains functions to perform a* search and ao* search algorithms

## Installation 
Run the following command to install:
```python
    pip install heuristicsearch
```

## Useage 
```python 
from a_star_search import AStar
from ao_star import AOStar
# object creation Astar(adjacency_list -> dictionary, heuristic_values -> dicitonary)
# call the apply_a_star method to find the shortest path
adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

heuristics = {'A':1, 'B':1, 'C':1, 'D':1}

graph1 = AStar(adjacency_list, heuristics)
graph1.apply_a_star(start='A',stop='B')
# similar approach for AOStar
# object creation AOStar(adjacency_list -> dictionary, heuristic_values -> dicitonary, startNode)
# call apply_AOStar method
```