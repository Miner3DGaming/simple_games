# The original tge file with every single function in one big mess before splitting them across multiple files
# What a true beauty of random comments, miscellaneous code, and unfinished/discarded functions

# """
# This script imports various Python libraries and modules for performing different operations such as generating random numbers, 
# manipulating files and directories, playing audio files, handling errors, working with dates and times, 
# performing mathematical operations, and defining data types.

# Summary of operations:
# - Random: generate random numbers and shuffle sequences
# - Time: handle time-related operations
# - OS and pathlib: work with the operating system, including manipulating files and directories
# - Base64 and binascii: encode and decode binary data
# - Pygame.mixer: play audio files
# - Datetime: work with dates and times
# - Math: perform mathematical operations
# - Shutil: work with file and directory operations at a higher level of abstraction

# Modules:
# - random: for generating random numbers and shuffling sequences
# - time: for handling time-related operations
# - os, pathlib: for working with the operating system, including manipulating files and directories
# - base64, binascii: for encoding and decoding binary data
# - pygame.mixer: for playing audio files
# - datetime: for working with dates and times
# - math: for performing mathematical operations
# - shutil: for working with file and directory operations at a higher level of abstraction

# Defined data types:
# - List[T]: for defining a list of values of type T
# - Tuple[T, ...]: for defining an ordered, immutable sequence of values of type T
# - Union[T1, T2, ...]: for defining a variable that can have one of several types T1, T2, etc.
# """


# from time import sleep, timezone
# from os import system as os_system, path as os_path, environ, makedirs as os_createDirectory, listdir as os_listdir, getcwd as os_getcwd, rename as os_rename, remove as os_remove; environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# from sys import stdout as sys_stdout


#from pytz import timezone as pytz_timezone
#from math import sqrt, log, log2, modf, ceil, floor, factorial
from . import List, Union, Tuple , Any





#from numpy import median as np_median, abs as np_abs, corrcoef as np_corrcoef
# from requests import get as requests_get, post as requests_post
# from importlib import import_module as importlib_import_module
# from bs4 import BeautifulSoup
#from re import split as re.split


#log = []

# def wtl(txt, lvl):
#     if lvl == 0:
#         pre = "[Info: '"
#     elif lvl == 1:
#         pre = "[Warning: '"
#     elif lvl == 2:
#         pre = "[Error: '"
#     else: pre = "[Info: '"
#     log.append(pre + txt + "']")

#nor = randint(0, 100)


#inventory = []
# wtl("Initialized", 0)


# def initSession(message) -> None:
#     """Initializes the session.

#     Calls initSessionTime() and prints the given message.
#     Initializes the global enemies, inventory, and AttackTypes dictionaries.
#     """
#     initSessionTime()
#     print(message)
#     global enemies
#     global inventory
#     global AttackTypes
#     enemies = {}
#     inventory = {}
#     AttackTypes = {}








# def count_len(input_item: Any) -> int:
#     """
#     Returns the length of the input item.

#     Arguments:
#     - input_item: object to determine length of

#     Returns:
#     - length of input_item if it is a string or list
#     - -1 otherwise
#     """
#     if type(input_item) == list:
#         return len(input_item)
#     else:
#         try:
#             input_item = str(input_item)
#             return len(input_item)
#         except:
#             return -1


def pass_func(*args: Any) -> None:
    """
    This function does nothing and has no side effects.
    
    Returns:
        None: This function does not return any value.
    
    """
    pass





def execute_function(func=pass_func, *args: Any, **kwargs: Any) -> Any:
    """
    Executes a function with the given arguments and keyword arguments.

    Parameters:
        func (callable): The function to be executed. Defaults to 'pass_func'.
        *args (Any): Variable length arguments to be passed to the function.
        **kwargs (Any): Keyword arguments to be passed to the function.

    Returns:
        Any: The result of executing the function.

    Example:
        # Define a sample function
        def add_numbers(a, b):
            return a + b

        # Call the 'execute_function' with the 'add_numbers' function
        result = execute_function(add_numbers, 5, 3)
        # The result will be 8
    """
    return func(*args, **kwargs)








from difflib import get_close_matches

