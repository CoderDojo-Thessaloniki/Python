for i in range(1,101):
	if i%15 == 0:
		print("FizzBuzz\n")
		continue
	if i%3 == 0:
		print("Fizz\n")
		continue
	if i%5 == 0:
		print("Buzz\n")
		continue
	print(str(i)+'\n')