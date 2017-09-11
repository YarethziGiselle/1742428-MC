>>> cnt=0
>>> def burbuja(arr):
	aux=arr[:]
	global cnt
	for i in range(len(arr)):
		for j in range(0,len(arr)-i-1):
			if(aux[j]>aux[j+1]):
				aux[j],aux[j+1]=aux[j+1],aux[j]
				cnt+=1
	return aux