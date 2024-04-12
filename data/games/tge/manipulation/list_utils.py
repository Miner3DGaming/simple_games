from itertools import permutations as itertools_permutations



def list_max(lst: list) -> int:
    """Find and return the maximum value in a list.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The highest value in the list.

    Example:
        >>> list_max([3, 1, 7, 4])
        7
    """
    sorted_lst = sorted(lst)
    return sorted_lst[-1]

def list_min(lst: list) -> int:
    """
    Returns the minimum value in a list of numbers.

    Args:
    - lst: a list of numbers

    Returns:
    - the lowest value in the list

    Example:
    >>> list_min([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7])
    1
    """
    sorted_lst = sorted(lst)
    return sorted_lst[0]

def list_sum(lst: list) -> int:
    total = 0
    for item in lst:
        if isinstance(item, (int, float)):
            total += item
    return total

def list_mul(lst: list) -> tuple:
    """
    Multiply all the numbers in the given list and return the result along with a success message.

    :param lst: A list of numbers to multiply.
    :type lst: list
    :return: A tuple containing the product of the numbers in the list and a success message.
    :rtype: tuple
    :raises TypeError: If the list contains non-numeric values.
    """
    prod = 1
    try:
        for item in lst:
            if isinstance(item, (int, float)):
                prod = prod * item
        return prod
    except TypeError:
        return 0
    
def remove_duplicates(list: list) -> list:
    """
    Removes duplicates from a given list and returns it.

    :param list: A list of items.
    :type list: list
    :return: A new list containing no duplicates.
    :rtype: list
    """
    result = []
    for item in list:
        if item not in result:
            result.append(item)
    return result

def count_occurrences(list: list, item: str) -> int:
    """
    Counts the number of occurrences of a given item in a list.

    :param list: The list to search for occurrences.
    :type list: list
    :param item: The item to count occurrences of.
    :type item: str
    :return: The number of occurrences of the given item in the list.
    :rtype: int
    """
    count = 0
    for obj in list:
        if obj == item:
            count += 1
    return count

def calculate_average(lst: list) -> int:
    total = list_sum(lst)
    length = len([item for item in lst if isinstance(item, (int, float))])
    
    if length == 0:
        return 0  # To avoid division by zero
    
    average = total / length
    return average

def find_common_elements(lst1: list, lst2: list) -> list:
    result = []
    for item in lst1:
        if item in lst2:
            result.append(item)
    return result

def median(lst: list) -> int:
    lst.sort()
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]
    
def reverse_list(lst: list) -> list:
    return lst[::-1]

def find_max_min_difference(lst: list) -> int:
    return max(lst) - min(lst)

def find_missing_number(lst: list) -> int:
    return sum(range(1, len(lst) + 1)) - sum(lst)

def remove_whitespace_from_list(lst: list) -> list:
    """
    Removes whitespace characters from all elements in a list of strings.
    
    Args:
        lst (list): List of strings
        
    Returns:
        list: List with whitespace removed from all elements
    """
    return [string.replace(" ", "") for string in lst]

def exponential_average(lst: list) -> float:
    return sum(lst) / len(lst)

def greatest_product(lst: list, lst2: list) -> int:
    return list_max(lst) * list_max(lst2)

def permutations(lst: list) -> list:
    return list(itertools_permutations(lst))

def limit_list(list: list, limit: int) -> list:
    return list[:limit]

def get_items_from_list(list: list, start: int, end: int) -> list:
    return list[start:end]

def sort_list_of_dictionaries(lst, key: str) -> tuple:
    try:
        return sorted(lst, key=lambda x: x[key]), True
    except:
        return lst, False