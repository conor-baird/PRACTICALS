from Guitar import Guitar

print("My Guitars")
name = input(":")
year = input(":")
cost = input(":")

print("{}, ({}) : ${} added".format(name, year, cost))

name = Guitar(name, year, cost)
guitars =[]
guitars.append(name)

