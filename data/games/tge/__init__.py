# __init__.py

import time as tm; start_import = tm.time()
importing = __name__ != '__main__'

__version__ = '1.0.0'
__name__ = "tge"
__author__ = "Miner3D"
__license__ = "LGPL, GNU Lesser General Public License"

__doc__ = """
    tge - Text Game Engine
    Originally made for displaying and creating console-based games but has evolved into a general-purpose library.

    This library provides a wide range of functions and utilities for text-based game development, console operations,
    data manipulation, conversions, math calculations, user interfaces, file operations, and more.

    With a collection of over 700 functions, tge tries to simplify the development process and offers capabilities for
    building text-based games, console applications, file manipulation, and various quality of life functions. (yep)
    """

"747 Functions"
"46 Files"
"Yep"
"That's totally manageable and not messy even in the slightest. Easily manageable by a solo developer"
"I'm always open for feedback so if you found a bug or have any suggestions, I'm grateful to hear them (well not actually since they are bugs and bugs are usually not good in these situations)"

# Import Times Dictionary
import_times = {}


start_importing = tm.time()
import sys

if importing:
    from .mini_lib import import_lib_mini
    from .mini_lib import platform_mini
else:
    import importlib.util as import_lib_mini
    import platform as platform_mini

import os
from typing import List, Union, Tuple , Any, Optional, Dict
from pathlib import Path as pathlib_path
import_times["build-in"] = tm.time() - start_importing


def init_internet_connectivity():
    """Initialize the internet connectivity tester."""
    import urllib.request
    global is_internet_connected
    def is_internet_connected(max_timeout: int = 5, website: str = "https://www.google.com"):
        """
        The internet connectivity tester.
        
        Input:
            >>> max_timeout = int(seconds)
            >>> website = str("Website to test for")
        """
        try:
            urllib.request.urlopen(website, timeout=max_timeout)
            return True
        except Exception as e:
            return False
    


def get_system():
    """Returns the current user system"""
    if sys.platform.startswith("java"):
        return "jython"
    elif sys.platform == "darwin":
        return "darwin"
    elif sys.platform == "win32":
        return "windows"
    elif platform_mini.system() == "Linux":
        return "linux"
    else:
        return "unknown"

SYSTEM_NAME = get_system()



# Library Installation Configuration
INSTALL_MISSING_LIBRARIES = False
install_custom_libraries = []

# Check for Environment Variables

# Hide Pygame Support Prompt
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

# Lists for Tracking Libraries
missing_libraries = []
error_libraries = []
installed_libraries = []

# Function to Test for Library Existence
def test_for_library(library_name) -> bool:
    """
    Tests for the accessability of a library using a custom mini 
    version of "import_lib" mostly only using the essential 
    functions needed for existence a library.
    """

    spec = import_lib_mini.find_spec(library_name)
    if spec is not None:
        installed_libraries.append(library_name)
        return True
    else:
        missing_libraries.append(library_name)
        return False

# Function to Download and Install Missing Libraries
def download_library(library_name: str) -> Tuple[str, bool]:
    """
    Downloads and installs a Python library using pip.

    Parameters:
        library_name (str): The name of the library to be installed.

    Returns:
        tuple: A tuple containing a boolean indicating whether the installation was successful
        and a message string providing additional information in case of an error.
        """
    import subprocess
    global installed_libraries
    try:
        subprocess.check_call(['pip', 'install', library_name])
        installed_libraries.append(library_name)
        return True, ""
    except subprocess.CalledProcessError as e:
        return False, str(e)


if "tge_install_missing_libraries" in os.environ:
    INSTALL_MISSING_LIBRARIES = True


