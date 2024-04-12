from . import os
import shutil
from filecmp import dircmp as file_dircmp, cmp as file_cmp
from ast import parse as ast_parse, walk as ast_walk, FunctionDef as ast_FunctionDef
import zipfile 

from pathlib import Path as pathlib_path
from . import List, Union, Tuple , Any
from . import REQUESTS, TKINTER, PYSHORTCUTS


if TKINTER:
    import tkinter as tk
if PYSHORTCUTS:
    import pyshortcuts

from .codec import decode, b64decode, b64encode

def create_missing_directory(directory: str) -> bool:
    """
    Creates a directory at the given path if it does not already exist.

    Args:
        directory (str): The path of the directory to create.

    Returns:
        Boolean: True if the directory was created, False if it already existed.

    If the directory already exists, this function does not modify it and does not raise any exceptions.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        return True
    else:
        return False

def delete_directory(directory: str) -> Tuple[bool, str]:
    """
    Deletes a directory and its contents.

    Args:
        directory (str): The name of the directory to delete.

    Returns:
        Tuple[bool, str]: A tuple with two items: a boolean indicating whether
        the directory was successfully deleted, and a string with a message
        indicating the result of the operation.
    """
    try:
        parent_dir = pathlib_path(__file__).resolve().parent
        full_path = os.path.join(parent_dir, directory)

        if os.path.exists(full_path):
            shutil.rmtree(full_path)
            return True, "Directory deleted"
        else:
            return False, "Directory not found"
    except:
        return False, "Error deleting directory"

def write_save_data(name: str, dir: str, data) -> Tuple[bool, str]:
    """
    Saves data to a file with the given name in the specified directory.

    :param name: The name of the file to be saved, without the ".save" extension.
    :param dir: The directory where the file should be saved.
    :param data: The data to be written to the file.
    :return: A tuple (success, message) where success is True if the file was saved
             successfully and False otherwise, and message is a string with a status
             message or an error message if an exception occurred.
    """
    try:
        name = name.replace(".save", "")
        file_path = os.path.join(dir, f"{name}.save")
        with open(file_path, "w") as f:
            f.write(data)
            return True, "File saved"
    except Exception as e:
        return False, f"Error saving file: {str(e)}"

def load_save_data(name: str, dir: str) -> Tuple[bool, str]:
    """
    Loads a file and returns the data.

    Args:
        name (str): The name of the .save file to load.
        dir (str): The directory containing the file to load.

    Returns:
        tuple: A tuple containing a boolean indicating success and the decoded data.
            The boolean is True if the file was loaded and decoded successfully, and False
            otherwise. The decoded data is returned as bytes if decoding was successful,
            or a string containing an error message if decoding was not successful.
    """
    try:
        name = name.rstrip(".save", "")
        file_path = os.path.join(dir, f"{name}.save")
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                data = f.read()
                success, decoded_data = decode(data)
                if success:
                    return True, decoded_data
                else:
                    return False, decoded_data
        else:
            return False, "File not found"
    except Exception as e:
        return False, f"Error loading file: {str(e)}"


def move_file(source_path: str, destination_path: str) -> bool:
    """
    Move a file from the source path to the destination path.

    This function checks if the file exists at the given source path and verifies its presence.
    If the file exists, it creates any missing directories in the destination path and then
    performs the file move using the `shutil.move` function. Returns True if the move is successful,
    and False if the source file does not exist.

    Args:
        source_path (str): The path to the source file.
        destination_path (str): The desired path for the moved file.

    Returns:
        bool: True if the file is successfully moved, False if the source file doesn't exist.

    Example:
        >>> move_file('source_folder/file.txt', 'destination_folder/file.txt')
        True
    """
    if doesDirectoryFileExist(source_path):
        create_missing_directory(destination_path)
        shutil.move(source_path, destination_path)
        return True
    else:
        return False

def copy_file(source_path: str, destination_path: str) -> bool:
    """
    Copies a file from the source path to the destination path.

    Args:
        source_path (str): The path to the source file.
        destination_path (str): The path where the file will be copied.

    Returns:
        bool: True if the file was successfully copied, False otherwise.
    """
    try:
        if doesDirectoryFileExist(source_path):
            create_missing_directory(destination_path)
            shutil.copy(source_path, destination_path)
            return True
        else:
            return False
    except:
        return False


def rename_file(source_path: str, name: str) -> bool:
    """
    Renames a file located at the given source path with the specified name.

    Args:
        source_path (str): The current path of the file to be renamed.
        name (str): The new name to be assigned to the file.

    Returns:
        bool: True if the file is successfully renamed, False otherwise.
    """
    try:
        if doesDirectoryFileExist(source_path):
            file_path = os.path.dirname(source_path)
            new_path = os.path.join(file_path, name)
            os.rename(source_path, new_path)
            return True
        else:
            return False
    except:
        return False

    
def copy_directory(source_path: str, destination_path: str) -> bool:
    """
    Copy the contents of a source directory to a destination directory.

    This function attempts to copy all files and subdirectories from the source directory
    to the destination directory. If the source directory exists and the copy operation is successful,
    the function returns True. If the source directory doesn't exist or an error occurs during the copy,
    the function returns False.

    Args:
        source_path (str): The path to the source directory to be copied.
        destination_path (str): The path to the destination directory where contents will be copied.

    Returns:
        bool: True if the copy operation is successful, False otherwise.
    """
    try:
        if doesDirectoryFileExist(source_path):
            create_missing_directory(destination_path)
            shutil.copytree(source_path, destination_path)
            return True
        else:
            return False
    except:
        return False


def move_directory(source_path: str, destination_path: str) -> bool:
    """
    Move a directory or file from the source path to the destination path.

    This function attempts to move the directory or file located at the source path
    to the specified destination path. If the source path points to an existing
    directory or file, the function creates any missing directories in the destination
    path and performs the move operation.

    Args:
        source_path (str): The path to the source directory or file.
        destination_path (str): The desired path for the moved directory or file.

    Returns:
        bool: True if the move operation is successful, False otherwise.

    Example:
        source_path = '/path/to/source_directory'
        destination_path = '/path/to/destination_directory'
        if move_directory(source_path, destination_path):
            print("Move successful!")
        else:
            print("Move failed or encountered an error.")
    """
    try:
        if doesDirectoryFileExist(source_path):
            create_missing_directory(destination_path)
            shutil.move(source_path, destination_path)
            return True
        else:
            return False
    except:
        return False


def rename_directory(source_path: str, name: str) -> bool:
    """
    Renames a directory at the given source path with the new provided name.

    This function attempts to rename the specified directory by changing its name
    to the provided new name while maintaining its location. The function first
    checks if the directory exists using the 'doesDirectoryFileExist' function.
    If the directory exists, it is renamed by updating its path accordingly.
    
    Args:
        source_path (str): The current path of the directory to be renamed.
        name (str): The new name to be assigned to the directory.

    Returns:
        bool: True if the directory was successfully renamed, False otherwise.
    """
    try:
        if doesDirectoryFileExist(source_path):
            file_path = os.path.dirname(source_path)
            new_path = os.path.join(file_path, name)
            os.rename(source_path, new_path)
            return True
        else:
            return False
    except:
        return False


def get_parent_path(path: str) -> str:
    """
    Returns the parent directory of a given path.
    param path: A string representing a path.
    type path: str
    return: A string representing the parent directory of the given path.
    rtype: str
    """
    return os.path.dirname(path)

def get_parent_folder(path: str) -> str:
    """
    Get the parent folder name from the given path.

    This function takes a path as input and returns the name of the parent folder.
    
    Args:
        path (str): A string representing the path to a file or directory.

    Returns:
        str: The name of the parent folder extracted from the path.

    Note:
        - The path can use either forward slashes ('/') or backslashes ('\\') as separators.
        - If the given path points to a directory, the name of the last folder in the path is returned.
        - If the given path points to a file, the name of the second-to-last folder in the path is returned.
          (This is assuming the file is located inside a folder within the path.)

    Examples:
        >>> get_parent_folder("C:\\Users\\Username\\Documents\\file.txt")
        'Documents'
        >>> get_parent_folder("/home/user/pictures/image.jpg")
        'user'
    """
    file_path = path.replace("\\", "/")
    if os.path.isdir(path):
        return file_path.split("/")[-1]
    else:
        final_file_path = file_path.split("/")[-2]
        #file_path = file_path.split("\\")[-1]
        # print(final_file_path)
        # print(file_path)
        # if os.path.isfile(file_path):
        #     return os.path.dirname(path)  
        return final_file_path
        
    

def combine_files(directory: str, output_directory: str, name: str) -> bool:
    """
    Combines multiple files from a directory into a single encrypted file.

    Args:
        directory (str): The directory path containing the files to be combined.
        output_directory (str): The directory path where the combined file will be saved.
        name (str): The name of the combined file (without extension).

    Returns:
        bool: True if the files are successfully combined and saved as an encrypted file,
              False if an error occurs during the process.

    Raises:
        Any exceptions raised during the execution will be caught and cause the function to return False.
    """
    try:
        file_data = []
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as file:
                    file_bytes = file.read()
                    file_data.append((file_name, file_bytes))
        
        combined_data = b''
        for file_name, file_bytes in file_data:
            combined_data += file_name.encode() + b':' + file_bytes + b'|'
        
        encoded_data = b64encode(combined_data)
        
        output_file = os.path.join(output_directory, name + '.encrypted')
        with open(output_file, 'wb') as file:
            file.write(encoded_data)
        
        return True
    except:
        return False

def split_file(directory: str, output_directory: str) -> bool:
    """
    Splits a combined encrypted file into individual files and saves them to the output directory.

    Args:
        directory (str): The path of the combined encrypted file.
        output_directory (str): The directory path where the individual files will be saved.

    Returns:
        bool: True if the combined file is successfully split into individual files and saved,
              False if an error occurs during the process.

    Raises:
        Any exceptions raised during the execution will be caught and cause the function to return False.
    """
    try:
        with open(directory, 'rb') as file:
            encoded_data = file.read()

        combined_data = b64decode(encoded_data)

        file_data = combined_data.split(b'|')[:-1]  # Remove the last empty element

        for data in file_data:
            file_name, file_bytes = data.split(b':', 1)
            output_file_path = os.path.join(output_directory, file_name.decode())
            with open(output_file_path, 'wb') as file:
                file.write(file_bytes)
        return True
    except:
        return False

def doesDirectoryFileExist(is_file: bool, directory: str) -> bool:
    """
    Check if a file or directory exists in the given path.

    Args:
        is_file (bool): True if checking for a file, False if checking for a directory.
        directory (str): The path to the file or directory.

    Returns:
        bool: True if the file or directory exists, False otherwise.
    """
    if is_file:
        if os.path.isfile(fr"{pathlib_path(__file__).resolve().parent}/{directory}") or os.path.isfile(directory):
            return True
        else:
            return False
    else:
        if os.path.exists(fr"{pathlib_path(__file__).resolve().parent}/{directory}" ) or os.path.exists(directory):
            return True
        else:
            return False

def doesFileExist(directory: str) -> bool:
    """
    Check if a file exists at the specified directory.

    Parameters:
    directory (str): The path to the directory or file to check.

    Returns:
    bool: True if the file exists and is a regular file, False otherwise.
    """
    return os.path.exists(directory) and os.path.isfile(directory)

def doesDirectoryExist(directory: str) -> bool:
    """
    Check if the specified directory exists and is a valid directory.

    Parameters:
    directory (str): The path to the directory to be checked.

    Returns:
    bool: True if the directory exists and is a valid directory, False otherwise.
    """
    return os.path.exists(directory) and os.path.isdir(directory)

def delete_file(name: str, dir: str) -> bool:
    """
    Deletes a file from a directory.

    Args:
        name (str): The name of the file to delete.
        dir (str): The name of the directory where the file is located.

    Returns:
        bool: True if the file was deleted, False otherwise.
    """
    if os.path.isfile(fr"{pathlib_path(__file__).resolve().parent}/{dir}/{name}"):
        os.system(f"rm {fr'{pathlib_path(__file__).resolve().parent}/{dir}/{name}'}")
        return True
    else:
        return False
    
def compare_file(directory1, directory2) -> Union[bool, str]:
    """
    Compares the contents of two files and returns True if they are identical, False otherwise.

    Args:
        directory1 (str): The path to the first file.
        directory2 (str): The path to the second file.

    Returns:
        bool: True if the contents of the files are identical, False otherwise.

    Raises:
        Any exception raised while opening or reading the files will be caught and the function will return False.

    """
    try:
        with open(directory1, "r") as f1, open(directory2, "r") as f2:
            return f1.read() == f2.read(), True
    except:
        return False, False

def compare_directory(directory1: str, directory2: str) -> Union[bool, str]:
    """
    Recursively compares the files in two directories and their subdirectories.

    Args:
        directory1 (str): The path to the first directory.
        directory2 (str): The path to the second directory.

    Returns:
        Union[bool, str]: 
        - If the directories are the same, returns True and a success message.
        - If the directories are different, returns False and an error message.
    """

    try:
        cmp = file_dircmp(directory1, directory2)
        
        for file in cmp.common_files: # Compare the files in the current directory
            file1 = os.path.join(directory1, file)
            file2 = os.path.join(directory2, file)
            if not file_cmp(file1, file2):
                return False
        
        for sub_cmp in cmp.subdirs.values(): # Recursively compare the files in subdirectories
            if not compare_directory(os.path.join(directory1, sub_cmp.left), os.path.join(directory2, sub_cmp.right)):
                return False
        
        return True, "Files are compared successfully"
    except OSError as e:
        return False, "Error: " + str(e)


def count_items_in_directory(directory_path) -> int:
    """
    Counts the number of items (files and directories) in the specified directory.

    Args:
        directory_path (str): The path of the directory.

    Returns:
        int: The total count of items in the directory.
    """
    return len(os.listdir(directory_path))

def get_current_working_directory() -> str:
    """
    Retrieve the current working directory path.

    Attempts to fetch the absolute path of the current working directory using the `os.getcwd()` function.
    
    Returns:
        str: The absolute path of the current working directory.
             Returns an empty string if an exception occurs during the retrieval process.
    """
    try:
        return os.getcwd()
    except:
        return ""


def get_file_extension(file_path: str) -> str:
    """
    Return the file extension from a given file path.

    :param file_path: A string representing the file path.
    :type file_path: str
    :return: A string representing the file extension.
    :rtype: str
    """
    return os.path.splitext(file_path)[1][1:]

def find_files_by_extension(directory_path: str, extension: str) -> list:
    """
    Retrieve a list of file names within the given directory that match the specified extension.

    Args:
        directory_path (str): The path to the directory where files will be searched.
        extension (str): The target file extension to filter files by.

    Returns:
        list: A list of file names that have the specified extension within the directory.
    """
    result = []
    for file in os.listdir(directory_path):
        _, file_extension = os.path.splitext(file)
        if file_extension == extension:
            result.append(file)
    return result


def get_file_size(file_path: str) -> int:
    """
    Get the size of a file located at the specified 'file_path'.

    This function checks if the provided path points to a valid file on the system.
    If the file exists, its size in bytes is returned; otherwise, 0 is returned.

    Args:
        file_path (str): The path to the file for which the size is to be determined.

    Returns:
        int: The size of the file in bytes if it exists, or 0 if the file doesn't exist.
    """
    if os.path.isfile(file_path):
        return os.path.getsize(file_path)
    else:
        return 0


def get_file_creation_time(file_path: str) -> str:
    """
    Retrieve the creation time of a file.

    This function takes a file path as input and returns the creation time
    of the file as a formatted string. If the provided path does not point
    to a valid file, an empty string is returned.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: A formatted string representing the creation time of the file,
        or an empty string if the file does not exist.
    """
    if os.path.isfile(file_path):
        return os.path.getctime(file_path)
    else:
        return ""

    
def count_functions_in_file(file_path: str) -> Tuple[int, list]:
    """
    Count and retrieve the names of top-level functions defined in the specified Python file.

    This function reads the content of the given Python file, parses its abstract syntax tree (AST),
    and identifies all top-level functions. It then returns the count of functions and a list of their names.

    Args:
        file_path (str): The path to the Python file to be analyzed.

    Returns:
        Tuple[int, list]: A tuple containing two elements:
            - The total number of top-level functions found in the file.
            - A list containing the names of the identified functions.

        If an error occurs during file reading or parsing, the function returns (0, []).
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tree = ast_parse(file.read())
            functions = [node.name for node in ast_walk(tree) if isinstance(node, ast_FunctionDef)]
            return len(functions), functions
    except:
        return 0, []


