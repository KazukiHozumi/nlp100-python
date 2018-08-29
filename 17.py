s = {}

with open("hightemp.txt") as f:
    lines = f.readlines()
    for i, l in enumerate(lines):
        l = l.split("\t")
        s[l[0]] = i

import operator
r = sorted(s.keys(), key=operator.itemgetter(1))
for l in r:
    print(l)
