import time
import sys
import threading

try:
    import pygame
except ImportError:
    print("pygame is not installed. Install it with 'pip install pygame' to play the birthday tune.")

def clear_console():
    """Clear the console screen."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def print_message_with_delay(message, delay=0.04):
    """Print the message with a delay to create a typing effect."""
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def birthday_animation():
    message = f"""
     __  __  __   __      ____    ____     ____  
    |  \/  | \ \_/ /     | __ )  |  _ \   / /\ \ 
    | |\/| |  \   /      |  _ \  | |_) | | |  | |
    | |  | |   | |       | |_) | |  _ <  |  \/  |
    |_|  |_|   |_|       |____/  |_| \_\  \____/ 


                      _..._  ,s$$$s.                                                                     
                    .$$$$$$$s$$ss$$$$,                                                                  
                    $$$sss$$$$s$$$$$$$                                                                  
                    $$ss$$$$$$$$$$$$$$    H A P P Y  B I R T H D A Y  M O U A Z !                                   
                    '$$$s$$$$$$$$$$$$'                                                                  
                     '$$$$$$$$$$$$$$'                                                                   
                       S$$$$$$$$$$$'                                                                    
                        '$$$$$$$$$'                                                                     
                          '$$$$$'   S U R P R I S E !                                                   
                            $$$ 
                             $                                                                        
    """
    clear_console()  
    print_message_with_delay(message)

def play_birthday_tune():
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/mouaz/Downloads/Project X/Forbidden folder/i said forbidden/fuck u/y2mate.com -  2022.mp3")  
    pygame.mixer.music.play()

    time.sleep(200)
    pygame.mixer.music.stop()

animation_thread = threading.Thread(target=birthday_animation)
music_thread = threading.Thread(target=play_birthday_tune)

animation_thread.start()
music_thread.start()

animation_thread.join()
music_thread.join()
