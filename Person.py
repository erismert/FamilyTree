class Person(object):
	"""docstring for Person"""
	def __init__(self,gender,name,surname,birthdate,deathdate):
		self.name      = name
		self.surname   = surname
		self.gender    = gender
		self.birthdate = birthdate
		self.deathdate = deathdate
		self.father    = None
		self.mother    = None
		self.children  = []
	def __str__(self):
	    return self.name+" "+self.surname	