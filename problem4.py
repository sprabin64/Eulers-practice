
palindromeNumber= []
def isPalindrome(n,b):
	x = []
	y=[]

	for i in n:
		x.append(i)

	
	for j in reversed(n):
		y.append(j)
		

	if x == y:
		palindromeNumber.append(int(n))
		#print("The number is palindrome and the number is",n)



	#if i!=j:
		#print("Sorry not palindrome")

def greatestPalindrome():

	c = ""
	for a in range(1,1000):
		for b in range(1,1000):
			numberCheck = str(a*b)
			isPalindrome(numberCheck,c)

def main():

	b=''
	greatestPalindrome()
	print(max(palindromeNumber))
	#isPalindrome("851158",b)

main()