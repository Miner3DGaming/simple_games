
from . import List, Union, Tuple , Any
from uuid import uuid4
from random import randint, choice, shuffle, uniform, getrandbits
from string import ascii_letters as string_ascii_letters, digits as string_digits, ascii_lowercase

from . import REQUESTS
if REQUESTS:
    from requests import get as requests_get

from .codec import decode_html_character

if REQUESTS:
    def generate_name(gen: int, ) -> str:
        """
        Generate a random name based on the specified gender or unisex option.

        Args:
            gen (int): An integer representing the desired gender or option for the name.
                    0: Male (can also be represented as "m" or "male")
                    1: Female (can also be represented as "f" or "female")
                    2: Unisex (can also be represented as "u", "unisex", or "unidentified")
                    3: Both (can also be represented as "both" or "b")

        Returns:
            str: A randomly generated name based on the specified gender or option.
                Returns an empty string if the input is invalid.

        Note:
            This function uses the "https://www.behindthename.com/random/random.php" endpoint to
            generate random names.

        Example:
            >>> generate_name(0)
            'John'
            >>> generate_name(1)
            'Emily'
            >>> generate_name(2)
            'Alex'
            >>> generate_name(3)
            'Jordan'
        """

        if gen == 0 or "m" or "male":
            gender = "m"
        elif gen == 1 or "f" or "female":
            gender = "f"
        elif gen == 2 or "u" or "unisex" or "unidentified":
            gender = "u"
        elif gen == 3 or "both" or "b":
            gender = "both"
        else:
            return ""
        url = "https://www.behindthename.com/random/random.php"
        params = {
            "gender": gender,
            "number": "1",
            "sets": "1",
            "surname": "",
            "all": "yes"
        }
        response = requests_get(url, params=params)
        name_text = str(response.text.split("\n")[165])
        idx = name_text.find('class="plain">') + 14
        name_text = name_text[idx:]
        idx2 = name_text.find('<')

        # middle_name = name_text[:idx2]
        # middle_name = decode_html_character(middle_name)
        # idx = name_text.find('class="plain">') + 14
        # name_text = name_text[idx:]
        # idx2 = name_text.find('<')

        name = name_text[:idx2]
        name = decode_html_character(name)
        return (name)

def generate_uuid() -> str:
    """
    Generate a Universally Unique Identifier (UUID) using the uuid4() function.

    Returns:
        str: A string representation of the generated UUID.

    Example:
        >>> generate_uuid()
        '46c8b81f-e1b3-4d87-a4f3-f690d9b7e4b4'
    """
    return str(uuid4())

def generate_password(length: int) -> str:
    """
    Generates a random password of the given length.
    
    :param length: An integer representing the length of the password.
    :type length: int
    
    :return: A string representing the generated password.
    :rtype: str
    """
    chars = string_ascii_letters + string_digits
    return ''.join(choice(chars) for _ in range(length))

def randomBool() -> bool:
    """
    Returns a random boolean value.

    The function uses the `getrandbits` method from the `random` module to
    generate a random integer with one bit (i.e., either 0 or 1), and then
    converts it to a boolean value using the `bool` function. The probability
    of getting a `True` or `False` result is equal (i.e., 50/50).

    :return: A random boolean value (`True` or `False`).
    :rtype: bool
    """
    return bool(getrandbits(1))

def randomStringFromList(input_list: list) -> str:
    """
    Returns a random item from the input list.

    Args:
        input_list (list): List of items to choose from.

    Returns:
        str: A randomly selected item from input_list.
    """
    return choice(input_list)

def shuffleList(input_list: list) -> list:
    """Shuffles the elements of the input list and returns the shuffled list.

    Args:
        input_list (list): The list to be shuffled.

    Returns:
        list: A new list containing the same elements as input_list, but in a
            random order.

    Example:
        >> shuffleList([1, 2, 3, 4, 5])
        [4, 2, 5, 1, 3]
    """
    return shuffle(input_list)

def generate_random_hex_color() -> str:
    """
    Generates a random hex color code.
    
    :return: A string representing a hex color code.
    :rtype: str
    """
    return "#" + "".join(choice("0123456789ABCDEF") for _ in range(6))

def generate_random_color() -> tuple:
    """
    Generates a random color by generating three random integers between 0 and 255, inclusive.
    No parameters are taken in.
    Returns a tuple of three integers representing the RGB values of the generated color.
    """
    randint1 = randint(0, 255)
    randint2 = randint(0, 255)
    randint3 = randint(0, 255)
    return (randint1, randint2, randint3)

def generate_random_string(length: int=1) -> str:
    """
    Generates a random string of specified length.

    Args:
        length (int): The length of the random string to be generated.

    Returns:
        str: A random string of specified length.
    """
    return ''.join(choice(string_ascii_letters + string_digits) for _ in range(length))

def randomInt(min: int, max: int, float: bool = False) -> Union[Tuple[bool, Union[int, float]], Tuple[bool, str]]:
    """
    Returns a random integer between `min` and `max`, inclusive.

    Args:
        min (int): The minimum value the random integer can take.
        max (int): The maximum value the random integer can take.
        float (bool): If True, returns a float instead of an integer.

    Returns:
        Tuple[bool, Union[int, float]] or Tuple[bool, str]: 
            If the function succeeds, returns a tuple with the first element False and the random integer or float as the second element.
            If the function fails because `min` is greater than `max`, returns a tuple with the first element True and a message as the second element.
    """

    if min < max:
        if float:
            return uniform(min, max)
        else: 
            return randint(min, max)
    else: 
        if min == max:
            return (min)
        else:
            return 0