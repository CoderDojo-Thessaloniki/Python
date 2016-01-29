class UniversityMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Αρχικοποίηση μέλους του Πανεπιστημίου:', self.name)     
    def display(self):
        print('Όνομα:"{0}" Ηλικία:"{1}"'.format(self.name, self.age), end=' ')

class Professor(UniversityMember):
    def __init__(self, name, age, salary):
        UniversityMember.__init__(self, name, age)
        self.salary = salary
        print('Αρχικοποίηση καθηγητή:', self.name)
    def display(self):
        UniversityMember.display(self)
        print('Μισθός:', self.salary)

class Student(UniversityMember):
    def __init__(self, name, age, am):
        UniversityMember.__init__(self, name, age)
        self.am = am
        print('Αρχικοποίηση φοιτητή:', self.name)
    def display(self):
        UniversityMember.display(self)
        print('ΑΜ:', self.am)
        
    


    




        





