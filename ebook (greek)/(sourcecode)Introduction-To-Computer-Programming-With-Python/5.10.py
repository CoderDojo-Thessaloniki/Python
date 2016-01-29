# υπολογισμός παραγοντικού με for
n = int(input('Δώστε έναν θετικό αριθμό:'))
f = 1
for i in range(2, n+1):
    f = f * i
print(str(n) + ' παραγοντικό = ' + str(f))

# υπολογισμός παραγοντικού με while
n = int(input('Δώστε έναν θετικό αριθμό:'))
f = 1
i = 2
while i <= n:
    f = f * i
    i = i + 1
print(str(n) + ' παραγοντικό = ' + str(f))


