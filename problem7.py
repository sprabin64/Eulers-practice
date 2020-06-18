prime=[]

def isPrime():
	pass
from math import ceil
def primeFinder():
	count=0

	for i in range(2,200000):
		a=1
		upr = ceil(i/2)+1
		for j in range(2,upr):
			
			if i%j==0:
				
				a=0
				break
				
		if a==1:
				
			prime.append(i)
			print(i)
			count+=1
			

		if count==10001:
			print("la sakyo")
			break

primeFinder()
print(len(prime))
print(prime[10000])
#print(prime)
