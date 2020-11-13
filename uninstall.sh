#!/bin/bash
#pip uninstall -r utils/requirements.txt

if [ $? -eq 0 ]; then
    echo pip uninstall requirements: OK
else
    echo pip uninstall requirements: FAILLED
fi

rm PyTorchGUI
if [ $? -eq 0 ]; then
    echo PyTorchGUI removed: OK
else
    echo PyTorchGUI removed: FAILLED
fi

rm test/PyTorchGuiTest
if [ $? -eq 0 ]; then
    echo test/PyTorchGuiTest removed: OK
else
    echo test/PyTorchGuiTest removed: FAILLED
fi