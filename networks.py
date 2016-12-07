#!/usr/bin/python
from igraph import Graph
from igraph import plot
import matplotlib.pyplot as plt
import cairo

def average_shortest_path(g):
	n = g.vcount()
	d = g.shortest_paths()
	d = reduce(lambda x,y: x+y, d, []) # flatten distances matrix
	d = filter(lambda x: x != float('Inf'), d) # remove Inf values
	l = sum(d)/float(n*(n-1))
	return l

def task1(n):
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

def task2_1():
	g = Graph(directed=False)
	g = g.Load('edges.txt', format='edgelist', directed=False)

	print '{} {}'.format('#edges:',g.ecount())
	print '{} {}'.format('#nodes:',g.vcount())
	print '{} {}'.format('diameter:',g.diameter())
	print '{} {:.3f}'.format('transitivity',g.transitivity_undirected())

	degrees = g.degree(g.vs)
	plt.hist(degrees,bins=g.maxdegree()); plt.title('degree distribution')
	plt.show(block=False)

	weigths = g.pagerank()
	g.vs['size'] = map(lambda x: x*1500, weigths)
	plot(g, layout=g.layout_lgl())

def task2_2():
	g = Graph(directed=False)
	g = g.Load('edges.txt', format='edgelist', directed=False)

	com = g.community_edge_betweenness()
	clust = com.as_clustering()
	print 'largest community size:', clust.giant().vcount()

	com_sizes = map(lambda s: s.vcount(),clust.subgraphs())
	plt.hist(com_sizes,bins=max(com_sizes)); plt.title('community size distribution')
	plt.show(block=False)

	plot(clust, layout = g.layout_kamada_kawai())




#task1(1000)
#task2_1()
task2_2()
