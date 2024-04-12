
from . import RE, REQUESTS

if RE:
    import re

if REQUESTS:
    import requests

from ipaddress import IPv4Address, IPv6Address, AddressValueError

from .manipulation.string_utils import reverse_string




def is_empty(text) -> bool:
    """
    Returns a boolean indicating whether the given text is empty or not.

    :param text: A string to check if it is empty.
    :type text: str
    :return: True if the given text is empty, False otherwise.
    :rtype: bool
    """
    return text == ""

def is_prime(number: int) -> bool:
    """
    Determines whether a given integer is a prime number or not.
    
    :param number: An integer to check for primality.
    :type number: int
    :return: True if the given number is prime, False otherwise.
    :rtype: bool
    """
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_palindrome(string: str) -> bool:
    """
    Check if a given string is a palindrome.

    :param string: A string to be checked.
    :type string: str
    :return: True if the string is a palindrome, False otherwise.
    :rtype: bool
    """
    return string == reverse_string(string)

def is_leap_year(year: int) -> bool:
    """
    Determine if a given year is a leap year or not.

    A leap year occurs every 4 years, except for years that are both divisible
    by 100 and not divisible by 400. These exceptions ensure that the calendar
    year remains synchronized with the astronomical year.

    Args:
        year (int): The year to be checked for leap year status.

    Returns:
        bool: True if the input year is a leap year, False otherwise.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_even(number: int) -> bool:
    """
    Determine whether the given integer is an even number.

    Parameters:
    number (int): The integer to be checked for evenness.

    Returns:
    bool: True if the input number is even, False otherwise.
    """
    return number % 2 == 0

def is_odd(number: int) -> bool:
    """
    Determine whether an integer is odd.

    Args:
        number (int): The integer to be checked for oddness.

    Returns:
        bool: True if the input integer is odd, False if it's even.
    """
    return not is_even(number)

if RE:
    def is_url(url: str) -> bool:
        """
        Check if a given string is a valid URL.

        This function uses regular expressions to determine whether the input string
        follows the typical pattern of a URL. It checks for patterns starting with
        'http://' or 'https://' followed by a valid domain name, and optional
        paths or query parameters.

        Args:
            url (str): The string to be checked as a potential URL.

        Returns:
            bool: True if the input string appears to be a valid URL, False otherwise.
        """
        pattern = re.compile(
            r'^(?:http|https)://'
            r'(?:[\w-]+\.)*[\w-]+'
            r'(?:\.[a-zA-Z]{2,})'
            r'(?:/?|(?:/[^\s]+)+)?$'
        )

        return bool(re.match(pattern, url))
else:
    def is_url(url: str) -> bool:
        """
        Check if a given URL is valid and reachable.

        This function takes a URL as input and determines by 
        checking if it can be reached with an URL check.

        If the 're' library is installed this function will change and check if the url is valid without needing to 
        
        Args:
            url (str): The URL to be checked.

        Returns:
            bool: True if the URL is considered valid and reachable, False otherwise.
        """
        if REQUESTS:
            return is_url_available(url=url, check_url=False)
        else:
            return None


if REQUESTS:
    def is_url_available(url: str, check_url: bool = True) -> bool:
        """
        Check the availability of a URL by sending a GET request and evaluating the response status code.

        Parameters:
        url (str): The URL to be checked for availability.
        check_url (bool, optional): If True, performs a basic URL format check before proceeding (default: True).

        Returns:
        bool: True if the URL is available and returns a status code of 200, False otherwise.
        """
        if check_url:
            check_url = not is_url(url)

        if not check_url:
            return False

        try:
            r = requests.get(url)
            if r.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout:
            return None
        

else:
    def is_url_available(url: str, check_url: bool = True) -> False:
        """
    This is a Fallback function if the 'requests' module isn't installed.

    Returns:
        bool: False
    """
        return False
    
def validate_email(email: str) -> bool:
    """
    Validate an email address using a regular expression pattern match.

    :param email: A string representing an email address.
    :type email: str
    :return: A boolean indicating whether the email address is valid or not.
    :rtype: bool
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_password(password, length: int, upper: bool, lower: bool, digit: bool, overwrite_special_characters: bool, overwritten_special_characters: str) -> bool:
    """
    Validates a password based on specified criteria.

    Args:
        password (str): The password string to be validated.
        length (int): The minimum required length of the password.
        upper (bool): Whether the password must contain at least one uppercase letter.
        lower (bool): Whether the password must contain at least one lowercase letter.
        digit (bool): Whether the password must contain at least one digit.
        overwrite_special_characters (bool): If True, the provided special characters will be used for validation.
                                            If False, a default set of special characters will be used.
        overwritten_special_characters (str): A string containing special characters to be used for validation,
                                            applicable only if overwrite_special_characters is True.

    Returns:
        bool: True if the password is valid based on the specified criteria, False otherwise.
    """
    # Check if password length is at least 8 characters
    if len(password) < length:
        return False

    # Check if password contains at least one uppercase letter
    if upper:
        if not any(char.isupper() for char in password):
            return False

    # Check if password contains at least one lowercase letter
    if lower:
        if not any(char.islower() for char in password):
            return False

    # Check if password contains at least one digit
    if digit:
        if not any(char.isdigit() for char in password):
            return False

    # Check if password contains at least one special character
    
    if overwrite_special_characters:
        special_characters = overwritten_special_characters
    else:
        special_characters = "!@#$%^&*()_-+=<>?/\\"
    if not any(char in special_characters for char in password):
        return False

    # All criteria passed, password is valid
    return True

