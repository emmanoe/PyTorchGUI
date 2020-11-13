import json
from collections import OrderedDict

"""
A function database contains a dictionary of all the default functions available at a path
"""
class FunctionDatabase:
    def __init__(self):
    	self.list = OrderedDict()

    def load(self,path):
    	with open(path) as json_file:
    		self.list = json.load(json_file, object_pairs_hook=OrderedDict)