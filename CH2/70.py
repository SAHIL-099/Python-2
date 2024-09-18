# 70 .Write a python program which creates following graph using networkx module in python


import networkx as nx
import matplotlib.pyplot as plt
graph = nx.DiGraph()
graph.add_edges_from([("A","B"),("B","C"),("B","D"),("C","D"),("D","A")])
nx.draw(graph,with_labels=True)
plt.show()