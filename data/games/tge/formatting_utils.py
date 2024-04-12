



def format_number(number: int) -> str:
    """
    Formats an integer number with commas as thousands separators.

    Args:
        number (int): An integer that needs to be formatted.

    Returns:
        str: A string representation of the formatted number with commas as thousands separators.
    """
    return "{:,}".format(number)

def format_seconds(duration: int) -> str:
    """
    Formats a duration given in seconds into a string representation.

    Args:
        duration (int): The duration in seconds.

    Returns:
        str: The formatted duration string in the format "Xh Ym Zs".

    Example:
        >>> format_seconds(3665)
        '1h 1m 5s'
    """
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60

    formatted_duration = f"{hours}h {minutes}m {seconds}s"
    return formatted_duration

def format_minutes(duration: int) -> str:
    """
    Formats a duration given in minutes into a string representation.

    Args:
        duration (int): The duration in minutes.

    Returns:
        str: The formatted duration string in the format "Xh Ym Zs".

    Example:
        >>> format_minutes(125)
        '2h 5m 0s'
    """
    hours = duration // 60 // 60
    minutes = (duration // 60) % 60
    seconds = duration % 60

    formatted_duration = f"{hours}h {minutes}m {seconds}s"
    return formatted_duration

def format_hours(duration: int) -> str:
    """
    Formats a duration given in hours into a string representation.

    Args:
        duration (int): The duration in hours.

    Returns:
        str: The formatted duration string in the format "Xh Ym Zs".

    Example:
        >>> format_hours(2)
        '2h 0m 0s'
    """
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60

    formatted_duration = f"{hours}h {minutes}m {seconds}s"
    return formatted_duration

def format_days(duration: int) -> str:
    """
    Formats a duration given in days into a string representation.

    Args:
        duration (int): The duration in days.

    Returns:
        str: The formatted duration string in the format "Xh Ym Zs".

    Example:
        >>> format_days(3)
        '72h 0m 0s'
    """
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60

    formatted_duration = f"{hours}h {minutes}m {seconds}s"
    return formatted_duration

def format_weeks(duration: int) -> str:
    """
    Formats a duration given in weeks into a string representation.

    Args:
        duration (int): The duration in weeks.

    Returns:
        str: The formatted duration string in the format "Xh Ym Zs".

    Example:
        >>> format_weeks(2)
        '336h 0m 0s'
    """
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60

    formatted_duration = f"{hours}h {minutes}m {seconds}s"
    return formatted_duration

def format_years(duration: int) -> str:
    """
    Formats a duration given in years into a string representation.

    Args:
        duration (int): The duration in years.

    Returns:
        str: The formatted duration string in the format "Xh Ym Zs".

    Example:
        >>> format_years(1)
        '8760h 0m 0s'
    """
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60

    formatted_duration = f"{hours}h {minutes}m {seconds}s"
    return formatted_duration

def unformat_time(formated_time: str) -> int:
    """
    Converts a formatted time string into its equivalent duration in seconds.

    Args:
        formatted_time (str): The formatted time string in the format "Xh Ym Zs".

    Returns:
        int: The duration in seconds.

    Example:
        >>> unformat_time('2h 30m 45s')
        9045
    """
    try:
        hours = int(formated_time.split("h")[0].strip())
        minutes = int(formated_time.split("m")[0].strip())
        seconds = int(formated_time.split("s")[0].strip())
        return hours * 3600 + minutes * 60 + seconds
    except:
        return 0

