
if __name__ == "__main__":
    import time; very_start = time.time()
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import datetime



def get_game_name(session, game_id):
    """
    Fetches the name of a game from Steam's website using its game ID.

    This function uses the provided session to make an HTTP GET request to the Steam Community
    page of the game with the given game ID. It then parses the HTML content of the page to
    extract the game's name.

    Args:
        session (requests.Session): A requests session object for making HTTP requests.
        game_id (int): The ID of the game on Steam.

    Returns:
        str or None: The name of the game if successfully retrieved, or None if an error occurred.

    Raises:
        None

    Note:
        The function handles potential network errors using requests.exceptions.RequestException
        and returns None in case of any error during the request.

    Example:
        session = requests.Session()
        game_id = 12345
        game_name = get_game_name(session, game_id)
        if game_name:
            print(f"The name of the game is: {game_name}")
        else:
            print("Failed to retrieve the game name.")
    """
    url = f"https://steamcommunity.com/app/{game_id}/"
    try:
        response = session.get(url, timeout=20)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        title_element = soup.find('title')
        if title_element:
            title_text = title_element.get_text()
            if "Welcome to Steam" not in title_text:
                game_name = title_text.replace(" on Steam", "").replace("Steam Community :: ", "")
                return game_name
    except requests.exceptions.RequestException:
        pass
    return None

def check_game_ids_with_names(game_ids, results = {}):
    """
    Retrieves game names associated with the provided game IDs using multi-threading.
    
    This function takes a list of game IDs and optionally a dictionary of results. It uses multi-threading
    to concurrently fetch the game names corresponding to the given game IDs by calling the 'get_game_name'
    function. The fetched game names are stored in the 'results' dictionary under the corresponding game ID.
    
    Args:
        game_ids (list): A list of game IDs for which to retrieve game names.
        results (dict, optional): A dictionary to store the results. The keys are game IDs and the values
            are dictionaries containing game information. If not provided, an empty dictionary is used.
            
    Returns:
        dict: A dictionary containing the results of the operation. The keys are game IDs and the values are
            dictionaries containing game information, including the fetched game name if available.
    """
    with requests.Session() as session, concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(get_game_name, session, game_id): game_id for game_id in game_ids}

        for future in concurrent.futures.as_completed(futures):
            game_id = futures[future]
            try:
                game_name = future.result()
                if game_name:
                    results[game_id]['name'] = game_name
                    
            except Exception:
                pass

    return results

def get_valid_game_ids_with_names():
    """
    Retrieves a list of valid game IDs along with their corresponding names from Steam.

    This function fetches game data from Steam using the 'get_steam_games' function and then filters
    out valid game IDs along with their names using the 'check_game_ids_with_names' function.

    Returns:
    list: A list of dictionaries, where each dictionary contains 'game_id' (unique identifier) and
        'game_name' (name of the game) for valid games on Steam.
    """
    game_ids, result = get_steam_games()
    valid_game_ids_with_names = check_game_ids_with_names(game_ids, result)
    return valid_game_ids_with_names

def get_response(session, game_id):
    """
    Retrieve the HTTP response content for a specific game on Steam Community.

    This function takes a session object and a game ID as input and constructs a URL
    to fetch information about the specified game from the Steam Community website.
    It sends an HTTP GET request to the constructed URL and returns the content of
    the response if the request is successful (HTTP status code 200). If there's any
    error during the request, a 'None' value is returned.

    Args:
        session (requests.Session): A requests session object to manage the HTTP connection.
        game_id (int): The ID of the game on Steam.

    Returns:
        bytes or None: The content of the HTTP response, or 'None' if an error occurs
                    during the request.

    Example:
        session = requests.Session()
        content = get_response(session, 12345)
        if content is not None:
            print(content.decode('utf-8'))
        else:
            print("Failed to retrieve the game information.")
    """
    url = f"https://steamcommunity.com/app/{game_id}/"
    try:
        response = session.get(url, timeout=20)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException:
        return None

