def triangle_numbers():
	t = 0
	count = 0
	while True:
		count += 1
		t += count 
		yield t

def build_graph():
	triangle_gen = triangle_numbers()
	f = open("triangle67.txt", "r")
	l = f.readlines()
	nodes = []
	edges = []
	for i in l:
		split = i.split(' ')
		for j in split:
			nodes.append(int(j))
			
	#now edges
	curr_triangle = triangle_gen.next()
	level = 0
	
	for i in range(len(nodes)):
		if i == curr_triangle: #End of a level
			curr_triangle = triangle_gen.next()
			level += 1
		if (i + level + 1) < len(nodes):
			edges.append([i + level + 1, i + level + 2])
	
	return (nodes, edges)
			

def greatest_sum(nodes, edges):
	"""A variation on dijkstra's shortest path algorithm for greatest sum on a triangle."""
	dist = []
	for i in range(len(nodes)):
		dist.append(0)
		
	dist[0] = nodes[0]
	
	for i in range(len(nodes)):
		if i < len(edges):
			for j in edges[i]:
				curr_sum = dist[i] + nodes[j]
				if dist[j] < curr_sum:
					dist[j] = curr_sum
				
	greatest = max(dist)
	return greatest

	
	
	#for i in range(len(nodes)):
	#	print str(i) + str(edges[i])

nodes, edges = build_graph()
print greatest_sum(nodes, edges)