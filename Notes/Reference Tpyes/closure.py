def a(x):
    def b(y):
        print(x,y)
    return b
xy=a(10)
xy(20)
xy(5)
xy(6)
