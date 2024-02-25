from colorama import Fore, Style, init
from art import *
from color import Color
from player import Player
from word_categories import WrodsCategories
from round import Round 

# Initialize Colorama
init(autoreset=True)

space:str = " " * 22
player_data:list = []

# Load player data
player_data = Player.load_player_data(player_data)
print()

Color.print_colored_art("---| GUESSING  WORDS  GAME |---",font=DEFAULT_FONT,color=Fore.BLUE) 
print()
print(Fore.CYAN + space + "Overview:")
print(space + "The Guessing Word Game challenges players to guess a word within a limited number of attempts. Each game consists of three rounds, \n" + 
    space + "during which players will guess words from chosen categories. Players can also track their progress and compare their performance with\n" +
    space + "others through the rank feature."
)
print()
print(Fore.CYAN + space + "Game Rules:")
print(space + "Each player starts by registering a nickname and selects a category to play. \n" + 
    space + "Players have three rounds to guess words within the chosen category.\n" +
    space + "In each round, players have 5 attempts to guess either a letter or the entire word.\n\n" +
    space + Fore.GREEN + "  Points are awarded based on correct guesses:\n" + Style.RESET_ALL +
    space + "       🌟 Guessing a letter correctly earns 2 points.\n" +
    space + "       🌟 Guessing the entire word earns 2 points for each letter in the word.\n\n" +
    space + Fore.RED + "    Points are deducted for incorrect guesses:\n" + Style.RESET_ALL +
    space + "       ❌ Incorrectly guessing a letter results in a deduction of 1 point.\n" +
    space + "       ❌ Incorrectly guessing the entire word results in a deduction of 1 point for each letter in the word.\n"
)

player_name = input(Fore.MAGENTA + space + "Let us to know your nickname 👥 → " + Style.RESET_ALL)
existing_player = Player.player_exists(player_name, player_data)
print()

if existing_player:
    print(Fore.BLUE + space + f"Welcome back {existing_player['name']}!! Your current score ⭐ → {existing_player['score']}")
else:
    print(Fore.BLUE + space + f"You are a new player!! Welcome to our game {player_name}!")
    existing_player = {"name": player_name, "score": 0}
    player_data.append(existing_player)

while True:
    try:
        # Menu TO:
        print()
        print(Fore.YELLOW + space + "↓ Welcome to the Guessing Word Game Menu ↓")
        print(space + "1. To Start the Geme 🚀")
        print(space + "2. To show Ranks 🏆")
        print(space + "3. Exit 🚪")
        print()
        player_choice:str = input(Fore.MAGENTA + space + "Please enter your choice here → " + Style.RESET_ALL)
        print()

        if player_choice == "1":
            while True:
                print(space + Fore.YELLOW + "↓ Choose a Category ↓")
                categories = list(WrodsCategories.word_categories.keys())
                # 🥘💻⛑️🛫🔬 #🎨🍳📚📷🏔️ #🥗🍣🌮🍩🍔
                for i, category in enumerate(categories, 1): # ممكن اسويه طباعة عشان الايموجي 
                    if category == "Hobbies":
                        print(space + f"{i}. {category} 🎭")
                    elif category == "Jobs":
                        print(space + f"{i}. {category} 💼")
                    elif category == "Food":
                        print(space + f"{i}. {category} 🍽️")
                print(space + f"{i + 1}. Back to main menu ◀️")
                print()
                category_choice:str = input(Fore.MAGENTA + space + "Please choose a category that you are excited to play → " + Style.RESET_ALL)
                if category_choice == str(i + 1):
                    break
                print()
                try:
                    category_index = int(category_choice) - 1
                    category = categories[category_index]
                    Color.print_colored_space_art(category, font=DEFAULT_FONT, color=Fore.WHITE)
                    print()
                    try:
                        ready_to_play:str = input(Fore.MAGENTA + space + "Are you ready to play 🕹️  (yes/no)? → " + Style.RESET_ALL)
                        print()
                        if ready_to_play == "yes":
                            print(space + f"Starting game for the category {category} 🚀🚀🚀..")
                            game_rounds = 3
                            used_words = set()
                            final_score = 0
                            
                            for current_round in range(game_rounds):
                                round_score = Round.play_round(used_words, category, current_round)
                                final_score += round_score 
                                print()  
                                print(Fore.BLUE +space + f"Round {current_round + 1} over with total score ⭐ → {final_score}")
                                print()
                            
                            if final_score > existing_player['score']:
                                existing_player['score'] = final_score
                                print()
                                print(Fore.YELLOW + space + f"NEW HIGHER SCORE 🎉🥇 ! Your score is now ⭐ → {final_score}" + Style.RESET_ALL) 
                            else:
                                print(space + f"Your FINAL SCORE is {final_score}. Your high score remains 🎖️  → {existing_player['score']}")
                                
                            Player.store_player_data(player_data)
                            Player.display_leaderboard_pretty(player_data)

                            play_again = input(Fore.MAGENTA + space + "Do you want to play again 🕹️  (yes/no)? →  " + Style.RESET_ALL).lower()
                            if play_again == "yes":
                                continue
                            elif play_again == "no":
                                print(Fore.YELLOW + space + "It was a great game!." + Style.RESET_ALL)
                                print()
                                break
                            else:
                                raise ValueError (space + "You have to choose 'yes' to play again or 'no' to go back to the main menu. ")
                        elif ready_to_play == "no":
                            continue
                        else:
                            raise ValueError(space + "You have to choose 'yes' to start the game or 'no' to go back to categories menu. ")  
                    except ValueError as e:
                        print(e)
                    break
                except (ValueError, IndexError):
                    print(space + "Invalid category choice.")
        elif player_choice == "2":
            Player.display_leaderboard_pretty(player_data)
        elif player_choice == "3":
            break 
        else:
            raise Exception (space + "You have to choose number only from the above menu (1-3).")
    except Exception as e:
        print(e)

Color.print_colored_art("-------| GAME OVER |--------",font=DEFAULT_FONT,color=Fore.BLUE)
    

