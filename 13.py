with open("col1.txt") as f1:
    with open("col2.txt") as f2:
        line1 = f1.readlines()
        line2 = f2.readlines()

with open("marge.txt", "w") as f3:
    for col1, col2 in zip(line1, line2):
        f3.write("\t".join([col1.rstrip(), col2]))
