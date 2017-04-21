from car import Car
from progamming_language import Language

# def main():
#      bus = Car(180)
#      bus.drive(30)
#      print("fuel =", bus.fuel)
#      print("odo =", bus.odometer)
#      print(bus)
# main()


# def main():
#     limo = Car(100)
#     # limo.name("car")
#     limo.add_fuel(20)
#     print("fuel =", limo.fuel)
#     limo.drive(115)
#     print("odo =", limo.odometer)
#     print(limo)
#
#
# main()

def main():
    ruby = Language("Ruby", "Dynamic", True, 1995)
    python = Language("Python", "Dynamic", True, 1991)
    vb = Language("Visual Basic", "Static", False, 1991)
    languages = [ruby, python, vb]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic() == True:
            print(language.name)
    print(vb.is_dynamic())
main()