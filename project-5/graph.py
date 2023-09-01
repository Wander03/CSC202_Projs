from __future__ import annotations
from typing import Any, Dict, List, Optional
from stack_array import * # Needed for Depth First Search
from queue_array import * # Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key: Any):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to: List = []
        self.check = False
        self.color = None

    def __repr__(self) -> str:
        return ("Vertex({!r}, {!r}, {!r}, {!r})".format(self.id, [x.id for x in self.adjacent_to], self.check, self.color))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vertex):
            return False
        else:
             return (self.id == other.id
                        and self.adjacent_to == other.adjacent_to
                        and self.check == other.check
                        and self.color == other.color)

    def __lt__(self, other: Vertex) -> bool:
        return self.id < other.id

    def checked(self) -> bool:
        return self.check

    def visit(self) -> None:
        self.check = True

    def leave(self) -> None:
        self.check = False

    def get_color(self) -> Any:
        return self.color

    def set_color(self, c: Any) -> None:
        self.color = c

    def un_color(self) -> None:
        self.color = None

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename: str):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.verticies: Dict = {}

        new_lines: List = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].strip()
                new_lines.append(lines[i].split())

            for line in new_lines:
                if line[0] not in self.verticies:
                    self.verticies[line[0]] = Vertex(line[0])
                if line[1] not in self.verticies:
                    self.verticies[line[1]] = Vertex(line[1])
                self.verticies[line[0]].adjacent_to.append(self.verticies[line[1]])
                self.verticies[line[1]].adjacent_to.append(self.verticies[line[0]])

    def add_vertex(self, key: Any) -> None:
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if str(key) not in self.verticies:
            self.verticies[key] = Vertex(key)

    def get_vertex(self, key: Any) -> Optional[Vertex]:
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if str(key) in self.verticies:
            return self.verticies[key]
        else:
            return None 

    def add_edge(self, v1: Any, v2: Any) -> None:
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.verticies[v1].adjacent_to.append(self.verticies[v2])
        self.verticies[v2].adjacent_to.append(self.verticies[v1])

    def get_vertices(self) -> List:
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        out: List = []

        for vertex in self.verticies:
            out.append(vertex)

        out.sort()
        return out

    def set_unvisited(self) -> None:
        for vertex in self.verticies:
            temp = self.get_vertex(vertex)
            if temp is not None:
                temp.leave()

    def set_no_color(self) -> None:
        for vertex in self.verticies:
            temp = self.get_vertex(vertex)
            if temp is not None:
                temp.un_color()

    def conn_components(self) -> List:
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        components = self.get_vertices()
        self.set_unvisited()
        final: List = []

        for vertex in components:
            vert = self.get_vertex(vertex)
            if vert is not None and not vert.checked():
                final.append(self.DFS(vertex))

        return final

    def DFS(self, start: str) -> List:
        '''Performs a Depth First Search.
           Returns a List of sorted connected vertecies.'''
        stack = Stack(len(self.verticies) * 3, [start])
        out: List = []

        while not stack.is_empty():
            vertex = self.get_vertex(stack.peek())
            if vertex is not None and vertex.checked():
                stack.pop()
            elif vertex is not None:
                vertex.visit()
                out.append(stack.pop())
                adjacent_vertcies = vertex.adjacent_to
                adjacent_vertcies.sort(reverse=True)
            for vert in adjacent_vertcies:
                if not vert.checked():
                    stack.push(vert.id)

        out.sort()
        return out

    def is_bipartite(self) -> bool:
        '''Returns True if the graph is bicolorable and False otherwise.
        This method MUST use Breadth First Search logic!'''
        components = self.get_vertices()
        self.set_unvisited()
        self.set_no_color()
        start = components[0]

        queue = Queue(len(self.verticies), [start])
        temp = self.get_vertex(start)
        if temp is not None:
            temp.visit()
            temp.set_color(1)

        while not queue.is_empty():
            removed = self.get_vertex(queue.dequeue())
            if removed is not None:
                adjacent_vertcies = removed.adjacent_to
                adjacent_vertcies.sort()

                colors = [1, 2]
                colors.remove(removed.get_color())

            for vert in adjacent_vertcies:
                if vert is not None and removed is not None and vert.get_color() == removed.get_color():
                    return False
                elif vert is not None and vert.get_color() is None:
                    vert.set_color(colors[0])

                if not vert.checked():
                    vert.visit()
                    queue.enqueue(vert.id)

        return True
