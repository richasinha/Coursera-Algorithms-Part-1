import sys
filename = "algo6_2sum.txt"
numbers = [int(l) for l in open(filename)]
print len(numbers)
targets = range(0,20001)
H = {}
answers = []
print len(numbers)
for i in numbers:
  H[i] = True
 
for i in numbers:
  for t in targets:
    if t - i in H:
      if i == t - i:
        continue
      if t not in answers:
        answers.append(t)


        #answers[t] = set([tuple(sorted([i, t - i]))])
      #else:
        #answers[t].add(tuple(sorted([i, t - i])))
 
print len(answers) 