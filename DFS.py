>>> def DFS(g,ni):
	visitados = []
	p=Pila()
	p.meter(ni)
	while(p.longitud>0):
		na =p.obtener()
		visitador.append(na)
		ln = g.vecinos[na]
		for nodo in ln:
			if nodo not in visitados:
				p.meter(nodo)
	return visitados