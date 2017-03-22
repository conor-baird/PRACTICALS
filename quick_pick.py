import random
num_picks = int(input("How many quick picks?: "))
numbers = 6
for i in range(num_picks):
    row = []
    count = 0
    for i in range(numbers):
        row.append(random.randint(1,45))
        row = list(set(row))
        row = sorted(row, key=int)
    row = ' '.join(str(e) for e in row)
    print(row)
