# Step 0:
# install the package networkx
# !pip install networkx

# Step 1: import the package
import networkx as networkx
#import matplotlib.pyplot as plt
from matplotlib import pyplot

# Step 2: open the graph from file or create one

# Create an example graph:
G = networkx.dodecahedral_graph()
#
#G = networkx.gnm_random_graph(20, 40)
G.nodes
G.edges


# Step 3: Choose the Positions of nodes
# Basic choice: random function -assigning random positions to the nodes
#nodes_position=networkx.random_layout(G)
# Other algorithm to position the nodes on the plane:
nodes_position = networkx.spring_layout(G)
#nodes_position=networkx.circular_layout(G)
# see here for more layouts: https://networkx.github.io/documentation/stable/reference/drawing.html

# Step 4: the plot
pyplot.figure();

networkx.draw(G, pos=nodes_position, node_color = 'r')  # use spring layout