def is_valid_game_id(session, game_id):
    """
    Check the validity of a game ID by retrieving the response content
    for the provided game ID using the given session object.

    Parameters:
    session (requests.Session): The session object to use for making HTTP requests.
    game_id (str): The ID of the game to validate.

    Returns:
    bool: True if the game ID is valid and corresponds to an existing game,
        False otherwise. A game ID is considered valid if a response is
        obtained and the title of the page retrieved does not contain
        the phrase "Welcome to Steam".
    """
    response_content = get_response(session, game_id)
    
    if response_content:
        soup = BeautifulSoup(response_content, 'html.parser')
        title_element = soup.find('title')
        
        if title_element:
            title_text = title_element.get_text()
            return "Welcome to Steam" not in title_text
    
    return False

def check_game_ids(game_ids):
    """
    Check the validity of a list of game IDs using multi-threading.
    
    This function takes a list of game IDs and utilizes a ThreadPoolExecutor to concurrently check the validity of each
    game ID using the 'is_valid_game_id' function. The results are stored in a dictionary where keys are game IDs and
    values indicate whether each game ID is valid or not.

    Args:
        game_ids (list): A list of game ID strings to be checked.

    Returns:
        dict: A dictionary containing game IDs as keys and their validity status (True, False, or None) as values.
            - True: The game ID is valid.
            - False: The game ID is invalid.
            - None: An exception occurred while processing the game ID.
    """
    results = {}
    
    with requests.Session() as session, concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(is_valid_game_id, session, game_id): game_id for game_id in game_ids}
        
        for future in concurrent.futures.as_completed(futures):
            game_id = futures[future]
            try:
                valid = future.result()
                results[game_id] = valid
            except Exception:
                results[game_id] = None
    
    return results




def get_steam_folders():
    """
    Retrieves a list of Steam library folders from the configuration file.

    This function reads the 'libraryfolders.vdf' configuration file of the Steam client
    located at 'C:\Program Files (x86)\Steam\config\libraryfolders.vdf'. It extracts
    the paths of additional library folders where Steam games can be stored.

    Returns:
        list: A list of paths to Steam library folders.
            The paths use forward slashes (/) as separators.
    """
    steam_folders = []

    try:
        with open(r"C:\Program Files (x86)\Steam\config\libraryfolders.vdf", "r") as f:
            data = f.read()
    except:
        return steam_folders

    lines = data.split('\n')
    for line in lines:
        line = line.strip()

        if line.startswith('"path"'):
            path = line.split('"')[3]
            path = path.replace('\\\\', '/')
            steam_folders.append(path)

    return steam_folders

def get_steam_accounts():
    """
    Retrieves Steam account information from the 'loginusers.vdf' file located in the Steam configuration directory.

    This function reads the 'loginusers.vdf' file, which contains information about Steam accounts that have logged into
    the Steam client. It extracts relevant information such as account IDs, usernames, remember login status, and more.

    Returns:
    dict: A dictionary containing information about the Steam account, where the keys represent various attributes
        such as 'id', 'AccountName', 'PersonaName', 'RememberPassword', and 'mostrecent'.
    """
    try:
        with open("C:/Program Files (x86)/Steam/config/loginusers.vdf") as f:
            data = f.read()
    except:
        return {}

    lines = data[8:-1]
    lines = lines.split("\n")

    brackets = 0
    account = {}
    
    for line in lines:
        line = line.lstrip("\t")
        
        if line == "{":
            brackets += 1
        elif line == "}":
            brackets -= 1
        else:
            if brackets == 0:
                break
            elif brackets == 1:
                account["id"] = line.strip('"')
            elif brackets == 2:
                elements = line.split('"')
                if elements[3] == "1":
                    boolean = True
                elif elements[3] == "0":
                    boolean = False
                else:
                    boolean = elements[3]

                account[elements[1]] = boolean
    return account

