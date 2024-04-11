import os


game_path = os.path.dirname(os.path.dirname(__file__))
language_folder = game_path + "/data/language/"

from builtins import print as builtin_print

DEBUG = "d"
INFO = "i"
WARNING = "w"
ERROR = "e"
CRITICAL_ERROR = "c"
GAME_OUTPUT = "g"

PRINT_LEVELS = {
    DEBUG: 0,
    INFO : 1,
    WARNING : 2,
    ERROR : 3,
    CRITICAL_ERROR : 4,
    GAME_OUTPUT: 10
}



PRINT_SUPPRESSION_LEVEL = 0


def print(info_level: str | int, *values: object, sep: str | None = " ", end: str | None = "\n", file = None, flush: bool = True):
    global PRINT_LEVELS, PRINT_SUPPRESSION_LEVEL, ERROR
    
    if not isinstance(info_level, (str, int)):
        info_level = str(info_level)
    
    if values == ():
        if info_level in PRINT_LEVELS:
            info_level = 0
            values = ""
        else:
            values = [info_level]
            info_level = PRINT_LEVELS[ERROR]
    elif isinstance(info_level, str):
        info_level = PRINT_LEVELS[info_level]
    
    if info_level >= PRINT_SUPPRESSION_LEVEL:
        builtin_print(*values, sep=sep, end=end, file=file, flush=flush)



class translation():
    def __init__(self, language:str|None=None) -> None:
        if language: self.load_language(language)
    
    def __repr__(self):
        return self.get_translation(self.key)

    def load_language(self, name):
        global language_folder
        filetype = os.path.splitext(name)[1][1:]
        if not self.is_language_filetype_supported(filetype=filetype): self.language = {}, print(ERROR, "Unsupported language filetype")
        if not self.does_language_exit(name):  self.language = {}, print(ERROR, "Language file not found")
        
        with open(language_folder+name, "r") as f:
            if filetype == "json":
                import json
                dictionary = json.load(f)
                del json
            elif filetype == "json5":
                import json5
                dictionary = json5.load(f)
                del json5
        self.language = dictionary


    def does_language_exit(self, name):
        global language_folder
        return os.path.isfile(language_folder+name)

    def is_language_filetype_supported(self, filetype):
        return filetype in ["json", "json5"]


    def get_translation(self, key):
        """
        Retrieve translation for a given key from a language dictionary.
        
        Parameters:
            key (str): The key for which to retrieve the translation.
            language (dict): A dictionary containing translations, where keys are words or phrases,
                            and values are the translations in the corresponding language.
                            
        Returns:
            str: The translation if the key exists in the language dictionary, 
                otherwise returns the key itself.
        """
        # if not isinstance(language, dict):
        #     raise ValueError("The 'language' parameter must be a dictionary.")
        
        return self.language.get(key, key)



