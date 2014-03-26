import os

from itertools import combinations
from itertools import product

import networkx as nx


def read_graph():
    """Generator that reads pickled graphs."""
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    for _, _, file_names in os.walk(data_dir):
        for file_name in file_names:
            if file_name.endswith('.gpickle'):
                path = data_dir + '/' + file_name
                graph = nx.read_gpickle(path)
                print 'Read graph from %s' % path
                yield graph

def is_balanced(triangle_signs):
    count = triangle_signs.count(1)
    if (count % 2):
        return False
    return True


def find_triangles(graph):
    """Find triangles in graph."""
    nodes = graph.nodes()
    for node in nodes:
        neigh = graph.neighbors(node)
        pairs = combinations(neigh, 2)
        for (a, b) in pairs:
            if graph.has_edge(a, b):
                weights1 =  [data.values()[0] for data in graph.get_edge_data(a,
                    b).values()]
                weights2 =  [data.values()[0] for data in graph.get_edge_data(node,
                    a).values()]
                weights3 =  [data.values()[0] for data in graph.get_edge_data(node,
                    b).values()]
                for triangle in product(weights1, weights2, weights3):
                    yield triangle
        graph.remove_node(node)


def main():
    for graph in read_graph():
        balanced = 0
        unbalanced = 0
        for triangle in find_triangles(graph):
            if is_balanced(triangle):
                balanced += 1
            else:
                unbalanced += 1
        print 'Balanced triangles: %d' % balanced
        print 'Unbalanced triangles: %d' % unbalanced

        
if __name__ == '__main__':
     main()
