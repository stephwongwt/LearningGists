#CoderByte Challenge. Reverse a given string, e.g. "Hello World" -> "dlroW olleH"

def FirstReverse(str): 
	# code goes here
	l = list(str)
	i = len(l)-1
	reversed = ''
	while i >= 0:
		reversed += l[i]
		i-=1
	return reversed
