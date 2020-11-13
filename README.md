## Installation 

Before installing PyTorchGUI, please install pip, TKinter lib and CMake

- **Install prerequiste (recommended):**
pip:

	> apt install pip

TKinter:

	> apt install python-tk 

CMake:

	> apt install cmake

Then, set QT 4 to be the default Qt version to be used

	> apt install qt4-default

Finally, run the install script in the project root directory wich will install all the dependencies :

	> ./install.sh 

## Launch the App :

	> ./PyTorchGUI

## Run the tests :

	> cd test
	> ./PyTorchGuiTest

### To run specific test, from root directory type:
	> python src/.test-unit.py PyTorchGuiTest.[test]
	[test]: test_defaults
		test_layerPickerBox
		test_addLayerButton
		test_activationFunctionPickerBox
		test_addActivationFunctionButton
