








def remove_duplicates_from_dictionary(dictionary):
    """
    Remove duplicates from a dictionary based on its values.

    Parameters:
    dictionary (dict): A dictionary to remove duplicates from based on values.

    Returns:
    dict: A new dictionary with unique values, where only the first occurrence
          of each value is retained, preserving the original key-value pairs.
    """
    unique_values = set(dictionary.values())
    new_dictionary = {}

    for key, value in dictionary.items():
        if value in unique_values:
            new_dictionary[key] = value
            unique_values.remove(value)

    return new_dictionary

def find_index(dictionary, key, value):
    for item in dictionary:
        if dictionary[item][key] == value:
            return item
    return None