# Click Macro for Window

21-05-12

class가 "ApplicationFrameWindow"인 '계산기' 등의 프로그램은 FindWindow 할 시에 반드시 class를 지정해 주어야함.

`hwnd = win32gui.FindWindow("ApplicationFrameWindow", self.name)`

hwnd 문제 때문에 get_window_title로 모든 title을 받아서 select하여 설정하는 방식으로 구현 할 것.
