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
        hs.HopsInteger("Count X", "X", "Number of node in X", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Count Y", "Y", "Number of node in Y", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Layout", "L", "Layout to order Nodes", hs.HopsParamAccess.ITEM, default= 0),
        hs.HopsInteger("Size", "S", "Size cliques", hs.HopsParamAccess.ITEM, default= 2),


    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST),
       hs.HopsNumber("Degrees","D","List of Degrees ", hs.HopsParamAccess.LIST),
       hs.HopsNumber("Degrees_values","D_val","List of Degrees_values ", hs.HopsParamAccess.LIST),
       hs.HopsNumber("Betweennes_centrality","B_centrality","Betweenness centrality", hs.HopsParamAccess.LIST)
    ]
)
def createGraph(X, Y, layout, S):

    G = geo.createGridGraph(X, Y)
    GW = geo.addRandomWeigrhs(G)

    nodes = geo.getNodes(GW, layout)
    edges = geo.getEdges(GW, layout)

    d = [len(list(GW.neighbors(n))) for n in GW.nodes]
    #print(type(d[0]))

    d_centr = nx.degree_centrality(GW)
    d_centr_val = list(d_centr.values())

    #highest node betweenes cent
    highest_n = geo.highest_bet_cent(GW)

    h = next(iter(highest_n))
    print(list(h))

    #print(type(highest_n), highest_n)    

    #h_a = highest_n[0]
    #print(h_a)

    max_cliques = geo.maximal_cliques(GW, S)

    #print(max_cliques)
    

    #print(n_betweennes_cent)
    #print(d_centr)


    


    

    



    #print(G)

    return nodes, edges, d, d_centr_val, h





if __name__== "__main__":
    app.run(debug=True)