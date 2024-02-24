from user import User
from art import*
from colorama import*

user1 = User()
tprint(" Welcome to Halthey Care ",font="cybermedum",chr_ignore=True)
print('-----------------------------------------------')
have_account = input(Fore.LIGHTYELLOW_EX+"Do you have account? Y (yes) / N (no)")
if have_account.lower() in ["y", "yes"]:
    user1.log_in()
    calor_value = user1.calculate_calories()
    print(Fore.BLUE+"Your calories are : "+str(calor_value) +"\n")
    cal_bmi_value = user1.calculate_bmi()
    print(Fore.BLUE+"Your BMI are : "+ str(cal_bmi_value)+"\n")

    user1.check_diet()
    user1.showfig()
else:
    user1.sign_up()
    user1.log_in()
    calor_value = user1.calculate_calories()
    print(Fore.BLUE+"Your calories are : "+str(calor_value) +"\n")
    cal_bmi_value = user1.calculate_bmi()
    print(Fore.BLUE+"Your BMI are : "+ str(cal_bmi_value)+"\n")

    user1.check_diet()
    user1.showfig()