def count_functions_in_directory(directory_path: str) -> Tuple[int, dict, list]:
    """
    Counts the number of functions in all Python files within a directory and its subdirectories.
    Returns a dictionary where the keys are the file paths and the values are tuples with the count and names of functions.
    Also returns the total count of functions across all files.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        tuple: A tuple containing the dictionary with file paths and function details, and the total count of functions.

    Raises:
        NotADirectoryError: If the specified directory path does not exist or is not a directory.
        IOError: If there was an error while reading any of the files.

    Example:
        >>> count_functions_in_directory('my_directory')
        (
            4,
            {
                'my_directory/file1.py': (3, ['function1', 'function2', 'function3']),
                'my_directory/subdirectory/file2.py': (1, ['function4'])
            },
        )
    """
    function_counts = {}
    total_function_count = 0
    error_files = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        tree = ast_parse(file.read())
                        functions = [node.name for node in ast_walk(tree) if isinstance(node, ast_FunctionDef)]
                        function_counts[file_path] = (len(functions), functions)
                        total_function_count += len(functions)
                except IOError:
                    # Handle file read error
                    error_files.append(file_path)

    return total_function_count, function_counts, error_files

if REQUESTS:

    def init_url_functions():
        """
    Initializes URL-related functions for downloading files.

    This function imports the 'requests' library and defines a function 'download_from_url_to_dir'
    for downloading a file from a given URL and saving it to a specified directory.

    Functions:
        download_from_url_to_dir(url: str, dir: str, create: bool) -> None:
            Downloads a file from the given URL and saves it to the specified directory.

            Args:
                url (str): The URL of the file to be downloaded.
                dir (str): The directory where the downloaded file will be saved.
                create (bool): If True, creates the directory if it doesn't exist.

            Returns:
                None

            Raises:
                Any exceptions raised during the download and file write process are caught,
                and the function returns False if an exception occurs.

            Note:
                This function uses the 'requests' library to download the file. If 'create' is
                set to True, it creates the missing directory structure before saving the file.
                The file is saved with the same name as the last part of the URL.

            Example:
                download_from_url_to_dir(
                    'https://example.com/file.txt', '/path/to/directory/', create=True
                )
    """
        import requests
        def download_from_url_to_dir(url: str, dir: str, create: bool) -> None:
            """
            Downloads a file from the given URL and saves it to the specified directory.

            Args:
                url (str): The URL of the file to be downloaded.
                dir (str): The directory where the downloaded file will be saved.
                create (bool): If True, creates the directory if it doesn't exist.

            Returns:
                None

            Raises:
                Any exceptions raised during the download and file write process are caught,
                and the function returns False if an exception occurs.

            Note:
                This function uses the 'requests' library to download the file. If 'create' is
                set to True, it creates the missing directory structure before saving the file.
                The file is saved with the same name as the last part of the URL.

            Example:
                download_from_url_to_dir(
                    'https://example.com/file.txt', '/path/to/directory/', create=True
                )
            """
            r = requests.get(url)
            try:
                if create:
                    create_missing_directory(dir)
                    with open(dir + r.url.split('/')[-1], 'wb', encoding='utf-8') as f:
                        f.write(r.content)
                    return True
                else:
                    with open(dir + r.url.split('/')[-1], 'wb', encoding='utf-8') as f:
                        f.write(r.content)
                    return True
            except:
                return False
    
