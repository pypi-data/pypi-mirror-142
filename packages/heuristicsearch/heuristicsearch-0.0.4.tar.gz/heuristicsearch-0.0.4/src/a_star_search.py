from graph import Graph

class AStar(Graph):
    def __init__(self, adjac_lis, heuristicNodeList):
        super().__init__(adjac_lis)
        self.heuristic = heuristicNodeList
    def __get_neighbors(self, v):
        return self.adjac_lis[v]
 
    def __get_heuristic(self, n):
        return self.heuristic[n]
    def apply_a_star(self, start, stop):
        self.__a_star_algorithm(start=start, stop=stop)
    
    def __a_star_algorithm(self, start, stop):
        # In open_lst is a list of nodes which have been visited, but who's 
        # neighbours haven't all been inspected, It starts off with the start node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_lst = set([start])
        closed_lst = set([])
 
        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {start:0}
 
        # par contains an adjac mapping of all nodes
        par = {start:start}
 
        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f(n) = g(n) + h(n)
            for v in open_lst:
                if n == None or poo[v] + self.__get_heuristic(v) < poo[n] + self.__get_heuristic(n):
                    n = v
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
                print("Path")
                for i in range(len(reconst_path) - 1):
                    print(f"{reconst_path[i]} -> ",end="")
                print(reconst_path[-1])
                print("Cost")
                for i in range(len(reconst_path) - 1):
                    print(f"{poo[reconst_path[i]]} -> ",end="")
                print(poo[reconst_path[-1]])
                # print('Path found: {} and the total cost is {}'.format(reconst_path,poo[stop]))
                return reconst_path
 
            # for all the neighbors of the current node do
            for (m, weight) in self.__get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None

adjacency_list = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('C', 3), ('G', 2)]
}

heuristics = {'S':5, 'A':3, 'B':4, 'C':2, 'D':6, 'G':0}

graph = AStar(adjacency_list, heuristics)
graph.apply_a_star(start='S',stop='G')