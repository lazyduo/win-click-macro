from PyQt5 import QtWidgets, uic
import sys
import os



class Ui(QtWidgets.QMainWindow):
    def __init__(self, **kwargs):
        super(Ui, self).__init__()
        self.ui_name = kwargs['name']

        # load custom gui
        self.path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), self.ui_name)
        uic.loadUi(self.path, self)


        # widget handle
        self.pushButton_4.clicked.connect(self.btn_clicked)

        self.show()

    def btn_clicked(self):
        print('hi')
