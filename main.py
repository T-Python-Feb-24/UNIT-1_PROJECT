from questions import generate_questions
from colorama import *
from ascii_animator import *
from art import *
from pyfiglet import figlet_format
from user import User


init(autoreset=True)
user_data = []
user_data = User.load_user_data(user_data)

#welcome
print(Fore.MAGENTA + figlet_format ("            WELCOME TO PYTHON QUIZ GAME" , font= "small"))
print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
print(Fore.CYAN  + "\n                           ⎯  About the game ⎯ \n\n")
print('''                 Get ready to test your Python knowledge. 
   Each question in this section is specifically designed to challenge 
  your understanding of Python programming. So, buckle up and let's dive 
                     into the world of Python trivia!\n ''')
print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")

#ask name
name = input("\n✦ Enter your name:\n").title()
print(Fore.CYAN + "\n☼✨ Happy to have you " + name + " with us today! ✨☼\n " )

new_user = {"name" : name , "score" : 0 }
user_data.append(new_user)

count = 10
while count > 0 :
    try:
        choice = input("\n\n✦ Are you ready to dive into the game? (yes/no):\n").lower()
        if choice == "yes": 
            print("\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
            print(Fore.CYAN + figlet_format ( "      Let's begin\n" , font= "graceful"))
            print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")

            #choose_category
            print(Fore.YELLOW + "\n✦ Choose a category:\n")
            print("   a) Syntax and Basics")
            print("   b) Data Structure")
            print("   c) Object Oriented Programming (OOP)\n")
            category_choice = input("✦ Enter the letter of the category: \n").lower()  
            questions = generate_questions(category_choice)
        elif choice == "no":
            print(Fore.RED + "\nExit game\n")
            break
        else:
            raise Exception("✦ Plese type 'yes' or 'no' ")
        
        
        while True:
            final_score = 0
            for question, options, correct_answer in questions:

                #display question
                print(question)
                for option, text in options.items():
                    print(f"{option}) {text}")

                #answer question
                answer = input("\n✦ Enter your answer (a/b/c/d): \n").lower()
                score = 0
            
                if answer == correct_answer:
                    score += 1
                    print("\n")
                    init(autoreset=True)
                    print(Fore.BLACK + Back.GREEN + "\nCORRECT ! ✅🎉")
                    print(f"\nYou gain {score} score !")
                else:
                    print(Fore.BLACK + Back.RED +"\nINCORRECT ! ❎🚨")
                    print(f"\nThe Correct answer is : {correct_answer}")
                final_score += score
                print(f"• You got: {final_score}/10\n")
                print("⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
            


            if final_score == 10:
                print(Fore.GREEN + "\nPerfect!")
            elif final_score >= 5 :
                print(Fore.CYAN + "\nGood job!")
            elif final_score <= 4:
                print(Fore.RED + "\nBetter luck next time!")



            if final_score > new_user['score']:
                new_user['score'] = final_score
            else:
                pass 
            

            #rank 
            User.save_user_data(user_data)
            print("\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
            print(Fore.MAGENTA + "\n\n\n• Leaderboard:\n")
            sorted_users = sorted(user_data, key=lambda x: x['score'], reverse=True)
            for i, player in enumerate(sorted_users, 1):
                print(f"    {i}. {player['name']} - Score: {player['score']}")
            break
    except Exception as e:
        print(e) 


    play_again = input("\n\n✦ Do you want to try again? (yes/no): \n").lower()
    if play_again == "yes":
        continue
    elif play_again == "no":
        break