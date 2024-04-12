from ..cursor_operations import ctypes, MOUSE_EVENTF_ABSOLUTE, MOUSE_EVENTF_MOVE, MOUSEEVENTF_RIGHTUP, MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_MIDDLEUP, MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_LEFTUP, MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_WHEEL, MOUSEEVENTF_HWHEEL, CURSOR_POINT, WHEEL_DELTA



def getScreenDimensions() -> tuple[int, int]:
    return ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)


SCREEN_WIDTH, SCREEN_HEIGHT = getScreenDimensions()

def mouseTo(x: int, y: int, screen_width: int= SCREEN_WIDTH, screen_height: int = SCREEN_HEIGHT) -> None:

    # Calculate absolute position
    abs_x = int(65535 * (x / screen_width))
    abs_y = int(65535 * (y / screen_height))
    
    # Move the mouse cursor to the target position
    ctypes.windll.user32.mouse_event(MOUSE_EVENTF_MOVE | MOUSE_EVENTF_ABSOLUTE, abs_x, abs_y, 0, 0)

def mouseGet() -> tuple[int, int]:
    ctypes.windll.user32.GetCursorPos(ctypes.byref(CURSOR_POINT))
    return CURSOR_POINT.x, CURSOR_POINT.y

def Click() -> None:
    # Perform a left mouse button click
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTDOWN
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTUP

def RightClick() -> None:
    # Perform a right mouse button click
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)  # MOUSEEVENTF_RIGHTDOWN
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)  # MOUSEEVENTF_RIGHTUP

def MiddleClick() -> None:
    # Perform a middle mouse button click
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)  # MOUSEEVENTF_MIDDLEDOWN
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)  # MOUSEEVENTF_MIDDLEUP

def ScrollV(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    # Simulate scrolling the mouse wheel up by sending wheel events
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, wheel_delta * clicks, 0)

def ScrollH(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_HWHEEL, 0, 0, wheel_delta * clicks, 0)

def Scroll(dx: int = None, dy: int = None, wheel_delta_x: int = WHEEL_DELTA, wheel_delta_y: int = WHEEL_DELTA) -> None:
    if dx:
        ScrollH(dx, wheel_delta=wheel_delta_x)
    if dy:
        ScrollV(dy, wheel_delta=wheel_delta_y)

def LeftMouseDown() -> None:
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTDOWN

def RightMouseDown() -> None:
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)  # MOUSEEVENTF_RIGHTDOWN

def MiddleMouseDown() -> None:
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)  # MOUSEEVENTF_MIDDLEDOWN

def LeftMouseUp() -> None:
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTUP

def RightMouseUp() -> None:
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)  # MOUSEEVENTF_RIGHTUP

def MiddleMouseUp() -> None:
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)  # MOUSEEVENTF_MIDDLEUP