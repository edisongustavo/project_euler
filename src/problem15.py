'''
Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.

0--1--2
|  |  |
*--*--3
|  |  |
*--*--4

0--1--*
|  |  |
*--2--3
|  |  |
*--*--4

...

How many routes are there through a 2020 grid?

Answer:

http://stackoverflow.com/questions/14272119/finding-the-number-of-paths-of-given-length-in-a-undirected-unweighted-graph?rq=1
'''
import numpy
from array import array


class Graph(object):

    def __init__(self, size):
        self.size = size


    def number_of_adjacents(self, node):
        return len(self.adjacents(node))


    def adjacents(self, node):
        x, y = node

        adjacents = set()

        adjacents.add((min(self.size - 1, x + 1), y))
        adjacents.add((x, min(self.size - 1, y + 1)))

        try:
            adjacents.remove(node)
        except KeyError:
            pass

        return adjacents

    def is_connected(self, a, b):
        return Graph.signed_manhattan_distance(a, b) == 1


    def to_node(self, continuous_node):

        y = continuous_node / self.size
        x = continuous_node - (y * self.size)

        return (x, y)

    def adjacency_matrix(self):
        n = self.size ** 2

        values = []
        for i in xrange(n):
            values.append(array('I', [0] * n))

            for j in xrange(max(0, i - 1), max(i + 1, n)):
                if i != j and abs(i - j) == 1:
                    values[i][j] = 1

        return numpy.matrix(values)


    @classmethod
    def signed_manhattan_distance(cls, a, b):
        x_a, y_a = a
        x_b, y_b = b

        d_x = x_b - x_a
        d_y = y_b - y_a

        return d_x + d_y


def find_number_of_paths_of_length(graph, start, end):
    m = graph.adjacency_matrix()
    k = graph.signed_manhattan_distance(start, end)
    c = m ** k

    x, y = end
    return c.item((x, y))


def solve_for_grid_size(grid_size):
    '''
    @param grid_size: int
    
    @return int
        The amount of differents paths
    '''
    start = (0, 0)
    end = (grid_size, grid_size)
    path = find_number_of_paths_of_length(Graph(grid_size + 1), start, end)
    return path


def test_Graph_Adjacents():
    assert Graph(2).adjacents((0, 0)) == set([(0, 1), (1, 0)])
    assert Graph(2).adjacents((1, 1)) == set()

    assert Graph(3).adjacents((1, 1)) == set([(2, 1), (1, 2)])
    assert Graph(3).adjacents((1, 2)) == set([(2, 2)])
    assert Graph(3).adjacents((2, 2)) == set([])


def test_GraphToNode():
    assert Graph(2).to_node(0) == (0, 0)
    assert Graph(2).to_node(1) == (1, 0)
    assert Graph(2).to_node(2) == (0, 1)
    assert Graph(2).to_node(3) == (1, 1)

    assert Graph(3).to_node(0) == (0, 0)
    assert Graph(3).to_node(1) == (1, 0)
    assert Graph(3).to_node(2) == (2, 0)
    assert Graph(3).to_node(3) == (0, 1)
    assert Graph(3).to_node(4) == (1, 1)
    assert Graph(3).to_node(5) == (2, 1)
    assert Graph(3).to_node(6) == (0, 2)
    assert Graph(3).to_node(7) == (1, 2)
    assert Graph(3).to_node(8) == (2, 2)


def test_GraphIsConnected():
    assert Graph(2).is_connected((1, 0), (1, 0)) == False
    assert Graph(2).is_connected((0, 0), (0, 0)) == False

    assert Graph(2).is_connected((0, 0), (1, 0)) == True
    assert Graph(2).is_connected((1, 0), (0, 0)) == False
    assert Graph(2).is_connected((0, 0), (2, 0)) == False
    assert Graph(2).is_connected((2, 0), (0, 0)) == False

    assert Graph(2).is_connected((0, 0), (0, 1)) == True


def test_GraphManhattanDistance():
    assert Graph.signed_manhattan_distance((1, 0), (3, 0)) == 2
    assert Graph.signed_manhattan_distance((1, 0), (3, 1)) == 3
    assert Graph.signed_manhattan_distance((1, 1), (1, 0)) == -1
    assert Graph.signed_manhattan_distance((0, 0), (0, 0)) == 0


def test_solve_for_grid_size():
    assert solve_for_grid_size(2) == 6
    assert solve_for_grid_size(3) == 20
    assert solve_for_grid_size(4) == 70
    assert solve_for_grid_size(5) == 252


if __name__ == '__main__':
    print(solve_for_grid_size(20))
