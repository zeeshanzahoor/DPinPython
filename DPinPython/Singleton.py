class Singleton:
	__instance = None;
	def getInstance():
		if Singleton.__instance == None:
			Singleton();
		return Singleton.__instance;

	def __init__(self):
		if Singleton.__instance != None:
			raise Exception("This class is a singleton")
		else:
			Singleton.__instance = self

s = Singleton()
print(s)

g = Singleton.getInstance()
print(g)

q = Singleton.getInstance()
print(q)
