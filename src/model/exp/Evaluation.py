class Evaluation:
	def __init__(self, network,data,lossFunction):
			self.network = network
			self.data=data
			self.lossFunction=lossFunction

	def evaluate(self, network, testloader, lossFunction):
		correct = 0
		total = 0
		with torch.no_grad():
		    for data in testloader:
			images, labels = data
			outputs = network(images)
			_, predicted = lossFunction(outputs.data, 1)
			total += labels.size(0)
			correct += (predicted == labels).sum().item()

		print('Accuracy of the network on the 10000 test images: %d %%' % (100 * correct / total))
