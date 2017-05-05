from taxi import SilverServiceTaxi

new_taxi = ("Prius 1", 100)

# taxi = Taxi("Prius 1", 100)
# taxi.drive(40)
# print(taxi)
# print(taxi.get_fare())
# taxi.start_fare()
# taxi.drive(100)
# print(taxi)
# print(taxi.get_fare())

silver_taxi = SilverServiceTaxi("Prius1", 100, 2)
silver_taxi.drive(10)
print(silver_taxi.get_fare())
print(silver_taxi)