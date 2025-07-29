
liststack=[7,8,9]
print(liststack)

liststack.append(10)
print(liststack)

liststack.append(3)
print(liststack)

liststack.pop()
print(liststack)

#List Queue
from collections import deque

queue=deque(["apple","orange","kiwi"])
print(queue)

queue.append("banana")
print(queue)

queue.popleft()
print(queue)

#del
a=[1,2,3,4,5,6,7,8,9]
print(a)

del a[6]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

del(a)
print(a)


