#!/bin/bash

#remove old run script if it exist
rm -f PyTorchGUI

# Check if required pip modules are available if not install them 
FILE=utils/requirements.txt
UNIQUE='-={GR}=-'
#
if [ -z "$FILE" ]; then
        exit;
fi;
#
for LINE in `sed "s/ /$UNIQUE/g" $FILE`; do
        LINE=`echo $LINE | sed "s/$UNIQUE/ /g"`;
        if python -c 'import sys; import pkgutil; fullname=(str(sys.argv[1])); exit(not pkgutil.find_loader(fullname))' $LINE; then
    		echo $LINE 'found'
   	 		echo 'No installation needed'
		else
    		echo $LINE 'Not found'
    		pip install $LINE
		fi

		if [ $? -eq 0 ]; then
			echo $LINE install: OK
			echo
		else
			echo $LINE install: FAILLED
			echo
		fi

done;

#Create the app run script

echo "#!/bin/bash
python src/.pytorchgui.py" > PyTorchGUI

chmod 755 PyTorchGUI

if [ $? -eq 0 ]; then
    echo PytTorchGUI generate: OK
	echo
else
    echo PyTorchGUI generate: FAILLED
	echo
fi

#Create the test run script

echo "#!/bin/bash
cd ../
python src/.test-unit.py" > test/PyTorchGuiTest


chmod 755 test/PyTorchGuiTest

if [ $? -eq 0 ]; then
    echo test/PyTorchGuiTest generate: OK
	echo
else
    echo test/PyTorchGuiTest generate: FAILLED
	echo
fi


