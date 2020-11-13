from collections import OrderedDict

"""
A layer is a step of a network, which is used to compute values
"""
class Layer:
    """
    :param type: the type of the layer, which corresponds to a PyTorch function
    """
    def __init__(self, type):
        self.name = None
        self.type = type
        self.parameters = OrderedDict()
        self.nextLayer = None

    def setParameter(self, name, value):
        self.parameters[name] = value
    
    """
    Sets the next layer of this layer
    :param layer: the layer which goes next to this one in the graph
    """
    def setNextLayer(self, layer):
        self.nextLayer = layer