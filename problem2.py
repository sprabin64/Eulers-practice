fibonacci = 1
a = 0
b = 1
totalsum = 0
for x in range(100000):
	if fibonacci<4000000:
		fibonacci = a+b
		a = b
		b = fibonacci

		print(fibonacci)
		if fibonacci%2==0:
			totalsum = totalsum + fibonacci
		if fibonacci>=4000000:
			print("Arrey kati error aako")

	
		
print(totalsum)