def count_function_names_in_directory(directory_path: str) -> Tuple[int, list]:
    """
    Count the total number of function names in Python files within the specified directory.

    This function recursively searches through all the Python files in the given directory
    and its subdirectories, tallying the total number of function names encountered. It returns
    a tuple containing the total count of function names and a list of unique function names.

    Args:
        directory_path (str): The path to the directory to be searched for Python files.

    Returns:
        Tuple[int, list]: A tuple containing the total count of function names and a list of
        unique function names extracted from the Python files.

    Note:
        This function depends on the 'count_functions_in_directory' utility function to perform
        the actual counting of function occurrences in the directory's Python files.
    """
    total_function_count, function_counts, error_files = count_functions_in_directory(directory_path)
    function_names = []

    for file_path, (count, names) in function_counts.items():
        for name in names:
            function_names.append(name)

    return len(function_names), function_names

def save_counted_function_names_from_directory(directory_path: str, file_name: str, output_path: str, create_missing_directory_bool: bool) -> bool:
    """
    Count the occurrences of function names in the Python files within the specified directory and save them to a file.

    Args:
        directory_path (str): The path to the directory containing Python files for function name counting.
        file_name (str): The name of the output file where the counted function names will be saved.
        output_path (str): The directory path where the output file will be saved.
        create_missing_directory_bool (bool): A flag indicating whether to create the output directory if it's missing.

    Returns:
        bool: True if the function names were successfully counted and saved, False otherwise.
    """
    functions = count_function_names_in_directory(directory_path)[1]
    if directory_path == "":
        directory_path = get_current_working_directory()
    
    if output_path == "":
        output_path = directory_path
    
    
    if file_name == "":
        file_name = "functions.txt"
    
    if create_missing_directory_bool:
        create_missing_directory(output_path)
    try:
        with open(output_path + file_name, 'w', encoding='utf-8') as f:
            for name in functions:
                f.write(name + '\n')
        return True
    except:
        return False
    
