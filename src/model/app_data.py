import torch
import torchvision
import torchvision.transforms as transforms
import sys
from data.Data import *
from net.Network import *
from utils.FunctionDatabase import *
from train.Trainer import *
from exp.Evaluation import *
import torch.optim as optim

"""
AppData is the central class of the model, it works as a link between them
"""
class AppData:
	def __init__(self):
		self.datalist = dict()
		self.network = Network()
		self.trainer = Trainer(self.network)
		self.layerDatabase = FunctionDatabase()
		self.layerDatabase.load("src/model/json_files/layerTypes.json")
		self.activationFunctionDatabase = FunctionDatabase()
		self.activationFunctionDatabase.load("src/model/json_files/activationFunctionTypes.json")
		self.lossFunctionDatabase = FunctionDatabase()
		self.lossFunctionDatabase.load("src/model/json_files/lossFunctionTypes.json")
		self.optimizerFunctionDatabase = FunctionDatabase()
		self.optimizerFunctionDatabase.load("src/model/json_files/optimizerFunctionTypes.json")

	def addData(self, type, path, trainingMode):
		idx = 1
		while (type + '_' + str(idx)) in self.datalist:
			idx += 1
		name = type + '_' + str(idx)
		self.datalist[name] = Data(type, path, trainingMode)

	def clearData(self):
		self.datalist.clear()