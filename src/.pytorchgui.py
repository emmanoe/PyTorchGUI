import sys
from PyQt4 import QtGui, uic
from controllers.UserController import UserController
from views.Home.mainview import MainWindow
from model.app_data import AppData

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app_data = AppData()
    controller = UserController(app_data)
    window = MainWindow(controller, app_data)
    sys.exit(app.exec_())
