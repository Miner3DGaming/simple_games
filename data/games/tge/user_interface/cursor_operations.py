from .. import CTYPES
from .. import PYNPUT
from .. import PYAUTOGUI
from .. import SYSTEM_NAME


if SYSTEM_NAME == "windows":
    WINDOWS = True
else:
    WINDOWS = False

KEYBOARD_MAPPING ={ #Generously stolen from pyautogui
    'backspace': 0x08, # VK_BACK
    '\b': 0x08, # VK_BACK
    'super': 0x5B, #VK_LWIN
    'tab': 0x09, # VK_TAB
    '\t': 0x09, # VK_TAB
    'clear': 0x0c, # VK_CLEAR
    'enter': 0x0d, # VK_RETURN
    '\n': 0x0d, # VK_RETURN
    'return': 0x0d, # VK_RETURN
    'shift': 0x10, # VK_SHIFT
    'ctrl': 0x11, # VK_CONTROL
    'alt': 0x12, # VK_MENU
    'pause': 0x13, # VK_PAUSE
    'capslock': 0x14, # VK_CAPITAL
    'kana': 0x15, # VK_KANA
    'hanguel': 0x15, # VK_HANGUEL
    'hangul': 0x15, # VK_HANGUL
    'junja': 0x17, # VK_JUNJA
    'final': 0x18, # VK_FINAL
    'hanja': 0x19, # VK_HANJA
    'kanji': 0x19, # VK_KANJI
    'esc': 0x1b, # VK_ESCAPE
    'escape': 0x1b, # VK_ESCAPE
    'convert': 0x1c, # VK_CONVERT
    'nonconvert': 0x1d, # VK_NONCONVERT
    'accept': 0x1e, # VK_ACCEPT
    'modechange': 0x1f, # VK_MODECHANGE
    ' ': 0x20, # VK_SPACE
    'space': 0x20, # VK_SPACE
    'pgup': 0x21, # VK_PRIOR
    'pgdn': 0x22, # VK_NEXT
    'pageup': 0x21, # VK_PRIOR
    'pagedown': 0x22, # VK_NEXT
    'end': 0x23, # VK_END
    'home': 0x24, # VK_HOME
    'left': 0x25, # VK_LEFT
    'up': 0x26, # VK_UP
    'right': 0x27, # VK_RIGHT
    'down': 0x28, # VK_DOWN
    'select': 0x29, # VK_SELECT
    'print': 0x2a, # VK_PRINT
    'execute': 0x2b, # VK_EXECUTE
    'prtsc': 0x2c, # VK_SNAPSHOT
    'prtscr': 0x2c, # VK_SNAPSHOT
    'prntscrn': 0x2c, # VK_SNAPSHOT
    'printscreen': 0x2c, # VK_SNAPSHOT
    'insert': 0x2d, # VK_INSERT
    'del': 0x2e, # VK_DELETE
    'delete': 0x2e, # VK_DELETE
    'help': 0x2f, # VK_HELP
    'win': 0x5b, # VK_LWIN
    'winleft': 0x5b, # VK_LWIN
    'winright': 0x5c, # VK_RWIN
    'apps': 0x5d, # VK_APPS
    'sleep': 0x5f, # VK_SLEEP
    'num0': 0x60, # VK_NUMPAD0
    'num1': 0x61, # VK_NUMPAD1
    'num2': 0x62, # VK_NUMPAD2
    'num3': 0x63, # VK_NUMPAD3
    'num4': 0x64, # VK_NUMPAD4
    'num5': 0x65, # VK_NUMPAD5
    'num6': 0x66, # VK_NUMPAD6
    'num7': 0x67, # VK_NUMPAD7
    'num8': 0x68, # VK_NUMPAD8
    'num9': 0x69, # VK_NUMPAD9
    'multiply': 0x6a, # VK_MULTIPLY
    'add': 0x6b, # VK_ADD
    'separator': 0x6c, # VK_SEPARATOR
    'subtract': 0x6d, # VK_SUBTRACT
    'decimal': 0x6e, # VK_DECIMAL
    'divide': 0x6f, # VK_DIVIDE
    'f1': 0x70, # VK_F1
    'f2': 0x71, # VK_F2
    'f3': 0x72, # VK_F3
    'f4': 0x73, # VK_F4
    'f5': 0x74, # VK_F5
    'f6': 0x75, # VK_F6
    'f7': 0x76, # VK_F7
    'f8': 0x77, # VK_F8
    'f9': 0x78, # VK_F9
    'f10': 0x79, # VK_F10
    'f11': 0x7a, # VK_F11
    'f12': 0x7b, # VK_F12
    'f13': 0x7c, # VK_F13
    'f14': 0x7d, # VK_F14
    'f15': 0x7e, # VK_F15
    'f16': 0x7f, # VK_F16
    'f17': 0x80, # VK_F17
    'f18': 0x81, # VK_F18
    'f19': 0x82, # VK_F19
    'f20': 0x83, # VK_F20
    'f21': 0x84, # VK_F21
    'f22': 0x85, # VK_F22
    'f23': 0x86, # VK_F23
    'f24': 0x87, # VK_F24
    'numlock': 0x90, # VK_NUMLOCK
    'scrolllock': 0x91, # VK_SCROLL
    'shiftleft': 0xa0, # VK_LSHIFT
    'shiftright': 0xa1, # VK_RSHIFT
    'ctrlleft': 0xa2, # VK_LCONTROL
    'ctrlright': 0xa3, # VK_RCONTROL
    'altleft': 0xa4, # VK_LMENU
    'altright': 0xa5, # VK_RMENU
    'browserback': 0xa6, # VK_BROWSER_BACK
    'browserforward': 0xa7, # VK_BROWSER_FORWARD
    'browserrefresh': 0xa8, # VK_BROWSER_REFRESH
    'browserstop': 0xa9, # VK_BROWSER_STOP
    'browsersearch': 0xaa, # VK_BROWSER_SEARCH
    'browserfavorites': 0xab, # VK_BROWSER_FAVORITES
    'browserhome': 0xac, # VK_BROWSER_HOME
    'volumemute': 0xad, # VK_VOLUME_MUTE
    'volumedown': 0xae, # VK_VOLUME_DOWN
    'volumeup': 0xaf, # VK_VOLUME_UP
    'nexttrack': 0xb0, # VK_MEDIA_NEXT_TRACK
    'prevtrack': 0xb1, # VK_MEDIA_PREV_TRACK
    'stop': 0xb2, # VK_MEDIA_STOP
    'playpause': 0xb3, # VK_MEDIA_PLAY_PAUSE
    'launchmail': 0xb4, # VK_LAUNCH_MAIL
    'launchmediaselect': 0xb5, # VK_LAUNCH_MEDIA_SELECT
    'launchapp1': 0xb6, # VK_LAUNCH_APP1
    'launchapp2': 0xb7, # VK_LAUNCH_APP2
    }

