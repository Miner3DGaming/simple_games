import sys
arguments = sys.argv[1:]


check_for_update_bool = not "--no_update_checking" in arguments



from data import download_update, check_for_update






need_for_update = check_for_update
