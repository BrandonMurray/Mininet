#building the graph of the network
graph = {
    'h1':{'S1':0},
    'h2':{'S1':0},
    'h3':{'S5':0},
    'h5':{'S6':0},
    'h6':{'S4':0},
    'h7':{'S4':0},
    'S1':{'S2':10,'S3':10, 'S5':5,'h1':0},
    'S2':{'S1':10, 'S4':15,'h2':0},
    'S3':{'S1':10, 'S4':5},
    'S4':{'S2':15,'S3':5, 'S6':10,'h6':0,'h7':0},
    'S5':{'S1':5,'S6':5,'h3':0},
    'S6':{'S4':10,'S5':5,'h5':0}}
    

def dijkstra(graph,source,destination):
    infinity = float("inf")
    unvisitedNodes = graph.copy()
    previousNode = {}
    lowestCost = {}
    path = []
    
    #set every node distance to inf except starting node 
    for node in unvisitedNodes:
        lowestCost[node] = infinity
    lowestCost[source] = 0

    #loop while still nodes unvisited.
    while unvisitedNodes:
        minNode = None
        #select node with shortest distance
        for node in unvisitedNodes:
            #check if its the first node
            if minNode is None:
                minNode = node
            #cost is lower at node than minNode swap for the node
            elif lowestCost[node] < lowestCost[minNode]:
                minNode = node

        for neighborNode, cost in graph[minNode].items():
            #compare current nodes cost plus edgeweight cost to neighbor nodes cost
            if cost + lowestCost[minNode] < lowestCost[neighborNode]:
                #reduce the neighborNodes cost 
                lowestCost[neighborNode] = cost + lowestCost[minNode]
                #set previous node for neighborNode to current minNode for the path
                previousNode[neighborNode] = minNode
        unvisitedNodes.pop(minNode)

    #trace from destination back to source for path
    currentNode = destination
    while currentNode != source:
        path.append(currentNode)
        currentNode = previousNode[currentNode]
        
    #add source node and reverse order        
    path.append(source)
    path.reverse()
   
    #print path
    print('The path from ' +str(source) + ' to ' +str(destination) +' : ' + str(path))

print('h1 to all other hosts')
dijkstra(graph, 'h1', 'h2')
dijkstra(graph, 'h1', 'h3')
dijkstra(graph, 'h1', 'h5')
dijkstra(graph, 'h1', 'h6')
dijkstra(graph, 'h1', 'h7')

print()
print('h2 to all other hosts')
dijkstra(graph, 'h2', 'h1')
dijkstra(graph, 'h2', 'h3')
dijkstra(graph, 'h2', 'h5')
dijkstra(graph, 'h2', 'h6')
dijkstra(graph, 'h2', 'h7')

print()
print('h3 to all other hosts')
dijkstra(graph, 'h3', 'h1')
dijkstra(graph, 'h3', 'h2')
dijkstra(graph, 'h3', 'h5')
dijkstra(graph, 'h3', 'h6')
dijkstra(graph, 'h3', 'h7')

print()
print('h5 to all other hosts')
dijkstra(graph, 'h5', 'h1')
dijkstra(graph, 'h5', 'h2')
dijkstra(graph, 'h5', 'h3')
dijkstra(graph, 'h5', 'h6')
dijkstra(graph, 'h5', 'h7')

print()
print('h6 to all other hosts')
dijkstra(graph, 'h6', 'h1')
dijkstra(graph, 'h6', 'h2')
dijkstra(graph, 'h6', 'h3')
dijkstra(graph, 'h6', 'h5')
dijkstra(graph, 'h6', 'h7')

print()
print('h7 to all other hosts')
dijkstra(graph, 'h7', 'h1')
dijkstra(graph, 'h7', 'h2')
dijkstra(graph, 'h7', 'h3')
dijkstra(graph, 'h7', 'h5')
dijkstra(graph, 'h7', 'h6')
