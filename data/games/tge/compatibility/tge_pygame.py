from .. import os
from importlib import import_module as importlib_import_module

import pygame

from ..random_generators import generate_random_string

from ..tbe import pass_func

from .. import PIL
if PIL:
    from ..image_processing import count_gif_frames


def update_screen(clock: pygame.time.Clock, fps: int = 0) -> None:
    """
    Update the display and control the frame rate.

    Parameters:
        clock (pygame.time.Clock): The Pygame clock object to control the frame rate.
        fps (int): The desired frames per second for the display.

    Returns:
        None: This function does not return anything.
    """
    pygame.display.update()
    clock.tick(fps)

def render_text(screen: pygame.Surface, text: str, font_name: str, size: int, color: tuple, position: tuple) -> None:
    """
    Renders and displays the given text on the specified Pygame screen.

    Parameters:
    - screen (pygame.Surface): The Pygame surface on which to render the text.
    - text (str): The text to be rendered.
    - font_name (str): The name of the font to be used for rendering.
    - size (int): The font size for rendering the text.
    - color (tuple): The RGB tuple representing the color of the rendered text.
    - position (tuple): The (x, y) tuple specifying the position to display the rendered text on the screen.

    Returns:
    - None: This function does not return any value.
    """
    font = pygame.font.SysFont(font_name, size)
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, position)

