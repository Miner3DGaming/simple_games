

HEX_CHARACTERS = "0123456789ABCDEF"





def convert_binary_to_decimal(binary: str) -> int:
    """
    Convert a binary number to its decimal equivalent.

    Parameters:
    binary (str): A binary number represented as a string.

    Returns:
    int: The decimal equivalent of the given binary number.
    """
    decimal = 0
    power = 0

    # Iterate over the binary digits in reverse order
    for digit in reversed(str(binary)):
        if digit == '1':
            decimal += 2 ** power
        power += 1

    return decimal

def convert_decimal_to_binary(decimal: int) -> str:
    """
    Convert a decimal integer to its binary representation.

    Parameters:
    decimal (int): The decimal integer to be converted.

    Returns:
    str: The binary representation of the input decimal integer.

    Examples:
    >>> convert_decimal_to_binary(10)
    '1010'
    >>> convert_decimal_to_binary(23)
    '10111'
    >>> convert_decimal_to_binary(0)
    '0'
    """
    binary = ''
    while decimal > 0:
        binary += str(decimal % 2)
        decimal //= 2
    return binary[::-1]

def convert_decimal_to_hexadecimal(decimal: int) -> str:
    """
    Convert a decimal integer to its hexadecimal representation.

    Parameters:
    decimal (int): The decimal integer to be converted.

    Returns:
    str: The hexadecimal representation of the input decimal number.
    """
    # Handle special case when the decimal number is 0
    if decimal == 0:
        return "0"

    # Convert decimal to hexadecimal
    hex_string = ""
    while decimal > 0:
        remainder = decimal % 16
        hex_digit = HEX_CHARACTERS[remainder]
        hex_string = hex_digit + hex_string
        decimal = decimal // 16

    return hex_string

def convert_hexadecimal_to_decimal(hexadecimal: str) -> int:
    """
    Convert a hexadecimal string to its decimal representation.

    Parameters:
    hexadecimal (str): A string representing a hexadecimal number.

    Returns:
    int: The decimal representation of the input hexadecimal number.

    Raises:
    ValueError: If the input is not a valid hexadecimal string.
    """
    # Handle special case when the hexadecimal number is 0
    if hexadecimal == "0":
        return 0

    # Convert hexadecimal to decimal
    decimal = 0
    for hex_digit in reversed(hexadecimal):
        decimal = decimal * 16 + HEX_CHARACTERS.index(hex_digit)