def determine_affirmative(text: str) -> bool:
    """
    Determines if the given text is an affirmative response or not.

    Args:
        text (str): The input text to be evaluated.

    Returns:
        bool: True if the text is an affirmative response, False if it is a negative response,
            and None if it cannot be determined.

    Example:
        >>> determine_affirmative("yeah")
        True
        >>> determine_affirmative("nope")
        False
        >>> determine_affirmative("maybe")
        None
    """
    positives = ["y", "yes", "yeah", "yup", "uh-huh", "sure", "affirmative", "absolutely", "indeed", "certainly", "of course", "definitely", "you bet", "roger", "right on", "no doubt", "by all means", "most certainly", "positively", "without a doubt", "naturally", "indubitably", "sure thing", "yuppers", "aye", "ok", "okey-dokey", "all right", "righto", "very well", "exactly", "precisely", "no problem", "for sure", "no doubt about it", "most assuredly", "you got it", "that's right", "sure as shooting", "all righty", "of course, my dear", "couldn't agree more", "a thousand times, yes", "i'm in", "it's a go", "i'll go along with that", "count me in", "i'm on board", "without hesitation", "undoubtedly", "yeye"]
    negatives = ["n", "no","nope","nah","nuh-uh","negative","not at all","absolutely not","certainly not","no way","never","i disagree","i'm afraid not","i can't agree with that","i beg to differ","i'm not convinced","not really","i'm not so sure","i'm inclined to say no","i have my doubts","that's not correct","that's incorrect","i don't think so","i'm not on board with that","i'm not buying it","i can't go along with that","i can't support that","i'm opposed to that","i'm against it","i'm not in favor of that","that's a negative","no chance","not a chance","no siree","i can't see that happening","i'm not inclined to agree","i can't accept that","i'm not on the same page","i'm not feeling it","i have reservations","i can't endorse that","that's out of the question","i can't support that notion","i'm skeptical","that doesn't work for me","i don't agree with that assessment","i don't think so","i'm not persuaded","i'm not buying into that","i don't subscribe to that view","i can't go along with that","i'm not swayed by that argument","i don't believe so","i'm not on board","i can't back that up","i'm not convinced of its validity","that's not my understanding","i'm not sold on that idea","i can't vouch for that", "i don't really feel like it", "not really"]

    closest_positive_match = get_close_matches(text, positives)
    closest_negative_match = get_close_matches(text, negatives)

    positive_blacklist = ["not really"]
    positive_whitelist = []
    if closest_positive_match and (text not in positive_blacklist or text in positive_whitelist):
        return True
    elif closest_negative_match:
        return False
    else:
        return None

def categorize_responses(text_list: List[str]) -> List[str]:
    """
    Categorizes a list of text responses as affirmative, negative, or uncertain.

    This function takes a list of text responses and categorizes each response
    as either affirmative, negative, or uncertain based on the result of the
    `determine_affirmative` function.

    Args:
        text_list (List[str]): A list of text responses to be categorized.

    Returns:
        List[str]: A list of categorized responses, where each response is
        classified as 'True' for affirmative, 'False' for negative, or 'None'
        for uncertain.

    Example:
        >>> responses = ["Yes", "No", "Maybe"]
        >>> categorized = categorize_responses(responses)
        >>> print(categorized)
        [True, False, None]
    """
    response_list = []

    for text in text_list:
        response = determine_affirmative(text)
        if response is True:
            response_list.append(True)
        elif response is False:
            response_list.append(False)
        else:
            response_list.append(None)

    return response_list

def get_available_variables() -> Tuple:
    """
    Retrieve and return the available global and local variables in the current scope.

    This function gathers both global and local variables, storing them in separate dictionaries.
    It collects global variables using the `globals()` function and local variables using the `locals()` function.
    The resulting dictionaries contain variable names as keys and their corresponding values as values.

    Returns:
        Tuple[Dict[str, Any], Dict[str, Any]]: A tuple containing two dictionaries.
        The first dictionary holds global variables, and the second dictionary holds local variables.
    """
    g_variables = {}
    l_variables = {}
    # Retrieve global variables
    global_vars = globals()
    for var_name, var_value in global_vars.items():
        g_variables[var_name] = var_value

    # Retrieve local variables
    local_vars = locals()
    for var_name, var_value in local_vars.items():
        l_variables[var_name] = var_value

    return g_variables, l_variables





