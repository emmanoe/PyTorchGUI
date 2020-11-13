"""
A function describes the type and the parameters we use to call a PyTorch function
"""
class Function:
	def __init__(self, type):
		self.type = type
		self.parameters = dict()

	def setParameter(self, name, value):
		self.parameters[name] = value