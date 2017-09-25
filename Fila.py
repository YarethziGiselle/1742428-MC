>>> class fila:
	def __init__(self):
		self.fila=[]
	def obtener(self):
		return self.fila.pop()
	def meter(self,e):
		self.fila.append(e)
		return len(self.fila)
	@property
	def longitud(self):
		return len(self.fila)

	
>>> l=fila()
>>> l.meter(2)
1
>>> l.meter(5)
2