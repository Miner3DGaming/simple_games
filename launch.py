import random
if random.random() > 0.95:
    print(random.choice([
                        "Starting Simple Game Launcher, a Crashaholic like no other!", 
                        "Starting Simple Game Launcher, stealing less user data than Google, Twitch, Microsoft, Firefox, Opera, Facebook, aaannndddd I'm on a hit list for writing this.",
                        "Starting Simple Game Launcher. You call it stealing code, I call it permanently borrowing it, we are not the same.", 
                        "Starting Simple Game Launcher, the Launcher containing code opposite to its name...."
                        ]))
else: print("Starting Simple Game Launcher...")

from data import library
translation = library.translation("en_us.json")

import sys, os

# Assure imports work anywhere
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__)+"/data")




# Deal with given file arguments
arguments = sys.argv[1:]
check_for_update_bool = not "--no_update_checking" in arguments
check_for_update_timeout_bool = "--check_for_internet_timeout" in arguments

# Check if to check for wifi or if to trust an inputted value
try:set_internet_connection = arguments.index("--set_internet_connection")
except: 
    internet_status = ""
    set_internet_connection = -1

if set_internet_connection != -1:
    internet_status = arguments[set_internet_connection+1]
del set_internet_connection
if internet_status == "--true":
    internet_status = True
elif internet_status == "--false":
    internet_status = False
else:
    internet_status = None


if internet_status is None:
    
    # Set custom timeout for the initial internet check
    try:custom_check_for_internet_timeout = int(arguments[arguments.index("--check_for_internet_timeout")+1][1:])
    except: 
        custom_check_for_internet_timeout = 1
    
    
    import socket
    def internet(host="8.8.8.8", port=53, timeout=1):
        """
        Host: 8.8.8.8 (google-public-dns-a.google.com)
        OpenPort: 53/tcp
        Service: domain (DNS/TCP)
        """
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error as ex:
            print(ex)
            return False
    is_connected_to_wifi = internet(timeout=custom_check_for_internet_timeout)
else:
    is_connected_to_wifi = internet_status
del internet_status

library.PRINT_SUPPRESSION_LEVEL = 1
if check_for_update_bool and is_connected_to_wifi:
    from data import check_for_update
    check_for_updates = check_for_update.check_for_updates("en_us.json")
    check_for_updates.library.PRINT_SUPPRESSION_LEVEL = 2
    need_for_update = check_for_updates.check_for_launcher_update()
    if need_for_update:
        from data import download_update
        if input("The launcher would like to update itself, would you like to cancel this action? (Inputting anything that isn't whitespace will stop it from doing so):").strip() == "":
            print("Please hold on a moment while the launcher is updating...")
            updater = download_update.download_update()
            updater.update()
            print("Done Downloading update, the launcher will now try to restart itself")
            import subprocess
            subprocess.run(f"cd {os.getcwd()} && python {__file__} {' '.join(arguments)}", shell=True, text=False, capture_output=False)
            quit()
        
        else:
            print("The launcher is a little disappointed it couldn't update")

def start_game(id):
    print(id)


from data.check_games import get_installed_games
from data.games import tge
console = tge.load_console_utils()

while True:
    console.clear_console()
    games = get_installed_games()
    print("Available Games:")
    for i in games:
        print(f'   - {games[i]["display_name"]} ({games[i]["version"]})')
    while True:
        print("\n Write what game you wanna play (Autocorrect X, Autocomplete ✓ ): ", end="")
        selection = input()
        if selection == "": break
        print([games[x]["display_name_lower"] for x in games])
        possible_games = tge.tbe.autocomplete(selection.lower(), [games[x]["display_name_lower"] for x in games])
        print(possible_games)
        if len(possible_games) == 1:
            game = games[tge.manipulation.dictionary_utils.find_index(games, "display_name_lower", possible_games[0])]
            start_game(game)
            quit()
        elif len(possible_games) == 0: break
        else:
            console.clear_console()
            print(f"There are several games starting with \"{selection}\":")
            for i in range(len(possible_games)):
                g = tge.manipulation.dictionary_utils.find_index(games, "display_name_lower", possible_games[i])
                print(f'   - {games[g]["display_name"]} ({games[g]["version"]})')