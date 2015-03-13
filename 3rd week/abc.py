data = "kargerAdj.txt"

Graph = {}
i = 0
if data:
	with open(data,'r') as my_file:
		all_line = my_file.readlines()
		for line in all_line:
			lst = []
			nodes = line.split()
			for adj_node in nodes[1:]:
				lst.append(adj_node)
			i = i + 1
			Graph[i] = lst


print Graph

#def kargerStep(G):
#    v1,v2= chooseRandomEdge(G)
    #1. attach v2's list to v1
    G[v1].extend(G[v2])
    #2. replace all appearance of v2 as v1
    for x in G[v2]:
        lst=G[x]
        for i in range(0,len(lst)):
            if lst[i]==v2: lst[i]=v1        
    #3.remove self-loop
    while v1 in G[v1]:
        G[v1].remove(v1)
    #4. remove v2's list
    del G[v2]

def karger(G): 
    while len(G)>2:
        kargerStep(G)
    return len(G[G.keys()[0]])

for x in G[v2]:
        nst=G[x]
        for i in range(0,len(lst)):
            if nst[i]==v2: nst[i]=v1        
    #3.remove self-loop
    while v1 in G[v1]:
        G[v1].remove(v1)
    #4. remove v2's list
    del G[v2]
