from PyQt5 import QtWidgets, uic
from win.window import Window
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

        # parameters
        self.selected_window = None
        self.selected_window_hwnd = None


        # widget handle
        self.listWidget_1.itemDoubleClicked.connect(self.set_window_list)
        self.pushButton_3.clicked.connect(self.run_macro)
        self.horizontalSlider_2.valueChanged.connect(self.set_x)
        self.verticalSlider.valueChanged.connect(self.set_y)
        # self.text_Edit_4.textChanged.connect(self.get_window)

        self.show()

    def btn_clicked(self):
        print('hi')

    def load_window_list(self, window_lists):
        for window_list in window_lists:
            self.listWidget_1.addItem(window_list)

    def set_window_list(self):
        self.selected_window = self.listWidget_1.currentItem().text()
        self.selected_window_hwnd = int(self.selected_window.split()[0], 0)
        print("selected window : {}".format(self.selected_window))
        self.textEdit_4.setText(self.selected_window)
        self.pushButton_3.setEnabled(True)
        
    def set_x(self):
        self.textEdit_6.setText(str(self.horizontalSlider_2.value()))

    def set_y(self):
        self.textEdit_7.setText(str(self.verticalSlider.value()))


    def run_macro(self):
        print("run macro")
        macro = Window(self.selected_window_hwnd)
        macro.set_foreground_window()
        
        return True