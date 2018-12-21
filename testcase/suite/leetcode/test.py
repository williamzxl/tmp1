# nums = [2, 7, 11, 15, 18]
# target = 9
l1 = [2, 4, 3]
l2 = []

str_l1 = ""
str_l2 = ""
for i in l1:
    str_l1 += str(i)
for j in l2:
    str_l2 += str(j)
r1 = int(str_l1) + int(str_l2)
r = []
for k in (str(r1)):
    r.append(int(k))
print(r[::-1])