# finding that lines are matching or not in files

line1 = "log.txt"
line2 = "this.txt"

with open(line1) as f:
    f1 = f.read()

with open(line2) as f:
    f2= f.read()

if f1 == f2:
    print("Lines are identical... MATCH FOUND !! ")
else:
    print("LIines are not identical.. NO Match !! ")