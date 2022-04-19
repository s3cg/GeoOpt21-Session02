from pickle import LIST
from typing import List
from cv2 import add
from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo
import networkx as nx


app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/createGraph",
    name = "Create Graph",
    inputs=[
        hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST),
        hs.HopsPoint("Nodes", "N", "List of Nodes", hs.HopsParamAccess.LIST),


    ],
    outputs=[
       
       hs.HopsCurve("Edges","Edges","List of Edges_output ", hs.HopsParamAccess.LIST),
       hs.HopsPoint("Nodes", "Nodes", "List of Nodes_output", hs.HopsParamAccess.LIST),
       hs.HopsString("Nodes_t", "Nodes_t", "List of Nodes_output_t", hs.HopsParamAccess.LIST),
       hs.HopsString("B_cent", "B_centt", "Highest between centrality node", hs.HopsParamAccess.LIST),
       hs.HopsString("D", "D", "Degrees", hs.HopsParamAccess.LIST),
       hs.HopsString("D_Cent", "D_Centrality", "Degrees Centrality", hs.HopsParamAccess.LIST),
       hs.HopsString("E_Weight", "E_weights", "Weight of the edge", hs.HopsParamAccess.LIST)
    ]
)
def createGraph(E, N):

    

    t = len(N)


    P_graph = geo.createPathGraph(t)

    P_graphx_nodes = geo.getNodes(P_graph)
    P_graphx_edges = geo.getEdges(P_graph)

    P_highes_node_cent = geo.highest_bet_cent(P_graph)
    P_hnc = next(iter(P_highes_node_cent))

    #print(P_hnc)


    d = [len(list(P_graph.neighbors(n))) for n in P_graph.nodes]
    #print(d)
    

    d_centr = nx.degree_centrality(P_graph)
    d_centr_val = list(d_centr.values())

    random_w = geo.addRandomWeigrhs(P_graph)
    
    rw = []
    
    for w, v, d in random_w.edges(data=True):
        #print(random_w[w][v]['weight'])

        rw.append(d)


    

    return E, N, t, P_hnc, d, d_centr_val, rw





if __name__== "__main__":
    app.run(debug=True)