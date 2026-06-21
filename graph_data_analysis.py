"""
Task 1: Graph Data Analysis
----------------------------
This program demonstrates fundamental graph data analysis techniques using
the NetworkX library:
  1. Creating a graph from data
  2. Basic graph properties (nodes, edges, density)
  3. Degree analysis
  4. Centrality measures (Degree, Closeness, Betweenness)
  5. Connected components
  6. Shortest path analysis
  7. Visualization

Requirements:
  pip install networkx matplotlib
"""

import networkx as nx
import matplotlib.pyplot as plt


def create_graph():
    """Create a sample graph. Replace edges with your own dataset."""
    G = nx.Graph()

    # Sample edge list: (node1, node2)
    edges = [
        ('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'),
        ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G'),
        ('E', 'G'), ('G', 'H')
    ]

    G.add_edges_from(edges)
    return G


def basic_properties(G):
    """Print basic structural information about the graph."""
    print("=" * 50)
    print("BASIC GRAPH PROPERTIES")
    print("=" * 50)
    print(f"Number of nodes : {G.number_of_nodes()}")
    print(f"Number of edges : {G.number_of_edges()}")
    print(f"Graph density   : {nx.density(G):.4f}")
    print(f"Is connected?   : {nx.is_connected(G)}")
    print()


def degree_analysis(G):
    """Analyze node degrees."""
    print("=" * 50)
    print("DEGREE ANALYSIS")
    print("=" * 50)
    degrees = dict(G.degree())
    for node, deg in sorted(degrees.items(), key=lambda x: -x[1]):
        print(f"Node {node}: degree = {deg}")

    avg_degree = sum(degrees.values()) / G.number_of_nodes()
    print(f"\nAverage degree: {avg_degree:.2f}")
    print()
    return degrees


def centrality_analysis(G):
    """Compute and display common centrality measures."""
    print("=" * 50)
    print("CENTRALITY ANALYSIS")
    print("=" * 50)

    degree_cent = nx.degree_centrality(G)
    closeness_cent = nx.closeness_centrality(G)
    betweenness_cent = nx.betweenness_centrality(G)

    print(f"{'Node':<6}{'Degree':<12}{'Closeness':<12}{'Betweenness':<12}")
    for node in G.nodes():
        print(f"{node:<6}{degree_cent[node]:<12.3f}"
              f"{closeness_cent[node]:<12.3f}{betweenness_cent[node]:<12.3f}")
    print()

    return degree_cent, closeness_cent, betweenness_cent


def connected_components_analysis(G):
    """Find and display connected components."""
    print("=" * 50)
    print("CONNECTED COMPONENTS")
    print("=" * 50)
    components = list(nx.connected_components(G))
    print(f"Number of connected components: {len(components)}")
    for i, comp in enumerate(components, start=1):
        print(f"Component {i}: {comp}")
    print()


def shortest_path_analysis(G, source, target):
    """Find the shortest path between two nodes."""
    print("=" * 50)
    print("SHORTEST PATH ANALYSIS")
    print("=" * 50)
    if nx.has_path(G, source, target):
        path = nx.shortest_path(G, source=source, target=target)
        length = nx.shortest_path_length(G, source=source, target=target)
        print(f"Shortest path from {source} to {target}: {path}")
        print(f"Path length: {length}")
    else:
        print(f"No path exists between {source} and {target}")
    print()


def visualize_graph(G, degree_cent):
    """Visualize the graph, scaling node size by degree centrality."""
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)

    node_sizes = [3000 * degree_cent[node] + 300 for node in G.nodes()]

    nx.draw(
        G, pos,
        with_labels=True,
        node_color='skyblue',
        node_size=node_sizes,
        edge_color='gray',
        font_size=10,
        font_weight='bold'
    )

    plt.title("Graph Data Analysis Visualization")
    plt.savefig("graph_visualization.png", dpi=150, bbox_inches='tight')
    print("Graph visualization saved as 'graph_visualization.png'")
    plt.close()


def main():
    G = create_graph()

    basic_properties(G)
    degrees = degree_analysis(G)
    degree_cent, closeness_cent, betweenness_cent = centrality_analysis(G)
    connected_components_analysis(G)
    shortest_path_analysis(G, 'A', 'H')
    visualize_graph(G, degree_cent)

    # Identify most influential node by each measure
    print("=" * 50)
    print("SUMMARY: MOST INFLUENTIAL NODES")
    print("=" * 50)
    print(f"Highest Degree centrality     : {max(degree_cent, key=degree_cent.get)}")
    print(f"Highest Closeness centrality  : {max(closeness_cent, key=closeness_cent.get)}")
    print(f"Highest Betweenness centrality: {max(betweenness_cent, key=betweenness_cent.get)}")


if __name__ == "__main__":
    main()