# for c in range(32, 128):
#     KEYBOARD_MAPPING[chr(c)] = ctypes.windll.user32.VkKeyScanA(ctypes.wintypes.WCHAR(chr(c)))

if CTYPES:
    import ctypes
    # for c in range(32, 128):
    #     KEYBOARD_MAPPING[chr(c)] = ctypes.windll.user32.VkKeyScanA(ctypes.wintypes.WCHAR(chr(c)))
    
    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

    USER32 = ctypes.windll.user32
    KERNEL32 = ctypes.windll.kernel32

    # // Mouse
    CURSOR_POINT = POINT()

    WHEEL_DELTA = 120  # The number of wheel clicks per notch
    MOUSE_EVENTF_MOVE = 0x0001 # Move Mouse Event
    MOUSEEVENTF_LEFTDOWN = 0x0002 # MOUSEEVENTF_LEFTDOWN
    MOUSEEVENTF_LEFTUP = 0x0004 # MOUSEEVENTF_LEFTUP
    MOUSEEVENTF_RIGHTDOWN = 0x0008 # MOUSEEVENTF_RIGHTDOWN
    MOUSEEVENTF_RIGHTUP = 0x0010 # MOUSEEVENTF_RIGHTUP
    MOUSEEVENTF_MIDDLEDOWN = 0x0020 # MOUSEEVENTF_MIDDLEDOWN
    MOUSEEVENTF_MIDDLEUP = 0x0040 # MOUSEEVENTF_MIDDLEUP
    MOUSEEVENTF_WHEEL = 0x0800  # Mouse wheel event
    MOUSEEVENTF_HWHEEL = 0x01000 # Horizontal wheel movement
    MOUSE_EVENTF_ABSOLUTE = 0x8000 # Move absolute event

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
    



if not CTYPES:
    for c in range(32, 128):
        KEYBOARD_MAPPING[chr(c)] = None



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

if True: #// Variants of setting the mouse position
    def set_mouse_pos(x: int,y: int) -> None:
        mouseTo(x, y)

    def moveTo(x: int, y: int) -> None:
        mouseTo(x, y)

    def set_mouse_location(x: int, y: int) -> None:
        mouseTo(x, y)

    def move_mouse(x: int, y: int) -> None:
        mouseTo(x, y)

    def set_mouse_position(x: int, y: int) -> None:
        mouseTo(x, y)

    def move_cursor(x: int, y: int) -> None:
        mouseTo(x, y)

    def set_pointer_position(x: int, y: int) -> None:
        mouseTo(x, y)

    def move_pointer(x: int, y: int) -> None:
        mouseTo(x, y)


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
    moveTo(x, y)
    RightClick()
    RightClick()

def TripleRightClickAt(x: int, y: int) -> None:
    moveTo(x, y)
    RightClick()
    RightClick()
    RightClick()

def TripleRightClick() -> None:
    RightClick()
    RightClick()
    RightClick()

def MiddleClickAt(x: int, y: int) -> None:
    moveTo(x, y)
    MiddleClick()

def DoubleMiddleClickAt(x: int, y: int) -> None:
    moveTo(x, y)
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