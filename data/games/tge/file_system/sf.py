import os

def _simple_hash(input_string: str, hash_value: int) -> int:
    """Create a simple hash without normalized values or a special collision algorithm."""
    for char in input_string:
        hash_value = (hash_value * 31 + ord(char)) % len(input_string)
    return hash_value

def simple_hash(input_string: str = "Hello World!") -> int:
    """Return a simple hash with a start hash of 0"""
    return _simple_hash(input_string, hash_value=0)

def _generate_random_number(seed : int, max : int) -> int:
    """Generate a 'random' number based on the given seed"""
    seed = (seed * 9301 + 49297) % 233280
    random_number = seed % max + 1
    return random_number

def generate_random_number(seed : str = "Hello world!", max : int =10) -> int:
    """Generate a 'random' number by generating a seed based on the given input string"""
    return _generate_random_number(_simple_hash(seed*max, 0), max)



#print(generate_random_number("", 1000))


class class_string:
    def __init__(self):
        pass


def lchop(string: str, substring: str) -> str:
    if string.startswith(substring):
        return string[len(substring):]
    else:
        return string

def rchop(string: str, substring: str) -> str:
    if string.endswith(substring):
        
        return string[:-len(substring)]
    else:
        return string

def chop(string: str, substring: str, rem: bool = True) -> str:
    if rem:
        if string.startswith(substring) and string.endswith(substring):
            return string[len(substring):-len(substring)]
        else: return string
    else:
        return lchop(rchop(string, substring), substring)


current_working_directory = os.getcwd()
home_directory = current_working_directory
default_offset_directory = ""
default_drive_letter = "C"



class SimFilDirSystem(): #Simple File Directory System
    def __init__(self, home_directory: str, current_drive_letter: str|None = None, current_offset_directory: str = "", create_missing_home_directory: bool = False, create_missing_offset_directory: bool = False, quit_notations = ["quit", "leave", "exit", "bye", "q"]): 
        
        # A variable to give information back.
        init_info = {}

        # If the current drive letter isn't provided, the default drive letter is used instead.
        if current_drive_letter is None:
            current_drive_letter = default_drive_letter
        
        # Setting the current directory (home directory without any "/" or "\\" at the end), directory branch and drive letter
        self.directory = class_string
        self.directory.home = lchop(home_directory.replace("\\", "/"), "/")
        self.directory.offset = chop(current_offset_directory.replace("\\", "/"), "/", rem=False)
        self.directory.drive_letter = current_drive_letter
        self.directory.full = self.directory.home + "/" + self.directory.offset
        
        self.last = str
        self.current_command_parameters_bool = bool
        self.input = str
        self.invalid_name_characters = ["/", "\\", ":", "*", "?", '"', "<", ">", "|"]
        

        # Removing the 
        
        if os.path.isdir(self.directory.home):
            init_info["home_directory"] = True
            if os.path.exists(self.directory.full):
                init_info["offset_directory"] = True
            else:
                init_info["offset_directory"] = False
        else:
            init_info["home_directory"] = False
            init_info["offset_directory"] = False

        if create_missing_home_directory:
            if create_missing_offset_directory:
                if not init_info["offset_directory"]:
                    os.mkdir(self.directory.full)
            elif not init_info["home_directory"]:
                os.mkdir(self.directory.home)
    

        # Setting the current command to nothing
        self.current_command = [str, list]

        # Setting stop notations and user commands
        self.quit_notations = quit_notations
        self.commands = {
            "change_directory" : {
                "cmd" : ["cd", "chdir", "change_directory"],
                "description" : "Displays the name of or changes the current directory.",
                "help" : "Displays the name of or changes the current directory.\n\nTo use this command you must specify one parameter as the path you to to append/change to."},
            
            "get_directory_items" : {
                "cmd" : ["dir", "get_directory_items"],
                "description" : "",
                "help" : ""},
            
            "make_directory" : {
                "cmd" : ["make_directory", "md", "mkdir", "create_directory", "crdir", "crd"],
                "description" : "Creates a directory.",
                "help" : "Create a directory with a given parameter.\n\nYou cannot create multiple directories like this: \n\tmkdir \\a\\b\\c\\d\n\nRather, you would need to use: \n\tmkdir a\n\tchdir a\n\tmkdir b\n\tchdir b\n\tmk c\n\tchdir c \n\tmkdir d"},
            
            "help" : {
                "cmd" : ["help"],
                "description" : "Provides information for commands.",
                "help" : "Provides information for commands.\n\nUse 'help [command]' to see more information about that command",
                "execute": self.help},
            
            "remove_directory" : {
                "cmd" : ["rm", "rmdir"],
                "description" : "", 
                "help" : ""},
            
            "rename_file" : {
                "cmd" : ["rename", "ren", "rename_file", "rn"],
                "description" : "Renames a file.",
                "help" : ""},

            "create_file" : {
                "cmd" : ["crf", "create_file", "crfile", "mkf", "mkfile", "make_file"],
                "description" : "",
                "help" : ""},

            "remove_file" : {
                "cmd" : ["rmf", "rmfile", "remove_file"],
                "description" : "",
                "help" : ""},

            "change_file" : {
                "cmd" : ["change", "chf", "ch", "change_file"],
                "description" : "",
                "help" : ""},
        
        }
    def get_command(self, command = None, parameters = None):
        if command is None:
            command = self.current_command[0]
        if parameters is None:
            parameters = self.current_command[1:]
        return command, parameters

    def execute(self, command = None):
        command = self.get_command(command=command)[0]
        for commands in self.commands:
            if command in self.commands[commands]["cmd"]:
                self.commands[commands]["execute"]()
            
        

    def help(self, command=None, parameters=None):
        print("help!")
        if command is None:
            pass

        

        






file_sys = SimFilDirSystem(home_directory=home_directory, current_drive_letter=default_drive_letter, current_offset_directory=default_offset_directory)

file_sys.execute(command="ch")

print(file_sys.directory.full)

