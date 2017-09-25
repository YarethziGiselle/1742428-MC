>>> class pila:
	def __init__(self):
		self.pila=[]
	def obtener(self):
		return self.pila.pop()
	def meter(self,e):
		self.pila.append(e)
		return len(self.pila)
	@property
	def longitud(self):
		return len(self.pila)

	
>>> p=pila()
>>> p.meter(1)
1
>>> p.meter(2)
2
>>> print(p.longitud)
2
>>> print(p.obtener())
2