
naturalSum=0
squareSum=0
def sumNatural(n):
	naturalSum =(n*(n+1))/2
	naturalSum= naturalSum*naturalSum 
	print(naturalSum)
	return naturalSum

def squareSum(n):
	squareSum=((2*n+1)*n*(n+1))/6
	print(squareSum)
	return squareSum
def main(n):
	sqSum = squareSum(n)
	natSum= sumNatural(n)
	diferenc = natSum-sqSum
	print("The difference between both is", diferenc)
n=100
main(n)
#sumNatural(10)
