import sys

N = int(sys.argv[1])

with open("hightemp.txt") as f:
    lines = f.readlines()
    p = len(lines) // N
    for n in range(N):
        b = p * n
        e = p * n + p if n < N else N
        with open("devide{}".format(n), "w")as fo:
            for l in lines[b:e]:
                fo.write(l)
