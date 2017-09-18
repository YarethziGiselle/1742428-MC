>>> def selection(arr):
	for i in range(0,len(arr)-1):
		val=i
		for j in range(i+1, len(arr)):
			if arr[j]<arr[val]:
				val=j
		if val!=1:
			aux=arr[i]
			arr[i]=arr[val]
			arr[val]=aux
	return arr

>>>> def burbuja(arr):
	aux=arr[:]
	for i in range(len(arr)):
		for j in range(0,len(arr)-i-1):
			if(aux[j]>aux[j+1]):
				aux[j],aux[j+1]=aux[j+1],aux[j]
				
	return aux

>>> def ordenar(arr):
	aux=arr[:]
	arrsort=[]
	for h in range(len(aux)):
		w=minimo(aux)
		aux.remove(w)
		arrsort.append(w)
	return arrsort

>>>def orden_por_insercion(array):
	global cnt
	for indice in range(1,len(array)):
		valor=array[indice] #valor es el elemento que vamor a comparar
		i=indice-1
		while i>=0:
			cnt+=1
			if valor<array[i]: #comparamos el valor con el elemento anterior
				array[i+1]=array[i]
				array[i]=valor
				i-=1
			else:
				break
		return array

>>> A=[1,4,1,654,8,3,53,7,8,0,4,74,3645,867,3,5,432,34,65,83]
>>> orden_por_insercion(A)


>>> B=[1,4,1,654,8,3,53,7,8,0,4,74,3645,867,3,5,432,34,65,83]
>>> ordenar(A)


>>> C=[1,4,1,654,8,3,53,7,8,0,4,74,3645,867,3,5,432,34,65,83]
>>> bubble(A)


>>> D=[1,4,1,654,8,3,53,7,8,0,4,74,3645,867,3,5,432,34,65,83]
>>> selection(A)