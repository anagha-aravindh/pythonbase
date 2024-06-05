# positiveornegativeno
x=int(input("Enter a no:"))
if x>0:
    print("x is positive number")
elif x==0:
    print("x is zero")
else:
    print("x is negative number")
# even or odd
y=int(input("Enter a no:"))
if y%2==0:
    print("y is even no")
else:

    print("y is odd no")
# calculator
x=int(input("Enter first no:"))
y=int(input("Enter second no:"))
z=input("Enter a operator:")
if z=='+':
    sum=x+y
    print(sum)
elif z=='-':
    dif=x-y
    print(dif)
elif z=='*':
    mul=x*y
    print(mul)
elif z=='/':
    div=x/y
    print(div)
else :
    print("invalid operator")
# factorial
n=int(input("enter a number:"))
fact=1
while(n>1):
    fact=fact*n
    n=n-1
print(fact)
# fibonacci series
x=int(input("enter the number:"))
n1=0
n2=1
print("fibonacci series:")
for z in range(0,x):
    if z<=1:
        n3=z
    else:
        n3=n1+n2
        n1=n2
        n2=n3
    print(n3,end='')
    
    