from graph import Graph 
class AOStar(Graph):
    def __init__(self, graph, heuristicNodeList, startNode):  #instantiate graph object with graph topology, heuristic values, start node
        super().__init__(graph)
        self.__H = heuristicNodeList
        self.__start = startNode
        self.__parent = {}
        self.__status = {}
        self.__solutionGraph = {}

    def applyAOStar(self):  # starts a recursive AO* algorithm
        self.__aoStar(self.__start, False)
        self.__printSolution()

    def __getNeighbors(self, v):  # gets the Neighbors of a given node
        return self.adjac_lis.get(v, '')

    def __getStatus(self, v):  # return the status of a given node
        return self.__status.get(v, 0)

    def __setStatus(self, v, val):  # set the status of a given node
        self.__status[v] = val

    def __getHeuristicNodeValue(self, n):
        return self.__H.get(n, 0)  # always return the heuristic value of a given node

    def __setHeuristicNodeValue(self, n, value):
        self.__H[n] = value  # set the revised heuristic value of a given node

    def __printSolution(self):
        print("FOR THE SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:", self.__start)
        print("------------------------------------------------------------")
        print(self.__solutionGraph)
        print("------------------------------------------------------------")

    def __computeMinimumCostChildNodes(self, v):  # Computes the Minimum Cost of child nodes of a given node v
        minimumCost = 0
        costToChildNodeListDict = {}
        costToChildNodeListDict[minimumCost] = []
        flag = True
        for nodeInfoTupleList in self.__getNeighbors(v):  # iterate over all the set of child node/s
            cost = 0
            nodeList = []
            for c, weight in nodeInfoTupleList:
                cost = cost + self.__getHeuristicNodeValue(c) + weight
                nodeList.append(c)
            if flag == True:  # initialize Minimum Cost with the cost of first set of child node/s
                minimumCost = cost
                costToChildNodeListDict[minimumCost] = nodeList  # set the Minimum Cost child node/s
                flag = False
            else:  # checking the Minimum Cost nodes with the current Minimum Cost
                if minimumCost > cost:
                    minimumCost = cost
                    costToChildNodeListDict[minimumCost] = nodeList  # set the Minimum Cost child node/s
        return minimumCost, costToChildNodeListDict[minimumCost]  # return Minimum Cost and Minimum Cost child node/s

    def __aoStar(self, v, backTracking):  # AO* algorithm for a start node and backTracking status flag
        # print("HEURISTIC VALUES :", self.__H)
        # print("SOLUTION GRAPH :", self.__solutionGraph)
        print("PROCESSING NODE :", v)
        print("-----------------------------------------------------------------------------------------")
        if self.__getStatus(v) >= 0:  # if status node v >= 0, compute Minimum Cost nodes of v
            minimumCost, childNodeList = self.__computeMinimumCostChildNodes(v)
            print(minimumCost, childNodeList)
            print()
            self.__setHeuristicNodeValue(v, minimumCost)
            self.__setStatus(v, len(childNodeList))
            solved = True  # check the Minimum Cost nodes of v are solved
            for childNode in childNodeList:
                self.__parent[childNode] = v
                if self.__getStatus(childNode) != -1:
                    solved = solved & False
            if solved == True:  # if the Minimum Cost nodes of v are solved, set the current node status as solved(-1)
                self.__setStatus(v, -1)
                self.__solutionGraph[
                    v] = childNodeList  # update the solution graph with the solved nodes which may be a part of solution
            if v != self.__start:  # check the current node is the start node for backtracking the current node value
                self.__aoStar(self.__parent[v],
                            True)  # backtracking the current node value with backtracking status set to true
            if backTracking == False:  # check the current call is not for backtracking
                for childNode in childNodeList:  # for each Minimum Cost child node
                    self.__setStatus(childNode, 0)  # set the status of child node to 0(needs exploration)
                    self.__aoStar(childNode,
                                False)  # Minimum Cost child node is further explored with backtracking status as false
