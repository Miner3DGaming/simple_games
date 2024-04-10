class download_update():
    def __init__(self, language) -> None:
        import MSY, library, requests
        self.load_msy = MSY.load
        self.project_link = "https://raw.githubusercontent.com/Miner3DGaming/simple_games/main/"
        self.requests = requests
        self.required_files_link = "data/required_files.msy"
        
        
        
        
    def get_parts_to_update(self):
        response = self.requests.get(self.project_link+self.required_files_link)
        print(self.project_link+self.required_files_link)
        if not response.status_code == 200: print("not gud");return
        print(response.text)



download_updates = download_update("hi")
download_updates.get_parts_to_update()