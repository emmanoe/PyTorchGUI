import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from tqdm import tqdm
import json,ast
from collections import OrderedDict
from Layer import *

"""
A network is a representation of a neural network
"""
class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
        self.layerList = OrderedDict()
        self.activationFunctionList = OrderedDict()
        self.firstLayer = None
        self.lossFunction = None
        self.optimizerFunction = None
	
    """
    Goes through all the added layers and functions, and converts them to PyTorch functions,
    which will made this network usable by PyTorch
    """
    def buildNetwork(self):
        for name, layer in self.layerList.items() : 
            params = layer.parameters
            functionToCall = getattr(nn, layer.type)
            setattr(self, name, functionToCall(**params))
        for name, function in self.activationFunctionList.items() :
            params = function.parameters
            functionToCall = getattr(nn, function.type)
            setattr(self, name, functionToCall(**params))
        if self.lossFunction:
            functionToCall = getattr(nn, self.lossFunction.type)
            setattr(self, "criterion", functionToCall(**self.lossFunction.parameters))
        if self.optimizerFunction:
            self.optimizerFunction.setParameter("params", self.parameters())
            functionToCall = getattr(optim, self.optimizerFunction.type)
            setattr(self, "optimizer", functionToCall(**self.optimizerFunction.parameters))

    """
    This function is used by the trainer to train the network
    It goes through all the layers, and computes them in the defined order
    :param input: Input provided by PyTorch when training the network
    """
    def forward(self, input):
        if self.firstLayer :
            current = self.firstLayer
            output = input
            while current:
                functionToCall = getattr(self, current.name)
                output = functionToCall(output)
                current = current.nextLayer
            return output
        else :
            raise Exception('First layer not defined')

    """
    Saves the network in a json file at the given path
    """
    def saveNetwork(self, PATH):
        #We need to convert the layerList parameters to a new dictionnary
        # to save it correctly
        rootSaveDict=OrderedDict()
        for name, layer in self.layerList.items():
            layerSaveDict = OrderedDict()
            layerSaveDict["class"] = "layer"
            layerSaveDict["type"] = layer.type
            layerSaveDict["parameters"] = layer.parameters
            if layer.nextLayer:
                nextLayerName = layer.nextLayer.name
                layerSaveDict["nextlayer"] = nextLayerName

            if self.firstLayer == layer:
                layerSaveDict["firstlayer"] = True
            rootSaveDict[name] = layerSaveDict

        for name, function in self.activationFunctionList.items():
            functionSaveDict = OrderedDict()
            functionSaveDict["class"] = "activation_function"
            functionSaveDict["type"] = function.type
            functionSaveDict["parameters"] = function.parameters
            if function.nextLayer:
                print(function.type + " " + name)
                nextLayerName = function.nextLayer.name
                functionSaveDict["nextlayer"] = nextLayerName

            rootSaveDict[name] = functionSaveDict

        with open(PATH,'w') as netSave:
            netSave.write(json.dumps(rootSaveDict,indent=1))

    """
    Loads a network from a json file, provided at the given path
    """
    def loadNetwork(self, PATH):
        self.layerList.clear()
        self.activationFunctionList.clear()
    	LoadedLayers= json.load(open(PATH), object_pairs_hook=OrderedDict)
        for name, layerDict in LoadedLayers.items():
            layer=Layer(layerDict['type'])
            layer.name=name
            layer.parameters=layerDict['parameters']
            if layerDict["class"] == "layer":
               self.layerList[layer.name]=layer
               if "firstlayer" in layerDict:
                    self.firstLayer = layer
            if layerDict["class"] == "activation_function":
                self.activationFunctionList[layer.name]=layer
        for name, layerDict in LoadedLayers.items():
            if "nextlayer" in layerDict:
                nextLayerName = layerDict['nextlayer']
                if nextLayerName in self.layerList:
                    nextLayer=self.layerList[nextLayerName]
                if nextLayerName in self.activationFunctionList:
                    nextLayer=self.activationFunctionList[nextLayerName]
                self.layerList[name].setNextLayer(nextLayer)

    """
    Used to check is the name provided is already taken
    If no, it returns the given name
    If yes, it returns a new name based on the orginal one
    """
    def getFreeLayerName(self, name):
        if name not in self.layerList and name not in self.activationFunctionList:
            return name
        idx = 2
        while ((name + '_' + str(idx)) in self.layerList) or ((name + '_' + str(idx)) in self.activationFunctionList):
            idx += 1
        return name + '_' + str(idx)


    def addLayer(self,layer):
        name = self.getFreeLayerName(layer.type)
        layer.name = name
        self.layerList[name] = layer

    def editLayer(self, layer, newName):
        self.layerList[layer.name] = layer
        if layer.name != newName:
            self.renameLayer(layer, newName)
 
    def addActivationFunction(self,function):
        name = self.getFreeLayerName(function.type)
        function.name = name
        self.activationFunctionList[name] = function

    def editActivationFunction(self, function, newName):
        #TODO : handle the rename
        self.activationFunctionList[function.name] = function
        if function.name != newName:
            self.renameActivationFunction(function, newName)

    def setFirstLayer(self,layer):
        self.firstLayer = layer
	
    def removeLayer(self,layerName):
        if layerName in self.layerList:
            del self.layerList[layerName]

    def removeActivationFunction(self,functionName):
        if functionName in self.activationFunctionList:
            del self.activationFunctionList[functionName]

    def renameLayer(self, layer, newName):
        oldName = layer.name
        validNewName = self.getFreeLayerName(newName)
        layer.name = validNewName
        #add in the dictionnary layerList the new key for
        # the old item self.layerList[layer.name]
        self.layerList[validNewName] = layer
    	#remove the layer if the network is already built and remove
    	#it from the layerList dictionnary
    	self.removeLayer(oldName)

    def renameActivationFunction(self,function,newName):
        oldName = function.name
        validNewName = self.getFreeLayerName(newName)
        function.name = validNewName
        self.activationFunctionList[validNewName] = function
        self.removeActivationFunction(oldName)

    def getLayer(self,Name):
	if Name in self.layerList:
		return self.layerList[Name]