from time import ctime
print(ctime())
c = ctime().split(" ")[4].split(":")
print(c)
if c[0] == "09" and c[1] == "37":
    print(ctime())