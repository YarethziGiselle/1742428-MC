Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> cnt=0
>>> def minimo(arr):
	h=arr[0]
	global cnt
	for w in arr:
		cnt+=1
		if(w<h):
			h=w

			
>>> return k
SyntaxError: 'return' outside function
>>> cnt=0
>>> def minimo(arr):
	h=arr[0]
	global cnt
	for w in arr:
		cnt+=1
		if(w<h):
			h=w
	return h
def ordenar(arr):
	
SyntaxError: invalid syntax
>>> cnt=0
>>> def minimo(arr):
	h=arr[0]
	global cnt
	for w in arr:
		cnt+=1
		if(w<h):
			h=w
	return h

>>> def ordenar(arr):
	aux=arr[:]
	arrsort=[]
	for h in range(len(aux)):
		w=minimo(aux)
		aux.remove(w)
		arrsort.append(w)
	return arrsort

>>> import random
>>> p=random.sample(range(0,100),40)
>>> print(p)
[96, 60, 83, 3, 41, 0, 23, 76, 52, 85, 29, 15, 74, 20, 69, 81, 34, 87, 61, 70, 40, 28, 68, 73, 66, 11, 33, 26, 5, 25, 2, 54, 75, 42, 93, 8, 64, 7, 94, 56]
>>> psort=ordenar(p)
>>> print(cnt)
820
>>> print(psort)
[0, 2, 3, 5, 7, 8, 11, 15, 20, 23, 25, 26, 28, 29, 33, 34, 40, 41, 42, 52, 54, 56, 60, 61, 64, 66, 68, 69, 70, 73, 74, 75, 76, 81, 83, 85, 87, 93, 94, 96]
>>> 
