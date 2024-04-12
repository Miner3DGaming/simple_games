from .cursor_operations import WINDOWS, CTYPES, USER32, KERNEL32, ctypes, CF_UNICODETEXT, GHND

if WINDOWS and CTYPES:
    def get_clipboard(user32 = USER32, kernel32 = KERNEL32) -> str: # About 20% faster on Windows than with pyperclip
        """
        Retrieve the current content of the system clipboard.

        Returns:
            str: The text content currently stored in the clipboard.
        """
        user32.OpenClipboard(0)
        handle = user32.GetClipboardData(CF_UNICODETEXT)

        # Lock the memory to get a pointer to the data
        locked_mem = kernel32.GlobalLock(handle)
        data = ctypes.c_wchar_p(locked_mem).value

        # Unlock and close the clipboard
        kernel32.GlobalUnlock(handle)
        user32.CloseClipboard()

        return data
    
    #set_clipboard_text
    def copy_to_clipboard(text, user32 = USER32, kernel32 = KERNEL32): # Roughly 95% to 1515% faster on Windows than pyperclip
        """
        Copy text to the system clipboard.

        Args:
            text (str): The text to be copied to the clipboard.
        """
        user32.OpenClipboard(0)
        user32.EmptyClipboard()

        # Allocate memory for the text and copy it
        handle = kernel32.GlobalAlloc(GHND, (len(text) + 1) * ctypes.sizeof(ctypes.c_wchar))
        locked_mem = kernel32.GlobalLock(handle)
        ctypes.memmove(locked_mem, text.encode('utf-16le'), (len(text) + 1) * ctypes.sizeof(ctypes.c_wchar))

        # Unlock and set the clipboard data
        kernel32.GlobalUnlock(handle)
        user32.SetClipboardData(CF_UNICODETEXT, handle)
        user32.CloseClipboard()

    
    def clear_clipboard(user32 = USER32) -> None: # Roughly 95% faster on Windows than pyperclip
        """
        Clear the contents of the clipboard.

        This function utilizes the 'pyperclip' library to copy an empty string to the clipboard,
        effectively clearing its contents.

        Returns:
            None: This function does not return any value.
        """
        user32.OpenClipboard(0)
        user32.EmptyClipboard()
        user32.CloseClipboard()

else:
    import pyperclip

    def copy_to_clipboard(text: str, user32 = None, kernel32 = None) -> None:
        """
        Copy text to the system clipboard.

        Args:
            text (str): The text to be copied to the clipboard.
        """
        pyperclip.copy(text)



    def get_clipboard(user32 = None, kernel32 = None) -> str:
        """
        Retrieve the current content of the system clipboard.

        Returns:
            str: The text content currently stored in the clipboard.
        """
        return pyperclip.paste()


    def clear_clipboard(user32 = None) -> None:
        """
        Clear the contents of the clipboard.

        This function utilizes the 'pyperclip' library to copy an empty string to the clipboard,
        effectively clearing its contents.

        Returns:
            None: This function does not return any value.
        """
        pyperclip.copy('')

from ..file_operations import get_file_extension

def save_clipboard_to_file(file_path: str) -> bool:
    """
    Saves the current contents of the clipboard to a specified file.

    This function attempts to open the specified file in write mode and writes the content
    currently stored in the clipboard to it. It uses the 'utf-8' encoding for writing the file.
    
    Args:
        file_path (str): The path to the file where the clipboard content will be saved.
        
    Returns:
        bool: Returns True if the clipboard content was successfully saved to the file,
            otherwise returns False if an error occurs during the process.
    """
    try:
        file = open(file_path, 'w', encoding='utf-8')
        file.write(get_clipboard())  # Assumes a 'get_clipboard()' function is defined elsewhere.
        file.close()
        return True
    except:
        return False


def load_clipboard_from_file(file_path: str) -> bool:
    """
    Loads text content from a file and copies it to the clipboard.

    This function reads the content of a file located at the given 'file_path',
    assuming it is encoded in UTF-8. The file's text content is then copied to
    the clipboard using the 'copy_to_clipboard' function. If the operation is
    successful, the function returns True. If any errors occur during file
    reading or clipboard copying, it returns False.

    Args:
        file_path (str): The path to the file from which content will be read.

    Returns:
        bool: True if the text was successfully copied to the clipboard, False otherwise.
    """
    try:
        file = open(file_path, 'r', encoding='utf-8')
        text = file.read()
        file.close()
        copy_to_clipboard(text)
        return True
    except:
        return False


def append_to_clipboard(text: str) -> None:
    """
    Appends the given text to the current content in the clipboard.

    Parameters:
    text (str): The text to be appended to the clipboard.

    Returns:
    None
        This function does not return any value.

    """
    clip = get_clipboard()
    clip += text
    copy_to_clipboard(clip)


def prepend_to_clipboard(text: str) -> None:
    """
    Prepends the provided text to the current clipboard content.

    This function takes a string 'text' and retrieves the current content
    of the clipboard using the 'get_clipboard()' function. It then prepends
    the provided 'text' to the clipboard content and updates the clipboard
    with the modified content using the 'copy_to_clipboard()' function.

    Parameters:
    text (str): The text to be prepended to the clipboard content.

    Returns:
    None: This function does not return any value, it directly modifies
        the clipboard content.
    """
    clip = get_clipboard()
    clip = text + clip
    copy_to_clipboard(clip)


def get_clipboard_size() -> int:
    """
    Get the size of the content currently stored in the clipboard.

    Returns:
        int: The size of the clipboard content in terms of the number of characters.
    """
    return len(get_clipboard())


def get_clipboard_file_extension() -> str:
    """
    Retrieves the file extension of the content currently stored in the clipboard.

    This function extracts the file extension from the content present in the clipboard.
    It first obtains the clipboard content using the 'get_clipboard()' function and then
    extracts the file extension using the 'get_file_extension()' utility function.

    Returns:
    str: The file extension of the content in the clipboard, or an empty string if no
        valid file extension is found.
    """
    return get_file_extension(get_clipboard())


