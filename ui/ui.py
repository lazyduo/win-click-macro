from PyQt5 import QtWidgets, uic
from win.window import Window
import time
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
        self.selected_window_name = None
        self.time_interval = 1


        # widget handle
        self.listWidget_1.itemDoubleClicked.connect(self.set_window_list)
        self.pushButton_3.clicked.connect(self.run_macro)
        self.horizontalSlider_2.valueChanged.connect(self.set_x)
        self.verticalSlider.valueChanged.connect(self.set_y)
        self.horizontalSlider.valueChanged.connect(self.set_time_interval)
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
        self.selected_window_name = self.selected_window.split()[-1]
        print("selected window : {}".format(self.selected_window))
        self.textEdit_4.setText(self.selected_window)
        self.pushButton_3.setEnabled(True)

    def set_x(self):
        self.textEdit_6.setText(str(self.horizontalSlider_2.value()))

    def set_y(self):
        self.textEdit_7.setText(str(self.verticalSlider.value()))

    def set_time_interval(self):
        self.label_6.setText("{}초".format(self.horizontalSlider.value()))


    def run_macro(self):
        print("run macro")
        self.time_interval = self.horizontalSlider.value()

        context ={'name': self.selected_window_name, 'hwnd': self.selected_window_hwnd}
        macro = Window(**context)

        for _ in range(5):
            time.sleep(self.time_interval)
            origin_hwnd, (init_x, init_y) = macro.get_origin()
            print("original_hwnd : {} / init_x : {} / init_y : {}".format(origin_hwnd, init_x, init_y))
            macro.set_foreground_window()
            macro.back_origin(origin_hwnd, (init_x, init_y))
        
        return True