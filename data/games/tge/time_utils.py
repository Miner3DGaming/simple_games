from typing import List, Union, Tuple , Any
from datetime import datetime#, timezone as datetime_timezone
# from codec import encode
# from file_operations import save_data, load_data
from time import sleep, timezone


# def initSessionTime() -> None:
#     """
#     Initializes global variables for the current date and time.

#     This function calls getDate() to get the current date and time as a tuple
#     of (year, month, day, hour, minute, second, weekday) and assigns each
#     value to a corresponding global variable named with the format
#     "session_{unit}". For example, the year is assigned to session_year.

#     Returns:
#     None.
#     """
#     global session_year, session_month, session_day, session_hour, session_minute, session_second
#     session_year, session_month, session_day, session_hour, session_minute, session_second, session_weekday = get_date()

# def getSessionTime() -> Union[Tuple[int, int, int, int, int, int], int]:
#     """
#     Get the time difference between the current session and the start of the session.

#     Returns:
#     tuple: A tuple of integers representing the time difference between the current session and the start of the session, in the format (years_diff, months_diff, days_diff, hours_diff, minutes_diff, seconds_diff).
#     - `years_diff` (int): The number of years between the current session and the start of the session.
#     - `months_diff` (int): The number of months between the current session and the start of the session.
#     - `days_diff` (int): The number of days between the current session and the start of the session.
#     - `hours_diff` (int): The number of hours between the current session and the start of the session.
#     - `minutes_diff` (int): The number of minutes between the current session and the start of the session.
#     - `seconds_diff` (int): The number of seconds between the current session and the start of the session.
#     Returns -1 if an exception occurs during the computation.

#     Note:
#     - The function computes the time difference between the current session and the start of the session by subtracting the current date and time from the date and time when the session started.
#     - The session start date and time are assumed to be stored in the global variables session_year, session_month, session_day, session_hour, session_minute, and session_second.
#     - The function returns -1 if an exception occurs during the computation.
#     """

#     try:
#         time = datetime.now()
#         date = time.split("-")
#         year = int(date[0])
#         month = int(date[1])
#         day = int(date[2])
#         hour = int(date[3])
#         minute = int(date[4])
#         second = int(date[5])
#         years_diff = year - session_year; months_diff = month - session_month; days_diff = day - session_day; hours_diff = hour - session_hour; minutes_diff = minute - session_minute; seconds_diff = second - session_second
#         return (years_diff, months_diff, days_diff, hours_diff, minutes_diff, seconds_diff)
#     except:
#         return -1



# def timerStart(name: str) -> Tuple[bool, str]:
#     """
#     Starts a timer with the given name.

#     Args:
#         name: A string representing the name of the timer.

#     Returns:
#         A tuple containing a boolean indicating if the timer was started
#         successfully and a string with a message about the result.

#     Raises:
#         None.
#     """

#     if type(name) == str:
#         year, month, day, hour, minute, second, weekday = get_date()
#         bool, encoded = encode(f"{year}-{month}-{day}-{hour}-{minute}-{second}")
#         if not bool:
#             return encoded, False
#         save_data(name, "data", encoded)
#         return "Timer started", True

# def timerStop(name: str) -> Tuple[bool, Union[str, Tuple[int, int, int, int, int, int]]]:
#     """
#     Stop a timer and return the time elapsed since the last time it was started.

#     Arguments:
#     - name: the name of the timer to stop, as a string.

#     Returns:
#     A tuple containing two elements:
#     - a boolean indicating whether the operation was successful (True) or not (False).
#     - either a string with an error message if the operation failed, or a tuple with six integers representing the time elapsed since the last time the timer was started, in years, months, days, hours, minutes, and seconds.

#     Raises:
#     This function does not raise any specific exception.

#     Examples:
#     >> timerStop("my_timer")
#     (True, (0, 0, 0, 1, 23, 42))
#     >> timerStop("non_existing_timer")
#     (False, "No data found for timer 'non_existing_timer'.")
#     """

#     year, month, day, hour, minute, second, weekday = get_date()
#     result, data = load_data(str(name), "data")

#     if not result:
#         return data, False # return the error message from load_game()
#     past_date = data.split("-")
#     if not result:
#         return past_date, False # return the error message from decode()
#     past_year = int(past_date[0])
#     past_month = int(past_date[1])
#     past_day = int(past_date[2])
#     past_hour = int(past_date[3])
#     past_minute = int(past_date[4])
#     past_second = int(past_date[5])

#     year = int(year)
#     month = int(month)
#     day = int(day)
#     hour = int(hour)
#     minute = int(minute)
#     second = int(second)

#     years_diff = year - past_year; months_diff = month - past_month; days_diff = day - past_day; hours_diff = hour - past_hour; minutes_diff = minute - past_minute; seconds_diff = second - past_second
#     return (years_diff, months_diff, days_diff, hours_diff, minutes_diff, seconds_diff), True

def get_date() -> Tuple[int, int, int, int, int, int, int]:
    """
    Get the current date and time.

    Returns:
        Tuple[int, int, int, int, int, int, int]: A tuple containing year, month, day, 
        hour, minute, second, and day of the week (as an integer, where Monday is 0 and Sunday is 6).
    """
    date = datetime.now()
    day = datetime.weekday(date)
    date = str(date).replace("-", " ").replace(":", " ").replace(".", " ").split(" ")
    return int(date[0]), int(date[1]), int(date[2]), int(date[3]), int(date[4]), int(date[5]), int(day)

def get_timezone_offset() -> int:
    """
    Get the timezone offset in hours from UTC (Coordinated Universal Time).

    Returns:
        int: The timezone offset, where positive values indicate time ahead of UTC,
             and negative values indicate time behind UTC.
    """
    return int(timezone / 3600)

def unix_converter(time: int) -> str:
    """
    Converts a Unix timestamp to a formatted string representing the date and time.

    Args:
        time (int): A Unix timestamp, representing the number of seconds since the epoch.

    Returns:
        str: A formatted string in the format "YYYY MM DD HH MM SS".

    Example:
        >>> unix_converter(1628784000)
        '2021 08 13 00 00 00'
    """
    return datetime.fromtimestamp(time).strftime("%Y %m %d %H %M %S")














