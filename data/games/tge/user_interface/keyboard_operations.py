from .. import PYAUTOGUI
from .. import CTYPES
from .cursor_operations import WINDOWS


if CTYPES and WINDOWS:
    ...


elif PYAUTOGUI:
    import pyautogui as pygui


    from ..user_interface.clipboard import get_clipboard

    def hold_key(key):
        pygui.keyDown(key)

    def release_key(key):
        pygui.keyUp(key)

    def press_key(key):
        pygui.press(key)

    def press_keys(keys):
        for key in keys:
            pygui.press(key)

    def paste(x):
        pygui.typewrite(x)

    def paste_clipboard():
        pygui.typewrite(get_clipboard())

    def press_keys_from_clipboard():
        for key in get_clipboard():
            press_key(key)