if TKINTER:
    def input_file_path(extension: str = None) -> str:
        """
        Prompts the user to select a file path for saving a file.

        This function opens a file dialog that allows the user to specify a file path
        for saving a file. The 'extension' parameter can be used to suggest a default
        file extension for the saved file.

        Parameters:
            extension (str, optional): A suggested file extension for the saved file.
                If provided, the file dialog will include this extension in the suggested
                file name and in the file type dropdown filter. Defaults to None.

        Returns:
            str: The selected file path for saving the file, including the chosen file name
            and extension.

        Note:
            This function requires the 'tkinter.filedialog' module to be imported in
            order to work properly.

        Example:
            >>> input_file_path(extension=".txt")
            '/path/to/save/file.txt'
        """
        return tk.filedialog.asksaveasfilename(defaultextension=extension)

    

    def input_directory_path() -> str:
        """
        Prompt user to select a directory using a file dialog.

        This function opens a file dialog window that allows the user to choose a directory.
        The selected directory's path is returned as a string.

        Returns:
            str: The path of the selected directory.
        """
        save_path = tk.filedialog.askdirectory()
        return save_path




def unzip_file(zip_path: str, extract_dir: str, create_missing_directory_bool: bool = False) -> Tuple[bool, bool]:
    """
    Unzips a zip file to the specified extract directory.
    
    Args:
        zip_path (str): pathlib_path to the zip file.
        extract_dir (str): Directory to extract the contents of the zip file to.
    """
    if zip_path == "":
        return False, False
    if extract_dir == "":
        return False, False
    try:
        if create_missing_directory_bool:
            existed = create_missing_directory(extract_dir)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        return True, True
    except:
        if create_missing_directory_bool:
            if existed:
                delete_directory(extract_dir)
        return False, True

