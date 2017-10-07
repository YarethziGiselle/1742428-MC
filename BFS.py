>>> def BFS(g,ni):
	visitados = []
	f=Fila()
	f.meter(ni)
	while(f.longitud>0):
		na =f.obtener()
		visitados.append(na)
		ln = g.vecinos[na]
		for nodo in ln:
			if nodo not in visitados:
				f.meter(nodo)
	return visitados