class Button(object):
	html = "";
	def getHtml(self):
		return self.html

class Image(Button):
	html = "<img></img>"

class Input(Button):
	html = "<input></input>"

class Flash(Button):
	html = "<obj></obj>"



class ButtonFactory():
	def createButton(self, type):
		targetClass = type.capitalize()
		cl = globals()[targetClass];
		return cl()

buttonFactory = ButtonFactory()
buttons = ["image", "input", "flash"]
for button in buttons:
    print(buttonFactory.createButton(button).getHtml())
