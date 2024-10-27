'''
Q3:Using the graph data structure in Python to calculate the degree of a given protein
Author: Dinuri Lokuwalpola
date: 25/11/2022
'''

import networkx as nx
#Open the tsv file
with open ("DREB1A.tsv",'r') as file1:
    #create a graph
    pn = nx.Graph()
    for line in file1:
        # print(repr(line.strip()))
        lines = line.strip()
        if lines != "\n":
            if "#" != lines[0]:
                lines =lines.split("\t")
                #add edges to the graph
                pn.add_edge(lines[0], lines[1], weight= lines[-1])
                nx.write_gml(pn,"protein_network")

# get the degree of DREB1A protein
print(pn.degree("ERF24"))


count = 0
#get all neighbour proteins of DREB1A
neighbour = pn.neighbors("ERF24")

for protein in neighbour:
    #increment count by 1 if weight of neighbour > 0.7
    if pn.edges[("ERF24", protein)]['weight'] > str(0.7):
        count +=1

print(count)






