import random,copy
data = "demo.txt"

G = {}
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
            G[i] = lst
print G

def chooseRandomEdge(G):
    v1= random.randint(1,len(G))
    while v1 not in G:
        v1 = random.randint(1,len(G))
    v2= random.randint(1,len(G))
    while ((v1 == v2) or (v2 not in G[v1])): #All restrictions on v2 implemented
        v2=random.randint(1,len(G))
    print v1,v2
    return v1, v2

def kargerStep(G):
    v1,v2 = chooseRandomEdge(G)
    print v1,v2
    if v2 not in G:
        print 'v2 nahi hai'
    else:
        print 'v2 mila re baba'
    G[v1].extend(G[v2])
    while v1 in G[v1]:
        G[v1].remove(v1)
    while v2 in G[v1]:
        G[v1].remove(v2)
    del G[v2]


def karger(G):
    while len(G) > 2:
        kargerStep(G)
    return len(G[G.keys()[0]])
    
minimum_val=karger(copy.deepcopy(G))
for i in range(0,1000): # run many tests
    instance=karger(copy.deepcopy(G))
    if instance<minimum_val:
        minimum_val=instance
print minimum_val