# from tge.random_generators import randomInt
# from tge import console_utils

# def higher_lower_game(random_num: int = None, max_num: int = None, min_num: int = None, num_of_guesses: int = 0, num_range: int = None):
#     if random_num is None:
#         randomInt(0, 10, False)
    
    
#     random_num = 5
#     while True:
#         guess = console_utils.typingInput("Your Guess:", 0.01)
#         try:
#             guess = int(guess)
#             break
#         except:
#             console_utils.clear_lines(1)




# higher_lower_game()



#hi = "post_to_discord_webhook"

import inspect
def get_docstring(obj: object) -> str:
    """
    Retrieve the docstring of a given object.

    This function attempts to extract and return the docstring of the provided object.
    
    Args:
        obj (object): The object for which the docstring is to be retrieved.

    Returns:
        str: The docstring of the object if available, otherwise an empty string.
    """
    try:
        return inspect.getdoc(obj)
    except:
        return ""





def convert_number_to_words_less_than_thousand(n:str, dash:bool = True) -> str:
        """
        Converts a number (less than one thousand) to its word representation.

        Args:
            n (int): The number to be converted. Should be between 0 and 999.

        Returns:
            str: The word representation of the input number.

        Example:
            >>> convert_number_to_words_less_than_thousand(356)
            'three hundred and fifty-six'
        """

        TINY_NUMBERS = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
        ]
        SMALL_NUMBERS = [
            "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
            ]

        if n >= 100:
            hundreds_digit = n // 100
            rest = n % 100
            result = TINY_NUMBERS[hundreds_digit] + " hundred"
            if rest > 0:
                result += " and " + convert_number_to_words_less_than_thousand(rest)
            return result
        elif n >= 20:
            tens_digit = n // 10
            rest = n % 10
            result = SMALL_NUMBERS[tens_digit]
            if rest > 0:
                if dash:
                    result += "-" + TINY_NUMBERS[rest]
                else:
                    result += " " + TINY_NUMBERS[rest]
            return result
        else:
            return TINY_NUMBERS[n]

