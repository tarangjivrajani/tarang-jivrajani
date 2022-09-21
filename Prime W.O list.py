n = int(input("enter N : "))
if n > 2:
    for i in range(3, int(n), 2):

        if n % i == 0:
            print(n, " is not prime")
            break

    else:
        print(n, " is prime")
