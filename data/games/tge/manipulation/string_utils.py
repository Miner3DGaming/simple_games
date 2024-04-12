



def truncate_string(string: str, length: int) -> str:
    """
    Truncates a string to the specified length.

    Args:
        string (str): The string to be truncated.
        length (int): The maximum length of the truncated string.

    Returns:
        str: The truncated string.
    """
    if len(string) <= length:
        return string
    else:
        return string[:length]
    

def reverse_string(string: str) -> str:
    """
    Reverses the order of characters in a string.

    Args:
        string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return string[::-1]

def check_anagram(word1: str, word2: str) -> bool:
    """
    Check if two words are anagrams of each other.

    Args:
        word1 (str): The first word to check.
        word2 (str): The second word to check.

    Returns:
        bool: True if the words are anagrams, False otherwise.
    """
    return sorted(word1) == sorted(word2)

def remove_duplicates_from_string(string: str) -> str:
    """
    Remove duplicate characters from a given string.

    Args:
        string (str): The input string.

    Returns:
        str: The string with duplicate characters removed.

    Examples:
        >>> remove_duplicates_from_string("hello")
        'helo'
        >>> remove_duplicates_from_string("abbcccdd")
        'abcd'
    """
    result = ""
    for char in string:
        if char not in result:
            result += char
    return result

def find_longest_word(string: str) -> str:
    """
    Find the longest word in a given string.

    Args:
        string (str): The input string.

    Returns:
        str: The longest word found in the string.

    Examples:
        >>> find_longest_word("Hello world")
        'Hello'
        >>> find_longest_word("This is a sentence")
        'sentence'
    """
    return max(string.split(), key=len)

def get_length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.

    Args:
        s (str): The input string.

    Returns:
        int: The length of the longest substring without repeating characters.

    Examples:
        >>> get_length_of_longest_substring("abcabcbb")
        3
        >>> get_length_of_longest_substring("bbbbb")
        1
        >>> get_length_of_longest_substring("pwwkew")
        3
    """
    if not s:
        return 0

    max_length = 0  # stores the length of the longest substring
    start = 0  # starting index of the current substring
    char_index_map = {}  # stores the most recent index of each character

    for i in range(len(s)):
        if s[i] in char_index_map and start <= char_index_map[s[i]]:
            # If the current character is already present in the substring,
            # update the starting index of the substring to the next index of the repeated character.
            start = char_index_map[s[i]] + 1
        else:
            # Calculate the length of the current substring and update the maximum length if necessary.
            max_length = max(max_length, i - start + 1)

        # Update the most recent index of the current character.
        char_index_map[s[i]] = i

    return max_length

def find_first_non_repeating_character(string: str) -> str:
    """
    Find the first non-repeating character in a given string.

    Args:
        string (str): The input string.

    Returns:
        str: The first non-repeating character found in the string, or None if no such character is found.

    Examples:
        >>> find_first_non_repeating_character("aabbc")
        'c'
        >>> find_first_non_repeating_character("hello")
        'h'
        >>> find_first_non_repeating_character("aabbcc")
        None
    """
    char_count = {}

    # Count the occurrences of each character in the string
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeating character
    for char in string:
        if char_count[char] == 1:
            return char

    # If no non-repeating character is found, return None
    return None


def count_consonants(string: str) -> int:
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0

    for char in string:
        if char in consonants:
            count += 1

    return count

def count_substring_occurrences(string: str, substring: str) -> int:
    return string.count(substring)

def capitalize_sentences(paragraph):
    sentences = paragraph.split('. ')  # Split the paragraph into individual sentences

    # Capitalize the first letter of each sentence
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]

    # Join the sentences back together
    formatted_paragraph = '. '.join(capitalized_sentences)

    return formatted_paragraph

def count_vowels(string: str) -> int:
    count = 0
    for char in string:
        if char in "aeiou":
            count += 1
    return count

