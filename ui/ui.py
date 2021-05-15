from PyQt5 import QtWidgets, uic
from win.window import Window
import threading
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
        self.macroThread = None
        self.stop = False
        self.stop_event = threading.Event()


        # widget handle
        self.listWidgetWindowlist.itemDoubleClicked.connect(self.set_window_list)
        self.pushButtonStartMacro.clicked.connect(self.run_macro)
        self.pushButtonRefreshWindowlist.clicked.connect(self.refresh_list)
        self.horizontalSliderXPos.valueChanged.connect(self.set_x)
        self.verticalSliderYPos.valueChanged.connect(self.set_y)
        self.horizontalSliderTimeInterval.valueChanged.connect(self.set_time_interval)
        self.pushButtonTestPos.clicked.connect(self.test_position)
        self.pushButtonStopMacro.clicked.connect(self.stopMacro)
        self.lineEditXPos.editingFinished.connect(self.setHorizontalSlider)
        self.lineEditYPos.editingFinished.connect(self.setVerticalSlider)
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

    def setHorizontalSlider(self):
        if self.lineEditXPos.text():
            x = int(self.lineEditXPos.text())
            self.horizontalSliderXPos.setValue(x)

    def setVerticalSlider(self):
        if self.lineEditYPos.text():
            y = int(self.lineEditYPos.text())
            self.verticalSliderYPos.setValue(y)

    def set_x(self):
        self.lineEditXPos.setText(str(self.horizontalSliderXPos.value()))
        self.x_ratio = self.horizontalSliderXPos.value()

    def set_y(self):
        self.lineEditYPos.setText(str(self.verticalSliderYPos.value()))
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
        self.pushButtonStopMacro.setEnabled(True)
        self.pushButtonStartMacro.setEnabled(False)
        self.listWidgetWindowlist.setEnabled(False)

        context ={'name': self.selected_window_name, 'hwnd': self.selected_window_hwnd}
        self.macroThread = threading.Thread(target=self.runMacro, daemon=True, kwargs=context)
        self.macroThread.start()
        

    def stopMacro(self):
        self.stop_event.set()
        print("stop macro...")
        self.pushButtonStopMacro.setEnabled(False)
        self.pushButtonStartMacro.setEnabled(True)
        self.listWidgetWindowlist.setEnabled(True)

    def runMacro(self, **kwargs):
        self.macro = Window(**kwargs)

        while True:
            self.origin_hwnd, (self.init_x, self.init_y) = self.macro.get_origin()
            print("original_hwnd : {} / self.init_x : {} / self.init_y : {}".format(self.origin_hwnd, self.init_x, self.init_y))
            self.macro.set_foreground_window()
            self.macro.click_target_window((self.x_ratio, self.y_ratio))
            self.macro.back_origin(self.origin_hwnd, (self.init_x, self.init_y))
            if self.stop_event.wait(timeout = self.time_interval):
                print("macro is stopped...")
                self.stop_event.clear()
                return
