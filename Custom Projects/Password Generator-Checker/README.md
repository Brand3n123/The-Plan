# Password Toolkit

A two-part Python project for generating and evaluating passwords.  

This project demonstrates practical use of:  
- **Modules** - separating reusable logic (`custom_password.py`) from the CLI (`password_tool.py`).  
- **Functions** - building and reusing `generate_password()` and `check_strength()`.  
- **Strings and Lists** - evaluating passwords with length and character diversity.  
- **Conditionals & Loops** - handling user input and validation.  
- **Input handling & error checking** - basic interactive CLI design.  

---

## Components  

- **`custom_password.py`**  
  Provides the core functionality:  
  - `generate_password(length)` - creates a secure random password.  
  - `check_strength(password)` - evaluates a password as **WEAK**, **MEDIUM**, or **STRONG**.  

- **`password_tool.py`**  
  A command-line interface (CLI) that lets users:  
  - Generate a new password of a chosen length.  
  - Check the strength of an existing password.  

---

## Usage  

Run the interactive tool with Python 3:  

```bash
python3 password_tool.py

Would you like to 'Generate' a new password, or 'Check' the strength of an existing password? Generate
Please enter the requested password length: 16
Your new password is gH8!@aRzQ1#mNp2W

Would you like to 'Generate' a new password, or 'Check' the strength of an existing password? Check
Please enter the password to be checked: Password123
Your password is WEAK.
