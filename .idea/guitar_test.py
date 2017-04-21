from Guitar import Guitar
name = "Gibson L-5 CES"
year = 1922
cost = 16035.4
gibson =  Guitar(name, year, cost)

if (2017-year) > 50:
    vintage = True
else:
    vintage = False

print("Expected {} , got {}".format((2017-year), gibson.get_age()))
print("Expected {} , got {}".format(vintage, gibson.is_vintage()))