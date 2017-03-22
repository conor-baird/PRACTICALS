

numbers = []
count = 0

while count < 5:
    input_numbers = int(input("Number: "))
    numbers.append(input_numbers)
    count += 1

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}.".format(sum(numbers)/len(numbers)))


