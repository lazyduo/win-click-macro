# main module

import win32api
import win32gui
import win32con
import time

class Window:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.hwnd = self.find_window()

        print(self.name)

    def leftClick():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        print('Left Click')
        pass

    def find_window(self):
        hwnd = win32gui.FindWindow(None, self.name)
        print("current window hwnd : {}".format(hwnd))
        return hwnd


    def set_foreground_window(self):
        # win32gui.ShowWindow(self.hwnd,5)
        win32gui.SetForegroundWindow(self.hwnd)
        # win32gui.ShowWindow(self.hwnd)
        print("set active window of {}".format(self.hwnd))
        pass


    # # hwnd = win32gui.GetActiveWindow()
    # # pos = (300, 900)
    # # win32api.SetCursorPos(pos)
    # hwnd = win32gui.FindWindow(None, "계산기")  
    # print(hwnd)

    # time.sleep(1)

    # pos = win32api.GetCursorPos()
    # print(pos)

    # (left, top, right, bottom) = win32gui.GetWindowRect(hwnd)

    # print("right: {}, top: {}".format(right, top))

    # right -= 10
    # top += 5

    # win32api.SetCursorPos((right, top))
    # leftClick()

