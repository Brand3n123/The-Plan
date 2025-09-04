import random
import string


def generate_password(length):
    password_bank = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(password_bank)
    return password



def check_strength(password):
    done = False
    password_strength_level = 0
    
    if len(password) >= 12:
        password_strength_level += 1

    for char in password:
        char_lower = str(char).lower()
        if char_lower == char:
                password_strength_level += 1
                break

    for char in password:
        char_upper = str(char).upper()
        if char_upper == char:
                password_strength_level += 1
                break

    for char in password:
        for num in string.digits:
            if char == num:
                password_strength_level += 1
                done = True
        if done == True:
            done = False
            break

    for char in password:
            for special in string.punctuation:
                if char == special:
                    password_strength_level += 1
                    done = True
            if done == True:
                break

    if password_strength_level < 3:
        return "WEAK"
    elif 3 <= password_strength_level < 5:
        return "MEDIUM"
    elif password_strength_level >= 5:
        return "STRONG"
