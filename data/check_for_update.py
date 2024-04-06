import requests

version_link = "https://raw.githubusercontent.com/Miner3DGaming/simple_games/main/version.txt"

response = requests.get(version_link)


if response.status_code == 200:
    print(response.text)
else:
    print("Failed to check for updates. Error code:", response.status_code)




