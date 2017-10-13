>>> memo={}
>>> cnt=0
>>> def fibonacci(n):
	global memo,cnt
	cnt+=1
	if n == 0 or n == 1:
		return (1)
	if n in memo:
		return memo[n]
	else:
		val=fibonacci(n-2)+fibonacci(n-1)
		memo[n]=val
		return val