def number_to_words(number) -> str:
    """
    Converts a given integer into its English word representation.
    
    Args:
        number (int): The integer to be converted into words.
        
    Returns:
        str: The English word representation of the input integer.
        
    Examples:
        >>> number_to_words(123456789)
        'one hundred twenty-three million four hundred fifty-six thousand seven hundred eighty-nine'
        
        >>> number_to_words(-42)
        'minus forty-two'
        
        >>> number_to_words(0)
        'zero'
    """

    big_numbers = [
    "", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion",
    "sextillion", "septillion", "octillion", "nonillion", "decillion", "undecillion",
    "duodecillion", "tredecillion", "quattuordecillion", "quindecillion", "sexdecillion",
    "septendecillion", "octodecillion", "novemdecillion", "vigintillion", "unvigintillion",
    "duovigintillion", "trevigintillion", "quattuorvigintillion", "quinvigintillion", 
    "sexvigintillion", "septenvigintillion", "octovigintillion", "novemvigintillion",
    "trigintillion", "untrigintillion", "duotrigintillion", "trevigintillion", "quattuortrigintillion",
    "quintrigintillion", "sextrigintillion", "septentrigintillion", "octotrigintillion",
    "novemtrigintillion", "quadragintillion", "unquadragintillion", "duoquadragintillion",
    "trequadragintillion", "quattuorquadragintillion", "quinquadragintillion", "sexquadragintillion",
    "septenquadragintillion", "octoquadragintillion", "novemquadragintillion", "quinquagintillion",
    "unquinquagintillion", "duoquinquagintillion", "trequinquagintillion", "quattuorquinquagintillion",
    "quinquinquagintillion", "sexquinquagintillion", "septenquinquagintillion",
    "octaquinquagintillion", "novemquinquagintillion", "sexagintillion",
    "unsexagintillion", "duosexagintillion", "tresexagintillion", "quattuorsexagintillion",
    "quinsexagintillion", "sexsexagintillion", "septensexagintillion",
    "octasexagintillion", "novemsexagintillion", "septuagintillion", "unseptuagintillion",
    "duoseptuagintillion", "treseptuagintillion", "quattuorseptuagintillion",
    "quinseptuagintillion", "sexseptuagintillion", "septenseptuagintillion",
    "octaseptuagintillion", "novemseptuagintillion", "octagintillion",
    "unoctogintillion", "duooctogintillion", "treoctogintillion","quattuoroctogintillion",
    "quinoctogintillion", "sexoctogintillion", "septenoctogintillion",
    "octaoctogintillion", "novemoctogintillion", "nonagintillion", "unnonagintillion",
    "duononagintillion", "trenonagintillion", "quattuornonagintillion",
    "quinnonagintillion", "sexnonagintillion", "septennonagintillion",
    "octanonagintillion", "novemnonagintillion", "centillion", "cenuntillion",
    "centretillion", "cenquattuortillion", "cenquintillion", "censextillion",
    "censeptentillion", "cenoctotillion", "cennovemtillion", "cendecillion",
    "centredecillion", "cenquattuordecillion", "cenquindecillion", "censexdecillion",
    "censeptendecillion", "cenoctodecillion", "cennovemdecillion", "cenvigintillion",
    "cenunvigintillion", "cendovigintillion", "centrevigintillion",
    "cenquattuorvigintillion", "cenquinvigintillion", "censexvigintillion",
    "censeptenvigintillion", "cenoctovigintillion", "cennovemvigintillion",
    "centrigintillion", "cenuntrigintillion", "cendotrigintillion",
    "centretrigintillion", "cenquattuortrigintillion", "cenquintrigintillion",
    "censextrigintillion", "censeptentrigintillion", "cenoctotrigintillion",
    "cennovemtrigintillion", "cenquadragintillion", "cenunquadragintillion",
    "cendoquadragintillion", "centrequadragintillion",
    "cenquattuorquadragintillion", "cenquinquadragintillion",
    "censexquadragintillion", "censeptenquadragintillion",
    "cenoctoquadragintillion", "cennovemquadragintillion",
    "cenquinquagintillion", "cenunquinquagintillion",
    "cendoquinquagintillion", "centrequinquagintillion",
    "cenquattuorquinquagintillion", "cenquinquinquagintillion",
    "censexquinquagintillion", "censeptenquinquagintillion",
    "cenoctoquinquagintillion", "cennovemquinquagintillion",
    "censexagintillion", "cenunsexagintillion", "cendosexagintillion",
    "centresexagintillion", "cenquattuorsexagintillion",
    "cenquinsexagintillion", "cenquinsexagintilliard", "censexagintillion",
    "censexsexagintilliard", "censeptensexagintillion", "censeptensexagintilliard",
    "cenoctosexagintillion", "cenoctosexagintilliard", "cennovemsexagintillion",
    "cennovemsexagintilliard", "censeptuagintillion", "censeptuagintilliard",
    "cenunseptuagintillion", "cenunseptuagintilliard", "cendoseptuagintillion",
    "cendoseptuagintilliard", "centreseptuagintillion", "centreseptuagintilliard",
    "cenquattuorseptuagintillion", "cenquattuorseptuagintilliard", "cenquinseptuagintillion",
    "cenquinseptuagintilliard", "censexseptuagintillion", "censexseptuagintilliard",
    "censeptenseptuagintillion", "censeptenseptuagintilliard", "cenoctoseptuagintillion",
    "cenoctoseptuagintilliard", "cennovemseptuagintillion", "cennovemseptuagintillion",
    "cennovemseptuagintilliard", "cenoctogintillion", "cenoctogintilliard", "cenunoctogintillion",
    "cenunoctogintilliard", "cendooctogintillion", "cendooctogintilliard",
    "centreoctogintillion"
    ]

        
    # Handling special cases for zero and negative numbers
    if number == 0:
        return "zero"
    elif number < 0:
        return "minus " + number_to_words(abs(number))
    
    # Split the number into groups of three digits and convert each group to words
    groups = []
    while number > 0:
        groups.append(number % 1000)
        number //= 1000
    
    
    result_parts = []
    for i, group in enumerate(groups):
        if group != 0:
            result_parts.append(convert_number_to_words_less_than_thousand(group) + " " + big_numbers[i])
    
    # Join the parts and return the final result
    return ", ".join(reversed(result_parts))








import ast
import os

