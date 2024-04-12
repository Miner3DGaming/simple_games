import os, sys
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__)+"/games")

game_folder_path = os.path.join(os.path.dirname(__file__), "games")

def get_installed_games():
    global game_folder_path
    games = {}
    candidates = [x for x in os.listdir(game_folder_path) if x.endswith(".py")]
    for potential_game in candidates:
        try:

            module_name = os.path.basename(potential_game).split('.')[0]
            module = __import__(f"games.{module_name}", fromlist=[module_name])
            GAME = getattr(module, "GAME")
            game_instance = GAME()
                
            if hasattr(game_instance, "get_game_type") and callable(game_instance.get_game_type) and hasattr(game_instance, "get_game_display_name") and callable(game_instance.get_game_display_name) and hasattr(game_instance, "get_game_version") and callable(game_instance.get_game_version):
                games[potential_game] = {}
                games[potential_game]["display_name"] = game_instance.get_game_display_name()
                games[potential_game]["display_name_lower"] = games[potential_game]["display_name"].lower()
                games[potential_game]["version"] = game_instance.get_game_version()
        except (AttributeError, TypeError): pass
        except Exception as e:
            print(f"Error while processing '{potential_game}': {e}")

    return games


