
# python program to put even and odd element of list in two diff list
list = []  #create a dynamic list
n = int(input("enter a length of list"))
for i in range(1 ,n+1):
    x = int(input("enter the value :"))
    list.append(x)
    print(list)
list_even = [] #create a even list
list_odd = [] #create a odd list
for j in list:
    if (j%2==0):
        list_even.append(j)
    else:
        list_odd.append(j)
print("even number:" , list_even)
print("odd number:" , list_odd)


