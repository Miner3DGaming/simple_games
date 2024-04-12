from .. import CTYPES
from .. import PYNPUT
from .. import PYAUTOGUI
from .. import SYSTEM_NAME


if SYSTEM_NAME == "windows":
    WINDOWS = True
else:
    WINDOWS = False




if CTYPES:
    import ctypes

    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

    USER32 = ctypes.windll.user32
    KERNEL32 = ctypes.windll.kernel32

    # // Mouse
    CURSOR_POINT = POINT()

    WHEEL_DELTA = 120               # The number of wheel clicks per notch
    MOUSE_EVENTF_MOVE = 0x0001      # Move Mouse Event
    MOUSEEVENTF_LEFTDOWN = 0x0002   # MOUSEEVENTF_LEFTDOWN
    MOUSEEVENTF_LEFTUP = 0x0004     # MOUSEEVENTF_LEFTUP
    MOUSEEVENTF_RIGHTDOWN = 0x0008  # MOUSEEVENTF_RIGHTDOWN
    MOUSEEVENTF_RIGHTUP = 0x0010    # MOUSEEVENTF_RIGHTUP
    MOUSEEVENTF_MIDDLEDOWN = 0x0020 # MOUSEEVENTF_MIDDLEDOWN
    MOUSEEVENTF_MIDDLEUP = 0x0040   # MOUSEEVENTF_MIDDLEUP
    MOUSEEVENTF_WHEEL = 0x0800      # Mouse wheel event
    MOUSEEVENTF_HWHEEL = 0x01000    # Horizontal wheel movement
    MOUSE_EVENTF_ABSOLUTE = 0x8000  # Move absolute event

    # // Clipboard
    CF_TEXT = 1
    CF_UNICODETEXT = 13
    GMEM_DDESHARE = 0x2000
    OPEN_EXISTING = 3
    GMEM_MOVEABLE = 0x0002
    GMEM_ZEROINIT = 0x0040
    GHND = (GMEM_DDESHARE | GMEM_MOVEABLE) 
    


elif PYNPUT:
    ...
    




if CTYPES:
    ...
        
elif PYNPUT:
    ...

elif PYAUTOGUI:
    import pyautogui as pygui







if WINDOWS and CTYPES:
    from .cursor.cursor_operations_ctypes import *

elif PYNPUT:
    from .cursor.cursor_operations_pynput import *
    
elif PYAUTOGUI: 
    from .cursor.cursor_operations_pyautogui import *
else:
    def mouseTo(x: int, y: int) -> tuple[int, int]:
        pass

    def mouseGet() -> tuple[int, int]:
        return (-1, -1)
    
    def Click() -> None:
        pass

    def RightClick() -> None:
        pass

    def MiddleClick() -> None:
        pass

    def Scroll(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
        pass
    
    def LeftMouseDown() -> None:
        pass
    
    def RightMouseDown() -> None:
        pass

    def MiddleMouseDown() -> None:
        pass

    def LeftMouseUp() -> None:
        pass

    def RightMouseUp() -> None:
        pass

    def MiddleMouseUp() -> None:
        pass






def ClickMouseButton(button_number: int) -> None:
    ClickMouseButtonList[button_number]()

def HoldMouseButton(button_number: int) -> None:
    HoldMouseButtonList[button_number]()

def ReleaseMouseButton(button_number: int) -> None:
    ReleaseMouseButtonList[button_number]()

def ClickMouseButtonAt(button_number: int, x: int, y: int) -> None:
    ClickMouseButtonAtList[button_number](x, y)

# if True: #// Variants of setting the mouse position
#     def set_mouse_pos(x: int,y: int) -> None:
#         mouseTo(x, y)

#     def moveTo(x: int, y: int) -> None:
#         mouseTo(x, y)

#     def set_mouse_location(x: int, y: int) -> None:
#         mouseTo(x, y)

#     def move_mouse(x: int, y: int) -> None:
#         mouseTo(x, y)

#     def set_mouse_position(x: int, y: int) -> None:
#         mouseTo(x, y)

#     def move_cursor(x: int, y: int) -> None:
#         mouseTo(x, y)

#     def set_pointer_position(x: int, y: int) -> None:
#         mouseTo(x, y)

#     def move_pointer(x: int, y: int) -> None:
#         mouseTo(x, y)


def LeftClick() -> None:
    Click()

def ClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    Click()

def DoubleClick() -> None:
    Click()
    Click()

def DoubleClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    Click()
    Click()

def TripleClick() -> None:
    Click()
    Click()
    Click()

def TripleClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    Click()
    Click()
    Click()

def RightClickAt(x: int, y: int) -> None:
    MouseTo(x, y)
    RightClick()

def DoubleRightClick() -> None:
    RightClick()
    RightClick()

def DoubleRightClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    RightClick()
    RightClick()

def TripleRightClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    RightClick()
    RightClick()
    RightClick()

def TripleRightClick() -> None:
    RightClick()
    RightClick()
    RightClick()

def MiddleClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    MiddleClick()

def DoubleMiddleClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    MiddleClick()
    MiddleClick()

def DoubleMiddleClick() -> None:
    MiddleClick()
    MiddleClick()

def TripleMiddleClick() -> None:
    MiddleClick()
    MiddleClick()
    MiddleClick()

def TripleMiddleClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    MiddleClick()
    MiddleClick()
    MiddleClick()





def drag_to(x,y):
    pygui.dragTo(x,y)

def drag_obj_to(x, y, a, b):
    mouseTo(x,y)
    hold_left_mouse()
    drag_to(a,b)
    release_left_mouse()

def hold_left_mouse():
    pygui.mouseDown("left")

def release_left_mouse():
    pygui.mouseUp("left")

def hold_right_mouse():
    pygui.mouseDown("right")

def release_right_mouse():
    pygui.mouseUp("right")

def hold_middle_mouse():
    pygui.mouseDown("middle")

def release_middle_mouse():
    pygui.mouseUp("middle")

def hold_mouse(mouse):
    if is_valid_mouse_buttons():
        pygui.mouseDown(mouse)
        return True
    else:
        return False

def release_mouse(mouse):
    if is_valid_mouse_buttons(mouse):
        pygui.mouseUp(mouse)
        return True
    else:
        return False

def is_valid_mouse_buttons(x):
    return x in ["left", "right", "middle"]




ClickMouseButtonList = [Click, MiddleClick, RightClick]
ClickMouseButtonAtList = [ClickAt, MiddleClickAt, RightClickAt]
HoldMouseButtonList = [LeftMouseDown, RightMouseDown, MiddleMouseDown]
ReleaseMouseButtonList = [LeftMouseUp, RightMouseUp, MiddleMouseUp]