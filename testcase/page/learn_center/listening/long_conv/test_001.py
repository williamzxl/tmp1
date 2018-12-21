# for i, j in zip(range(3),["a","b","c"]):
#     print(i,j)

a = [1,2,3]
def test(a):
    print(a)
    return a

b = test(a)
print(type(b))
for i in b:
    print(i)