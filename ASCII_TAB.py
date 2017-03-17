LOWER_LIMIT = 33
UPPER_LIMIT = 127


def main():

    character_test = str(input("Enter a character: "))
    char_ASCII = ord(character_test)
    print("The ASCII code for {} is : {}".format(character_test, char_ASCII))
    number = get_number(LOWER_LIMIT,UPPER_LIMIT)
    num_ASCII = chr(number)
    print("The Character for {} is : {}".format(number, num_ASCII))
    print("{}{:>5}".format(number,num_ASCII))

def get_number(lower, upper):
    number = int(input("Enter a number between {} and {}: ".format(lower, upper)))
    while number < lower or number > upper:
        print("Invalid Input")
        number = int(input("Enter a number between {} and {}: ".format(lower , upper)))
    return number

main()