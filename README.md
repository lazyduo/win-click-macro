# Click Macro for Window


# Memo & TODO

- 21-05-12

class가 "ApplicationFrameWindow"인 '계산기' 등의 프로그램은 FindWindow 할 시에 반드시 class를 지정해 주어야함.

`hwnd = win32gui.FindWindow("ApplicationFrameWindow", self.name)`

hwnd 문제 때문에 get_window_title로 모든 title을 받아서 select하여 설정하는 방식으로 구현 할 것.


- 21-05-13
 
gui class, window control class, main 기본 연결 완료.


- 21-05-14 TODO

[pynput](https://github.com/moses-palmer/pynput) -> mouse listner를 통해서 클릭 위치를 받아 올 것.

adjustment 버튼 클릭 -> 마우스 움직일 때 마다 좌표 업로드. 클릭시 해당 좌표 기억.

sequence 만들기. 클릭, 엔터, 타이핑 등의 sequence를 추가하여 run 할 수 있도록 구현
