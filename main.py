from PyQt5.uic.properties import QtWidgets
from win.window import Window
from ui.ui import Ui
from PyQt5 import QtWidgets, uic
import os
import yaml
import time
import sys


if __name__ == '__main__':
    cfg_file = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'config.yaml')
    with open(cfg_file, 'r', encoding="utf-8") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
        w = Window(None, **cfg['window'])

    # w.set_foreground_window()
    # w.get_window_title()



    app = QtWidgets.QApplication(sys.argv)
    ui = Ui(**cfg['ui'])
    ui.load_window_list(w.get_window_title())
    app.exec_()
