"""
Program Name: graph_program_ehlert.py
Author: Tony Ehlert
Date: 8/31/2023

Program Description: This programs contains a graph and finds the shortest path between two given nodes, the node
with the most edges, and all isolated nodes
"""
def shortest_path(graph, start_node, end_node, path = []):
    """
    This function finds the shortest path between two nodes of a graph
    :param graph: the graph to be searched
    :param start_node: starting node
    :param end_node: ending node
    :return: list of nodes contained in the shortest path between the start and end nodes
    """
    # create initial path
    path = path + [start_node]

    # check for start_node and end_node being the same node
    if start_node == end_node:
        return path

    # if statement to check if key is in graph
    if graph.get(start_node) is None:
        return None

    # create a variable to hold the shortest found path
    shortest = None

    # loop through each value of matching key/node
    for current_node in graph[start_node]:
        # check if current_node is already contained  in path list, if not recurse on shortest_path to get value for new_path
        if current_node not in path:
            new_path = shortest_path(graph, current_node, end_node, path)
            # check if new_path value returned from recursive call of shortest_path is present
            if new_path:
                # check if shortest is still == None or if length of new_path is less than length of shortest, shortest = new_path
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest

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
    graph = {}
    graph["A"] = ["D"]
    graph["D"] = ["A", "B", "G", "H"]
    graph["G"] = ["D", "E"]
    graph["B"] = ["D", "F"]
    graph["E"] = ["F", "G", "I"]
    graph["H"] = ["D"]
    graph["C"] = []
    graph["F"] = ["B", "E"]
    graph["I"] = ["E"]

    # find the shortest path between node "A" and node "I"
    start_node = "A"
    end_node = "I"
    shortest_path_list = shortest_path(graph, start_node, end_node)
    print(f"the shortest path from node \"{start_node}\" to node \"{end_node}\" is:")
    print(shortest_path_list)

    # print blank line to console for easier reading of results
    print()

    # find the node with the most edges
    find_node_with_most_edges(graph)

    # find all isolated nodes
    isolated_nodes = []
    for key, value in graph.items():
        if len(value) == 0:
            isolated_nodes.append(key)
    print("\nIsolated Nodes:")
    print(isolated_nodes)
