>>> def primo(n):
	cnt=1
	for i in range(2, math.ceil(math.sqrt(n))):
		cnt = cnt+1
		if ((n%i) == 0):
			break
	return cnt
