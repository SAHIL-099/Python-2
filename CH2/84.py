# You have been hired as a network analyst by a company to analyze the social network of their employees. The company has provided you with 
# the following data:
#  There are 5 employees in the company, each identified by a unique ID from 1 to 5.
#  The following relationships exist between the employees:
#  1. Employee 1 is friends with Employee 2 and Employee 3.
#  2. Employee 2 is friends with Employee 4.
#  3. Employee 3 is friends with Employee 5.
#  Your task is to create a NetworkX graph representing this social network and display it.

import networkx as nx
import matplotlib.pyplot as plt

g=nx.DiGraph()
g.add_nodes_from([1,2,3,4,5])
g.add_edges_from([(1,2),(2,3),(2,4),(3,5)])

nx.draw(g,node_color='red',edge_color='green',with_labels=True)
plt.show()