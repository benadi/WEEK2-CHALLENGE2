def Fizzbuzz(a, b):
	lengtha = len(a)
	lengthb = len(b)
	combination = lengtha + lengthb
	if combination%3 == 0:
		print("fizz")
	elif combination%5 == 0:
		print("Buzz")
	elif combination%3==0 and combination%5 ==0:
		print("Fizzbuzz")
print(Fizzbuzz([1, 2, 3], [1, 2]))