def read_age():
    while True:
        try:
            n = int(input('Δώστε την ηλικία σας:'))
            return n    
        except ValueError:
            print('Πρέπει να δώσετε ακέραιο αριθμό.')


age = read_age()
print(age)





          
          
