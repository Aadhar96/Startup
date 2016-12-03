import networkx as n
import matplotlib.pyplot as p
from matplotlib.patches import *

def d(G,pos,ax,sg=None):

    for n in G:
        c=Circle(pos[n],radius=0.02,alpha=0.5)
        axis.add_patch(c)
        G.node[n]['attr']=c
        x,y=pos[n]

    for (u,v,d) in G.edges(data=True):
        n1=G.node[u]['attr']
        n2=G.node[v]['attr']
        rad=0.1
        
        alpha=0.5
        color='#009900'

        e = FancyArrowPatch(n1.center,n2.center,patchA=n1,patchB=n2,
                            arrowstyle='wedge',
                            connectionstyle='arc3,rad=%s'%rad,
                            mutation_scale=10.0,
                            lw=2,
                            alpha=alpha,
                            color=color)

        axis.add_patch(e)
    return e


G=n.Graph([(1,2),(1,3),(2,3)])

pos=n.krackhardt_kite_graph(G)
axis=p.gca()
d(G,pos,axis)
axis.autoscale()
p.axis('equal')
p.axis('off')
p.show()
