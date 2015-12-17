##--- Day 9: All in a Single Night ---
##
##Every year, Santa manages to deliver all of his presents in a single night.
##
##This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?
##
##For example, given the following distances:
##
##London to Dublin = 464
##London to Belfast = 518
##Dublin to Belfast = 141
##The possible routes are therefore:
##
##Dublin -> London -> Belfast = 982
##London -> Dublin -> Belfast = 605
##London -> Belfast -> Dublin = 659
##Dublin -> Belfast -> London = 659
##Belfast -> Dublin -> London = 605
##Belfast -> London -> Dublin = 982
##The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.
##
##What is the distance of the shortest route?

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def addNeighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

    def getWeight(self, neighbor):
        return self.neighbors[neighbor]

    def getKey(self):
        return self.key

    def getNeighbors(self):
        return self.neighbors
            

class Graph:
    def __init__(self):
        self.vertices = {}

    def addEdge(self, nodeA, nodeB, weight):
        if (nodeA not in self.vertices):
            self.vertices[nodeA] = Vertex(nodeA)
        if (nodeB not in self.vertices):
            self.vertices[nodeB] = Vertex(nodeB)
        self.vertices[nodeA].addNeighbor(self.vertices[nodeB],weight)
        self.vertices[nodeB].addNeighbor(self.vertices[nodeA],weight)
        
    def getVertices(self):
        return self.vertices;
    
santasMap = Graph()

def fillGraph(lines):
    for line in lines:
        lineParts = line.split(" ")
        cityA, cityB, distance = [lineParts[i].strip() for i in (0,2,-1)]
        santasMap.addEdge(cityA,cityB,int(distance))
    
def determineShortestPath():
    minDistance = float("inf")
    cities = santasMap.getVertices().values()
    for city in cities:
        startCityName = city.getKey()
        minDistance = min(minDistance, minTravelFromCity(city, 0, [startCityName]))
    return minDistance

# Side-note: I have such a love-hate relationship with recursion...

## startCity(Vertex), distanceSoFar(int), visitedCities(list-of-strings)
def minTravelFromCity(startCity, distanceSoFar, visitedCities):
    if (len(visitedCities) == len(santasMap.getVertices())):
        # We've been around the world! Report back the distance...
        return distanceSoFar
    
    neighbors = startCity.getNeighbors()
    minTravelFromNeighbors = []
    for city in neighbors:
        if (city.getKey() in visitedCities):
            continue
        
        # Create a new copy of the visited cities, other wise we'll pass the current one in by reference.
        newVisited = visitedCities[:]
        newVisited.append(city.getKey())
        minTravelFromNeighbors.append(minTravelFromCity(city,distanceSoFar + city.getWeight(startCity),newVisited))
        
    return min(minTravelFromNeighbors)
        
def printGraph():
    for vertex in santasMap.getVertices().values():
        for neighbor in vertex.getNeighbors():
            vertexKey = vertex.getKey()
            neighborKey = neighbor.getKey()
            print ("%s -> %s = %d)"  % ( vertexKey, neighborKey, vertex.getWeight(neighbor)))

f = open('day9-input.txt','r')
fillGraph(f.readlines())

# printGraph()
print("Part One:", determineShortestPath())
