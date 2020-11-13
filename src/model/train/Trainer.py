from TrainParameter import *
from ..data.Data import *
from tqdm import tqdm
import time
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn
import torch.nn.functional as F

"""
This class allows to train a neural network
"""
class Trainer:
	def __init__(self, network):
		self.network = network
		self.trainParameter = None

	def startTrain (self,trainParameter):
		self.network.buildNetwork()
		self.trainParameter = trainParameter
		trainLoader = self.import_data_loader()
		criterion = self.network.criterion
		optimizer = self.network.optimizer
		batchSize=int(len(trainLoader)/100)
		allLoss=[]
		x_tab=[]
		# loop over the dataset multiple times (with tqdm for progress bar)
		for epoch in tqdm(range(trainParameter.epochs)):
			running_loss = 0.0
			iterationList=[]
			running_lossList=[]
			for i, data in tqdm(enumerate(trainLoader, 0)):
				# get the inputs
				inputs, labels = data
				# zero the parameter gradients not working ! 
				optimizer.zero_grad()
				# forward et backward + optimize
				outputs = self.network(inputs)
				loss = criterion(outputs, labels)
				loss.backward()
				optimizer.step()

				# print statistics
				running_loss += loss.item()
				#draw graphics
				
				if (i % batchSize == batchSize-1):    
					# print every  mini-batches
					print('[%d, %5d] loss: %.3f' %
                              (epoch + 1, i + 1, running_loss / batchSize))
					iterationList.append(i)
					running_lossList.append(running_loss/batchSize)
					allLoss.append(running_loss/batchSize)
					running_loss = 0.0
			# Draw a graph for each epoch 
			plt.figure(epoch)
    			plt.plot(iterationList,running_lossList)
			plt.savefig('resultTraining/epoch'+ str(epoch)+'.png')
			plt.close()
		plt.figure(0)
		print(len(allLoss))
		for i in range(batchSize,self.trainParameter.epochs*len(trainLoader)+1,batchSize):
			x_tab.append(i)
		print(len(allLoss),len(x_tab))
		plt.plot(x_tab,allLoss)
		plt.savefig('resultTraining/loss_evolution.png')
		plt.close()
		print('Finished Training')
		#Show the graphs need to close them, mays be we can save them and clear directly
		# and propose a solution to print the png file
	def import_data_loader(self):
		dataset = self.trainParameter.dataset
		batchSize = self.trainParameter.batchSize
		shuffling = self.trainParameter.shuffling
		numWorkers = self.trainParameter.numWorkers
		return torch.utils.data.DataLoader(dataset, batch_size=batchSize,shuffle=shuffling, num_workers=numWorkers)
