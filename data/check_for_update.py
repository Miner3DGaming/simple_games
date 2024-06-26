class check_for_updates():
    def __init__(self, language):
        import requests, os, library
        self.requests = requests
        self.os = os
        self.library = library
        temp = library.translation(language)
        self.get_translation = temp.get_translation
        self.print = library.print


        self.base_path = os.path.dirname(os.path.dirname(__file__))

        self.local_version_file = self.base_path + "/data/version.txt"
        self.version_link = "https://raw.githubusercontent.com/Miner3DGaming/simple_games/main/version.txt"



        self.NEWER_VERSION_AVAILABLE = "nva"
        self.LOCAL_VERSION_IS_NEWER = "lvin"
        self.SAME_VERSIONS = "sv"
        self.LOCAL_FILE_ERROR = "lfe"
        self.ONLINE_FILE_ERROR = "ofe"
        self.ACHIEVEMENT_MADE_HOW_DID_WE_GET_HERE = "uuuhhhhhh_huh?_this_isn't_supposed_to_happen"


    def compare_versions(self, version):
        """
            Check if the given version if newer than the local version.
            How? By comparing the value by between and outside the dots and magic.
        """
        with open(self.local_version_file, 'r') as f:
            local_version = f.read()
        if version == local_version: return self.SAME_VERSIONS
        
        local_version = local_version.split('.')
        version = version.split('.')
        
        local_version_length = len(local_version)
        version_length = len(version)
        for idx in range(local_version_length if local_version_length < version_length else version_length):
            try: mini_version = int(version[idx])
            except ValueError: return self.ONLINE_FILE_ERROR
            try: local_mini_version = int(local_version[idx])
            except ValueError: return self.LOCAL_FILE_ERROR
            local_mini_version = int(local_mini_version)
            if mini_version > local_mini_version: return self.NEWER_VERSION_AVAILABLE
            if mini_version < local_mini_version: return self.LOCAL_VERSION_IS_NEWER
        if local_version_length > version_length: return self.LOCAL_VERSION_IS_NEWER
        if local_version_length < version_length: return self.NEWER_VERSION_AVAILABLE
        
        return self.ACHIEVEMENT_MADE_HOW_DID_WE_GET_HERE



    def check_for_launcher_update(self):
        """
            Returns if an update is available as a bool
        """
        response = self.requests.get(self.version_link)
        if response.status_code != 200: print(self.library.ERROR, self.get_translation("launcher.update.connection_error") % response.status_code)
        else:
            version_status = self.compare_versions(response.text)
            if version_status == self.NEWER_VERSION_AVAILABLE:
                self.print(self.library.INFO, self.get_translation("launcher.update.newer_version_available"))
                return True
            
            elif version_status == self.LOCAL_VERSION_IS_NEWER: self.print(self.library.DEBUG, self.get_translation("launcher.update.local_version_is_newer"))
                
            
            elif version_status == self.SAME_VERSIONS: self.print(self.library.DEBUG, self.get_translation("launcher.update.is_up_to_date"))  
            
            elif version_status == self.LOCAL_FILE_ERROR:
                self.print(self.library.WARNING, self.get_translation("launcher.update.local_version_file_error") % self.local_version_file)
                return None

            elif version_status == self.ONLINE_FILE_ERROR: self.print(self.library.WARNING, self.get_translation("launcher.update.online_version_file_error"))
            
            elif version_status == self.ACHIEVEMENT_MADE_HOW_DID_WE_GET_HERE: self.print(self.library.WARNING, self.get_translation("launcher.update.online_version_file_error"))
        return False


