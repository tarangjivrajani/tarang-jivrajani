#fibonacci

n = int(input("enter the N: "))
a,b = 0,1
while b<n:
    print(b)
    a,b = b,a+b
