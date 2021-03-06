'''
Created on Nov 10, 2016

@author: irma
'''
import graph.visualization as vis
import networkx as nx
import graph.graph_analyzer as an
import pickle

FILE_NAME = "/home/irma/workspace/some_scripts_martin_sampling/DATA/e_mail_enron/e_mail_enron.gpickle"
edges="/home/irma/workspace/some_scripts_martin_sampling/DATA/e_mail_enron/Email-Enron.txt"

edges_map={}
nodes={}
nr_edges=0
line_nr=0
 
node_id=0
with open(edges,'r') as f:
    for line in f.readlines():
        line_nr+=1
        edge1=int(line.split("\t")[0].rstrip())
        edge2=int(line.split("\t")[1].rstrip())
        if edge1 not in nodes:
            nodes[edge1]=node_id
            node_id+=1
        if edge2 not in nodes:
            nodes[edge2]=node_id
            node_id+=1
        if edge1 in edges_map.keys():
            edges_map[edge1].append(edge2)
            nr_edges+=1
        else:
            edges_map[edge1]=[edge2]
            nr_edges+=1
 

G=nx.Graph() 
for n in nodes.keys():
    G.add_node(nodes[n],id=nodes[n],predicate='user')
     
for e in edges_map.keys():
    for e1 in edges_map[e]:
      G.add_edge(nodes[e],nodes[e1])
 

pickle.dump(G, open(FILE_NAME,'wb'))

data=nx.read_gpickle(FILE_NAME)
number_of_pages=0
for node in data.nodes():
        if data.node[node]['predicate']=='page':
            number_of_pages+=1

vis.visualize_graph_standard(data)
      
