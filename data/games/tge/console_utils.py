
from . import time
from . import os
from sys import stdout as sys_stdout
from . import List, Union, Tuple , Any
from random import random, choice

from .tbe import determine_affirmative#, pass_func



def clear_console() -> Tuple[bool, str]:
    """
    Clears the console screen on Unix-like systems.

    :return: A tuple containing a boolean value indicating whether the screen was successfully cleared,
            and a string message describing the result of the operation.
            If an error occurs, the boolean value will be False and the message will include the specific
            error message.
    :rtype: tuple[bool, str]
    """
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        return True, "Screen cleared successfully"
    except Exception as e:
        return False, f"Error clearing screen: {str(e)}"
    





def typingPrint(text: str, delay: float) -> None:
    """
    Prints the given text with a typing effect.

    Args:
        text: The string to print.

    Returns:
        None
    """
    
    if not delay > 0:
        delay = 0.05
    for character in text:
        sys_stdout.write(character)
        sys_stdout.flush()
        time.sleep(delay)

def typingInput(text: str, delay: float = 0) -> str:
    """
    Displays the given text character by character with a delay of 0.05 seconds,
    then waits for the user to type a string and press Enter. Returns the entered string.

    Parameters:
    text (str): The text to be displayed before waiting for input.

    Returns:
    str: The string entered by the user.

    Example:
    >> typingInput("Please type your name: ")
    Please type your name: Alice
    'Alice'
    """
    if not delay > 0:
        delay = 0.05
    for character in text:
        sys_stdout.write(character)
        sys_stdout.flush()
        time.sleep(delay)
    value = input("")  
    return value

def writeSentencesToConsole(punctuations, o_text: str, type_delay: float, line_delay: float) -> Tuple[bool, str]:
    """
    Writes text and splits it into sentences with punctuations and prints them

    Args:
    - punctuations: a list of valid sentence-ending punctuations
    - o_text: the input text to split into sentences and print

    Returns:
    - A tuple containing a boolean indicating if the function succeeded and a message string
    """

    try:
        o_text = str(o_text)
        if type(punctuations) != list:
            punctuations [punctuations]
    except:
        return False

    punctuations = [".", "!", "?", ":", ";"]
    for punctuation in punctuations:
        o_text = o_text.replace(punctuation, punctuation + "Þ")
    text = o_text.split("Þ")
    idx = 0
    t_idx = 0

    if not line_delay >= 0:
        line_delay = 0.7

    # print(" ")
    # time.sleep(0.05)
    typingPrint(o_text[t_idx:len(text[idx])+t_idx], type_delay)
    time.sleep(line_delay)
    t_idx += len(text[idx])+1
    idx += 1

    for i in range(o_text.count("Þ")-1):
        print(" ")
        time.sleep(line_delay)
        write = (o_text[t_idx:len(text[idx])+t_idx])[1:]
        if not write == "":
            typingPrint(write, type_delay)
        t_idx += len(text[idx])+1
        idx += 1
    return True

def chooseFromTextMenu(text: list, prompt: str, ans_prompt: str) -> int:
    """
    Displays a text menu and prompts the user to choose an option.

    Args:
        text (list): List of options to display in the menu.
        prompt (str): Prompt to display before the menu.
        ans_prompt (str): Prompt to display when asking for user input.

    Returns:
        int: The index of the chosen option in the 'text' list.

    Raises:
        None.

    Example:
        text = ['Option 1', 'Option 2', 'Option 3']
        prompt = "Please select an option:"
        ans_prompt = "Enter the option number:"

        index = chooseFromTextMenu(text, prompt, ans_prompt)
        # User is prompted with the menu and enters an option number
        # Returns the index of the chosen option
    """
    chooseMenu = True
    print(prompt)
    while chooseMenu:
        for i in range(len(text)):
            typingPrint(f"{i}: {text[i]}")
            print(" ")
            time.sleep(0.05)
        time.sleep(0.25)
        answer = typingInput(ans_prompt)
            
        try:
            if answer in text:
                return text.index(answer)
            answer = int(answer)
            print("")
        except:
            print("")
        if type(answer) == int:
            if answer <= len(text) and answer >= 0:
                chooseMenu = False
                return int(answer)
            
def skip_line() -> None:
    """Prints a newline character to skip to the next line."""
    print("\n")

