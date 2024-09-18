# 72 The following dictionary shows how five people follow each other on Instagram:
#  instagram = {'person1': [0,1,1,0,1], 'person2': [0,0,1,0,1], 'person3': [1,1,0,1,1],'person4': [1,1,1,0,0], 'person5': [1,1,0,0,0]}
#  E.g., the list for person1 has the value on index 2 as 1 which means person1 followsperson3 and a directed edge should be added from 
# person1 to person3.
#  Using networkx library, create a directed graph.

import networkx as nx
import matplotlib.pyplot as plt

instagram = {'person1': [0,1,1,0,1], 
             'person2': [0,0,1,0,1], 
             'person3': [1,1,0,1,1],
             'person4': [1,1,1,0,0], 
             'person5': [1,1,0,0,0]}
# Create a directed graph
G = nx.DiGraph()
# Add nodes
for person in instagram.keys():
    G.add_node(person)
# Add edges
for follower, follows in instagram.items():
    for i, follow in enumerate(follows):
        if follow == 1:
            G.add_edge(follower, f'person{i+1}')
# Visualize the graph
nx.draw(G,with_labels=True, node_size=700, node_color='skyblue', font_size=10, arrows=True)
plt.title('Instagram Follow Relationships')
plt.show()


