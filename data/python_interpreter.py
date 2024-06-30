## The source code of the python interpreters
import sys, os



class ArgumentHandler:
    def __init__(self, arguments: None | list = None) -> None:
        if arguments is None:
            arguments = sys.argv[1:]
        self.arguments: list = arguments

    def get_argument(self, argument: str, is_unordered: bool = True) -> str | None:
        if not argument in self.arguments:
            return None
        value_id = self.arguments.index(argument)
        value = self.arguments.pop(value_id)
        if is_unordered:
            value = self.arguments.pop(value_id)
        return value

    def is_empty(self)->bool:
        return len(self.arguments) == 0


arguments = ArgumentHandler()


if arguments.is_empty():
    print("No arguments given")
    os._exit(0)

# File
file_location = arguments.get_argument("-file")

if file_location is None:
    print("No file location given")
    os._exit(0)

if not os.path.exists(file_location):
    print("Inputted file doesn't exist")
    os._exit(0)


# Encoding
encoding = arguments.get_argument("-encoding")
if encoding is None:
    encoding = "utf-8"
else:
    import encodings

    if not encoding in set(encodings.aliases.aliases.values()):
        print("Inputted encoding is not supported")
    os._exit(0)
    del encodings


# Directory to execute in
executing_directory = arguments.get_argument("-directory")

if not executing_directory is None:
    if not os.path.exists(executing_directory):
        print("Inputted executing directory doesn't exist")
        os._exit(0)

    current_directory = os.getcwd()

    def change_directory(target_directory: str):
        """
        Changes the current working directory to the target directory.

        Parameters:
        target_directory (str): The path to the directory to change to.

        Returns:
        None
        """
        try:
            os.chdir(target_directory)
        except Exception as e:
            print(
                f"An error occurred: '{e}', please report this\n\t-The change_directory function (python interpreter file)"
            )
            os._exit(0)

    change_directory(executing_directory)
else:
    current_directory = None




with open(file=file_location, encoding=encoding) as f:
    to_execute = f.read()
name = os.path.basename(file_location)


del arguments, ArgumentHandler, sys, file_location, encoding, __name__, __doc__, __package__,__spec__,__annotations__,executing_directory,__builtins__,f,__file__,__loader__


exec(compile(source=to_execute, filename=name,mode="exec",optimize=2))





if not current_directory is None:
    change_directory(current_directory)