def print_table(data: List[List[str]]) -> Tuple[bool, str]:
    """
    Prints a table representation of the provided data.

    Args:
        data (list): A list of lists containing the data to be printed as a table.
    
    Returns:
        tuple: A tuple containing a boolean value and a string message.
            - The boolean value indicates the success or failure of the table printing.
            - The string message provides additional information in case of failure.
    
    Raises:
        None
    
    Example:
        data = [['Name', 'Age', 'Country'],
                ['John', 25, 'USA'],
                ['Emily', 32, 'Canada']]
        success, message = print_table(data)
        if success:
            print("Table printed successfully!")
        else:
            print("Error:", message)
    """
    try:
        # Determine the maximum length of each column
        column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

        # Print the table header
        header = "+" + "+".join("-" * (width + 2) for width in column_widths) + "+"
        print(header)
        
        # Print the table rows
        for row in data:
            formatted_row = "| " + " | ".join(str(item).ljust(width) for item, width in zip(row, column_widths)) + " |"
            print(formatted_row)
        
        # Print the table footer
        print(header)
        return True, ""
    except:
        return False, "Unable to print table, make sure the data is a list of lists"
    
def progress_bar(progress_name: str, current: int, total: int, length, show_float: bool = True, empty_tile: str = '-', full_tile: str = '#') -> None:
    """
    Displays a progress bar indicating the completion of a task.

    Parameters:
    - progress_name (str): Name of the progress bar (optional).
    - current (int): Current progress value.
    - total (int): Total value representing the completion of the task.
    - length: Length of the progress bar (number of tiles).
    - show_float (bool): Determines whether to show the percentage as a float or an integer.
    - empty_tile (str): Symbol representing empty tiles in the progress bar (default: '-').
    - full_tile (str): Symbol representing filled tiles in the progress bar (default: '#').

    Returns:
    None

    Example:
    >>> progress_bar("Loading", 50, 100, 20, False,'-', '#')
    Loading: [##########----------] 50%
    """
    if show_float:
        percent = float(int(float(current / total * 100) * 10) / 10)

    else:
        percent = int(current / total * 100)
    filled_length = int(length * current // total)


    bar = f'{full_tile}' * filled_length + f'{empty_tile}' * (length - filled_length)
    if progress_name == "":
        sys_stdout.write(f'\r[{bar}] {percent}%')
        sys_stdout.flush()
    else:
        sys_stdout.write(f'\r{progress_name}: [{bar}] {percent}%')
        sys_stdout.flush()

def colorize_text(text: str, color: str) -> str:
    """
    Colorizes the input text using the specified color.

    Args:
        text (str): The text to be colorized.
        color (str): The color to be applied to the text. It should be one of the following options:
                    'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
                    'bright_black', 'bright_red', 'bright_green', 'bright_yellow', 'bright_blue',
                    'bright_magenta', 'bright_cyan', 'bright_white', 'bg_black', 'bg_red',
                    'bg_green', 'bg_yellow', 'bg_blue', 'bg_magenta', 'bg_cyan', 'bg_white',
                    'bg_bright_black', 'bg_bright_red', 'bg_bright_green', 'bg_bright_yellow',
                    'bg_bright_blue', 'bg_bright_magenta', 'bg_bright_cyan', 'bg_bright_white',
                    or 'reset'.

    Returns:
        str: The colorized text.

    Raises:
        ValueError: If an invalid color is specified.
    """
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'bright_black': '\033[90m',
        'bright_red': '\033[91m',
        'bright_green': '\033[92m',
        'bright_yellow': '\033[93m',
        'bright_blue': '\033[94m',
        'bright_magenta': '\033[95m',
        'bright_cyan': '\033[96m',
        'bright_white': '\033[97m',
        'bg_black': '\033[40m',
        'bg_red': '\033[41m',
        'bg_green': '\033[42m',
        'bg_yellow': '\033[43m',
        'bg_blue': '\033[44m',
        'bg_magenta': '\033[45m',
        'bg_cyan': '\033[46m',
        'bg_white': '\033[47m',
        'bg_bright_black': '\033[100m',
        'bg_bright_red': '\033[101m',
        'bg_bright_green': '\033[102m',
        'bg_bright_yellow': '\033[103m',
        'bg_bright_blue': '\033[104m',
        'bg_bright_magenta': '\033[105m',
        'bg_bright_cyan': '\033[106m',
        'bg_bright_white': '\033[107m',
        'reset': '\033[0m'
    }
    if color not in colors:
        raise ValueError("Invalid color specified.")
    return colors[color] + text + colors['reset']

