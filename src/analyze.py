import os

import networkx as nx


def read_graph():
    data_dir = os.path.join(os.path.dirname(__file__), '../data')
    for _, _, file_names in os.walk(data_dir):
        for file_name in file_names:
            if file_name.endswith('.gpickle'):
                graph = nx.read_gpickle(file_name)
                yield graph


def main():
    for graph in read_graph():

        
if __name__ == '__main__':
     main()
