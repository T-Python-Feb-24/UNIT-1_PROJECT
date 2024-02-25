import random
from colorama import Fore, Style, init
from art import *
from color import Color
from word_categories import WrodsCategories


init(autoreset=True)
space:str = " " * 22

class Round:
    def play_round(used_words, category, current_round):

        guessed_letters:set = set()
        attempts:int = 5
        score:int = 0

        # Check for the availablty of the word
        available_words = [match_word for match_word in WrodsCategories.word_categories[category] if match_word[0] not in used_words]
        
        if not available_words:
            print("No more words available.")
            return 0
        
        word, description = random.choice(available_words) #ممكن ابغى اضيف جزئية للهينت كتابه 

        # To avoid repeat the word twoic
        used_words.add(word) 

        # Start the round 
        Color.print_colored_space_art("............................", font=DEFAULT_FONT,color=Fore.YELLOW)
        Color.print_colored_space_art(f"........ Round   {current_round + 1} ........", font=DEFAULT_FONT,color=Fore.YELLOW)
        

        # Guess word -> out if no more attempts (only have 5 attempts)
        while attempts > 0:

            print()
            print(Fore.CYAN + space + f"DESCRIPTION 💡... {description}")
            # Word presentaion 
            word_letters = [letter if letter in guessed_letters else '_' for letter in word]
            # Style the word
            Color.print_colored_space_art(" ".join(word_letters), font=DEFAULT_FONT, color=Fore.WHITE)
            
            try:
                # Start to guess
                guess = input(Fore.CYAN + space + "Guess a letter or word 🤔 → " + Style.RESET_ALL).lower()
                if guess.isalpha(): # Only letters is allowed

                    if len(guess) == 1:  # if guessing a letter

                        if guess in guessed_letters:
                            print(Fore.YELLOW + space + " ⚠️ You've already guessed that letter, just try another letter!! ⚠️ " + Style.RESET_ALL)
                            continue

                        guessed_letters.add(guess)
                        if guess in word:
                            score += 2 
                            if all(letter in guessed_letters for letter in word):
                                Color.print_colored_space_art( " ".join(word),font=DEFAULT_FONT,color=Fore.GREEN)
                                print(Fore.GREEN + space + "✔️  CORRECT!! +2 socre" + Style.RESET_ALL)
                                print(Fore.GREEN + space + f"🎉 Congratulations! You've guessed the word correctly 🥳" + Style.RESET_ALL)
                                print(Fore.MAGENTA + space + f"🟢 Good job! Score ⭐ → {score}")
                                return score
                            print(Fore.GREEN + space + "✔️  CORRECT!! +2 socre" + Style.RESET_ALL)
                            print(Fore.MAGENTA + space + f"🟢 Good job! Score ⭐ → {score}")
                        else:
                            attempts -= 1
                            score -= 1
                            if attempts == 0:
                                Color.print_colored_space_art( " ".join(word),font=DEFAULT_FONT,color=Fore.RED)
                                print(Fore.RED + space + f"❌ WRONG!! -1 socre")
                                print(Fore.RED + space + f"💢 Sorry! You failed to guess the word correctly 😞" + Style.RESET_ALL)
                                print(Fore.MAGENTA + space + f"🔴 Score ⭐ → {score}")
                                break
                            print(Fore.RED + space + f"❌ WRONG!! -1 socre")
                            print(Fore.RED + space + f"🔴 Be careful you have {attempts} {'attempt' if attempts == 1 else 'attempts'} left")
                            print(Fore.MAGENTA + space + f"🔴 Score ⭐ → {score}")

                    elif len(guess) == len(word) and guess == word:  # if guessing the whole word correctly
                        Color.print_colored_space_art( " ".join(word),font=DEFAULT_FONT,color=Fore.GREEN)
                        score += len(word) * 2  
                        print(Fore.GREEN + space + f"✔️  CORRECT!! +{len(word) * 2} socre" + Style.RESET_ALL)
                        print(Fore.GREEN + space + f"🎉 Congratulations! You've guessed the word correctly 🥳" + Style.RESET_ALL)
                        print(Fore.MAGENTA + space + f"🟢 Score ⭐ → {score}")
                        return score
                    elif guess != word:
                        attempts -= 1
                        score -= len(word)
                        if attempts == 0:
                            Color.print_colored_space_art( " ".join(word),font=DEFAULT_FONT,color=Fore.RED)
                            print(Fore.RED + space + f"❌ WRONG!! -{len(word)} socre")
                            print(Fore.RED + space + f"💢 Sorry! You failed to guess the word correctly 😞" + Style.RESET_ALL)
                            print(Fore.MAGENTA + space + f"🔴 Score ⭐ → {score}")
                            break
                        print(Fore.RED + space + f"❌ WRONG!! -{len(word)} socre")
                        print(Fore.RED + space + f"🔴 Be careful you have {attempts} {'attempt' if attempts == 1 else 'attempts'} left")
                        print(Fore.MAGENTA + space + f"🔴 Score ⭐ → {score}")
        
                else:
                    raise ValueError(Fore.YELLOW + space +  "⚠️ Invalid input. Only letters are allowed ⚠️" + Style.RESET_ALL)
            except ValueError as e:
                print(e)
        return score