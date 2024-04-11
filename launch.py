
import sys, os

# Assure imports work anywhere
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__)+"/data")

from data import library
translation = library.translation("en_us.json")


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
if internet_status == "true":
    internet_status = True
elif internet_status == "false":
    internet_status = False
else:
    internet_status = None


if internet_status is None:
    
    # Set custom timeout for the initial internet check
    try:custom_check_for_internet_timeout = int(arguments[arguments.index("--check_for_internet_timeout")]+1)
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
    is_connected_to_wifi = internet()
else:
    is_connected_to_wifi = internet_status


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
            print("Done Downloading update, please restart the program")
            quit()
        
        else:
            print("The launcher is a little disappointed it couldn't update")









