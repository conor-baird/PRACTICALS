
files = ("HarkTheHerald.txt", "JoyToTheWorld.txt","AngelsWeHaveHeard.txt")
new_file = ""

def get_fixed_filename(files_new):
    new_file = ""
    for filename in files_new:
        for i, letter in enumerate(filename):
            new_file += letter

            print(new_file)
            try:
                if letter.islower() and filename[i + 1].isupper():
                    new_file += "_"



            except IndexError:
                continue
    return new_file

for filenames in files:
    print(get_fixed_filename(filenames))






