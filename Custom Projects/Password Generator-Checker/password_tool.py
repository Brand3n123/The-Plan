from custom_password import generate_password
from custom_password import check_strength

user_input = input("Would you like to 'Generate' a new password, or 'Check' the strength of an existing password? ")

def user_prompt_command(user_input):
    while True:
        if user_input.lower() == "generate":
            try:
                length = int(input("Please enter the requested password length: "))
                print(f"Your new password is {generate_password(length)}")
            except ValueError:
                print("Please enter a valid number.")
                user_prompt_command(user_input)
                
        elif user_input.lower() == "check":
            password = (input("Please enter the password to be checked: "))
            print(f"Your password is {check_strength(password)}.")
        else:
            print("Please enter a valid input of either Generate or Check.")
            user_input = input("Would you like to 'Generate' a new password, or Check the strength of an existing password? ")
            user_prompt_command(user_input)

user_prompt_command(user_input)