from model.net.Layer import *
from model.net.Function import *
from model.train.TrainParameter import *

class UserController:
	def __init__(self, app_data):
		self.app_data = app_data

	def openData (self, path, type, trainingMode):
		self.app_data.addData(str(type), path, trainingMode)

	def addLayer(self, type, params):
		layer = Layer(type)
		for name,value in params.items():
			layer.setParameter(name, value)
		self.app_data.network.addLayer(layer)

	def editLayer(self, layerName, newName, type, params, nextLayerName):
		layer = self.app_data.network.layerList[layerName]
		if nextLayerName != "None":
			if nextLayerName in self.app_data.network.layerList:
				nextLayer = self.app_data.network.layerList[nextLayerName]
			if nextLayerName in self.app_data.network.activationFunctionList:
				nextLayer = self.app_data.network.activationFunctionList[nextLayerName]
			if nextLayer:
				layer.setNextLayer(nextLayer)
		for name,value in params.items():
			layer.setParameter(name, value)
		self.app_data.network.editLayer(layer, newName)

	def addActivationFunction(self, type, params):
		function = Layer(type)
		for name,value in params.items():
			function.setParameter(name, value)
		self.app_data.network.addActivationFunction(function)

	def editActivationFunction(self, functionName, newName, type, params, nextLayerName):
		function = self.app_data.network.activationFunctionList[functionName]
		if nextLayerName != "None":
			if nextLayerName in self.app_data.network.layerList:
				nextLayer = self.app_data.network.layerList[nextLayerName]
			if nextLayerName in self.app_data.network.activationFunctionList:
				nextLayer = self.app_data.network.activationFunctionList[nextLayerName]
			if nextLayer:
				function.setNextLayer(nextLayer)
		for name,value in params.items():
			function.setParameter(name, value)
		self.app_data.network.editActivationFunction(function, newName)

	def setLossFunction(self, type, params):
		function = Function(type)
		for name,value in params.items():
			function.setParameter(name, value)
		self.app_data.network.lossFunction = function

	def setOptimizerFunction(self, type, params):
		function = Function(type)
		for name,value in params.items():
			function.setParameter(name, value)
		self.app_data.network.optimizerFunction = function

	def startTrain(self, epochs, trainingSetName, batchSize, numWorkers, shuffling):
		dataset = self.app_data.datalist[trainingSetName].dataset
		parameters = TrainParameter(epochs, dataset, batchSize, shuffling, numWorkers)
		self.app_data.trainer.startTrain(parameters)

	def setFirstLayer(self, layerName):
		layer = self.app_data.network.layerList[layerName]
		self.app_data.network.firstLayer = layer