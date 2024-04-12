

from . import pathlib_path
from . import List, Union, Tuple , Any

from . import GTTS
from . import PYGAME

if GTTS:
    from gtts import gTTS

if PYGAME:
    from pygame import mixer as playsound




from tge.file_operations import get_file_extension, create_missing_directory, doesFileExist

if PYGAME:
    def load_sound(name: str, dir: str) -> Tuple[playsound.Sound | str, bool]:
        """
        Loads a sound from a directory

        Args:
        - name (str): name of the sound file
        - dir (str): directory containing the sound file

        Returns:
        - audio (playsound.Sound): sound
        o
        - error (str): error message
        """

        if not not dir: 
            if not not name:
                dir = dir.replace(fr"{pathlib_path(__file__).resolve().parent}/", "")
                dir = dir.replace(fr"{pathlib_path(__file__).resolve().parent}", "")
                if doesFileExist(fr"{pathlib_path(__file__).resolve().parent}/{dir}/{name}"):
                    audio = playsound.Sound(fr"{pathlib_path(__file__).resolve().parent}/{dir}/{name}")
                    return audio, True
                else: return "File in Directory can not be found", False
            else: return "Name cannot be empty", False
        else: return "Directory cannot be empty", False

    def play_sound(audio, volume: int, fadeout: int) -> Tuple[bool, str]:
        """
        Plays a sound file with the given attributes.

        Args:
            audio (str): The name of the audio file to be played.
            volume (int): The volume at which to play the audio file (0-100).
            fadeout (int): The time (in milliseconds) it takes for the audio to fade out.

        Returns:
            Tuple[bool, str]: A tuple containing a boolean indicating whether or not the 
            audio played successfully, and a string message explaining the result. 
            If the audio played successfully, the boolean will be True and the message will 
            be "Playing sound". If the audio failed to play for any reason, the boolean will 
            be False and the message will provide an explanation for the failure.

        Raises:
            None.

        """

        if audio != "": 
            if volume >= 0:
                try:
                    
                    audio.set_volume(volume)
                    audio.play()
                    if fadeout > 0:
                        audio.fadeout(fadeout)
                    return True, "Playing sound"
                except:
                    return False, "Error loading sound, are you sure this is a sound file?"
            else: return False, "Volume cannot be negative"
        else: return False, "Name cannot be empty"

    def stop_sound(audio) -> bool:
        """
        Stop the audio playback.

        Args:
        audio (str or object): The audio to stop playback for. Can be a string representing a file path
        or an object representing an ongoing audio playback.

        Returns:
        bool: True if the audio playback was stopped successfully, False if not.

        Note:
        - If audio is a string representing a file path, the function stops playback of the audio file
        associated with that path.
        - If audio is an object representing an ongoing audio playback, the function stops that playback.
        - If audio is an empty string, the function attempts to stop playback of the most recently played audio.
        """

        if audio != "":
            audio.stop()
            return True
        else: 
            playsound.stop()
            return False

    def pause_sound(audio) -> bool:
        """
        Pause the audio playback.

        Args:
            audio (Audio): The audio object to pause.

        Returns:
            bool: True if the audio was paused, False if there was no audio to pause.
        """
        if audio != "":
            audio.pause()
            return True
        else:
            playsound.pause()
            return False

    def unpause_sound(audio) -> bool:
        """
        Unpauses the given audio object or the default sound if audio is not provided.

        Args:
            audio: an instance of a sound object to unpause

        Returns:
            True if the sound was successfully unpaused, False otherwise.
        """
        if audio != "":
            audio.unpause()
            return True
        else:
            playsound.unpause()
            return False

    def get_sound_status(audio, raw: bool) -> tuple:
        """
        Returns the status of the sound.

        Parameters:
        audio : The sound object to get the status of.
        raw (bool): Whether to return the raw audio data or not.

        Returns:
        tuple: A tuple containing a boolean indicating whether the audio is loaded or not,
            and either the volume and length of the audio (if `raw` is False), or the
            raw audio data (if `raw` is True).

        Raises:
        Exception: If there was an error loading the audio file.
        """

        try:
            if audio != "":
                if not raw:
                    return (audio.get_volume(), audio.get_length()), True
                else: return audio.get_raw(), True
            else: return "No sound loaded", False
        except: return "Error loading audio, are you sure this is an audio file?", False

    def sound_stats(name: str, dic: str) -> tuple:
        """
        Returns a tuple containing the volume and length of a sound file.

        Args:
        - name (str): the name of the sound file.
        - dic (str): the directory where the sound file is located.

        Returns:
        - A tuple containing:
            - True if the sound file was successfully loaded, False otherwise.
            - A tuple containing the volume (in dB) and length (in seconds) of the sound file.

        If either 'name' or 'dic' are empty strings, the function returns (False, "Name cannot be empty")
        or (False, "Directory cannot be empty"), respectively.
        """

        if name != "": 
            if dic != "": 
                    audio = playsound.Sound(fr"{pathlib_path(__file__).resolve().parent}/{dic}/{name}")
                    return (audio.get_volume(), audio.get_length()), True
            else: return "Directory cannot be empty", False
        else: return "Name cannot be empty", False

if GTTS:
    def save_text_to_speech(text: str, name: str, dir: str) -> None:
        """
        Convert the provided text into speech using the Google Text-to-Speech (gTTS) API
        and save it as an audio file.

        Args:
            text (str): The text to be converted to speech.
            name (str): The desired name of the output audio file.
            dir (str): The directory path where the audio file should be saved.
                    If dir is an empty string, the current directory will be used.

        Returns:
            None

        Note:
            If the provided 'name' does not have a valid file extension, '.mp3' will be appended.
            The function attempts to create any missing directories in the specified 'dir' path.
            If successful, the generated audio file is saved in the format 'dir/name'.
            If an exception occurs during the saving process, the function returns None.

        Example:
            save_text_to_speech("Hello, how are you?", "greeting", "output_audio")
            # Converts the text to speech and saves it as 'output_audio/greeting.mp3'

        """
        if dir == "":
            dir = "."
        tts = gTTS(text=text, lang='en')
        if get_file_extension(name) == '':
            name = name.split('.')[0]
            name += '.mp3'
        create_missing_directory(dir)
        try:
            tts.save(f'{dir}/{name}')
        except:
            pass

