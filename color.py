from art import *
class Color:
    # colors codes
    color_code_cyan = '\033[96m'  # Cyan color
    color_code_green = '\033[92m'  # Green color
    color_code_yellow = '\033[93m'  # Yellow color
    color_code_red = '\033[91m'  # Red color
    color_code_reset = '\033[0m'  # Reset color
    color_code_purple = '\033[35m'
    color_code_orange = '\033[43m'
    color_code_blue = '\033[44m'
    darkgrey='\033[90m'

    # لازم اضفلها دوكيومنتيشن
    def print_colored_art(text, font, color): #تاخد البرنت الي بالارت وتلونه 
        # Generate ASCII art
        art_text = text2art(text, font=font)
        # Apply color using colorama
        colored_art = f"{color}{art_text}"
        # Print the colored ASCII art
        print(colored_art)

    def print_colored_space_art(text, font, color): #تاخد البرنت الي بالارت وتلونه 
        # Generate ASCII art
        art_text = text2art( " " * 22 + text, font=font)
        # Apply color using colorama
        colored_art = f"{color}{art_text}"
        # Print the colored ASCII art
        print(colored_art)