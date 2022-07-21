# 4.1 Given a directed graph and two nodes (S and E), desgin an algorithm to find out whether there is a route from S to E

import unittest

"""
# dfs recursion solution
def find_path(graph, start, end, path=[]):
        path = path + [start] # create initial path
        if start == end: # return if path found
            return path
        if not start in graph: # if the node is not in the graph
            return None
        for node in graph[start]: # iterate through all neighboring nodes
            if node not in path: # if the node has not been visited
                newpath = find_path(graph, node, end, path) # visit the node
                if newpath: return newpath # if we found a path, return it
        return None # no path found
"""

# bfs iterative solution with a queue
def is_route(graph, start, end):
    if start == end:
        return True
    queue = []
    visited = set()
    queue.append(start)
    while queue:
        curr = queue.pop(0)
        for node in graph[curr]:
            if node not in visited:
                if node == end:
                    return True
                else:
                    queue.append(node)
        visited.add(curr)
    return False

class Test(unittest.TestCase):

    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

    tests = [
        ("A", "L", True),
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A", False),
        ("P", "B", False),
    ]

    def test_is_route(self):
        for [start, end, expected] in self.tests:
            actual = is_route(self.graph, start, end)
            assert actual == expected

if __name__ == "__main__":
    unittest.main()

