from flask import Flask
import ghhops_server as hs

import cv2

#notice, we import another file as a library
import geometry as geo

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/moreRandomPoints",
    name = "More Random Points",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Z range of randomness", "Z", "Maximum randomness in Z directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("tol range of tolerance", "T", "Range of tolerance T", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
       #hs.HopsPoint("Random Points","RP","List of generated random points ", hs.HopsParamAccess.LIST)
        hs.HopsPoint("Random Spheres", "RP","List of spheres", hs.HopsParamAccess.LIST),
        hs.HopsPoint("Random Pts", "RPts","List of points", hs.HopsParamAccess.LIST),
        hs.HopsCurve("Random Cvs", "Cvs","List of curves", hs.HopsParamAccess.LIST),
        hs.HopsPoint("Points At", "PtsAt","List of points_at", hs.HopsParamAccess.LIST),
        hs.HopsBrep("S_sph", "Sph","List Sph", hs.HopsParamAccess.LIST),
    ]
)
def moreRandomPoints(count, rX, rY, rZ, T):

    randomSpheres = geo.createRandomPoints(count, rX, rY, rZ, T)

    return randomSpheres


if __name__== "__main__":
    app.run(debug=True)