import random
r = random.Random()
OG = []
ON = set()
#### Loading of the Graph from the file ####
for l in open('kargerAdj.txt'):
    x = l.strip().split()
    ON.add(x[0])
    for b in x[1:]:
        OG.append([x[0],b])
        ON.add(b)

print OG
print ON