def find_longest_substring(string: str) -> str:
    longest_substring = ""
    current_substring = ""
    
    for char in string:
        if char in current_substring:
            # Found a repeating character, update the longest substring if needed
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            # Reset the current substring after the repeated character
            current_substring = current_substring.split(char)[-1]
        
        # Add the current character to the current substring
        current_substring += char
    
    # Check if the current substring is longer than the longest substring
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring
    
    return longest_substring

def check_pangram(string: str) -> bool:
    alphabet = set(string.ascii_lowercase)  # Create a set of all lowercase letters
    
    # Convert the string to lowercase and remove any non-alphabetic characters
    # by using only the characters present in the alphabet set
    filtered_string = ''.join(filter(lambda c: c in alphabet, string.lower()))
    
    # Check if the filtered string contains all the letters of the alphabet
    return set(filtered_string) == alphabet

def find_common_characters(string1: str, string2: str) -> str:
    return "".join(set(string1) & set(string2))

def split_text(text, chunk_size):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]


class TextManipulation:
    def __init__(self, text):
        self.text = text

    def len(self):
        return len(self.text)
    
    def split_text(self, chunk_size):
        return [self.text[i:i + chunk_size] for i in range(0, len(self.text), chunk_size)]
    
    def find_common_characters(self, string2):
        return "".join(set(self.text) & set(string2))

    def find_longest_substring(self):
        longest_substring = ""
        current_substring = ""
        
        for char in self.text:
            if char in current_substring:
                # Found a repeating character, update the longest substring if needed
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
                # Reset the current substring after the repeated character
                current_substring = current_substring.split(char)[-1]
            
            # Add the current character to the current substring
            current_substring += char
        
        # Check if the current substring is longer than the longest substring
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
        
        return longest_substring
    
    def check_pangram(self):
        import string
        alphabet = set(string.ascii_lowercase)
        filtered_string = ''.join(filter(lambda c: c in alphabet, self.text.lower()))
        return set(filtered_string) == alphabet
    
    def count_vowels(self):
        count = 0
        for char in self.text:
            if char in "aeiou":
                count += 1
        return count

    def capitalize_sentences(self):
        sentences = self.text.split('. ')
        capitalized_sentences = [sentence.capitalize() for sentence in sentences]
        formatted_paragraph = '. '.join(capitalized_sentences)
        return formatted_paragraph

    def count_consonants(self):
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        count = 0

        for char in self.text:
            if char in consonants:
                count += 1

        return count

    def find_first_non_repeating_character(self):
        char_count = {}

        for char in self.text:
            char_count[char] = char_count.get(char, 0) + 1

        for char in self.text:
            if char_count[char] == 1:
                return char

        return None
    
    def reverse(self):
        return self.text[::-1]
    
    def check_anagram(self, word2):
        return sorted(self.text) == sorted(word2)
    
    def remove_duplicates(self):
        result = ""
        for char in self.text:
            if char not in result:
                result += char
        return result
    
    def find_longest_word(self):
        return max(self.text.split(), key=len)
    
    def get_length_of_longest_substring(self):
        s = self.text
        if not s:
            return 0

        max_length = 0  # stores the length of the longest substring
        start = 0  # starting index of the current substring
        char_index_map = {}  # stores the most recent index of each character

        for i in range(len(s)):
            if s[i] in char_index_map and start <= char_index_map[s[i]]:
                # If the current character is already present in the substring,
                # update the starting index of the substring to the next index of the repeated character.
                start = char_index_map[s[i]] + 1
            else:
                # Calculate the length of the current substring and update the maximum length if necessary.
                max_length = max(max_length, i - start + 1)

            # Update the most recent index of the current character.
            char_index_map[s[i]] = i

        return max_length
    
    def truncate(self, length):
        """
        Truncates the instance's text to the specified length.

        Args:
            length (int): The maximum length of the truncated string.

        Returns:
            str: The truncated string.
        """
        if len(self.text) <= length:
            return self.text
        else:
            return self.text[:length]

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