def get_steam_games(result={}):
    """
    Retrieves Steam game information from the localconfig.vdf file.

    This function reads the Steam configuration file located at the specified path
    and extracts relevant game information including playtime, cloud save details,
    and last played timestamps.

    Args:
        result (dict, optional): A dictionary to store the extracted game information.
            Defaults to an empty dictionary.

    Returns:
        tuple: A tuple containing two elements - a list of game IDs and a dictionary
        containing extracted game information. The dictionary structure is as follows:
        {
            "game_id": {
                "last_played": ["YYYY", "MM", "DD", "HH", "MM", "SS"],
                "Playtime2wks": int,
                "playtime": int,
                "BadgeData": int,
                "cloud": {
                    "state": str,
                    "quota_bytes": int,
                    "quota_files": int,
                    "used_bytes": int,
                    "used_files": int,
                    "lastlaunch": ["YYYY", "MM", "DD", "HH", "MM", "SS"],
                    "lastexit": ["YYYY", "MM", "DD", "HH", "MM", "SS"]
                }
            },
            ...
        }
    """
    steam_config_path = r"C:\Program Files (x86)\Steam\userdata\1093663613\config\localconfig.vdf"
    
    try:
        with open(steam_config_path, "r", encoding="utf-8") as f:
            data = f.read()
    except:
        return result
    
    lines = data.split("\n")
    brackets = 0
    last_bracket = 0
    cloud = False
    autocloud = False
    picking_games = False
    game_ids = []

    for line in lines:
        line = line.lstrip("\t")

        if line == "{":
            brackets += 1
        elif line == "}":
            brackets -= 1
        else:
            if brackets == 7:
                if cloud:
                    line_section = line.split("\t")
                    variable, value = line_section[0][1:-1], line_section[-1][1:-1]
                    if last_game not in result:
                        result[last_game] = {}
                    if 'cloud' not in result[last_game]:
                        result[last_game]['cloud'] = {}

                    if variable == "last_sync_state":
                        result[last_game]['cloud']['state'] = value
                        cloud = False
                    else:
                        special = ["quota_bytes", "quota_files", "used_bytes", "used_files"]
                        if variable in special:
                            result[last_game]['cloud'][variable] = value
                        else:
                            print(variable, "Cloud")
                            quit()

                elif autocloud:
                    if 'cloud' not in result[last_game]:
                        result[last_game]['cloud'] = {}
                    line_section = line.split("\t")
                    variable, value = line_section[0][1:-1], line_section[-1][1:-1]
                    if variable == "lastlaunch":
                        date = datetime.datetime.fromtimestamp(value)
                        date = date.strftime("%Y %m %d %H %M %S")  # YYYY MM DD HH MM SS, Year Month Day Hour Minute Second
                        date = date.split(" ")

                        result[last_game]['cloud']['lastlaunch'] = date

                    elif variable == "lastexit":
                        date = datetime.datetime.fromtimestamp(value)
                        date = date.strftime("%Y %m %d %H %M %S")  # YYYY MM DD HH MM SS, Year Month Day Hour Minute Second
                        date = date.split(" ")

                        result[last_game]['cloud']['lastexit'] = date
                        autocloud = False
                    else:
                        print(variable, "AutoCloud")
                        quit()

            if not "\t" in line:
                if brackets == 4:
                    section = line[1:-1]
                    if not picking_games:
                        if section == "apps":
                            picking_games = True
                    else:
                        break
                elif picking_games:
                    if brackets == 5:
                        section = line[1:-1]
                        if len(section) > 0:
                            game_ids.append(section)
                            last_game = section
                    elif brackets == 6:
                        section = line[1:-1]
                        if section == "cloud":
                            cloud = True

            elif brackets == 6:
                line_section = line.split("\t")
                variable, value = line_section[0][1:-1], int(line_section[-1][1:-1])
                result[last_game] = {}

                result[last_game]['last_played'] = []
                result[last_game]['Playtime2wks'] = 0
                result[last_game]['playtime'] = 0
                result[last_game]['BadgeData'] = 0

                num_val = ["playtime", "Playtime2wks", "BadgeData"]
                if variable == "LastPlayed":
                    value = datetime.datetime.fromtimestamp(value)
                    value = value.strftime("%Y %m %d %H %M %S")  # YYYY MM DD HH MM SS, Year Month Day Hour Minute Second
                    date = value.split(" ")
                    result[last_game]['last_played'] = date
                elif variable in num_val:
                    result[last_game]['playtime'] = value
                elif "_eula_" in variable:
                    pass
                else:
                    print(variable, "Nope")
                    quit()

            last_bracket = brackets

    checked_game_ids = check_game_ids(game_ids)
    game_ids = [game_id for game_id in game_ids if checked_game_ids[game_id]]
    try:
        game_ids.remove('0')
    except:
        pass

    return game_ids, result

