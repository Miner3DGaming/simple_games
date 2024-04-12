from base64 import b64encode, b64decode
from binascii import hexlify, unhexlify, Error as BinasciiError
from typing import List, Union, Tuple , Any

from . import RE
if RE:
    import re



def encode(x: str) -> Tuple[bool, str]: 
    """
    Encode a string using base64 and hexadecimal encoding.

    Args:
        x (str): The string to be encoded.

    Returns:
        Tuple[bool, Union[str, bytes]]: A tuple containing a boolean value indicating whether
            the encoding was successful or not, and either the encoded string or an error message
            if the encoding failed.
    """
    try:
        x = b64encode(bytes(x, 'latin-1'))
        x = hexlify(x).decode('latin-1')
        return x
    except:
        return ""

def decode(data: str)-> Tuple[str, bool]:
    """
    Decodes a string from hexadecimal and base64 encoding.

    Args:
        data (str): A string to decode.

    Returns:
        A tuple containing a boolean indicating whether the decoding was successful and
        the decoded string if successful, or an error message if unsuccessful.
    """
    try:
        data = unhexlify(data)
        decoded_data = b64decode(data)
        return decoded_data.decode('latin-1'), True
    except BinasciiError as e:
        return f'Error decoding string (BinasciiError): {e}', False
    except UnicodeError as e:
        return f'Error decoding string (UnicodeError): {e}', False
    except Exception as e:
        return f'Unknown error decoding string (UnknownError): {e}', False
    
def encode_base64(string: str) -> str:
    """
    Encodes a given string in base64 format.

    Args:
        string (str): The string to be encoded.

    Returns:
        str: The encoded string in base64 format.
    """
    return b64encode(string.encode()).decode()

def decode_base64(string: str) -> str:
    """
    This function decodes a given string in base64 format and returns the decoded string.
    
    Args:
        string (str): A string in base64 format to be decoded.
    
    Returns:
        str: The decoded string.
    """
    return b64decode(string.encode()).decode()

if RE:
    def decode_html_character(text: str):
        """
        Decode HTML-encoded characters in the given text.

        This function takes a string containing HTML-encoded characters and replaces them
        with their corresponding decoded characters. It supports a predefined set of special
        HTML-encoded characters.

        Args:
            text (str): The input text containing HTML-encoded characters.

        Returns:
            str: The input text with HTML-encoded characters replaced by their decoded counterparts.
        """
        special_encoding = ["&Agrave;", "&Aacute;", "&Acirc;", "&Atilde;", "&Auml;", "&Aring;", "&agrave;", "&aacute;", "&acirc;", "&atilde;", "&auml;", " &aring;", "&AElig;", "&aelig;", "&szlig;", "&Ccedil;", "&ccedil;", "&Egrave;", "&Eacute;", "&Ecirc;", "&Euml;", "&egrave;", "&eacute;", "&ecirc;", "&euml;", "&#131;", "&Igrave;", "&Iacute;", "&Icirc;", "&Iuml;", "&igrave;", "&iacute;", "&icirc;", "&iuml;", "&Ntilde;", "&ntilde;", "&Ograve;", "&Oacute;", "&Ocirc;", "&Otilde;", "&Ouml;", "&ograve;", "&oacute;", "&ocirc;", "&otilde;", "&ouml;", "&Oslash;", "&oslash;", "&#140;", "&#156;", "&#138;", "&#154;", "&Ugrave;", "&Uacute;", "&Ucirc;", "&Uuml;", "&ugrave;", "&uacute;", "&ucirc;", "&uuml;", "&#181;", "&#215;", "&Yacute;", "&#159;", "&yacute;", "&yuml;", "&#176;", "&#134;", "&#135;", "&lt;", "&gt;", "&#177;", "&#171;", "&#187;", "&#191;", "&#161;", "&#183;", "&#149;", "&#153;", "&copy;", "&reg;", "&#167;", "&#182;"]
        special_character = ["À", "Á", "Â", "Ã", "Ä", "Å", "à", "á", "â", "ã", "ä", "å", "Æ", "æ", "ß", "Ç", "ç", "È", "É", "Ê", "Ë", "è", "é", "ê", "ë", "ƒ", "Ì", "Í", "Î", "Ï", "ì", "í", "î", "ï", "Ñ", "ñ", "Ò", "Ó", "Ô", "Õ", "Ö", "ò", "ó", "ô", "õ", "ö", "Ø", "ø", "Œ", "œ", "Š", "š", "Ù", "Ú", "Û", "Ü", "ù", "ú", "û", "ü", "µ", "×", "Ý", "Ÿ", "ý", "ÿ", "°", "†", "‡", "<", ">", "±", "«", "»", "¿", "¡", "·", "•", "™", "©", "®", "§", "¶"]
        
        # Use regex to find HTML-encoded characters within the text
        encoded_chars = re.findall("&\w+;", text)
        
        # Iterate over the found encoded characters and replace them with decoded counterparts
        for encoded_char in encoded_chars:
            if encoded_char in special_encoding:
                index = special_encoding.index(encoded_char)
                decoded_char = special_character[index]
                text = text.replace(encoded_char, decoded_char)
        
        return text

