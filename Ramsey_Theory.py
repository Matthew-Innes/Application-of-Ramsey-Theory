
import networkx as nx
import matplotlib.pyplot as plt
import itertools

def create_colored_graph(n, edge_colors):
    """Create a complete graph with `n` vertices and color edges using `edge_colors`."""
    G = nx.complete_graph(n)
    color_map = {}
    
    for (u, v), color in edge_colors.items():
        color_map[(u, v)] = color
        color_map[(v, u)] = color  # Since the graph is undirected
    
    return G, color_map

def find_monochromatic_triangles(G, color_map):
    """Find all monochromatic triangles in the graph `G`."""
    monochromatic_triangles = []
    
    for triangle in itertools.combinations(G.nodes(), 3):
        u, v, w = triangle
        edges = [(u, v), (v, w), (w, u)]
        edge_colors = [color_map.get(edge) for edge in edges]
        
        if None not in edge_colors and len(set(edge_colors)) == 1:
            monochromatic_triangles.append(triangle)
    
    return monochromatic_triangles

def draw_graph(G, color_map, monochromatic_triangles):
    """Draw the graph and highlight monochromatic triangles."""
    pos = nx.spring_layout(G)
    edge_colors = [color_map.get(edge, 'black') for edge in G.edges()]
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color=edge_colors, node_size=700, font_size=16, font_weight='bold')
    
    for triangle in monochromatic_triangles:
        nx.draw_networkx_edges(G, pos, edgelist=[(triangle[i], triangle[j]) for i in range(3) for j in range(i+1, 3)], edge_color='red', width=2.5)
    
    plt.show()

# Example usage
n = 6
# Define edge colors (0 and 1 representing two colors)
edge_colors = {
    (0, 1): 'red', (0, 2): 'blue', (0, 3): 'red', (0, 4): 'blue', (0, 5): 'red',
    (1, 2): 'blue', (1, 3): 'red', (1, 4): 'blue', (1, 5): 'red',
    (2, 3): 'blue', (2, 4): 'red', (2, 5): 'blue',
    (3, 4): 'red', (3, 5): 'blue',
    (4, 5): 'red'
}

G, color_map = create_colored_graph(n, edge_colors)
monochromatic_triangles = find_monochromatic_triangles(G, color_map)
draw_graph(G, color_map, monochromatic_triangles)

print("Monochromatic triangles found:", monochromatic_triangles)