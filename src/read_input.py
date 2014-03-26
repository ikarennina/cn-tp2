import os

import networkx as nx

DATA_DIR = os.path.join(os.path.dirname(__file__), '../data/')

def main():
    for _, _, file_names in os.walk(DATA_DIR):
        for file_name in file_names:
            if file_name.endswith('.gz'):
                print 'Reading data from file %s' % file_name
                path = DATA_DIR + file_name
                graph = nx.read_weighted_edgelist(path, create_using=nx.DiGraph())
                out_name = path.replace('.gz', '.gpickle')
                print 'Saving data to %s' % out_name
                graph = directed_to_undirected_multi(graph)
                nx.write_gpickle(graph, out_name)


def directed_to_undirected_multi(digraph):
    """Transform a directed graph in an unidrected multigraph.
    >>> graph = nx.DiGraph()
    >>> graph.add_path([1, 2, 3, 1], weight=1)
    >>> graph.add_edge(1, 3, weight=0)
    >>> directed_to_undirected_multi(graph) 
    """
    multigraph = nx.MultiGraph()
    multigraph.add_edges_from(digraph.edges(data=True))
    return multigraph


if __name__ == '__main__':
     main()
