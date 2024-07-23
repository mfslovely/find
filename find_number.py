import random

user = int(input("guess a no. between 1 to 10: "))
num = random.randint(1,10)

if num == user:
    print(f"congratulation you win {num}")

else:
    print(f"you failed no. is {num}")

print(" better luck next time")


