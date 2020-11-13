import torch
import torchvision
import torchvision.transforms as transforms

"""
This class is a container for PyTorch datasets, on which we added more attributes
"""
class Data:
	"""
	:param type: The type of Data (CIFAR10, CIFAR100, etc...)
	:param path: The path on the disk from which we load the data, or where it will be downloaded
	:param trainingMode: If the data is in training mode, it means it will make a training set, otherwise it will be a testing set
	"""
	def __init__(self, type, path, trainingMode):
		self.type = type
		self.path = str(path)
		self.trainingMode = trainingMode
		self.import_dataset()
	
	def import_dataset(self):
		transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
		if(self.type =='CIFAR10'):
			self.dataset = torchvision.datasets.CIFAR10(self.path, train=self.trainingMode, transform=transform, target_transform=None, download=True)
		if(self.type == 'CIFAR100'):
			self.dataset = torchvision.datasets.CIFAR100(self.path, train=self.trainingMode, transform=transform, target_transform=None, download=True)
		if(self.type == 'MNIST'):
			self.dataset = torchvision.datasets.MNIST(self.path, train=self.trainingMode, transform=transform, target_transform=None, download=True)

	def getSize(self):
		return len(self.dataset)