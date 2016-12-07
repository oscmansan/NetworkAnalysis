#!/usr/bin/python
from igraph import Graph
from igraph import plot
import matplotlib.pyplot as plt

n = 1000

def average_shortest_path(g):
	d = g.shortest_paths()
	d = reduce(lambda x,y: x+y, d, []) # flatten distances matrix
	d = filter(lambda x: x != float('Inf'), d) # remove Inf values
	l = sum(d)/float(n*(n-1))
	return l

x = []
y1 = []
y2 = []

p = 0.0001;
while p <= 1:
	g = Graph.Watts_Strogatz(1,n,2,p)
	c = g.transitivity_undirected()
	l = average_shortest_path(g)
	#l = g.diameter(directed=False)
	x.append(p)
	y1.append(c)
	y2.append(l)
	print '{:8f}{:10f}{:12f}'.format(p, c, l)
	p *= 1.5;

y1 = map(lambda x: x/y1[0],y1) # normalize
y2 = map(lambda x: x/y2[0],y2) # normalize

plt.plot(x,y1,'ro', label='clustering coefficient')
plt.plot(x,y2,'bo', label='average shortest-path')
plt.xscale('log')
plt.legend(loc=0,fontsize=8,numpoints=1)
plt.show()