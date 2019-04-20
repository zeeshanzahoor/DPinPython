class Wheel:
	size = None

class Body:
	shape = None

class Engine:
	HorsePower = None

class Builder:
	def getWheel(self):pass
	def getEngine(self):pass
	def getBody(self):pass

class SedanBuilder(Builder):
	def getWheel(self):
		wheel =  Wheel()
		wheel.size = 20
		return wheel

	def getEngine(self):
		engine = Engine()
		engine.HorsePower = 120
		return engine

	def getBody(self):
		body = Body()
		body.shape = "Sedan"
		return body

class JeepBuilder(Builder):
	def getWheel(self):
		wheel = Wheel()
		wheel.size = 22
		return wheel;

	def getBody(self):
		body = Body()
		body.shape = "SUV"
		return body

	def getEngine(self):
		engine = Engine()
		engine.HorsePower = 400
		return engine

class Car:
	def __init__(self, *args, **kwargs):
		self.__wheels = list()
		self.__engine = None
		self.__body = None

	def setBody(self, body):
		self.__body = body

	def attachWheel(self, wheel):
		self.__wheels.append(wheel)

	def setEngine(self, engine):
		self.__engine = engine


	def spec(self):
		print("body : " + self.__body.shape)
		print("engine : " + str(self.__engine.HorsePower))
		print("Wheel Size : " + str(self.__wheels[0].size))

class Director :
	__builder = None

	def setBuilder(self, builder):
		self.__builder = builder

	def getCar(self):
		if self.__builder == None:
			raise Exception("builder not set")
		
		car = Car()
		car.setBody(self.__builder.getBody())
		car.setEngine(self.__builder.getEngine())
		for x in range(0,4):
			car.attachWheel(self.__builder.getWheel())
		return car

def main():
	jeepBuilder = JeepBuilder()
	sedanBuilder = SedanBuilder()

	director = Director()
	print("--- jeep ---")
	director.setBuilder(jeepBuilder)
	jeep = director.getCar()
	jeep.spec()

	print("--- Sedan ---")
	director.setBuilder(sedanBuilder)
	sedan = director.getCar()
	sedan.spec()

if __name__ == "__main__":
	main()