def zip_directory(directory_path: str, output_path: str, create_missing_directory_bool: bool = False) -> Tuple[bool, bool]:
    """
    Zip a given directory and save the resulting zip file to the output path.

    Args:
        directory_path (str): pathlib_path to the directory to be zipped.
        output_path (str): pathlib_path to save the resulting zip file.

    Returns:
        None
    """
    if directory_path == "":
        return False, False
    if output_path == "":
        return False, False
    if not output_path.endswith(".zip"):
        output_path += ".zip"
    try:
        if create_missing_directory_bool:
            create_missing_directory(output_path)
        
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipfile:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipfile.write(file_path, os.path.relpath(file_path, directory_path))
        return True, True
    except: 
        return False, True

def get_appdata_path() -> str:
    """
    Retrieve the path to the 'AppData' directory of the current user.

    Returns:
        str: The expanded and absolute path to the 'AppData' directory.
    """
    return os.path.expanduser("~\AppData")


if PYSHORTCUTS:
    def create_shortcut(name: str, target_path: str, shortcut_path: str, description: str = "") -> None:
        """
        Creates a shortcut to a target file or script.

        This function generates a shortcut (or symbolic link) to a specified target file or script
        at the specified shortcut path location. Additional properties like the working directory,
        description, and execution settings can be customized for the shortcut.

        Args:
            name (str): The name of the shortcut (without the file extension).
            target_path (str): The path to the target file or script that the shortcut points to.
            shortcut_path (str): The path where the shortcut should be created.
            description (str, optional): An optional description for the shortcut (default is "").

        Returns:
            None

        Note:
            - The 'pyshortcuts' library is used to create the shortcut. Make sure it is installed.
            - The 'executable' parameter is set to 'target_path', indicating the executable to run
            when the shortcut is activated.

        Example:
            create_shortcut("MyScriptShortcut", "/path/to/myscript.py", "/desktop/shortcuts/",
                            "Shortcut to run my custom script.")
        """
        target_parent_folder = os.path.dirname(target_path)
        pyshortcuts.make_shortcut(name=name, script=target_path, working_dir=target_parent_folder, folder=shortcut_path, description=description, executable=target_path)

