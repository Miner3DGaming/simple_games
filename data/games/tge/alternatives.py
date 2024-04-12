

from time import sleep  
from math import sqrt, log, ceil, floor
from . import List, Union, Tuple , Any
from . import sys

from . import PYGAME
if PYGAME:
    from pygame import quit as pygame_quit



def wait(seconds: int) -> None:
    """
    This function waits for a specified number of seconds.
    """
    sleep(seconds)

def pause(seconds: int) -> None:
    """
    This function pauses the program for a specified number of seconds.
    """
    sleep(seconds)

def num_abs(num: Union[int, float]) -> float:
    """
    Returns the absolute value of a number.
    """
    return abs(num)

def num_sqrt(num: Union[int, float]) -> float:
    """
    Returns the square root of a number.
    """
    return sqrt(num)

def num_log(num: Union[int, float]) -> float:
    """
    Returns the natural logarithm of a number after taking its absolute value.
    """
    return log(abs(num))

def num_floor(num: Union[int, float]) -> int:
    """
    Returns the floor of a number.
    """
    return floor(num)

def ceiling(num: Union[int, float]) -> int:
    """
    Returns the ceiling of a number.
    """
    return ceil(num)

if PYGAME:
    def safe_exit() -> None:
        """
        Safely exits the program if pygame is still running.
        """
        pygame_quit()
        sys.exit()

    def safe_quit() -> None:
        """
        Safely exits the program if pygame is still running.
        """
        pygame_quit()
        sys.exit()

def force_exit() -> None:
    """
    Exits the program forcefully.
    This function is an alternative for the `os.exit()` function.
    """
    sys.exit()