from PIL import Image
from typing import List, Union, Tuple , Any

from . import NUMPY
from tge.file_operations import doesDirectoryFileExist

def rotate_image(image_path: str, angle: int) -> bool:
    """
    Rotate an image by the specified angle and save the rotated image back to the original path.

    Args:
        image_path (str): The file path to the image.
        angle (int): The angle in degrees by which to rotate the image clockwise.

    Returns:
        bool: True if the image rotation and saving were successful, False otherwise.

    Raises:
        This function does not raise any explicit exceptions. Any exceptions encountered during
        image processing or saving will cause the function to return False.

    Example:
        if rotate_image("image.jpg", 90):
            print("Image rotated successfully")
        else:
            print("Image rotation failed")
    """
    try:
        image = Image.open(image_path)
        rotated_image = image.rotate(angle)
        rotated_image.save(image_path)
        return True
    except:
        return False


def flip_image_vertically(image_path: str) -> bool:
    """
    Flips an image vertically and saves the result to the same file path.

    Args:
        image_path (str): The file path to the image.

    Returns:
        bool: True if the image was successfully flipped and saved, False otherwise.

    Notes:
        - This function uses the Pillow (PIL) library to open, flip, and save the image.
        - The original image is backed up before any modification attempt.
        - If an exception occurs during the flipping process, the function attempts to restore
          the original image from the backup and returns False.
    """
    try:
        image = Image.open(image_path)
        image_backup = image.copy()
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        image.save(image_path)
        return True
    except Exception:
        image_backup.save(image_path)
        return False


def flip_image_horizontally(image_path: str) -> bool:
    """
    Flips an image horizontally and saves the result back to the original file path.

    Args:
        image_path (str): The path to the image file to be flipped.

    Returns:
        bool: True if the image was successfully flipped and saved, False otherwise.
    """
    try:
        image = Image.open(image_path)
        image_backup = image.copy()
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
        image.save(image_path)
        return True
    except Exception as e:
        image_backup.save(image_path)
        return False


