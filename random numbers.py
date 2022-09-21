# import random numbers:
# guessing number game
import random

num = random.randint(1, 25)
i = int(input("guess a number  : "))
if i < num:
    print("computer guessing ", num)
    print("your guess is smaller")
elif i > num:
    print(num)
    print("your guess is greater")
else:
    print(num)
    print("your guess number is correct")
