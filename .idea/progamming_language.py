

class Language:

    def __init__(self, name, type, reflection, year=0):
        self.name = name
        self.type = type
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.type.lower() == "dynamic":
            status = True
        else:
            status = False
        return status

    def __str__(self):
        return "{}, {}, Reflection = {}, First Appeared in {}".format(self.name, self.type, self.reflection, self.year)
