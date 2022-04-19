from numpy import size
import rhino3dm as rg
import networkx as nx
import random
from itertools import combinations

def createGridGraph(x, y):

    M = nx.grid_2d_graph(x,y)

    #print(M)
    return M

def addRandomWeigrhs(G):

    NG = nx.Graph()
    for u,v,data in G.edges(data=True):
        #print(u, v)
        #w = data['weight'] if 'weight' in data else 1.0
        w = random.randint(1,10)
        if NG.has_edge(u,v):
            NG[u][v]['weight'] += w
        else:
            NG.add_edge(u, v, weight=w)
    
    #degrees = [len(list(NG.neighbors(n))) for n in NG.nodes]
    
    #d_centr = nx.degree_centrality(NG)
    #d_cent_val = list(d_centr.values())

    #print(d_cent_val)
    
    #print(degrees)
        
    
    return NG

def getNodes(G, layout = 0):

    if layout == 1 : 
        lay =  nx.kamada_kawai_layout(G)
        #print('kamada_kawai_layout')
    
    elif layout == 2 : 
        lay =  nx.circular_layout(G)
        #print('circular_layout')
    
    elif layout == 3 : 
        lay =  nx.shell_layout(G)
        #print('shell_layout')
    
    elif layout == 4 : 
        lay =  nx.spiral_layout(G)
        #print('spiral_layout')
    
    elif layout == 5 : 
        lay = nx.spectral_layout(G)
        print('spectral_layout')

    elif layout == 6 : 
        lay = nx.spring_layout(G)
        #print('spring_layout')
    
    
    else: lay = nx.planar_layout(G)

    nodes = []
    for d in lay.values():
        pt = rg.Point3d( d[0], d[1] , 0)
        nodes.append(pt)
    


    return nodes


def highest_bet_cent(G):
    
    bet_cent = nx.betweenness_centrality(G)

    max_bc = max(list(bet_cent.values()))

    n = set()

    for k , v in bet_cent.items():

        if v == max_bc:

            n.add(k)

    return n

def maximal_cliques(G, size):

    mcs = []
    for clique in nx.find_cliques(G):
        if len(clique) == size:
            mcs.append(clique)
    
    return mcs


def getEdges(G, layout = 0):

    if layout == 1 : 
        lay =  nx.kamada_kawai_layout(G)
    
    elif layout == 2 : 
        lay =  nx.circular_layout(G)
    
    elif layout == 3 : 
        lay =  nx.shell_layout(G)
    
    elif layout == 4 : 
        lay =  nx.spiral_layout(G)
    
    elif layout == 5 : 
        lay = nx.spectral_layout(G)
    
    elif layout == 6 : 
        lay = nx.spring_layout(G)
    
    
    else: 
        lay = nx.planar_layout(G)


    edges = []
    for e in G.edges:
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


