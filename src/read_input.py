import os

import networkx as nx

DATA_DIR = os.path.join(os.path.dirname(__file__), '../data/')

def main():
    for _, _, file_names in os.walk(DATA_DIR):
        for file_name in file_names:
            if file_name.endswith('.gz'):
                print 'Reading data from file %s' % file_name
                graph = nx.read_weighted_edgelist(file_name, create_using=nx.DiGraph())
                out_name = file_name.replace('.gz', '.gpickle')
                print 'Saving data to %s' % out_name
                nx.write_gpickle(graph, out_name)

if __name__ == '__main__':
     main()