def validate_strong_password(password: str) -> bool:
    """
    Validate if a given password meets the criteria for a strong password.

    A strong password must satisfy the following conditions:
    - Have a minimum length of 12 characters.
    - Contain at least one uppercase letter.
    - Contain at least one lowercase letter.
    - Contain at least one digit.
    - Optionally, special characters can be included, with the possibility to overwrite the default set of characters.

    Args:
        password (str): The password string to be validated.

    Returns:
        bool: True if the password meets the strong password criteria, False otherwise.
    """
    return validate_password(password, 12, upper=True, lower=True, digit=True, overwrite_special_characters=True, overwritten_special_characters="!@#$%^&*()_-+=<>?/\\")

def validate_credit_card(number: int) -> bool:
    """
    Validates a credit card number using the Luhn algorithm.

    This function takes an integer representing a credit card number and performs the
    Luhn algorithm to determine its validity.

    The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a
    simple checksum formula used to validate a variety of identification numbers,
    including credit card numbers. It works by performing a series of mathematical
    operations on the digits of the credit card number and checking whether the
    resulting sum is divisible by 10.

    Args:
        number (int): The credit card number to be validated.

    Returns:
        bool: True if the credit card number is valid according to the Luhn algorithm,
            False otherwise.
    """
    # Remove any spaces or dashes from the credit card number
    number = number.replace(" ", "").replace("-", "")
    
    # Check if the number contains only digits
    if not number.isdigit():
        return False
    
    # Reverse the number
    reversed_number = number[::-1]
    
    # Calculate the Luhn checksum
    checksum = 0
    for i in range(len(reversed_number)):
        digit = int(reversed_number[i])
        
        # Double every second digit
        if i % 2 == 1:
            digit *= 2
            
        # Subtract 9 from digits greater than 9
        if digit > 9:
            digit -= 9
            
        checksum += digit
    
    # The number is valid if the checksum is divisible by 10
    return checksum % 10 == 0

def isStr(input_string: str) -> bool:
    """Return True if the given input is a string, False otherwise.

    This function is an alternative for checking if a variable is a string with the
    isinstance built-in function.

    Args:
        input_string (str): The input to check if it is a string.

    Returns:
        bool: True if the input is a string, False otherwise.
    """
    return isinstance(input_string, str)

def isDic(input_string) -> bool:
    """
    This function is an alternative for checking if a variable is a dictionary with the
    isinstance built-in function.

    Args:
        input_string (Any): The input object to check.

    Returns:
        bool: True if the input is a dictionary object, False otherwise.
    """
    return isinstance(input_string, dict)

def isInt(input_string) -> bool:
    """
    This function is an alternative for checking if a variable is an integer with the
    isinstance built-in function.

    Args:
        input_string (any): The variable to be checked.

    Returns:
        bool: True if input_string is an integer, False otherwise.
    """
    return isinstance(input_string, int)

def isFloat(input_string) -> bool:
    """
    This function is an alternative for checking if a variable is a float with the
    isinstance built-in function.

    Args:
        input_string (any): The input value to check.

    Returns:
        bool: True if the input value is a float, False otherwise.
    """
    return isinstance(input_string, float)

def check_valid_ipv6(ip_address: str) -> bool:
    """
    Check the validity of an IPv6 address.

    This function takes an IPv6 address in string format and attempts to create an IPv6Address
    object from the 'ip_address' parameter. If the address is valid, the function returns True;
    otherwise, it returns False.

    Parameters:
    ip_address (str): A string representing the IPv6 address to be checked.

    Returns:
    bool: True if the IPv6 address is valid, False if it is not.

    Example:
    >>> check_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
    True
    >>> check_valid_ipv6("invalid_address")
    False
    """
    try:
        ip = IPv6Address(ip_address)
        return True
    except AddressValueError:
        return False

def check_valid_ipv4(ip_address: str) -> bool:
    """
    Check the validity of an IPv4 address.

    This function takes an IPv4 address in string format and attempts
    to create an IPv4Address object from the `ipaddress` module. If the
    address is valid, the function returns True. If the address is not
    a valid IPv4 address, it returns False.

    Args:
        ip_address (str): The IPv4 address to be checked.

    Returns:
        bool: True if the input is a valid IPv4 address, False otherwise.
    """
    try:
        ip = IPv4Address(ip_address)
        return True
    except AddressValueError:
        return False
    
def compare(file1, file2) -> bool:
    """
    Compare two files and return a boolean indicating whether they are equal or not.

    Args:
        file1 (str): The path to the first file.
        file2 (str): The path to the second file.

    Returns:
        bool: True if the files are equal, False otherwise.
    """
    return file1 == file2