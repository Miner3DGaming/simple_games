class download_update():
    def __init__(self, language) -> None:
        import MSY, library, requests, os
        self.load_msy = MSY.load
        self.project_link = "https://raw.githubusercontent.com/Miner3DGaming/simple_games/main/"
        self.requests = requests
        self.required_files_link = "data/required_files.msy"
        self.os = os
        self.base_path = os.path.dirname(os.path.dirname(__file__))
        
        
        
    def get_parts_to_update(self)->list:
        response = self.requests.get(self.project_link+self.required_files_link)
        if not response.status_code == 200: 
            print("not gud")
            return
        missing_files = self.get_missing_installed_files(self.load_msy(response.text)["CONSTANTS"])
        missing_files.extend(self.load_msy(response.text)["DYNAMIC"])
        return missing_files

    def get_missing_installed_files(self, list:list):
        missing = []
        for item in list:
            if not self.os.path.exists(self.os.path.join(self.base_path, item)):
                missing.append(item)
        return missing

    def download_outdated_files(self, list:list):
        for item in list:
            home_path = self.os.path.join(self.base_path, item)
            project_path = self.os.path.join(self.project_link, item)

            response = self.requests.get(project_path)
            if response.status_code == 200:
                if self.os.path.exists(home_path):
                    with open(home_path, "r") as f:
                        file = f.read()
                else: file = ""
                try:
                    with open(home_path, "w") as f:
                        f.write(str(response.text))
                except Exception as e: print(e)
                finally:
                    with open(home_path, "r") as rf:
                        if rf.read() == "":
                            with open(home_path, "w") as wf:
                                wf.write(file)

    def update(self):
        self.download_outdated_files(self.get_parts_to_update())
