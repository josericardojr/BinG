class Attributes:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def name(self):
        return self.name

    def value(self):
        return self.value

    def myprint(self):
        print('{0}: {1}'.format(self.name, self.value))
