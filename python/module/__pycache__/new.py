i=input(':')
a=i
b=0
c=0
while True:
    b=i%10
    c=c*10+b
    i=i//10
if(a==c):
    print('The number is palindrome')
else:
    print('The number is not palindrome')
