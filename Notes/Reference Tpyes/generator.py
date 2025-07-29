def num():
    for i in range(0,11):
        yield i
m=num()
for x in m:
    print(x)

