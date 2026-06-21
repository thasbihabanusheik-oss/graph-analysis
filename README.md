Task 1: Graph Data Analysis

Course/Subject: Data Science
Task: Graph Data Analysis using Python

Objective

The objective of this task is to perform graph data analysis using Python, applying core graph theory concepts to understand the structure and properties of a network. This includes graph construction, computation of structural metrics, centrality analysis, and visualization.

Tools & Libraries Used

LibraryPurposenetworkxGraph creation and graph-theoretic computationsmatplotlibVisualizing the graph

Concepts Covered


Graph Construction – Building a graph from a set of nodes and edges
Basic Graph Properties – Number of nodes, edges, density, and connectivity check
Degree Analysis – Degree of each node and average degree of the graph
Centrality Measures

Degree Centrality
Closeness Centrality
Betweenness Centrality



Connected Components – Identifying groups of connected nodes
Shortest Path Analysis – Finding the shortest path between two nodes
Graph Visualization – Plotting the graph with node sizes scaled by centrality


How to Run


Install the required libraries:


bash   pip install -r requirements.txt


Run the script:


bash   python graph_data_analysis.py


Output:

Console output showing all computed metrics
A saved image graph_visualization.png showing the graph





Output

==================================================
BASIC GRAPH PROPERTIES
==================================================
Number of nodes : 8
Number of edges : 10
Graph density   : 0.3571
Is connected?   : True

==================================================
DEGREE ANALYSIS
==================================================
Node B: degree = 3
Node C: degree = 3
Node D: degree = 3
Node E: degree = 3
Node G: degree = 3
Node A: degree = 2
Node F: degree = 2
Node H: degree = 1

Average degree: 2.50

==================================================
CENTRALITY ANALYSIS
==================================================
Node  Degree      Closeness   Betweenness 
A     0.286       0.350       0.000       
B     0.429       0.467       0.119       
C     0.429       0.467       0.119       
D     0.429       0.583       0.571       
E     0.429       0.583       0.571       
F     0.286       0.438       0.000       
G     0.429       0.467       0.286       
H     0.143       0.333       0.000       



Show Image

File Structure

Task1_Graph_Data_Analysis/
│
├── graph_data_analysis.py   # Main Python program
├── requirements.txt         # Required libraries
├── graph_visualization.png  # Output graph image
└── README.md                # Task documentation

Conclusion

This task demonstrates how Python's NetworkX library can be used to model real-world networks as graphs and extract meaningful insights such as the most influential nodes, the overall connectivity of the network, and shortest paths between entities — all of which are foundational techniques in graph-based data science applications such as social network analysis, recommendation systems, and fraud detection.
