

#import tkinter
from tkinter import messagebox

def show_message(message_level, user_feedback_level=0, title=None, message=None, **options):
    """
    Display a message box to the user with customizable parameters.

    This function provides a convenient way to display different types of message boxes
    with varying levels of user feedback options. It uses the `messagebox` module from
    the `tkinter` library to create the message box dialog.

    Parameters:
    message_level (int): The level of the message box. Should be an integer between 0 and 3.
                        0: Information message
                        1: Warning message
                        2: Error message
                        3: Question message

    user_feedback_level (int, optional): The level of user feedback options. Should be
                                        an integer between 0 and 5. Defaults to 0.
                                        0: OK button
                                        1: OK and Cancel buttons
                                        2: Yes and No buttons (returns True for 'yes' and False for 'no')
                                        3: Yes, No, and Cancel buttons
                                        4: Retry and Cancel buttons
                                        5: Abort, Retry, and Ignore buttons

    title (str, optional): The title of the message box. Defaults to None.

    message (str, optional): The message content to be displayed in the message box.
                            Defaults to None.

    **options: Additional options that can be passed to the `messagebox` module for
            further customization of the message box appearance.

    Returns:
    - For user_feedback_level 2 (Yes/No): True if 'yes' is clicked, False if 'no' is clicked.
    - For other user_feedback_levels: The button text that was clicked ('ok', 'cancel', etc.).

    Example usage:
    ```
    result = show_message(1, 2, "Warning", "Are you sure you want to proceed?")
    if result:
        print("User confirmed.")
    else:
        print("User declined.")
    ```

    Note:
    - If the provided `message_level` or `user_feedback_level` values are out of range,
    they will be adjusted to the nearest valid value.
    - The actual appearance of the message box may vary depending on the platform's
    native dialog styles.
    """
    
    levels = ['info', 'warning', 'error', 'question']
    feedback = ['ok', 'okcancel', 'yesno', 'yesnocancel', 'retrycancel', 'abortretryignore']
    if message_level < 0 or message_level > len(levels):
        message_level = 0
    if user_feedback_level < 0 or user_feedback_level > len(feedback):
        user_feedback_level = 0
    answer = messagebox._show(title, message, levels[message_level], feedback[user_feedback_level], **options)
    if user_feedback_level == 2:
        if answer == 'yes':
            return True
        else:
            return False
    else:
        return answer

if __name__ == "__main__":
    print(show_message(message_level=2, user_feedback_level=0, title="Error!", message="An Error occurred."))



