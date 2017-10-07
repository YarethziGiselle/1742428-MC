>>> class Grafo:
	def __init__(self):
		self.V = set()
		self.E = dict()
		self.vecinos = dict()
	def agrega(self, v):
		self.V.add(v)
		if not v in self.vecinos:
			self.vecinos[v] = set()
	def conecta(self, v, u, peso=1):
		self.agrega(v)
		self.agrega(u)
		self.E[(v,u)] = self.E[(u,v)] = peso
		self.vecinos[v].add(u)
		self.vecinos[u].add(v)
	def complemento(self):
		comp= Grafo()
		for v in self.V:
			for w in self.V:
				if v != w and (v,w) not in self.E:
					comp.conecta(v, w, 1)
		return comp