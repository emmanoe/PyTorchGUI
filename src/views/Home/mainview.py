from PyQt4 import QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import views.Network as Network
import views.Network.qtnodes as qtnodes
import views.Network.widget as Widget

class MainWindow(QtGui.QMainWindow):
	def __init__(self, controller,app_data):
		super(MainWindow, self).__init__()
		self.controller = controller
		self.app_data = app_data
		self.loadUi()
		self.setProperties()
		self.createEvents()
		self.show()

	def loadUi(self):
		uic.loadUi('src/views/Home/pytorchGui.ui', self)

	def setProperties(self):
		self.dataTable.setHorizontalHeaderLabels(['Name', 'Size', 'Dataset mode'])
		self.dataTable.horizontalHeader().show()
		self.openDataFileButton.setEnabled(False)
		self.dataTypePicker.model().item(0).setEnabled(False)
		self.displayLayerPicker()
		self.displayActivationFunctionPicker()
		self.displayLossFunctionPicker()
		self.lossFunctionPicker.model().item(0).setEnabled(False)
		self.displayOptimizerFunctionPicker()
		self.optimizerFunctionPicker.model().item(0).setEnabled(False)
		self.updateTrainingSetPicker()
		self.setFirstLayerButton.setEnabled(False)

	def createEvents(self):
		self.connect(self.dataTypePicker, SIGNAL('currentIndexChanged(QString)'), self.enableOpenDataFileButton)
		self.connect(self.addedLayerPicker, SIGNAL('currentIndexChanged(QString)'), self.updateEditLayerButtons)
		self.openDataFileButton.clicked.connect(self.openData)
		self.clearDataButton.clicked.connect(self.clearData)
		self.addLayerButton.clicked.connect(self.addLayer)
		self.addActivationFunctionButton.clicked.connect(self.addActivationFunction)
		self.setLossFunctionButton.clicked.connect(self.setLossFunction)
		self.setOptimizerFunctionButton.clicked.connect(self.setOptimizerFunction)
		self.startTrainButton.clicked.connect(self.startTrain)
		self.actionNew.triggered.connect(self.editNewNetwork)
		self.setFirstLayerButton.clicked.connect(self.setFirstLayer)
		self.editLayerButton.clicked.connect(self.editLayerOrFunction)
		self.loadNetworkButton.clicked.connect(self.loadNetwork)
		self.saveNetworkButton.clicked.connect(self.saveNetwork)

	def displayDatatable(self):
		self.dataTable.clearContents()
		self.dataTable.setRowCount(len(self.app_data.datalist))
		self.dataTable.setHorizontalHeaderLabels(['Name', 'Size', 'Dataset mode'])
		idx = 0
		for name,data in self.app_data.datalist.items():
			self.dataTable.setItem(idx, 0, QTableWidgetItem(name))
			self.dataTable.setItem(idx, 1, QTableWidgetItem(str(data.getSize())))
			if(data.trainingMode):
				self.dataTable.setItem(idx, 2, QTableWidgetItem('Training'))
			else:
				self.dataTable.setItem(idx, 2, QTableWidgetItem('Testing'))
			idx += 1

	def enableOpenDataFileButton(self):
		self.openDataFileButton.setEnabled(True)

	def openData(self):
		fname = QFileDialog.getExistingDirectory(self, 'Select data root directory', QDir.current().path()+'/../data', QtGui.QFileDialog.ShowDirsOnly)
		if fname:
			trainingMode = False
			if self.trainingSetButton.isChecked():
				trainingMode = True
			self.controller.openData(fname,self.dataTypePicker.currentText(),trainingMode)
			self.displayDatatable()
			self.updateTrainingSetPicker()
		else : 
			print('Info: No file loaded')

	def editNewNetwork(self): 
		self.netGFView = Widget.NodeGraphWidget()
		self.netGFView.setGeometry(100, 100, 800, 600)
		self.netGFView.show()
		self._registerNodeClass()


	def clearData(self):
		reply = QMessageBox.question(self, 'Confirmation', 'Do you really want to clear data ?', QMessageBox.Yes, QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			self.app_data.clearData()
			self.displayDatatable()
			self.updateTrainingSetPicker()

	def displayGraphic(self, fname):
		scene = QGraphicsScene()
		pixmap = QPixmap(fname)
		scene.addPixmap(pixmap)
		self.graphicsView.setScene(scene)
	
	def displayMessage(self):
		scene = QGraphicsScene()
		scene.addText("Message: No visualization available ");
		self.graphicsView.setScene(scene)

	def displayLayerPicker(self):
		for layerType, params in self.app_data.layerDatabase.list.items():
			self.layerPicker.addItem(layerType)

	def getFieldValue(self, paramType, field):
		if paramType == "str":
			return field.text()
		if paramType == "number":
			return field.value()
		if paramType == "float":
			return field.value()
		if paramType == "boolean":
			return field.isChecked()

	def generateFormFields(self, form, params, chosenParams, oldParams):
		for paramName, paramValue in params.items():
			paramType = paramValue["type"]
			if oldParams:
				paramDefaultValue = oldParams[paramName]
			else:
				paramDefaultValue = paramValue["default"]
			label = QLabel(paramName)

			if paramType == "number":
				field = QSpinBox()
				chosenParams[paramName] = field
				field.setRange(-10000,10000)
				if paramDefaultValue:
					field.setValue(paramDefaultValue)
			if paramType == "float":
				field = QDoubleSpinBox()
				chosenParams[paramName] = field
				field.setRange(-1000,1000)
				if paramDefaultValue:
					field.setValue(paramDefaultValue)
			if paramType == "boolean":
				field = QCheckBox()
				chosenParams[paramName] = field
				if paramDefaultValue:
					field.setChecked(paramDefaultValue)
			if paramType == "str":
				field = QLineEdit()
				chosenParams[paramName] = field
				if paramDefaultValue:
					field.setText(str(paramDefaultValue))

			form.addRow(label, field)

	def addLayer(self):
		layerType = str(self.layerPicker.currentText())
		#eval("qtnodes."+layerType)(scene=self.netGFView.scene)
		params = self.app_data.layerDatabase.list[layerType]

		self.addLayerWindow = QWidget()
		addLayerForm = QFormLayout()
		chosenParams = dict()
		self.generateFormFields(addLayerForm, params, chosenParams, None)
		
		self.addButton = QPushButton("Add")
		self.addButton.clicked.connect(lambda: self.validateAddLayer(layerType, chosenParams))
		quitButton = QPushButton("Cancel")
		quitButton.clicked.connect(self.closeAddLayerWindow)
		addLayerForm.addRow(self.addButton,quitButton)

		self.addLayerWindow.setLayout(addLayerForm)

		self.addLayerWindow.setWindowTitle("Adding a \"" + layerType + "\" layer")
		self.addLayerWindow.setMinimumWidth(350)
		self.addLayerWindow.show()
		

	def displayActivationFunctionPicker(self):
		for functionType, params in self.app_data.activationFunctionDatabase.list.items():
			self.activationFunctionPicker.addItem(functionType)

	def addActivationFunction(self):
		functionType = str(self.activationFunctionPicker.currentText())
		params = self.app_data.activationFunctionDatabase.list[functionType]

		self.addActivationFunctionWindow = QWidget()

		addActivationFunctionForm = QFormLayout()
		chosenParams = dict()
		self.generateFormFields(addActivationFunctionForm, params, chosenParams, None)
		
		self.addButton = QPushButton("Add")
		self.addButton.clicked.connect(lambda: self.validateAddActivationFunction(functionType, chosenParams))
		self.quitButton = QPushButton("Cancel")
		self.quitButton.clicked.connect(self.closeAddActivationFunctionWindow)
		addActivationFunctionForm.addRow(self.addButton,self.quitButton)

		self.addActivationFunctionWindow.setLayout(addActivationFunctionForm)

		self.addActivationFunctionWindow.setWindowTitle("Adding a \"" + functionType + "\" function")
		self.addActivationFunctionWindow.setMinimumWidth(350)
		self.addActivationFunctionWindow.show()

	def closeAddLayerWindow(self):
		self.addLayerWindow.close()

	def validateAddLayer(self, layerType, paramsIn):
		paramsOut = dict()
		for paramName, field in paramsIn.items():
			paramType = self.app_data.layerDatabase.list[layerType][paramName]["type"]
			paramsOut[paramName] = self.getFieldValue(paramType, field)
		self.controller.addLayer(layerType, paramsOut)
		self.updateAddedLayerPicker()
		self.closeAddLayerWindow()

	def closeAddActivationFunctionWindow(self):
		self.addActivationFunctionWindow.close()

	def validateAddActivationFunction(self, functionType, paramsIn):
		paramsOut = dict()
		for paramName, field in paramsIn.items():
			paramType = self.app_data.activationFunctionDatabase.list[functionType][paramName]["type"]
			paramsOut[paramName] = self.getFieldValue(paramType, field)
		self.controller.addActivationFunction(functionType, paramsOut)
		self.updateAddedLayerPicker()
		self.closeAddActivationFunctionWindow()

	def displayLossFunctionPicker(self):
		for functionType, params in self.app_data.lossFunctionDatabase.list.items():
			self.lossFunctionPicker.addItem(functionType)

	def setLossFunction(self):
		functionType = str(self.lossFunctionPicker.currentText())
		params = self.app_data.lossFunctionDatabase.list[functionType]

		self.setLossFunctionWindow = QWidget()

		setLossFunctionForm = QFormLayout()
		chosenParams = dict()
		self.generateFormFields(setLossFunctionForm, params, chosenParams, None)
		
		setButton = QPushButton("Set")
		setButton.clicked.connect(lambda: self.validateSetLossFunction(functionType, chosenParams))
		quitButton = QPushButton("Cancel")
		quitButton.clicked.connect(self.closeSetLossFunctionWindow)
		setLossFunctionForm.addRow(setButton,quitButton)

		self.setLossFunctionWindow.setLayout(setLossFunctionForm)

		self.setLossFunctionWindow.setWindowTitle("Setting a \"" + functionType + "\" function")
		self.setLossFunctionWindow.setMinimumWidth(350)
		self.setLossFunctionWindow.show()

	def closeSetLossFunctionWindow(self):
		self.setLossFunctionWindow.close()

	def validateSetLossFunction(self, functionType, paramsIn):
		paramsOut = dict()
		for paramName, field in paramsIn.items():
			paramType = self.app_data.lossFunctionDatabase.list[functionType][paramName]["type"]
			paramsOut[paramName] = self.getFieldValue(paramType, field)
		self.controller.setLossFunction(functionType, paramsOut)
		self.closeSetLossFunctionWindow()

	def displayOptimizerFunctionPicker(self):
		for functionType, params in self.app_data.optimizerFunctionDatabase.list.items():
			self.optimizerFunctionPicker.addItem(functionType)

	def setOptimizerFunction(self):
		functionType = str(self.optimizerFunctionPicker.currentText())
		params = self.app_data.optimizerFunctionDatabase.list[functionType]

		self.setOptimizerFunctionWindow = QWidget()

		setOptimizerFunctionForm = QFormLayout()
		chosenParams = dict()
		self.generateFormFields(setOptimizerFunctionForm, params, chosenParams, None)
		
		setButton = QPushButton("Set")
		setButton.clicked.connect(lambda: self.validateSetOptimizerFunction(functionType, chosenParams))
		quitButton = QPushButton("Cancel")
		quitButton.clicked.connect(self.closeSetOptimizerFunctionWindow)
		setOptimizerFunctionForm.addRow(setButton,quitButton)

		self.setOptimizerFunctionWindow.setLayout(setOptimizerFunctionForm)

		self.setOptimizerFunctionWindow.setWindowTitle("Setting a \"" + functionType + "\" function")
		self.setOptimizerFunctionWindow.setMinimumWidth(350)
		self.setOptimizerFunctionWindow.show()

	def closeSetOptimizerFunctionWindow(self):
		self.setOptimizerFunctionWindow.close()

	def validateSetOptimizerFunction(self, functionType, paramsIn):
		paramsOut = dict()
		for paramName, field in paramsIn.items():
			paramType = self.app_data.optimizerFunctionDatabase.list[functionType][paramName]["type"]
			paramsOut[paramName] = self.getFieldValue(paramType, field)
		self.controller.setOptimizerFunction(functionType, paramsOut)
		self.closeSetOptimizerFunctionWindow()

	def updateTrainingSetPicker(self):
		self.trainingSetPicker.clear()
		for name, data in self.app_data.datalist.items():
			if data.trainingMode:
				self.trainingSetPicker.addItem(name)

	def startTrain(self):
		trainingSetName = str(self.trainingSetPicker.currentText())
		epochNumber = self.epochNumberBox.value()
		batchSize = self.batchSizeBox.value()
		numWorkers = self.numWorkersBox.value()
		shuffling = self.shufflingCheckBox.isChecked()

		self.controller.startTrain(epochNumber, str(trainingSetName), batchSize, numWorkers, shuffling)

	def updateAddedLayerPicker(self):
		currentLayerName = str(self.addedLayerPicker.currentText())

		self.addedLayerPicker.clear()
		for name, layer in self.app_data.network.layerList.items():
			self.addedLayerPicker.addItem(name)
		for name, function in self.app_data.network.activationFunctionList.items():
			self.addedLayerPicker.addItem(name)

		index = self.addedLayerPicker.findText(currentLayerName)
		if index >= 0:
			self.addedLayerPicker.setCurrentIndex(index)

	def updateEditLayerButtons(self):
		selectedLayer = str(self.addedLayerPicker.currentText())
		firstLayerName = ""
		if self.app_data.network.firstLayer:
			firstLayerName = self.app_data.network.firstLayer.name
		if selectedLayer in self.app_data.network.layerList:
			self.editLayerButton.setText("Edit layer")
			if selectedLayer != firstLayerName:
				self.setFirstLayerButton.setEnabled(True)
		else:
			self.editLayerButton.setText("Edit activation function")
			self.setFirstLayerButton.setEnabled(False)

	def setFirstLayer(self):
		layerName = str(self.addedLayerPicker.currentText())
		self.controller.setFirstLayer(layerName)
		self.updateEditLayerButtons()

	def editLayerOrFunction(self):
		layerFunctionName = str(self.addedLayerPicker.currentText())
		if layerFunctionName in self.app_data.network.layerList:
			self.editLayer()
		if layerFunctionName in self.app_data.network.activationFunctionList:
			self.editActivationFunction()

	def editLayer(self):
		layerName = str(self.addedLayerPicker.currentText())
		layer = self.app_data.network.layerList[layerName]
		layerType = layer.type
		params = self.app_data.layerDatabase.list[layerType]
		oldParams = layer.parameters

		self.editLayerWindow = QWidget()
		editLayerForm = QFormLayout()
		chosenParams = dict()

		nameField = QLineEdit()
		nameField.setText(str(layerName))
		editLayerForm.addRow(QLabel("Layer name"), nameField)
		self.generateFormFields(editLayerForm, params, chosenParams, oldParams)

		currentNextLayerName = None
		if layer.nextLayer:
			currentNextLayerName = layer.nextLayer.name
		nextLayerField = QComboBox()
		nextLayerField.addItem("None")
		for name in self.app_data.network.layerList.keys():
			if name != layerName:
				nextLayerField.addItem(name)
		for name in self.app_data.network.activationFunctionList.keys():
			if name != layerName:
				nextLayerField.addItem(name)
		if currentNextLayerName:
			nextLayerIndex = nextLayerField.findText(currentNextLayerName)
			if nextLayerIndex >= 0:
				nextLayerField.setCurrentIndex(nextLayerIndex)
		editLayerForm.addRow(QLabel("Next layer"), nextLayerField)
		
		confirmButton = QPushButton("Confirm")
		confirmButton.clicked.connect(lambda: self.validateEditLayer(layerName, layerType, chosenParams, nameField, nextLayerField))
		quitButton = QPushButton("Cancel")
		quitButton.clicked.connect(self.closeEditLayerWindow)
		editLayerForm.addRow(confirmButton,quitButton)

		self.editLayerWindow.setLayout(editLayerForm)

		self.editLayerWindow.setWindowTitle("Editing a \"" + layerType + "\" layer")
		self.editLayerWindow.setMinimumWidth(350)
		self.editLayerWindow.show()

	def closeEditLayerWindow(self):
		self.editLayerWindow.close()

	def validateEditLayer(self, layerName, layerType, paramsIn, nameField, nextLayerField):
		paramsOut = dict()
		newName = str(nameField.text())
		nextLayerName = str(nextLayerField.currentText())
		for paramName, field in paramsIn.items():
			paramType = self.app_data.layerDatabase.list[layerType][paramName]["type"]
			paramsOut[paramName] = self.getFieldValue(paramType, field)
		self.controller.editLayer(layerName, newName, layerType, paramsOut, nextLayerName)
		self.updateAddedLayerPicker()
		self.closeEditLayerWindow()

	def editActivationFunction(self):
		functionName = str(self.addedLayerPicker.currentText())
		function = self.app_data.network.activationFunctionList[functionName]
		functionType = function.type
		params = self.app_data.activationFunctionDatabase.list[functionType]
		oldParams = function.parameters

		self.editActivationFunctionWindow = QWidget()
		editActivationFunctionForm = QFormLayout()
		chosenParams = dict()

		nameField = QLineEdit()
		nameField.setText(str(functionName))
		editActivationFunctionForm.addRow(QLabel("Layer name"), nameField)
		self.generateFormFields(editActivationFunctionForm, params, chosenParams, oldParams)

		currentNextLayerName = None
		if function.nextLayer:
			currentNextLayerName = function.nextLayer.name
		nextLayerField = QComboBox()
		nextLayerField.addItem("None")
		for name in self.app_data.network.layerList.keys():
			if name != functionName:
				nextLayerField.addItem(name)
		for name in self.app_data.network.activationFunctionList.keys():
			if name != functionName:
				nextLayerField.addItem(name)
		if currentNextLayerName:
			nextLayerIndex = nextLayerField.findText(currentNextLayerName)
			if nextLayerIndex >= 0:
				nextLayerField.setCurrentIndex(nextLayerIndex)
		editActivationFunctionForm.addRow(QLabel("Next layer"), nextLayerField)
		
		confirmButton = QPushButton("Confirm")
		confirmButton.clicked.connect(lambda: self.validateEditActivationFunction(functionName, functionType, chosenParams, nameField, nextLayerField))
		quitButton = QPushButton("Cancel")
		quitButton.clicked.connect(self.closeEditActivationFunctionWindow)
		editActivationFunctionForm.addRow(confirmButton,quitButton)

		self.editActivationFunctionWindow.setLayout(editActivationFunctionForm)

		self.editActivationFunctionWindow.setWindowTitle("Editing a \"" + functionType + "\" function")
		self.editActivationFunctionWindow.setMinimumWidth(350)
		self.editActivationFunctionWindow.show()

	def closeEditActivationFunctionWindow(self):
		self.editActivationFunctionWindow.close()

	def validateEditActivationFunction(self, functionName, functionType, paramsIn, nameField, nextLayerField):
		paramsOut = dict()
		newName = str(nameField.text())
		nextLayerName = str(nextLayerField.currentText())
		for paramName, field in paramsIn.items():
			paramType = self.app_data.activationFunctionDatabase.list[functionType][paramName]["type"]
			paramsOut[paramName] = self.getFieldValue(paramType, field)
		self.controller.editActivationFunction(functionName, newName, functionType, paramsOut, nextLayerName)
		self.updateAddedLayerPicker()
		self.closeEditActivationFunctionWindow()

	def loadNetwork(self):
		ext = "JSON File (*.json)"
		fname = QFileDialog.getOpenFileName(self, 'Open file', '', ext)
		if fname:
			self.app_data.network.loadNetwork(fname)
			self.updateAddedLayerPicker()
			self.updateEditLayerButtons()
	def saveNetwork(self):
		ext = "JSON File (*.json)"
		fname = QFileDialog.getOpenFileName(self, 'Choose a path', '', ext)
		if fname:
			self.app_data.network.saveNetwork(fname)





	def _registerNodeClass(self):
		#Convolution Layer
		self.netGFView.registerNodeClass(qtnodes.Conv1d)
		self.netGFView.registerNodeClass(qtnodes.Conv2d)
		self.netGFView.registerNodeClass(qtnodes.Conv3d)
		self.netGFView.registerNodeClass(qtnodes.ConvTranspose1d)
		self.netGFView.registerNodeClass(qtnodes.ConvTranspose2d)
		self.netGFView.registerNodeClass(qtnodes.ConvTranspose3d)
		self.netGFView.registerNodeClass(qtnodes.Unfold)
		self.netGFView.registerNodeClass(qtnodes.Fold)
		#Pooling Layer
		self.netGFView.registerNodeClass(qtnodes.MaxPool1d)
		self.netGFView.registerNodeClass(qtnodes.MaxPool2d)
		self.netGFView.registerNodeClass(qtnodes.MaxPool3d)
		self.netGFView.registerNodeClass(qtnodes.MaxUnpool1d)
		self.netGFView.registerNodeClass(qtnodes.MaxUnpool2d)
		self.netGFView.registerNodeClass(qtnodes.MaxUnpool3d)
		self.netGFView.registerNodeClass(qtnodes.AvgPool1d)
		self.netGFView.registerNodeClass(qtnodes.AvgPool2d)
		self.netGFView.registerNodeClass(qtnodes.AvgPool3d)
		self.netGFView.registerNodeClass(qtnodes.FractionalMaxPool2d)
		self.netGFView.registerNodeClass(qtnodes.LPPool1d)
		self.netGFView.registerNodeClass(qtnodes.LPPool2d)
		self.netGFView.registerNodeClass(qtnodes.AdaptiveMaxPool1d)
		self.netGFView.registerNodeClass(qtnodes.AdaptiveMaxPool2d)
		self.netGFView.registerNodeClass(qtnodes.AdaptiveMaxPool3d)
		self.netGFView.registerNodeClass(qtnodes.AdaptiveAvgPool1d)
		self.netGFView.registerNodeClass(qtnodes.AdaptiveAvgPool2d)
		self.netGFView.registerNodeClass(qtnodes.AdaptiveAvgPool3d)
		#Padding Layers
		self.netGFView.registerNodeClass(qtnodes.ReflectionPad1d)
		self.netGFView.registerNodeClass(qtnodes.ReflectionPad2d)
		self.netGFView.registerNodeClass(qtnodes.ReplicationPad1d)
		self.netGFView.registerNodeClass(qtnodes.ReplicationPad2d)
		self.netGFView.registerNodeClass(qtnodes.ReplicationPad3d)
		self.netGFView.registerNodeClass(qtnodes.ZeroPad2d)
		self.netGFView.registerNodeClass(qtnodes.ConstantPad1d)
		self.netGFView.registerNodeClass(qtnodes.ConstantPad2d)
		self.netGFView.registerNodeClass(qtnodes.ConstantPad3d)
		self.netGFView.registerNodeClass(qtnodes.Linear)