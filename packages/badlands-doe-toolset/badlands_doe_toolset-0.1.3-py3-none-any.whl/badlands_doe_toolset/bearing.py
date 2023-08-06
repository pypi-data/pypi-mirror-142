#bearing math
import badlands_doe_toolset.postproc_utils as ppu
import math
import numpy as np
import pandas as pd


#define the connection pairs from the input data
#connect pair
def flow_azi(conpair,ff):
    import math
    p1p=conpair[0][0]
    p2p=conpair[0][1]
    p1=ff.coords[p1p,0:3]
    p2=ff.coords[p2p,0:3]
    x1=p1[0]
    y1=p1[1]
    z1=p1[2]
    x2=p2[0]
    y2=p2[1]
    z2=p2[2]
    azi=bearing(x1,y1,x2,y2)
#    dist=np.sqrt((x1-x2)**2+(y1-y2)**2) #+(z1-z2)**2)
#    slope=90-(math.degrees(np.arctan(z1-z2/dist)))
    return azi#+180 #+180 to azimuth to adjust bearing calc
    #return p1p, (azi+180), dist, slope #+180 to azimuth to adjust bearing calc
#bearing between 2 points
def bearing(x1,y1,x2,y2):
    import math
    dx = x1-x2
    dy = y1-y2
    if dx > 0:
        bearing = 90 - np.degrees(np.arctan(dy/dx))
    elif dx < 0:
        bearing = 270 - np.degrees(np.arctan(dy/dx))
    elif dx == 0:
        if dy > 0:
            bearing = 0
        elif dy < 0 :
            bearing = 180
        else :
            bearing=-9999 # so there's no error on a duplicate point
    return bearing

def bearing_flow(flowhdf):

    ff=ppu.Flowfile()
    ff.loadFlow(flowhdf)

    connect_all=[]
    for i in range(0,len(ff.coords)):
        connect_all.append(ff.connect[np.where(ff.connect[:,0]==i)])
        
        
    azi_list=[]
    for i in range(len(connect_all)):
        if len(connect_all[i])==0:
            a=-9999
        else:
            a=flow_azi(connect_all[i].tolist(),ff)
        azi_list.append(a) 
    return azi_list
    

    