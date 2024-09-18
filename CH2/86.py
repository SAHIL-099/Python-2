# You have been hired by an Airlines company to analyze their routes. The company has provided you following data.
# Your task is to create a NetworkX directed graph representing the routes and display it.
# Figure size should be (15,15), node color should be green, take appropriate node size, edge color should be red.
# Data:
# Kolkata to Mumbai 
# Mumbai to Pune 
# Mumbai to Goa
# Kolkata to Delhi 
# Kolkata to Bhubaneshwar 
# Mumbai to Delhi 
# Delhi to Chandigarh 
# Delhi to Surat 
# Kolkata to Hyderabad 
# Hyderabad to Chennai 
# Chennai to Thiruvananthapuram 
# Thiruvananthapuram to Hyderabad 
# Kolkata to Varanasi 
# Delhi to Varanasi 
# Mumbai to Bangalore 
# Chennai to Bangalore 
# Hyderabad to Bangalore 
# Kolkata to Guwahati 

import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()
g.add_edges_from([("Kolkata", "Mumbai"), ("Mumbai", "Pune"), ("Mumbai", "Goa"),
("Kolkata", "Delhi"), ("Kolkata", "Bhubaneshwar"), ("Mumbai", "Delhi"),
("Delhi", "Chandigarh"), ("Delhi", "Surat"), ("Kolkata", "Hyderabad"),
("Hyderabad", "Chennai"), ("Chennai", "Thiruvananthapuram"),
("Thiruvananthapuram", "Hyderabad"), ("Kolkata", "Varanasi"),
("Delhi", "Varanasi"), ("Mumbai", "Bangalore"), ("Chennai", "Bangalore"),
("Hyderabad", "Bangalore")])

plt.figure(figsize=(15,15))
nx.draw(g,node_size=1000,with_labels=True,node_color="green",edge_color="red")
plt.show()