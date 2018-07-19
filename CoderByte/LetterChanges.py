def LetterChanges(str): 
	# code goes here
	givenl = list(str)
	for i in range(0, len(givenl)):
		oldchar = ord(givenl[i])
		newchar = oldchar+1
		if 97 <= oldchar <= 123:
			givenl[i] = oldchar+1
			if newchar in [97, 101, 105, 111, 117]:
				givenl[i] = chr(newchar-32)
			else:
				givenl[i] = chr(newchar)
	return ''.join(givenl)
