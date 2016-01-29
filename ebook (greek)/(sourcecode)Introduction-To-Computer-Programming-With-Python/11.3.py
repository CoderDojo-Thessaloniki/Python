class Person:
    def __init__(self, name = '', age = 0):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Πρόσωπο(%s, %d)' % (self.name, self.age)

    def __repr__(self):
        return str(self)


    




        





