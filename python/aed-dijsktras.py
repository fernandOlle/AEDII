class Graph():
  
  def __init__(self, vertices):
    self.V = vertices
    self.graph = [[0 for column in range(vertices)] 
      for row in range(vertices)]

  def printSolution(self, dist):
    print ("Vertex \tDistance from Source")
    for node in range(self.V):
      print (node, "\t", dist[node])

  # A utility function to find the vertex with 
  # minimum distance value, from the set of vertices 
  # not yet included in shortest path tree
  def minDistance(self, dist, sptSet):
    maxint = 1000000
    # Initilaize minimum distance for next node
    min = maxint
    # Search not nearest vertex not in the 
    # shortest path tree
    for v in range(self.V):
      if dist[v] < min and sptSet[v] == False:
        min = dist[v]
        min_index = v

    return min_index
 
  # Funtion that implements Dijkstra's single source 
  # shortest path algorithm for a graph represented 
  # using adjacency matrix representation
  def dijkstra(self, src):
    maxint = 1000000

    dist = [maxint] * self.V
    dist[src] = 0
    sptSet = [False] * self.V

    for cout in range(self.V):

    # Pick the minimum distance vertex from 
    # the set of vertices not yet processed. 
    # u is always equal to src in first iteration
      u = self.minDistance(dist, sptSet)

      # Put the minimum distance vertex in the 
      # shotest path tree
      sptSet[u] = True

      # Update dist value of the adjacent vertices 
      # of the picked vertex only if the current 
      # distance is greater than new distance and
      # the vertex in not in the shotest path tree
      for v in range(self.V):
        if self.graph[u][v] > 0 and sptSet[v] == False and \
        dist[v] > dist[u] + self.graph[u][v]:
          dist[v] = dist[u] + self.graph[u][v]

    self.printSolution(dist)
  
# Driver program
g = Graph(9)
g.graph = [
            [0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]

          ]

print("Entre o primeiro valor de 1 a 20 : ")
first = input()
print("Entre o segundo valor de 1 a 20 : ")
second = input()

g.dijkstra(8)

nMatrix = [
            [0, 7, 9, 0, 6, 6, 1, 5, 2, 1, 2, 0, 7, 3, 5, 1, 3, 7, 6, 4],
            [7, 0, 6, 0, 8, 0, 7, 6, 6, 4, 5, 7, 4, 2, 4, 9, 6 ,9, 4, 8],
            [9, 6, 0, 2, 8, 1, 3, 9, 1, 7, 5, 3, 9, 8, 1, 9, 7, 7, 6, 7],
            [0, 0, 2, 0, 6, 5, 0, 4, 0, 6, 2, 8, 5, 4, 1, 1, 6, 9, 2, 6],
            [6, 8, 8, 6, 0, 3, 6, 7, 7, 4, 6, 7, 8, 8, 0, 5, 2, 5, 9, 1],
            [6, 0, 1, 5, 3, 0, 9, 5, 1, 1, 9, 5, 7, 8, 0, 3, 2, 8, 7, 7],
            [1, 7, 3, 0, 6, 9, 0, 4, 9, 6, 6, 7, 6, 1, 5, 5, 1, 6, 5, 2],
            [5, 6, 9, 4, 7, 5, 4, 0, 4, 3, 7, 4, 7, 6, 5, 5, 8, 2, 7, 4],
            [2, 6, 1, 0, 7, 1, 9, 4, 0, 1, 0, 4, 1, 5, 8, 1, 5, 7, 4, 4],
            [1, 4, 7, 6, 4, 1, 6, 3, 1, 0, 7, 7, 3, 2, 2, 7, 4, 0, 8, 2],
            [2, 5, 5, 2, 6, 9, 6, 7, 0, 7, 0, 8, 3, 4, 1, 4, 0, 0, 0, 4],
            [0, 7, 3, 8, 7, 5, 7, 4, 4, 7, 8, 0, 7, 0, 2, 9, 5, 9, 6, 2],
            [7, 4, 9, 5, 8, 7, 6, 7, 1, 3, 3, 7, 0, 0, 0, 3, 8, 6, 4, 3],
            [3, 2, 8, 4, 8, 8, 1, 6, 5, 2, 4, 0, 0, 0, 8, 4, 1, 8, 2, 6],
            [5, 4, 1, 1, 0, 0, 5, 5, 8, 2, 1, 2, 0, 8, 0, 2, 2, 6, 8, 7],
            [1, 9, 9, 1, 5, 3, 5, 5, 1, 7, 4, 9, 3, 4, 2, 0, 0, 7, 9, 6],
            [3, 6, 7, 6, 2, 2, 1, 8, 5, 4, 0, 5, 8, 1, 2, 0, 0, 0, 7, 1],
            [7, 9, 7, 9, 5, 8, 6, 2, 7, 0, 0, 9, 6, 8, 6, 7, 0, 0, 1, 9],
            [6, 4, 6, 2 ,9, 7, 5, 7, 4 ,8, 0, 6, 4, 2, 8, 9, 7, 1, 0, 8],
            [4, 8, 7, 6, 1, 7, 2, 4, 4, 2, 4, 2, 3, 6, 7, 6, 1, 9, 8, 0]
          ]