def get_steam_friends(): 
    """
    Retrieve Steam friends and groups information from the localconfig.vdf file.

    This function reads the localconfig.vdf file located at the specified Steam
    configuration path to extract information about a user's Steam friends and groups.
    It parses the file to extract friend and group data and returns two dictionaries:
    one for the friends and another for the groups the user belongs to.

    Returns:
        tuple: A tuple containing two dictionaries.
            - The first dictionary represents the user's Steam friends. The keys are
            friend usernames, and the values are dictionaries containing various
            attributes of each friend.
            - The second dictionary contains information about the Steam groups the
            user is a part of. The keys are group usernames, and the values are the
            corresponding attributes of each group.

        If there is any issue reading the file or parsing the data, two empty
        dictionaries are returned.
    """
    steam_config_path = r"C:\Program Files (x86)\Steam\userdata\1093663613\config\localconfig.vdf"
    try:
        with open(steam_config_path, "r", encoding="utf-8") as f:
            data = f.read()
    except:
        return {}, {}
    
    lines = data.split("\n")
    brackets = 0
    reading_friends = False
    friends = {}
    
    for line in lines:
        line = line.lstrip("\t")

        if line == "{":
            brackets += 1
        elif line == "}":
            brackets -= 1
        else:
            if not reading_friends:
                if brackets == 1:
                    if not line.__contains__("\t"):
                        content = line[1:-1]
                        if content == "friends":
                            reading_friends = True
            else:
                if brackets == 1:
                    break
                if brackets == 2:
                    if not line.__contains__("\t"):
                        user = line[1:-1]
                        friends[user] = {}
                elif brackets == 3:
                    if line.__contains__("\t"):
                        line = line.split("\t")
                        variable, value = line[0][1:-1], line[-1][1:-1]
                        friends[user][variable] = value
                    else:
                        content = line[1:-1]
                        friends[user][content] = {}
                elif brackets == 4:
                    line = line.split("\t")
                    variable, value = line[0][1:-1], line[-1][1:-1]
                    friends[user][content][variable] = value
                        
    
    groups = {}
    
    for i in friends:
        try:
            friends[i]["tag"]
            groups[i] = friends[i]
        except:
            pass
    
    for i in groups:
        del friends[i]
    
    return friends, groups

def get_steam_data():
    """
    Retrieve Steam-related data for folders, accounts, games, and social connections.

    This function gathers information about the user's Steam setup, including folders,
    linked accounts, game IDs and names, as well as friends and groups in the social network.

    Returns:
        dict: A dictionary containing the following keys:
            - 'folders' (list): A list of Steam folders on the system.
            - 'accounts' (list): A list of linked Steam accounts.
            - 'games' (dict): A dictionary of valid game IDs mapped to their names.
            - 'social' (dict): A sub-dictionary containing social connections:
                - 'friends' (list): A list of Steam friends.
                - 'groups' (list): A list of Steam groups.
    """
    steam_data = {}
    steam_data["folders"] = get_steam_folders()
    steam_data["accounts"] = get_steam_accounts()
    steam_data["games"] = get_valid_game_ids_with_names()
    steam_data["social"] = {}
    steam_data["social"]["friends"], steam_data["social"]["groups"] = get_steam_friends()
    return steam_data



def convert_to_datetime(timestamp):
    """
    Converts a Unix timestamp to a datetime object.

    This function takes a Unix timestamp as input and returns a corresponding
    datetime object in the local time zone. The Unix timestamp represents the
    number of seconds that have elapsed since January 1, 1970 (UTC).

    Parameters:
    timestamp (float or int): The Unix timestamp to be converted.

    Returns:
    datetime.datetime: A datetime object representing the date and time
    corresponding to the provided Unix timestamp in the local time zone.
    """
    return datetime.datetime.fromtimestamp(timestamp)

if __name__ == "__main__":
    print(f"Initialized in {time.time() - very_start}")
    start = time.time()


    steam_data = get_steam_data()
    for i in steam_data:
        print(steam_data[i])

    print(f"Finished in {time.time() - start}")







































