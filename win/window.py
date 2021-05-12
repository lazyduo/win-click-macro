# main module

import win32api
import win32gui
import win32con
import time

class Window:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        print(self.name)
    


    # def leftClick():
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #     time.sleep(.1)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #     print('Left Click')

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

