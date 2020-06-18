#check if the given number is divided by numbers from 1 to 20

divide = [1,2,3,5,7,11,13,17,19]

for j in range(9699690,9000000000,9699690):
	count=0
	for i in range(1,21):

		if j%i==0:
			count+=1

		if j%i!=0:
			break
	if count==20:
		print("Hurray! it is the number",j)
#else:
	#print("Sorry it is not the number")