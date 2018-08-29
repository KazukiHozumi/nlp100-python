with open("hightemp.txt") as f:
    lines = f.readlines()
    r = []
    for l in lines:
        r.append(l.replace("\t", " "))
    for l in r:
        print(l[:-1])