def find_undocumented_functions(file_path):
    undocumented_functions = []

    with open(file_path, 'r', encoding="utf8") as file:
        tree = ast.parse(file.read())

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if not ast.get_docstring(node):
                undocumented_functions.append(node.name)

    return undocumented_functions

def check_directory_for_undocumented_functions(directory_path):
    undocumented_functions_dict = {}

    for filename in os.listdir(directory_path):
        if filename.endswith('.py'):
            file_path = os.path.join(directory_path, filename)
            undocumented_functions = find_undocumented_functions(file_path)
            if undocumented_functions:
                undocumented_functions_dict[filename] = undocumented_functions

    return undocumented_functions_dict

def check_directory_and_sub_directory_for_undocumented_functions(directory_path):
    undocumented_functions_dict = {}

    def _check_directory_and_sub_directory_for_undocumented_functions_traverse_directory(current_path):
        for item in os.listdir(current_path):
            item_path = os.path.join(current_path, item)

            if os.path.isdir(item_path):
                # Recursively traverse subdirectories
                _check_directory_and_sub_directory_for_undocumented_functions_traverse_directory(item_path)
            elif item.endswith('.py'):
                undocumented_functions = find_undocumented_functions(item_path)
                if undocumented_functions:
                    # Store undocumented functions for the current file
                    filename = os.path.relpath(item_path, directory_path)
                    undocumented_functions_dict[filename] = undocumented_functions

    _check_directory_and_sub_directory_for_undocumented_functions_traverse_directory(directory_path)

    return undocumented_functions_dict











# def download_multiple_videos(video_dict, save_path):
#     video_infos = [(url_id, save_path, file_name) for url_id, file_name in video_dict.items()]
    
#     with Pool() as pool:
#         results = pool.map(download_youtube_video, video_infos)
    
#     return results



def autocomplete(prefix, word_list):
    return [word for word in word_list if word.startswith(prefix)]



























































































































































































































































































































































































































































































































































































































# Old way to check if a library exist. Very inefficient. Don't use.
# def test_for_library(library_name) -> bool:
#     if library_name in IGNORE_LIBRARIES:
#         return False
#     try:
#         start_importing = tm.time()
#         __import__(library_name)
#         import_times[library_name] = tm.time() - start_importing
#         installed_libraries.append(library_name)
#         del library_name
#         return True
#     except ModuleNotFoundError:
#         missing_libraries.append(library_name)
#         return False
#     except ImportError:
#         error_libraries.append(library_name)
#         return False














# types = {}

# def create_type(name: str, weak_against_type: list, strong_against_type: list, against_self: int):
#     name = name.lower()
#     weak_against_type = [weak.lower() for weak in weak_against_type]
#     strong_against_type = [strong.lower() for strong in strong_against_type]
    
#     strengths = []
#     weaknesses = []
    
#     for other_type, other_stats in types.items():
#         if name in other_stats["weak_against_type"]:
#             strengths.append(other_type)
#         if name in other_stats["strong_against_type"]:
#             weaknesses.append(other_type)
    
#     strengths.extend(strong_against_type)
#     weaknesses.extend(weak_against_type)
    
#     types[name] = {
#         "weak_against_type": weak_against_type,
#         "strong_against_type": strong_against_type,
#         "self": against_self,
#         "strengths": list(set(strengths)),
#         "weaknesses": list(set(weaknesses))
#     }




# def print_type_stats(input_type: str):
#     if input_type != "":
#         type_stats = types.get(input_type.lower())
#         if type_stats:
#             print_type_info(input_type, type_stats)
#     else:
#         for type_name, type_stats in types.items():
#             print_type_info(type_name, type_stats)
#             print()

# def print_type_info(type_name: str, type_stats: dict):
#     print(type_name.title() + ":")
#     print("\t•Weak against:")
#     weak_against_type = type_stats["weak_against_type"]
#     print_type_attributes(weak_against_type)
    
#     print("\n\t•Strong against:")
#     strong_against_type = type_stats["strong_against_type"]
#     print_type_attributes(strong_against_type)
    
#     print("\n")
#     print_type_damage_to_self(type_stats["self"])


# def print_type_attributes(attributes: list):
#     for attribute in attributes:
#         print("\t\t" + attribute.title())

