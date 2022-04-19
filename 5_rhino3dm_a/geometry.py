#we import all the libraries that our functions need here too
import random as r
#from matplotlib.pyplot import gray
import rhino3dm as rg
import cv2
import numpy as np

def createRandomPoints(count,rX, rY, rZ, T):

    randomPts = []


    for i in range(count):

        #in each itereation generate some random points
        random_x = r.uniform(-rX, rX)
        random_y = r.uniform(-rY, rY)
        random_z = r.uniform(-rZ, rZ)
        

        #print(random_x, random_y, random_z)

        #create a point with rhino3dm
        random_pt = rg.Point3d(random_x, random_y, random_z)

        #l_rpts = [random_pt]

        #print(type(l_rpts))

        randomPts.append(random_pt)
    
    pt_a = randomPts[0]
    pt_b  = randomPts[-1]
    #print(pt_a, pt_b)

    b_b = rg.BoundingBox(pt_a, pt_b)
    bb_c = b_b.Center

    lns = []
    points_at = []

    sphr = []

    for pts in randomPts:
        curves_ln = rg.LineCurve(bb_c, pts)
        #print(type(curves_ln))
        lns.append(curves_ln)

        #print(curves_ln.Line.Length)

        Tol_c = curves_ln.Line.Length * T

        #print(Tol_c)


        pts_at = curves_ln.PointAt(Tol_c)

        #poly = rg.Polyline(pts_at)

        sph = rg.Sphere(pts_at, 1.0)

        sph_a = rg.Sphere.ToBrep(sph)

        sphr.append(sph_a)


        points_at.append(pts_at)



        

    #print(type(randomPts))

    #print(type(lns))



    return bb_c, randomPts, lns, points_at, sphr


