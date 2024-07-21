*Ramsey Theory Monochromatic Triangles*

- This repository contains a Python script that visualizes and analyzes monochromatic triangles in a complete graph with colored edges. It demonstrates a basic application of Ramsey Theory by finding and highlighting monochromatic triangles in a graph with colored edges.

- The script generates a complete graph, colors its edges, and identifies monochromatic triangles (triangles where all edges have the same color). It then visualizes the graph and highlights these monochromatic triangles.

- To run the script, you need Python 3 and the following libraries:
     *networkx for graph manipulation
     *matplotlib for graph visualization
  
- You can install these libraries using pip:
     *pip install networkx matplotlib


*Code Overview*

- create_colored_graph(n, edge_colors):
     *Creates a complete graph with n vertices and colors its edges based on the edge_colors dictionary.
     *Parameters:
       n: Number of vertices.
       edge_colors: Dictionary mapping each edge (as a tuple of vertices) to a color.

- find_monochromatic_triangles(G, color_map):
     *Finds all monochromatic triangles in the given graph G.
     *Parameters:
       G: The graph object.
       color_map: Dictionary mapping edges to colors.
       Returns: A list of tuples representing the vertices of monochromatic triangles.

- draw_graph(G, color_map, monochromatic_triangles):
     *Draws the graph and highlights monochromatic triangles.
     *Parameters:
       G: The graph object.
       color_map: Dictionary mapping edges to colors.
       monochromatic_triangles: List of monochromatic triangles to be highlighted.
  

*Example Usage*

- The script includes an example configuration with 6 vertices and predefined edge colors. It demonstrates the process of creating the graph, finding monochromatic triangles, and visualizing the result.


*Running the Script*

- To execute the script, save it to a file (e.g., ramsey_theory.py) and run it using Python:
     python3 ramsey_theory.py

- The script will display the graph with nodes, colored edges, and highlighted monochromatic triangles.


*Customization*

- You can customize the number of vertices and edge colors by modifying the n and edge_colors variables in the script:
    n = 6
    edge_colors = {
    (0, 1): 'red', (0, 2): 'blue', (0, 3): 'red', (0, 4): 'blue', (0, 5): 'red',
    (1, 2): 'blue', (1, 3): 'red', (1, 4): 'blue', (1, 5): 'red',
    (2, 3): 'blue', (2, 4): 'red', (2, 5): 'blue',
    (3, 4): 'red', (3, 5): 'blue',
    (4, 5): 'red'
     }
  
- Modify the colors or add more edges to explore different configurations.