def add_anti_aliasing(image_path: str) -> bool:
    """
    Applies anti-aliasing to an image using a two-step resizing process.
    
    This function takes an image file path as input, opens the image, and applies
    anti-aliasing through a two-step process. The image is initially resized to
    double its dimensions and then back to its original dimensions, which helps
    in reducing aliasing artifacts. If the process is successful, the modified
    image is saved to the same path, and the function returns True. If any errors
    occur during the process, the function restores the original image and returns False.

    Args:
        image_path (str): The file path of the image to which anti-aliasing will be applied.
        
    Returns:
        bool: True if anti-aliasing is successfully applied and saved, False otherwise.
    """
    try:
        image = Image.open(image_path)
        image_backup = image
        image = image.resize((image.width * 2, image.height * 2))
        image.save(image_path)
        image = Image.open(image_path)
        image = image.resize((image.width // 2, image.height // 2))
        image.save(image_path)
        return True
    except:
        image_backup.save(image_path)
        return False

def count_gif_frames(file_path) -> Union[bool, int, str]:
    """
    Counts the number of frames in a GIF file.

    Args:
        file_path (str): The path to the GIF file.

    Returns:
        tuple: A tuple containing three elements:
            - success (bool): Indicates if the file was processed successfully.
            - frame_count (int): The number of frames in the GIF file.
            - message (str): A message indicating the result of the operation.

            Possible messages:
                - If success is True:
                    - If the file is animated: "The file at [file_path] is animated".
                    - If the file is not animated: "The file at [file_path] is not animated".
                - If success is False:
                    - If the file does not exist: "The file at [file_path] does not exist".
                    - If an error occurred while opening the file: "An error occurred while opening the file at [file_path]".
    """
    if doesDirectoryFileExist(True, file_path):
        try:
            with Image.open(file_path) as im:
                # Check if the image is animated (a GIF)
                if hasattr(im, 'is_animated') and im.is_animated:
                    # Iterate through all frames and count them
                    frame_count = 0
                    while True:
                        try:
                            im.seek(frame_count)
                            frame_count += 1
                        except EOFError:
                            break
                    return True, frame_count, "The file at " + file_path + " is animated"
                else:
                    return True, 1, "The file at " + file_path + " is not animated"
        except IOError:
            return False, 0, "An error occurred while opening the file at " + file_path
    else:
        return False, 0, "The file at " + file_path + " does not exist"

def get_image_metadata(file_path: str = None, image: str = None) -> Tuple[Any, str]:
    """
    Retrieve metadata from an image file.

    This function takes either an image file path or an image object as input and
    returns the extracted EXIF metadata along with an error message string, if applicable.

    Args:
        file_path (str, optional): The path to the image file. If provided, the function
            attempts to open the image file and extract its EXIF metadata.
        image (str, optional): An alternative to providing a file_path. If an image
            object is passed, this function directly attempts to extract its EXIF metadata.

    Returns:
        Tuple[Any, str]: A tuple containing two elements. The first element is a dictionary
        containing the extracted EXIF metadata of the image. The second element is a string
        that provides an error message if any issues occur during the process.

    Note:
        The function internally uses the `doesDirectoryFileExist` function to check the
        existence of the provided file path.

    Raises:
        None. Exceptions are caught internally, and error messages are returned.

    Example:
        exif_data, error_msg = get_image_metadata(file_path="path/to/image.jpg")
        if not error_msg:
            print("Image EXIF metadata:", exif_data)
        else:
            print("Error:", error_msg)
    """
    if image:
        pass
    elif file_path:
        if doesDirectoryFileExist(True, file_path):
            image = Image.open(image)
        else:
            return {}, "The file at " + file_path + " does not exist"
    else:
        return {}, "No valid image/file path was provided"
    try:
        return image.getexif(), ""
    except:
        return {}, "An error occurred while getting the image metadata"

def convert_image(file_path: str, extension: str, output_path: str = None) -> bool:
    """
    Convert and save an image to a different format.

    This function takes the input image file, converts it to the specified format,
    and saves the converted image to the specified output path. If no output path
    is provided, the converted image will be saved in the same location as the
    input file. The function returns True if the conversion and saving are
    successful, and False otherwise.

    Args:
        file_path (str): The path to the input image file.
        extension (str): The desired format to which the image should be converted
            (e.g., 'JPEG', 'PNG', 'GIF').
        output_path (str, optional): The path where the converted image should be
            saved. If not provided, the converted image will be saved in the same
            location as the input file.

    Returns:
        bool: True if the conversion and saving are successful, False otherwise.
    """
    if doesDirectoryFileExist(True, file_path):
        try:
            if not output_path:
                output_path = file_path
            image = Image.open(file_path)
            image.save(output_path, extension)
            return True
        except:
            return False
    else:
        return False

if NUMPY:
    from PIL import Image
    import numpy as np

    def image_to_ascii(image_path: str = "", image=None, width: int = None, unicode: bool = False, ascii_chars: str = "") -> str:
        """
        Convert an image into ASCII art.

        Parameters:
            image_path (str, optional): Path to the image file.
            image (PIL.Image.Image, optional): PIL image object.
            width (int, optional): Desired width of the ASCII art. If not specified, the width of the original image is used.
            unicode (bool, optional): Use Unicode characters for the ASCII art. If False, regular ASCII characters are used.
            ascii_chars (str, optional): Custom set of characters to be used for the ASCII art. If not specified, default characters are used based on the `unicode` flag.

        Returns:
            str: ASCII art representation of the image.

        Notes:
            - Provide either `image_path` or `image` parameter to specify the image source.
            - If `width` is not provided, the original image width is used.
            - The `unicode` flag determines whether to use Unicode or regular ASCII characters.
            - If `ascii_chars` is empty, a default set of characters is used based on the `unicode` flag.
            - Brighter pixels in the image correspond to darker characters in the ASCII art.
        """
        Image.MAX_IMAGE_PIXELS = None
        if image_path:
            if not image:
                image = Image.open(image_path)
        elif not image:
            return ""

        aspect_ratio = image.height / image.width
        if width is None:
            width = image.width
        height = int(width * aspect_ratio)
        image = image.resize((width, height)).convert('L')  # Resize and convert to grayscale
        image_array = np.array(image)

        if ascii_chars == "":
            if unicode:
                ascii_chars = "█▮■▩▦▣▤@#$+=□:▫-. "
            else:
                ascii_chars = "@%#$*+=-:. "

        pixel_intensity = 255 - image_array
        ascii_chars_indices = (pixel_intensity / 255 * (len(ascii_chars) - 1)).astype(int)
        ascii_art_array = np.array(list(ascii_chars))[ascii_chars_indices]
        ascii_art = '\n'.join(''.join(row) for row in ascii_art_array)

        return ascii_art
