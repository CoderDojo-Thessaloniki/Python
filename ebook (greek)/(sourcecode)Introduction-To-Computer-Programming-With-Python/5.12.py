n = int(input('Δώστε έναν θετικό ακέραιο αριθμό:'))
count = 0
while n != 0:
    count = count + 1
    n = n // 10
print('Πλήθος ψηφίων =', count)


