'''def add(a,b):
    return a+b
print(add(12,25))
a=add(12,2)
print(a*12)

add=lambda a,b:a+b
print(add(12,2))

'''

a=[1,2,3,4,5]
m=map(lambda x:x*5,a)
print(list(m))

f=filter(lambda x:x%2==0,a)
print(list(f))

n=filter(lambda x:x%2==1,a)
print(list(n))

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(6))











