from ..cursor_operations import pygui, WHEEL_DELTA


def getScreenDimensions() -> tuple[int, int]:
    return pygui.size()

SCREEN_WIDTH, SCREEN_HEIGHT = getScreenDimensions()

def mouseTo(x: int, y: int) -> None:
    pygui.moveTo(x,y)

def mouseGet() -> tuple[int, int]:
    return pygui.position()

def Click() -> None:
    pygui.click(_pause=False)

def RightClick() -> None:
    pygui.rightClick(_pause=False)

def MiddleClick() -> None:
    pygui.middleClick(_pause=False)

def ScrollV(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    pass # ???

def ScrollH(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    pass # ???

def Scroll(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    pygui.scroll(clicks, _pause=False)

def LeftMouseDown() -> None:
    pygui.keyDown("left", _pause=False)

def RightMouseDown() -> None:
    pygui.keyDown("right", _pause=False)

def MiddleMouseDown() -> None:
    pygui.keyDown("middle", _pause=False)

def LeftMouseUp() -> None:
    pygui.keyUp("left", _pause=False)

def RightMouseUp() -> None:
    pygui.keyUp("right", _pause=False)

def MiddleMouseUp() -> None:
    pygui.keyUp("middle", _pause=False)