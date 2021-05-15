from PyQt5 import QtWidgets, uic
from win.window import Window
import time
import os



class Ui(QtWidgets.QMainWindow):
    def __init__(self, **kwargs):
        super(Ui, self).__init__()
        self.ui_name = kwargs.get('name', None)

        # load custom gui
        self.path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), self.ui_name)
        uic.loadUi(self.path, self)

        # parameters
        self.selected_window = None
        self.selected_window_hwnd = None
        self.selected_window_name = None
        self.time_interval = 1
        self.x_ratio = self.horizontalSliderXPos.value()
        self.y_ratio = self.verticalSliderYPos.value()


        # widget handle
        self.listWidgetWindowlist.itemDoubleClicked.connect(self.set_window_list)
        self.pushButtonStartMacro.clicked.connect(self.run_macro)
        self.pushButtonRefreshWindowlist.clicked.connect(self.refresh_list)
        self.horizontalSliderXPos.valueChanged.connect(self.set_x)
        self.verticalSliderYPos.valueChanged.connect(self.set_y)
        self.horizontalSliderTimeInterval.valueChanged.connect(self.set_time_interval)
        self.pushButtonTestPos.clicked.connect(self.test_position)
        # self.text_Edit_4.textChanged.connect(self.get_window)

        self.show()


    def load_window_list(self, window_lists):
        self.listWidgetWindowlist.clear()
        for window_list in window_lists:
            self.listWidgetWindowlist.addItem(window_list)

    def set_window_list(self):
        self.selected_window = self.listWidgetWindowlist.currentItem().text()
        self.selected_window_hwnd = int(self.selected_window.split()[0], 0)
        self.selected_window_name = self.selected_window.split()[-1]
        print("selected window : {}".format(self.selected_window))
        self.textEditSelectedWindow.setText(self.selected_window)
        self.pushButtonStartMacro.setEnabled(True)
        self.pushButtonTestPos.setEnabled(True)

    def set_x(self):
        self.textEditXPos.setText(str(self.horizontalSliderXPos.value()))
        self.x_ratio = self.horizontalSliderXPos.value()

    def set_y(self):
        self.textEditYPos.setText(str(self.verticalSliderYPos.value()))
        self.y_ratio = self.verticalSliderYPos.value()

    def set_time_interval(self):
        self.labelTimeInterval.setText("{}초".format(self.horizontalSliderTimeInterval.value()))

    def refresh_list(self):
        win = Window()
        window_list = win.get_window_title()
        self.load_window_list(window_list)
        self.textEditSelectedWindow.clear()
        self.pushButtonStartMacro.setEnabled(False)
        self.pushButtonTestPos.setEnabled(False)

    def test_position(self):
        context ={'name': self.selected_window_name, 'hwnd': self.selected_window_hwnd, 'test': True}
        test_win = Window(**context)
        test_win.set_foreground_window()
        test_win.click_target_window((self.x_ratio, self.y_ratio))

    def run_macro(self):
        print("run macro...")
        self.time_interval = self.horizontalSliderTimeInterval.value()

        context ={'name': self.selected_window_name, 'hwnd': self.selected_window_hwnd}
        macro = Window(**context)

        # TODO thread
        for _ in range(5):
            origin_hwnd, (init_x, init_y) = macro.get_origin()
            print("original_hwnd : {} / init_x : {} / init_y : {}".format(origin_hwnd, init_x, init_y))
            macro.set_foreground_window()
            macro.click_target_window((self.x_ratio, self.y_ratio))
            macro.back_origin(origin_hwnd, (init_x, init_y))
            time.sleep(self.time_interval)
        
        return True