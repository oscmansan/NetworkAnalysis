#!/usr/bin/python
from igraph import Graph
from igraph import plot
import matplotlib.pyplot as plt

n = 750

def sumWoutInf(l):
	s = 0
	for v in l:
		if v != float('Inf'): 
			s += v
	return s


def average_shortest_path(g):
	d = g.shortest_paths(g.vs, g.vs)
	d = reduce(lambda x,y: x+y, d, [])
	x = float(sumWoutInf(d))/float(n*(n-1))
	print x
	return x

x = []
y1 = []
y2 = []

p = 0.0001;
while p <= 1:
	g = Graph.Watts_Strogatz(1,n,2,p)
	c = g.transitivity_undirected()
	l = average_shortest_path(g)
	x.append(p)
	y1.append(c)
	y2.append(l)
	p *= 1.5;

y1 = map(lambda x: x/y1[0],y1)
y2 = map(lambda x: x/y2[0],y2)

for xe, ye in zip(x, zip(y1,y2)):
	plt.scatter([xe] * len(ye), ye)

plt.xscale('log')
plt.show()