if PIL:
    def load_images_from_directory(directory_path: str) -> None:
        """
        Loads all images in the specified directory to pygame.

        Args:
            directory_path (str): The path of the directory.
        """

        supported_extensions = [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tga", ".lbm", ".pbm", ".ppm", ".svg", ".tiff", ".webp", ".xbm", ".xpm", ".tif"]
        skipped = []
        files = {}
        
        for file in os.listdir(directory_path):
            file_name, file_extension = os.path.splitext(file)
            if file_extension in supported_extensions:
                try:
                    if file_extension == ".gif":
                        if count_gif_frames(directory_path + "/" + file)[1] == 1:
                            pass
                        else: 
                            skipped.append(file)
                            continue
                    files[file_name] = file
                except:
                    skipped.append(file)
                    continue
        if len(files) == 0:
            return False
        successful_files = 0
        temp_file_name = generate_random_string(20)
        with open(f"{temp_file_name}.py", "w") as f:
            f.write("from pygame import image\n")
            f.write("def pygame_load_images_from_directory_temp_file():\n")
            f.write("\tsuccessful_files = 0\n")
            for file in files:
                f.write(f"\tglobal {file}\n")
                f.write(f"\t{file} = image.load('{directory_path}/{files[file]}')\n")
                f.write("\tsuccessful_files += 1\n")
            f.write("\treturn successful_files")
        try:
            generated_module = importlib_import_module(temp_file_name)
            successful_files = generated_module.pygame_load_images_from_directory_temp_file()
        except:
            return skipped, successful_files, False
        os.remove(f"{temp_file_name}.py")

        if len(skipped) == 0:
            return skipped, successful_files, True
        else:
            return skipped, successful_files, False
else:
    def load_images_from_directory(directory_path: str) -> None:
        "A fallback function if Pillow is not installed"
        return [], 0, False

def handle_input(quit_callback = exit, key_callback = pass_func, mouse_button_callback = pass_func):
    """
    Handles various input events in a Pygame application.

    Args:
        quit_callback (function, optional): A callback function to handle the quit event.
            Defaults to the exit function.
        key_callback (function, optional): A callback function to handle key press events.
            Defaults to the pass_func function.
        mouse_button_callback (function, optional): A callback function to handle mouse button press events.
            Defaults to the pass_func function.

    Returns:
        None

    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Handle the quit event
            if quit_callback:
                quit_callback()
        elif event.type == pygame.KEYDOWN:
            # Handle key press events
            if key_callback:
                key_callback(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle mouse button press events
            if mouse_button_callback:
                mouse_button_callback(event.button)
                
class SpriteAnimator:
    def __init__(self, images: list, frame_delay: int) -> None:
        """
        Initializes the SpriteAnimator.

        Args:
            images (list): A list of pygame.Surface objects representing the frames of the animation.
            frame_delay (int): The delay (in milliseconds) between each frame.
        """
        self.images = images
        self.frame_delay = frame_delay
        self.num_frames = len(images)
        self.frame_index = 0
        self.frame_counter = 0

    def animate_sprite(self, sprite: pygame.sprite.Sprite) -> None:
        """
        Animates a sprite using the initialized images and frame delay.

        Args:
            sprite (pygame.sprite.Sprite): The sprite to animate.

        Returns:
            None
        """
        frame = self.images[self.frame_index]
        sprite.image = frame
        # Update the sprite's rect if needed
        # sprite.rect = frame.get_rect()

        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.frame_index = (self.frame_index + 1) % self.num_frames
            self.frame_counter = 0

        # Update the screen or sprite group
        # pygame.display.update() or your_sprite_group.draw(your_screen)

        # Delay between frames
        pygame.time.delay(self.frame_delay)

def check_collision(*rects: pygame.Rect) -> bool:
    """
    Check for collision between multiple rectangles.

    Parameters:
    - rects: Variable number of pygame.Rect objects representing the rectangles

    Returns:
    - True if any of the rectangles collide, False otherwise
    """
    for i in range(len(rects)):
        for j in range(i + 1, len(rects)):
            if rects[i].colliderect(rects[j]):
                return True
    return False

def check_collision_with_all(*rects: pygame.Rect) -> bool:
    """
    Check for collision with all rectangles.

    Parameters:
    - rects: Variable number of pygame.

    Returns:
    - True if all of the rectangles collide, False otherwise
    """
    for i in range(len(rects)):
        for j in range(len(rects)):
            if not rects[i].colliderect(rects[j]):
                return False
    return True

def pygame_exit() -> None:
    """
    ㅤ
    >>> pygame.quit()
    """
    pygame.quit()

def background_color(window: pygame.Surface, color: tuple) -> None:
    """
    Fill the given Pygame window surface with the specified color.

    Args:
        window (pygame.Surface): The Pygame window surface to be filled.
        color (tuple): A tuple representing the RGB values of the desired color.
    
    Returns:
        None
    """
    window.fill(color)


def draw_texture_at(surface: pygame.Surface, texture: pygame.Surface, position: tuple) -> None:
    """
    Draws a texture onto a surface at a specified position.

    Args:
        surface (pygame.Surface): The surface onto which the texture will be drawn.
        texture (pygame.Surface): The texture image to be drawn onto the surface.
        position (tuple): The position (x, y) where the texture will be drawn on the surface.

    Returns:
        None
    """
    surface.blit(texture, position)


def exit():
    """
    Exit the program safely and without errors just with one line
    >>> pygame.quit()
    >>> quit()
    """
    pygame.quit()
    quit()

# def convert_num_to_key(num):
#     index = {
        
        
        
        
#         8: 'backspace',
#         9: 'tab',
        
#         13: 'enter',
        
#         27: 'esc',
        
        
#         32: 'space',
        
#         35: '#',
        
        
#         43: '+',
#         44: ',',
#         45: '-',
#         46: '.',
        
#         48: '0',
#         49: '1',
#         50: '2',
#         51: '3',
#         52: '4',
#         53: '5',
#         54: '6',
#         55: '7',
#         56: '8',
#         57: '9',
        
        
        
        
        
        
        
        
        
#         94: '^',
#         97: 'a',
#         98: 'b',
#         99: 'c',
#         100: 'd',
#         101: 'e',
#         102: 'f',
#         103: 'g',
#         104: 'h',
#         105: 'i',
#         106: 'j',
#         107: 'k',
#         108: 'l',
#         109: 'm',
#         110: 'n',
#         111: 'o',
#         112: 'p',
#         113: 'q',
#         114: 'r',
#         115: 's',
#         116: 't',
#         117: 'u',
#         118: 'v',
#         119: 'w',
#         120: 'x',
#         121: 'y',
#         122: 'z',
        
        
#         127: 'del',
        
#         180: '´',
        
        
#         223: 'ß',
        
#         246: 'ö',
#         228: 'ä',
#         252: 'ü',
        
        
        
#         1073741925: 'menu',
        
#         1073742048: 'ctrl',
#         1073742049: 'shift',
#         1073742050: 'alt',
#         1073742051: 'windows',
#         1073742052: 'rctrl',
#         1073742053: 'rshift',
#         1073742054: 'alt ctrl',
#         1073742055: 'rwindows',
        
#         1073741881: 'caps lock',
#         1073741882: 'f1',
#         1073741883: 'f2',
#         1073741884: 'f3',
#         1073741885: 'f4',
#         1073741886: 'f5',
#         1073741887: 'f6',
#         1073741888: 'f7',
#         1073741889: 'f8',
#         1073741890: 'f9',
#         1073741891: 'f10',
#         1073741892: 'f11',
#         1073741893: 'f12',
#         1073741894: 'print',
#         1073741895: 'scroll lock',
#         1073741896: 'pause',
#         1073741897: 'insert',
#         1073741898: 'home',
#         1073741899: 'page up',
        
#         1073741901: 'end',
#         1073741902: 'page down',
#         1073741903: 'right',
#         1073741904: 'left',
#         1073741905: 'down',
#         1073741906: 'up',
#         1073741907: 'num lock',
#         1073741908: 'divide',
#         1073741909: 'multiply',
#         1073741910: 'subtract',
#         1073741911: 'add',
#         1073741912: 'renter',
#         1073741913: 'num1',
#         1073741914: 'num2',
#         1073741915: 'num3',
#         1073741916: 'num4',
#         1073741917: 'num5',
#         1073741918: 'num6',
#         1073741919: 'num7',
#         1073741920: 'num8',
#         1073741921: 'num9',
#         1073741922: 'num0',
#         1073741923: 'comma',
        
        
        
        
        
        
        
#     }
#     if isinstance(num, int):
#         try:
#             return index[num]
#         except:
#             return str(num) + ' <- Missing key'
#     elif isinstance(num, str):
#         try:
#             return next(key for key, value in index.items() if value == num)
#         except StopIteration:
#             return num + ' <- Invalid key'