# Check for the Existence of Specific Libraries
PYGAME = test_for_library("pygame")           # pygame
TKINTER = test_for_library("tkinter")         # tkinter
PYAUTOGUI = test_for_library("pyautogui")     # pyautogui
GTTS = test_for_library("gtts")               # gtts
PYPERCLIP = test_for_library("pyperclip")     # pyperclip
RE = test_for_library("re")                   # re
PYTUBE = test_for_library("pytube")           # pytube
PYSHORTCUTS = test_for_library("pyshortcuts") # pyshortcuts
PIL = test_for_library("PIL")                 # pillow
BS4 = test_for_library("bs4")                 # bs4
PYNPUT = test_for_library("pynput")           # pynput
CTYPES = test_for_library("ctypes")           # ctypes
NUMPY = test_for_library("numpy")             # numpy
SCREENINFO = test_for_library("screeninfo")   # screeninfo
PYGETWINDOW = test_for_library("pygetwindow") # pygetwindow

if PYTUBE or BS4:
    REQUESTS = True
else:
    REQUESTS = test_for_library("requests")   # requests


# Install Missing Libraries (if internet is connected)

if INSTALL_MISSING_LIBRARIES:
    if len(missing_libraries) > 0:
        for i in missing_libraries:
            successful, error = download_library(i)
                

if len(install_custom_libraries) > 0:
    for i in install_custom_libraries:
        download_library(i)

# Printing Timing Information (if not importing as a module)
if not importing:
    INIT_TIME = tm.time() - start_import
    library_importing_time = 0
    for i in import_times:
        library_importing_time += import_times[i]
    
    
    import_times = sorted(import_times.items(), key=lambda x: x[1])
    idx = 0
    sorted_import_times = {}
    for i in import_times:
        sorted_import_times[import_times[idx][0]] = import_times[idx][1]
        idx += 1
    import_times = dict(reversed(list(sorted_import_times.items())))



    print(f"\nTotal loading time: {INIT_TIME}")
    print(f"Library importing time: {library_importing_time}")
    print(f"Total loading time without library importing time: {INIT_TIME - library_importing_time}")
    # for i in import_times:
    #     print(f"{i}: {import_times[i]}")
    
    if len(missing_libraries) > 0:
        print(f"\nMissing libraries: ")
        for lib in missing_libraries:
            print(f"\t {lib}")

    if len(error_libraries) > 0:
        print(f"\nErrored on these libraries: ")
        for lib in error_libraries:
            print(f"\t{lib}")
    quit()

INIT_TIME_BEFORE_IMPORTING = tm.time() - start_import





#   Import modules from "manipulation"
from .manipulation import string_utils
from .manipulation import list_utils
from .manipulation import dictionary_utils as dict_utils

#   Import modules from "compatibility"
if PYGAME:
    def load_tge_pygame():
        from .compatibility import tge_pygame
        return tge_pygame

if TKINTER:
    def load_tge_tkinter():
        from .compatibility import tge_tkinter
        return tge_tkinter



#   Import modules from "conversion"
from .conversion import convert_binary as binary
from .conversion import convert_temperature as temperature
from .conversion import convert_time as time
from .conversion import convert_units as units
from .conversion import data_conversion as data


#   Import modules from "math_functions"
from .math_functions import financial_calculations 
from .math_functions import geometry_calculations
from .math_functions import math_functions
from .math_functions import statistics_calculations


#   Import modules from "user_interface"
def load_system_interaction():
    from .user_interface import system_interactions
    from .user_interface import clipboard
    return system_interactions, clipboard


#   Import modules from root directory
def load_tge_alternative_functions():
    from . import alternatives
    return alternatives
def load_tge_audio():
    from . import audio
def load_console_utils():
    from . import console_utils
    return console_utils
def load_random():
    from . import random_generators as tge_random
    return tge_random
def load_validation():
    from . import validation
    return validation
def load_internet():
    from . import internet
    return internet
from . import tbe
from . import codec
from . import time_utils
from . import file_operations
from . import formatting_utils as formatting
from . import bool_operations
from . import bitwise
#from .file_system import SimDirFilSystem


if PIL:
    def load_image_processing():
        from . import image_processing
        return image_processing

if BS4:
    def load_game_scrapper():
        from . import steam_scrapper
        return steam_scrapper





tim = tm.time()
IMPORT_TIME = tim - INIT_TIME_BEFORE_IMPORTING
INIT_TIME = tim - start_import
del tim, INSTALL_MISSING_LIBRARIES, install_custom_libraries
