
i=int(input('Enter a number:'))
a=i
b=0
c=0
while i>0:
    b=i%10
    c=c*10+b
    i=i//10
if(a==c):
    print('palindrome number')
else:
    print('not a palindrome number')