def visualize_directory(path, prefix='', lines=None) -> None:
    """
    Recursively visualizes the directory structure of a given path.

    Args:
        path (str): The path of the directory to visualize.
        prefix (str, optional): The prefix for indentation in the visualization.
                                Defaults to an empty string.
        lines (list, optional): The list to store the visualization lines.
                                Defaults to an empty list.

    Returns:
        None

    Raises:
        None

    This function recursively traverses the directory structure starting from
    the given path and prints the directory structure using ASCII characters.
    Directories are represented in square brackets and files are indicated with
    a forward slash ("/"). If a directory or file cannot be accessed due to
    permission issues, "(Access Denied)" is displayed.

    Example:
        >>> visualize_directory('/path/to/directory')
        [directory]
        ├── [subdirectory1]
        │   ├── /file1.txt
        │   └── [subsubdirectory]
        └── [subdirectory2]
            ├── /file2.txt
            └── /file3.txt
    """
    if lines is None:
        lines = []

    if prefix == '':
        base_name = os.path.basename(path)
        lines.append(f"[{base_name}]")

    is_last = False  # Define a default value for is_last

    try:
        with os.scandir(path) as entries:
            entries = list(entries)
            for i, entry in enumerate(entries):
                is_last = (i == len(entries) - 1)
                marker = "└──" if is_last else "├──"

                if entry.is_dir():
                    lines.append(f"{prefix}{marker}[{entry.name}]")
                    new_prefix = prefix + "│   " if not is_last else prefix + "    "
                    visualize_directory(entry.path, new_prefix, lines)
                else:
                    lines.append(f"{prefix}{marker}/{entry.name}")
    except PermissionError:
        marker = "└──" if is_last else "├──"  
        lines.append(f"{prefix}{marker}(Access Denied)")

    return lines

def clear_lines(num_lines: int, move_front: bool = False) -> None:
    """
    Clears a specified number of lines on the console screen.

    Args:
    num_lines (int): The number of lines to clear on the console screen.

    Returns:
    None: This function does not return anything.

    Raises:
    None

    Description:
    This function moves the cursor up num_lines lines on the console screen and clears the current line, effectively clearing a specified number of lines. It uses escape sequences to control the cursor and clear the line.

    Example:
    clear_lines(3)
    This will move the cursor up 3 lines and clear the current line, effectively clearing 3 lines on the console screen.
    """
    sys_stdout.write('\033[F' * num_lines) # Move the cursor up `num_lines` lines
    sys_stdout.write('\033[K') # Clear the current line and move the cursor to the beginning
    #if move_front is true, the cursor should be moved by 1 character
    if move_front:
        sys_stdout.write('\033[F')
        
    


def prompt_bool(question: str, none_return=None, tries: int=0, delete_lines = True, try_return=None) -> bool:
    """
    Prompts the user with a yes/no question and returns their response as a boolean value.
    
    Args:
        question (str): The question to prompt the user with.
        none_return (optional): The value to return if the user's input is not recognized as yes or no. 
                            Defaults to None, which means no return value will be provided in this case.
        tries (int, optional): The number of times the user can attempt to provide a valid response.
                            Defaults to 0, which means the user has an unlimited number of tries.
        delete_lines (bool, optional): Specifies whether to delete the previous lines of the console output 
                                    before displaying the question. Defaults to True.
        try_return (optional): The value to return if the user exceeds the maximum number of tries.
                            Defaults to None, which means no return value will be provided in this case.

    Returns:
        bool: True if the user responds affirmatively (e.g., 'yes', 'y'), False if the user responds negatively 
            (e.g., 'no', 'n'), or a custom return value specified by the `none_return` or `try_return` arguments.

    """
    tries_count = 0
    while True:
        tries_count += 1
        input_ans = str(input(question)).lower()
        ans = determine_affirmative(input_ans)
        if ans is not None:
            return ans
        else: 
            if none_return is not None:
                return none_return(input_ans)
        if tries > 0:
            if tries_count >= tries:
                if try_return is not None:
                    return try_return(input_ans)
                else:
                    return None
        if delete_lines:
            clear_lines(1)

def prompt_number(question: str, min: int=None, max: int=None, incorrect=None, error=None, delete_lines = True, tries=0, try_return=None) -> int:
    """
    Asks the user a number question and validates the input.

    Args:
        question (str): The question to ask the user.
        min (int, optional): Minimum allowed value. Defaults to None.
        max (int, optional): Maximum allowed value. Defaults to None.
        incorrect (callable, optional): Callback function to handle incorrect input. Defaults to None.
        error (callable, optional): Callback function to handle errors during input conversion. Defaults to None.
        delete_lines (bool, optional): Whether to delete previous lines. Defaults to True.
        tries (int, optional): Maximum number of tries. Defaults to 0.
        try_return (callable, optional): Callback function to handle reaching maximum tries. Defaults to None.

    Returns:
        int: The validated input number or None if maximum tries reached.

    Raises:
        ValueError: If the input cannot be converted to an integer.

    """
    tries_count = 0
    while True:
        tries_count += 1
        try:
            input_ans = int(input(question))
            if min is None or max is None:
                return input_ans
            elif min <= input_ans <= max:
                return input_ans
            else: 
                if tries > 0:
                    if tries_count >= tries:
                        if try_return is not None:
                            return try_return(input_ans)
                        else:
                            return None
                if delete_lines:
                    clear_lines(1)
                if incorrect is not None:
                    return incorrect(input_ans)
        except:
            if tries > 0:
                if tries_count >= tries:
                    if try_return is not None:
                        return try_return(input_ans)
                    else:
                        return None
            if delete_lines:
                clear_lines(1)
            if error is not None:
                return error(input_ans)