def encode_html_character(text: str) -> str:
    """
    Encodes special characters in the input text into their corresponding HTML character entities.

    This function takes a string as input and replaces specific special characters with their equivalent
    HTML character entity codes. The conversion includes characters like accented letters, symbols, and
    other non-standard characters commonly used in text.

    Args:
        text (str): The input text containing special characters to be encoded.

    Returns:
        str: The input text with special characters replaced by their corresponding HTML character entities.
    """
    special_encoding = ["&Agrave;", "&Aacute;", "&Acirc;", "&Atilde;", "&Auml;", "&Aring;", "&agrave;", "&aacute;", "&acirc;", "&atilde;", "&auml;", " &aring;", "&AElig;", "&aelig;", "&szlig;", "&Ccedil;", "&ccedil;", "&Egrave;", "&Eacute;", "&Ecirc;", "&Euml;", "&egrave;", "&eacute;", "&ecirc;", "&euml;", "&#131;", "&Igrave;", "&Iacute;", "&Icirc;", "&Iuml;", "&igrave;", "&iacute;", "&icirc;", "&iuml;", "&Ntilde;", "&ntilde;", "&Ograve;", "&Oacute;", "&Ocirc;", "&Otilde;", "&Ouml;", "&ograve;", "&oacute;", "&ocirc;", "&otilde;", "&ouml;", "&Oslash;", "&oslash;", "&#140;", "&#156;", "&#138;", "&#154;", "&Ugrave;", "&Uacute;", "&Ucirc;", "&Uuml;", "&ugrave;", "&uacute;", "&ucirc;", "&uuml;", "&#181;", "&#215;", "&Yacute;", "&#159;", "&yacute;", "&yuml;", "&#176;", "&#134;", "&#135;", "&lt;", "&gt;", "&#177;", "&#171;", "&#187;", "&#191;", "&#161;", "&#183;", "&#149;", "&#153;", "&copy;", "&reg;", "&#167;", "&#182;"]
    special_character = ["À", "Á", "Â", "Ã", "Ä", "Å", "à", "á", "â", "ã", "ä", "å", "Æ", "æ", "ß", "Ç", "ç", "È", "É", "Ê", "Ë", "è", "é", "ê", "ë", "ƒ", "Ì", "Í", "Î", "Ï", "ì", "í", "î", "ï", "Ñ", "ñ", "Ò", "Ó", "Ô", "Õ", "Ö", "ò", "ó", "ô", "õ", "ö", "Ø", "ø", "Œ", "œ", "Š", "š", "Ù", "Ú", "Û", "Ü", "ù", "ú", "û", "ü", "µ", "×", "Ý", "Ÿ", "ý", "ÿ", "°", "†", "‡", "<", ">", "±", "«", "»", "¿", "¡", "·", "•", "™", "©", "®", "§", "¶"]
    
    # Iterate over the special characters and replace them with their encoded counterparts
    for encoding, character in zip(special_encoding, special_character):
        text = text.replace(character, encoding)
    
    return text

