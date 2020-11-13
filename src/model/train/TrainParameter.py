class TrainParameter:
	def __init__(self, epochs, dataset, batchSize,shuffling,numWorkers):
		self.epochs = epochs
		self.dataset = dataset
		self.batchSize = batchSize
		self.shuffling = shuffling
		self.numWorkers = numWorkers
		
