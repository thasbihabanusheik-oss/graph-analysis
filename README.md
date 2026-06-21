GRAPH DATA ANALYSIS
====================

A Python program demonstrating core graph data analysis techniques using
NetworkX and Matplotlib - covering graph construction, structural metrics,
centrality measures, connected components, shortest paths, and visualization.


FEATURES
--------
- Build a graph from an edge list
- Compute basic properties: node/edge count, density, connectivity
- Degree analysis (per-node degree, average degree)
- Centrality measures: Degree, Closeness, Betweenness
- Connected components detection
- Shortest path computation between two nodes
- Graph visualization saved as a PNG image


REQUIREMENTS
------------
- Python 3.7+
- NetworkX
- Matplotlib


INSTALLATION
------------
1. Clone the repository:
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>

2. Install dependencies:
   pip install -r requirements.txt


USAGE
-----
Run the script:
   python graph_data_analysis.py

This will:
1. Build a sample graph
2. Print basic properties, degree stats, and centrality measures to console
3. Detect connected components
4. Find the shortest path between two sample nodes
5. Save a visualization as graph_visualization.png


CUSTOMIZING THE GRAPH
----------------------
To analyze your own data, edit the create_graph() function in
graph_data_analysis.py and replace the sample edge list with your own
edges, or load them from a CSV file using pandas:

    import pandas as pd

    def create_graph():
        G = nx.Graph()
        df = pd.read_csv("your_edges.csv")  # columns: source, target
        edges = list(zip(df["source"], df["target"]))
        G.add_edges_from(edges)
        return G


PROJECT STRUCTURE
------------------
graph-data-analysis/
|
|-- graph_data_analysis.py   - Main analysis script
|-- requirements.txt         - Python dependencies
|-- graph_visualization.png  - Sample output image
|-- README.txt               - Project documentation


LICENSE
-------
This project is open source and available under the MIT License.