def matrix_rain(rows: int, columns: int, speed: float=0.1, density: float=0.2, matrix_time: float = None, symbols: list = ['0', '1']) -> None:
    """
    Displays a matrix rain animation on the console.

    Args:
        rows (int): The number of rows in the matrix.
        columns (int): The number of columns in the matrix.
        speed (float, optional): The speed at which the raindrops fall. Default is 0.1.
        density (float, optional): The density of raindrops in the matrix. Default is 0.2.
        matrix_time (float, optional): The duration (in seconds) for which the matrix rain should be displayed. If not provided, it runs indefinitely.

    Returns:
        None

    Raises:
        None

    Note:
        - The animation can be stopped by pressing a key if `matrix_time` is not provided.
        - The raindrops are represented by '0' and '1' characters.
        - The console is cleared before each frame is printed.
    """
    global tge_matrix_console_stop
    tge_matrix_console_stop = False
    mat_time = time.time()


    # Create an empty matrix
    matrix = [[' ' for _ in range(columns)] for _ in range(rows)]

    while True:
        # Generate a new row of raindrops
        for i in range(columns):
            if random() < density:
                matrix[0][i] = choice(symbols)
            else:
                matrix[0][i] = ' '

        # Move the raindrops down the matrix
        for i in range(rows - 1, 0, -1):
            for j in range(columns):
                matrix[i][j] = matrix[i-1][j]


        # Print the matrix
        clear_console()
        
        for row in matrix:
            print(''.join(row))
            
        if matrix_time is not None:
            if time.time() - mat_time > matrix_time:
                break
        elif tge_matrix_console_stop:
            break   
            
        time.time.sleep(speed)








from . import sys
from io import StringIO

class ConsoleCapture:
    def __init__(self) -> None:
        """
        A context manager for capturing and redirecting standard output.

        This class provides functionality to capture and redirect the standard output
        during its context, allowing you to capture printed output into a string buffer.

        Usage:
        ------
        To use this context manager, create an instance of OutputCapture within a `with` block.
        During the block's execution, any printed output will be captured into a buffer.
        """
        self.original_stdout = sys.stdout
        self.captured_output = StringIO()
        self.capturing = False
    
    def start_capture(self) -> None:
        """
        Start capturing the standard output if capturing is not already active.

        This method is used to redirect the standard output (stdout) to the captured output stream
        associated with this object. The captured output can be useful for logging or saving the
        output of specific code segments.

        If capturing is already active, calling this method will have no effect.
        """
        if self.capturing == False:
            sys.stdout = self.captured_output
    
    def stop_capture(self) -> None:
        """
        Stops capturing the standard output and restores the original stdout if capturing is currently active.

        This method checks the state of the 'capturing' attribute in the instance and, if it is currently set to True,
        it restores the original stdout stream, effectively stopping the redirection of output that was previously
        enabled by the 'start_capture' method.

        Parameters:
            self (object): The instance of the capturing class.
        """
        if self.capturing == True:
            sys.stdout = self.original_stdout
    
    def get_captured_output(self) -> StringIO:
        """
        Retrieve the content from the captured output buffer.

        This method returns the content stored in the internal captured output buffer,
        which is typically used to capture and store the output produced by various
        operations or functions. The buffer is first rewound to the beginning to ensure
        reading starts from the start of the content.

        Returns:
            str: The content stored in the captured output buffer.
        """
        self.captured_output.seek(0)
        return self.captured_output.read()

def suppress_print() -> None:
    """
    Temporarily suppresses the standard output (print statements) by capturing
    and redirecting them. This function initializes a global 'console_capture'
    object of type 'ConsoleCapture' and starts capturing the console output.
    
    Usage:
    suppress_print()
    # ... code block where print statements should be suppressed ...
    release_print()  # To release the suppressed print statements
    """
    global console_capture
    console_capture = ConsoleCapture()
    console_capture.start_capture()

def enable_print() -> StringIO:
    """
    Reverses the effect of a previously enabled console output capture,
    allowing the standard output to be displayed in the console again.

    This function stops the capture of console output that was previously
    initiated through the 'console_capture' global object. It retrieves the
    captured output and returns it as a string.

    Returns:
        str: The captured console output accumulated since capture started.
    """
    global console_capture
    console_capture.stop_capture()
    captured_output = console_capture.get_captured_output()
    return captured_output







