#Coderbyte Challenge. Input a number, e.g. 4 and get the factorial result of 4! = (4*3*2*1) = 24

def FirstFactorial(num): 
	total = 1
	i = 1
	while i <= num:
		total *= i
		i += 1
	return total
