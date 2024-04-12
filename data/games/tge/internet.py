from . import RE, PYTUBE, REQUESTS
from . import List, Union, Tuple , Any, Tuple, Dict, Optional
if RE:
    import re
if PYTUBE:
    from pytube import YouTube

if RE:
    def remove_html_tags(string: str) -> str:
        """
        Removes HTML tags from the given string.

        Args:
            string (str): The input string containing HTML tags.

        Returns:
            str: The modified string with HTML tags removed.

        Examples:
            >>> remove_html_tags('<p>Hello, <b>world!</b></p>')
            'Hello, world!'
            >>> remove_html_tags('<h1>Title</h1>')
            'Title'
        """
        return re.sub(r'<.*?>', '', string)

if PYTUBE and RE:
    def download_youtube_video(url: str, save_path: str, file_name: str) -> Tuple[bool, str]:#
        """
        Download a YouTube video as audio from the given URL and save it to the specified location.

        Args:
            url (str): The YouTube video URL or video ID. If a video ID is provided, it should be exactly 11 characters long.
                    If a URL is provided, the function handles short URLs and non-standard formats.
            save_path (str): The directory path where the downloaded video will be saved.
            file_name (str): The desired name for the downloaded video file. If no file extension is provided, '.mp4' will be added.

        Returns:
            Tuple[bool, str]: A tuple containing a boolean indicating the success of the download (True for success, False for failure)
                            and a string describing the outcome.

        Note:
            The function uses the 'pytube' library to download YouTube videos. It attempts to download the audio-only stream,
            but you can modify the stream selection based on your preferences.

        Example:
            success, message = download_youtube_video("https://www.youtube.com/watch?v=VIDEO_ID", "/path/to/save", "my_audio")
            if success:
                print("Download successful")
            else:
                print("Download failed:", message)
        """
        if not len(url) == 11:
            if url.__contains__("/shorts/"):
                url = url.replace("/shorts/", "/watch?v=")
            if url.__contains__("watch?v="):
                pass
            else:
                return False, "False"
        else:
            url = f"https://www.youtube.com/watch?v={url}"
        if not re.search(r'.\..', file_name):
            file_name += ".mp4"
        try:
            yt = YouTube(url)
            video = yt.streams.get_audio_only()  # You can choose a different stream based on your preferences
            video.download(output_path=save_path, filename=file_name)
            return True, "True"
        except Exception as e:
            return False, str(e)




if REQUESTS:
    import requests

    def post_to_discord_webhook(message_content: str, webhook: str, name: str, avatar_url: str = None, mention: bool = True, activate_voice: bool = False) -> Any:
        """
        Posts a message to a Discord webhook. Returns the response code and the content of the message.
        """
        data = {"content": message_content, #Contents of the message
            "username": name, #Name for the user
            "tts": activate_voice, #Activate TTS (Automatic reading voice)
            "allowed_mentions": {"parse": []} if mention else {}, #Allow mentions
            
            }
        if avatar_url is not None:
            data["avatar_url"] = avatar_url
        
        response = requests.post(webhook, json=data) 
        return response.status_code, response.content


from urllib.parse import urlparse, parse_qs
def extract_youtube_info(link: str) -> Dict[str, Optional[str]]:
    """
    Extracts information from a YouTube video link.

    This function takes a YouTube video link as input and parses it to extract relevant information,
    including the video ID and other query parameters. The parsed information is returned as a dictionary.

    Args:
        link (str): The YouTube video link to be parsed.

    Returns:
        Dict[str, Optional[str]]: A dictionary containing extracted information.
            - 'video_id' (str): The unique ID of the YouTube video.
            - 'params' (dict): Other query parameters present in the URL, excluding the video ID.
                            The keys are parameter names, and the values are parameter values.

    Example:
        link = "https://www.youtube.com/watch?v=s7LS5lh0dLQ&feature=share"
        result = extract_youtube_info(link)
        # Result:
        # {
        #     'video_id': 's7LS5lh0dLQ',
        #     'params': {'feature': 'share'}
        # }
    """
    parsed_url = urlparse(link)
    query_params = parse_qs(parsed_url.query)
    if link.__contains__("/shorts/"):
            link = link.replace("/shorts/", "/watch?v=")
    
    video_id = query_params.get('v', [None])[0]
    
    other_params = {key: value[0] for key, value in query_params.items() if key != 'v'}
    
    return {
        'video_id': video_id,
        'params': other_params,
    }
