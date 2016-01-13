import itertools
import math
import copy
timeTable = [[],[0, 1, 2], [1, 2], [1], [2, 3, 4], [3, 4, 5, 7], [3, 4, 5, 6, 7], [3, 4, 5, 6, 0]]
minSize = 2
maxSize = 3
minTime = 2
removedList = []
tallyList = []
tagList = []
idList = [0, 1, 2, 3, 4, 5, 6, 7]

def tallyNTag(timeTable, minSize, minTime, removedList, tallyList, tagList):
    print 'in function tallyNTag, timeTable = ', timeTable
    current = []
    intersection = []
    timeSlots = []
    for i in timeTable:
        if (len(i) < minSize):
            print 'i = ', i, 'index  in original timeTable = ', timeTable.index(i) + len(removedList)
            removedList.append(timeTable.index(i) + len(removedList))
            currentIndex = timeTable.index(i)
            timeTable.remove(i)
            #i = timeTable[timeTable.index(i)]
            print 'timeTable after remove = ', timeTable
        else:
            timeSlots.append(timeTable.index(i) + len(removedList))

    numberOfTimeSlots = len(timeTable)        
    print 'new timeTable = ', timeTable
    print 'removedList = ', removedList
    print 'timeSlots = ', timeSlots
    print 'numberOfTimeSlots = ', numberOfTimeSlots

    #for y in range(0, minTime):
    #    current.append(y) #current is the "time signature" you are looking at now

##    removedListIndex = 0
##    for y in range(0, numberOfTimeSlots):
##        if (y != removedList[removedListIndex]):
##            print("y = ", y + removedListIndex)
##            timeSlots.append(y + removedListIndex)
##        else:
##            if (removedListIndex < len(removedList) - 1):
##                removedListIndex = removedListIndex + 1
    
    for u in list(itertools.combinations(timeSlots, minTime)):
        current = list(u)
        for z in range(0,math.factorial(24*7 - len(removedList)) / (math.factorial(minTime) * math.factorial(24*7 - len(removedList) - minTime))):
            for x in range(0, minTime - 1):
                intersection = timeTable[current[x]]
                intersection = set(timeTable[current[x+1]]).intersection(set(intersection))
            tallyList.append(len(intersection))
            #print(intersection)
            for w in intersection:
                tagList.append(current)
            #increment current
            #print(tallyList)
        

class Edge(object):
    def _init_(self, u, v, w):
        self.source = u
        self.sink = v
        self.capacity = w
    def _repr_(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)

class FlowNetwork(object):
    def _init_(self):
        self.adj = {}
        self.flow = {}

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def get_edges(self, v):
        return self.adj[v]

    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u, v, w)
        redge = Edge(v, u, 0)
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0

    def find_path(self, source, sink, path, path_set):
        if source == sink:
            return path
        for edge in self.get_edges(source):
                residual = edge.capacity - self.flow[edge]
                if residual > 0 and not (edge,residual) in path_set:
                    path_set.add((edge, residual))
                    result = reslf.find_path(edge.sink, sink, path + [(edge, residual)], path_set)
                    if result != None:
                        return result
    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [], set())
        while path != None:
            flow = min(res for edge, res in path)
            for edge, res in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
                path = self.find_path (source, sink, [], set())
            return sum(self.flow[edge] for edge in self.get_edges(source))
        

def buildGraph(idList, tallyList, tagList):
    print("buildGraph")
    graph = FlowNetwork()
    #[graph.add_vertex(v) for v in 
    
def optimize(idList, timeTable, minSize, maxSize, minTime, removedList):

    tallyNTag(timeTable, minSize, minTime, removedList, tallyList, tagList)
    buildGraph(idList, tallyList, tagList)


optimize(idList, timeTable, minSize, maxSize, minTime, removedList)
    
    



        
    
