COLOURS = {"coral": "ff7f50", "coral1": "ff7256", "coral2": "ee6a50", "coral3": "cd5b45", "coral4": "8b3e2f"}

colour_name = input("Enter colour: ")
while colour_name != "":
    if colour_name in COLOURS:
        print(COLOURS[colour_name])
    else:
        print("Invalid colour")
    colour_name = input("Enter colour: ")