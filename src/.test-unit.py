"""
Test the margarita mixer GUI.
"""

import sys
import unittest
import torch

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt

from controllers.UserController import UserController
from model.app_data import AppData
from views.Home import mainview 

app = QApplication(sys.argv)
app_data = AppData()
controller = UserController(app_data)

class PyTorchGuiTest(unittest.TestCase):
    '''Test the PyTorch GUI'''
    def setUp(self):
        '''Create the GUI'''
        self.form = mainview.MainWindow(controller, app_data)

    def test_defaults(self):
        '''Test the GUI Data Tab in its default state'''  
        #Data Tab
        self.assertEqual(self.form.dataTypePicker.itemText(0), "Select the type of Data")
        self.assertEqual(self.form.trainingSetButton.isChecked(), True)
        self.assertEqual(self.form.testingSetButton.isChecked(), False)
        
        #Network Tab  
        self.assertEqual(self.form.layerPicker.itemText(0), "Conv1d")
        self.assertEqual(self.form.addLayerButton.text(), "Add a layer")

        self.assertEqual(self.form.activationFunctionPicker.itemText(0), "ELU")
        self.assertEqual(self.form.addActivationFunctionButton.text(), "Add an activation function")

        self.assertEqual(self.form.addedLayerPicker.itemText(0), "") #Test if there is no already added layer
        self.assertEqual(self.form.editLayerButton.text(), "Edit layer")
        self.assertEqual(self.form.setFirstLayerButton.text(), "Set as first layer")

        self.assertEqual(self.form.lossFunctionPicker.itemText(0), "Select a loss function")
        self.assertEqual(self.form.setLossFunctionButton.text(), "Confirm")
        self.assertEqual(self.form.optimizerFunctionPicker.itemText(0), "Select optimizer function")
        self.assertEqual(self.form.setOptimizerFunctionButton.text(), "Confirm")

        #Train tab
        self.assertEqual(self.form.shufflingCheckBox.isChecked(), True)

    def test_layerPickerBox(self):
        '''Test if each values of the listes deroulantes layerPicker in torch.nn module'''
        AllLayers = [self.form.layerPicker.itemText(i) for i in range(self.form.layerPicker.count())]
        for layer in AllLayers:
            self.assertIn(layer, dir(torch.nn))
          
    def test_addLayerButton(self):
        '''Pushes the "Add a layer" button, and checks if the instance is created:'''
        for i in range(self.form.layerPicker.count()):
            self.form.layerPicker.setCurrentIndex(i)
            QTest.mouseClick(self.form.addLayerButton, Qt.LeftButton)
            QTest.mouseClick(self.form.addButton, Qt.LeftButton)
        #self.assertEqual(self.form.app_data.network.layerList.get('Conv1d'), self.form.layerPicker.itemText(0))    

    def test_activationFunctionPickerBox(self):
        '''Test if each values of the listes deroulantes activationFunctionPicker in torch.nn module'''
        AllActivationFunction = [self.form.activationFunctionPicker.itemText(i) for i in range(self.form.activationFunctionPicker.count())]
        for activationFunction in AllActivationFunction:
            self.assertIn(activationFunction, dir(torch.nn))

    def test_addActivationFunctionButton(self):
        '''Pushes the "Add an activation function" button, and checks if the instance is created:'''
        for j in range (0,100):
            for i in range(self.form.activationFunctionPicker.count()):
                self.form.activationFunctionPicker.setCurrentIndex(i)
                QTest.mouseClick(self.form.addActivationFunctionButton, Qt.LeftButton)
                QTest.mouseClick(self.form.addButton, Qt.LeftButton)

if __name__ == "__main__":
    unittest.main()