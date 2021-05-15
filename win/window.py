# main module

import win32api
import win32gui
import win32con
import time

class Window(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.hwnd = kwargs.get('hwnd', None)
        self.test_state = kwargs.get('test', False)
        # self.hwnd = self.find_window()
        self.dic = {}

    def leftClick(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        print('Left Click')
        pass

    def find_window(self):
        hwnd = win32gui.FindWindow(None, self.name)
        print(win32gui.GetClassName(hwnd))
        print(hwnd)
        hwnd = win32gui.FindWindow("ApplicationFrameWindow", self.name)
        print(win32gui.GetClassName(hwnd))
        print("current window hwnd : 0x{:08x}".format(hwnd))
        return hwnd

    def get_origin(self):
        hwnd = win32gui.GetForegroundWindow()
        (x, y) = win32api.GetCursorPos()
        return hwnd, (x, y)

    def back_origin(self, origin_hwnd, Pos):
        win32gui.ShowWindow(origin_hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(origin_hwnd)
        win32api.SetCursorPos(Pos)


    def set_foreground_window(self):
        # win32gui.ShowWindow(self.hwnd,5)
        
        win32gui.ShowWindow(self.hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(self.hwnd)
    
        # win32gui.ShowWindow(self.hwnd)
        print("set ForegroundWindow : 0x{:08x} : {}".format(self.hwnd, self.name))
        pass

    def click_target_window(self, Pos_ratio):
        (x, y) = Pos_ratio
        print("x, y : {}, {}".format(x, y))
        (left, top, right, bottom) = win32gui.GetWindowRect(self.hwnd)
        new_x = int(left + (right-left) * x / 100)
        new_y = int(top + (bottom-top) * y / 100)

        win32api.SetCursorPos((new_x, new_y))
        if not self.test_state :
            self.leftClick()
    
    def click_target_window_test(self, Pos_ratio):
        (x, y) = Pos_ratio
        print("x, y : {}, {}".format(x, y))
        (left, top, right, bottom) = win32gui.GetWindowRect(self.hwnd)
        new_x = int(left + (right-left) * x / 100)
        new_y = int(top + (bottom-top) * y / 100)

        win32api.SetCursorPos((new_x, new_y))



    def get_window_title(self):
        win_list = []
        win32gui.EnumWindows(self.callback, win_list)
        return win_list

    
    def callback(self, hwnd, strings):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            if window_title and right-left and bottom-top:
                strings.append('0x{:08x} : {}'.format(hwnd, window_title))
        
        return True

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