# def print_type_damage_to_self(damage_value: int):
#     if damage_value == 0:
#         print("\t•Deals normal damage to its own type")
#     elif damage_value == 1:
#         print("\t•Deals strong damage to its own type")
#     elif damage_value == 2:
#         print("\t•Deals weak damage to its own type")
#     elif damage_value == 3:
#         print("\t•Is immune to its own type")

# def get_weaknesses(type_name: str):
#     weaknesses = []
#     for other_type, other_stats in types.items():
#         if type_name.lower() in other_stats["strong_against_type"]:
#             weaknesses.append(other_type)
#     return weaknesses

# def get_strengths(type_name: str):
#     strengths = []
#     for other_type, other_stats in types.items():
#         if type_name.lower() in other_stats["weak_against_type"]:
#             strengths.append(other_type)
#     return strengths

# def missing_types(type_name: str):
#     all_types = []
#     if type_name == "":
#         for m_type in types:
#             for strong in types[m_type]["strong_against_type"]:
#                 if strong not in all_types:
#                     all_types.append(strong)
#             for weak in types[m_type]["weak_against_type"]:
#                 if weak not in all_types:
#                     all_types.append(weak)

#         print("Missing types:")
        
#         for check_type in all_types:
#             if check_type not in types and check_type != "":
#                 print(check_type.title())

# create_type("ice", ["lava", ""], ["fire"], 2)
# create_type("wood", ["lava","magma", "fire"], ["earth"], 0)
# create_type("wind", ["stone", "earth"], ["water"], 3)
# create_type("fire", ["stone"], ["wood"], 0)
# create_type("water", ["magma", "lava", "ice"], ["fire", "stone"], 2)
# create_type("rock", ["magma"], [""], 1)
# create_type("grass", ["fire", "lava", "magma", "rock"], ["earth"], 0)
# create_type("stone", ["water"], ["wind"], 0)
# create_type("magma", ["fire"], [""], 0)

# print_type_stats("")
# missing_types("")

# def newEnemy(name: str, entity_type: str, health: int, attack: int, defense: int, speed: int, resistant: list, weakness: list, behavior: int, loot: list):
#     if type(weakness) != list:
#         try:
#             weakness = list(weakness)
#         except: return False, "Weakness must be lists or strings"
#     if not type(resistant) != list:
#         try:
#             resistant = list(resistant)
#         except: return False, "Resistance must be lists or strings"

#     if not type(resistant) == list:
#         return False, "Resistance must be a list"
#     elif not type(weakness) == list:
#         return False, "Weakness must be a list"

#     if not name in enemies:
#         if name != "":
#             if entity_type != "":
#                 if health > 0:
#                     if attack >= 0:
#                         if defense >= 0:
#                             if behavior >= 0:
#                                 enemies[name] = {"health": health, "type": entity_type, "attack": attack, "defense": defense, "speed": speed, "resistance": resistant, "weakness": weakness, "behavior": behavior, "loot": loot}
#                                 return True, "Enemy created"
#                             else: return False, "Behavior must be greater or equal to 0"
#                         else: return False, "Defense must be greater or equal to 0"
#                     else: return False, "Attack must be greater or equal to 0"
#                 else: return False, "Health must be greater than 0"
#             else: return False, "Entity type cannot be empty"
#         else: return False, "Name cannot be empty"
#     else: return False, "Enemy already exists"


#def doesEnemyExist(name: str):
#    return name in enemies


#def attackEnemy(name: str, damage: int, type):
#    x = enemies.items()
#    damage = damage-enemies[name]["resistance"]
#    if damage <= 0: 
#        damage = 0
#    
#    if name in enemies:
#        enemies[name] = {**enemies[name], "health": enemies[name]["health"] - damage, "type": type}
#    else: return False, "Enemy does not exist"

#def newAttackType(name, weakness):
#    AttackTypes[name]



#initSession()
#newEnemy("test", 10, 10, 10, 10, 10, 10, 10, 10, [])
#x, y = newEnemy("test2", 10, 10, 10, 10, ["hi"], ["no"], 10, 10, ["stuff"])
#print(x)
#print(y)
#newEnemy("test2", 10, 10, 10, 10, 10, 10, 10, 10, [])
#print(doesEnemyExist("test"))
#attackEnemy("test", 10, "test")

#print(enemies)


