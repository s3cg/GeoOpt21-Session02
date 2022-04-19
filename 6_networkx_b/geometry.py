
from cProfile import label
import rhino3dm as rg
import networkx as nx
import random
from itertools import combinations

def createGridGraph(x, y):

    M = nx.grid_2d_graph(x,y)

    #print(M)
    return M

def createPathGraph(Pl):
    Path_g = nx.path_graph(Pl, create_using = nx.DiGraph())

    return Path_g




def addRandomWeigrhs(P_graph):

    NG = nx.Graph()
    for u,v,data in P_graph.edges(data=True):
        #print(u, v)
        #w = data['weight'] if 'weight' in data else 1.0
        w = random.randint(1,10)
        if NG.has_edge(u,v):
            NG[u][v]['weight'] += w
        else:
            NG.add_edge(u, v, weight=w)

    
    return NG

def getNodes(P_graph):

    lay =  nx.planar_layout(P_graph)
    print('planar_layout')
    

    nodes = []
    for d in lay.values():
        pt = rg.Point3d( d[0], d[1] , 0)
        nodes.append(pt)
    
    return nodes


def setAtt(P_graph):

    lay =  nx.planar_layout(P_graph)
    print('planar_layout')

    att = []
    for d in lay.values():
        #pt = rg.Point3d( d[0], d[1] , 0)
        attributes_g = nx.set_node_attributes(P_graph, d, "labels" )

        att.append(attributes_g)
    print(att)
    
    return att


def highest_bet_cent(P_graph):
    
    bet_cent = nx.betweenness_centrality(P_graph)

    max_bc = max(list(bet_cent.values()))

    n = set()

    for k , v in bet_cent.items():

        if v == max_bc:

            n.add(k)

    return n




def getEdges(P_graph):

    lay =  nx.planar_layout(P_graph)
    print('planar_layout_edges')

    edges = []
    for e in P_graph.edges:
        p1 = rg.Point3d( lay[e[0]][0], lay[e[0]][1], 0 )
        p2 = rg.Point3d( lay[e[1]][0], lay[e[1]][1], 0 )
        line = rg.LineCurve(p1, p2)
        edges.append(line)
    


    return edges



"""
G = createGridGraph(3,3)
GW = addRandomWeigrhs(G)

nodes = getNodes(G)
edges = getEdges(G)
"""


