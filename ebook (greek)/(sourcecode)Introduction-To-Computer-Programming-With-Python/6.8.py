name = 'Mariza'
def sayHello():
    print('Hello ' + name)

def changeName(new_name):
    global name
    name = new_name

sayHello()
changeName('Katerina')
sayHello()