def encode_morse_code(message: str) -> str:
    """
    Encode a given message into Morse code.

    This function takes a string message and encodes it into Morse code
    using a predefined dictionary of characters and their corresponding
    Morse code representations.

    Args:
        message (str): The message to be encoded into Morse code.

    Returns:
        str: The encoded message in Morse code.

    Example:
        >>> encode_morse_code("hello")
        '.... . .-.. .-.. ---'
        >>> encode_morse_code("123")
        '.---- ..--- ...--'
    """
    morse_code = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        ',': '--..--',
        '.': '.-.-.-',
        '?': '..--..',
        '/': '-..-.',
        '-': '-....-',
        '(': '-.--.',
        ')': '-.--.-',
        '&': '.-...',
        '@': '.--.-.',
        '!': '-.-.--',
        '$': '...-..-',
        '%': '.-.-.',
        '=': '-...-',
        '+': '.-.-.',
        '_': '..--.-',
        '"': '.-..-.',
        '<': '.-.-',
        '>': '.-..-.',
        ':': '---...',
        ';': '-.-.-.',
        ' ': '/'
    }
    
    return ''.join([morse_code[letter] for letter in message.lower()])

def decode_morse_code(message: str) -> str:
    """
    Decodes a Morse code message into plain text.

    Args:
        message (str): The Morse code message to be decoded.

    Returns:
        str: The decoded plain text message.

    Morse code dictionary:
        The function uses a predefined dictionary `morse_code` to map Morse code sequences
        to their corresponding plain text characters. Each character is separated by a space.

    Example:
        >>> decode_morse_code('.... . .-.. .-.. ---   ... --- ...')
        'hello sos'
    """
    morse_code = {
        '.-': 'a',
        '-...': 'b',
        '-.-.': 'c',
        '-..': 'd',
        '.': 'e',
        '..-.': 'f',
        '--.': 'g',
        '....': 'h',
        '..': 'i',
        '.---': 'j',
        '-.-': 'k',
        '.-..': 'l',
        '--': 'm',
        '-.': 'n',
        '---': 'o',
        '.--.': 'p',
        '--.-': 'q',
        '.-.': 'r',
        '...': 's',
        '-': 't',
        '..-': 'u',
        '...-': 'v',
        '.--': 'w',
        '-..-': 'x',
        '-.--': 'y',
        '--..': 'z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '--..--': ',',
        '.-.-.-': '.',
        '..--..': '?',
        '-..-.': '/',
        '-....-': '-',
        '-.--.': '(',
        '-.--.-': ')',
        '.-...': '&',
        '.--.-.': '@',
        '-.-.--': '!',
        '...-..-': '$',
        '.-.-.': '%',
        '-...-': '=',
        '.-.-.': '+',
        '..--.-': '_',
        '.-..-.': '"',
        '.-.-': '<',
        '.-..-.': '>',
        '---...': ':',
        '-.-.-.': ';',
        '/': ' '

    }
    message = message.replace(' ', '/').replace('_', '/')
    return ''.join([morse_code[letter] for letter in message.lower()])

# def decimal_to_binary(n: int) -> int: Inefficient! 
#     """
#     Convert a decimal integer to its binary representation.

#     Parameters:
#     n (int): The decimal integer to be converted.

#     Returns:
#     str: The binary representation of the decimal integer 'n'.

#     Examples:
#     >>> decimal_to_binary(10)
#     '1010'
#     >>> decimal_to_binary(-5)
#     '1011'
#     >>> decimal_to_binary(0)
#     '0'
#     """
    
#     if n < 0:
#         n = abs(n)
#     elif n == 0:
#         return "0"
#     else:
#         binary_str = ""
#         while n > 0:
#             remainder = n % 2
#             binary_str = str(remainder) + binary_str
#             n = n // 2
#         return binary_str

# def binary_to_decimal(binary_str: int | str) -> int: Inefficient! 
#     """
#     Convert a binary string or integer to its decimal representation.

#     Parameters:
#     binary_str (int | str): The binary string or integer to be converted to decimal.

#     Returns:
#     int: The decimal representation of the input binary string or integer.
#     """
#     decimal_num = 0
#     binary_str = str(binary_str[::-1])  # Reverse the binary string for easier processing

#     for i in range(len(binary_str)):
#         if binary_str[i] == '1':
#             decimal_num += 2 ** i

#     return decimal_num     
        






