"""
Program Name: graph_program_ehlert.py
Author: Tony Ehlert
Date: 8/31/2023

Program Description: This programs contains a graph and finds the shortest path between two given nodes, the node
with the most edges, and all isolated nodes
"""
def shortest_path(graph, start_node, end_node):
    """
    This function finds the shortest path between two nodes of a graph
    :param graph: the graph to be searched
    :param start_node: starting node
    :param end_node: ending node
    :return: list of nodes contained in the shortest path between the start and end nodes
    """
    path_list = start_node
    path_index = 0

    # variable to track previously visited node
    prev_nodes = {start_node}

    if start_node == end_node:
        return path_list

    while path_index < len(path_list):
        # variable to hold current_path from index of path_list
        current_path = path_list[path_index]

        # assign the last node listed in the current_path to last_node variable
        last_node = current_path[-1]

        # assign list of nodes connected to last node to conn_nodes list variabl;e
        conn_nodes = graph[last_node]

        # search for end_node in conn_nodes list. If found, append to current_path list and return current_path list
        if end_node in conn_nodes:
            current_path.append(end_node)
            return current_path

        # add new paths
        for curr_node in conn_nodes:
            # if statement to check to ensure curr_node has not already been visited
            if not curr_node in prev_nodes:
                # make a copy of current_path variable and assign to new_path with slice [:]
                new_path = current_path[:]

                # add curr_node to new_path list
                new_path.append(curr_node)

                # add new_path list to path_list
                path_list.append(new_path)

                # add curr_node to prev_nodes list
                prev_nodes.add(curr_node)
            # update path_index to continue to the next path in path_list
            path_index += 1

    # if no path to node is found return empty list
    return []

def find_node_with_most_edges(graph):
    """
    This function finds the node(s) with the most edges and adds it to a list that gets returned
    :param graph: graph of nodes to be searched
    :return: list containing nodes with most edges
    """
    most_edges_nodes = []
    max_edges = 0
    # find highest number of edges
    for value in graph.values():
        if len(value) >= max_edges:
            max_edges = len(value)

    # find keys equaling highest number of edges
    for key, value in graph.items():
        if len(value) == max_edges:
            most_edges_nodes.append(key)
    print(f"Node(s) with the most edges ({max_edges}):")
    print(most_edges_nodes)

if __name__ == "__main__":
    # create graph
    graph = {"A":["D"],
             "D":["A", "B", "G", "H"],
             "G":["D", "E"],
             "B":["D", "F"],
             "E":["F", "G"],
             "H":["D"],
             "C":[],
             "F":["B", "E"],
             "I":["E"]}

    # find the shortest path between node "A" and node "I"
    # shortest_path_list = shortest_path(graph, "A", "I")
    # print(shortest_path_list)

    # find the node with the most edges
    find_node_with_most_edges(graph)

    # find all isolated nodes
    isolated_nodes = []
    for key, value in graph.items():
        if len(value) == 0:
            isolated_nodes.append(key)
    print("\nIsolated Nodes:")
    print(isolated_nodes)
