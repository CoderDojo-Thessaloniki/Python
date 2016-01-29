fname = input('Δώστε όνομα αρχείου:')

try:
    f = open(fname, 'r')
    print(f.read())
    f.close()
except FileNotFoundError:
    print('Δεν υπάρχει αρχείο με όνομα', fname)


          
          
