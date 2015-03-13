import random
r = random.Random()
EdgesOfGraph = []
CompleteNodeList = set()
#### Loading of the Graph from the file ####
for l in open('kargerAdj.txt'):
    x = l.strip().split()
    CompleteNodeList.add(x[0])
    for b in x[1:]:
        EdgesOfGraph.append([x[0],b]) #the number of edges
        CompleteNodeList.add(b)           #total nodes of graph
##########################################

ans = 300000
for t in xrange(len(CompleteNodeList)**2): ##### N^2.log N iteration
    G=EdgesOfGraph
    N=set(CompleteNodeList)
    while len(N)!=2: ### continue until TWO nodes remain
        #print len(N)
        NG = []
        a,b = G[r.randint(0,len(G)-1)] ### choose random edge.. call it a-b. We will rename b as a from hereon
        for c,d in G:
            if c==b: c=a  # renaming b to a
            if d==b: d=a # renaming b to a
            if c==d: continue # self edges ignored
            NG.append([c,d]) # other edges will be considered for next iteration
        N.remove(b) # We can safely remove b, as b is collapsed into a
        G = NG

    ans = min(ans,len(G)/2)
    print [t,len(G)/2,ans]
    