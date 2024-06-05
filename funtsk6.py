# factusingfunction
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print(fact(5))
# fibo
def fib(num):
    a=0
    b=1
    i=0
    while i<n:
        print(a,end=" , ")
        c=a+b
        a=b
        b=c
        i+=1
n=int(input("enter the limit:"))
fibon=fib(n)
print(fib)
# sumofn
def sum(n):
    t=0
    for i in range(1,n+1):
        t+=i
    return t
n=int(input("enter a no:"))
print(sum(n))
# sumofsquare
def sumofsq(n1):
    return(n1*(n1+1)*(2*n1+1)//6)
n=int(input("enter the number"))
print(sumofsq(n))
# pattern*
l=int(input("enter a limit:"))
for i in range(l):
    for j in range(l-i-1):
        print(" ", end='')
    for j in range(i+1):
        print("*", end=' ')
    print()