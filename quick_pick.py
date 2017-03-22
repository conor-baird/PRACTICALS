import random

num_picks = int(input("How many quick picks?: "))
numbers = random.randint(1,45)
row = []
count = 0

for i in range(1, num_picks + 1):
    while count < 6:
        row.append(numbers)
    print(row)
