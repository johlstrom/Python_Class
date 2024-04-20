from random import choice, randint, shuffle
import time

# ---------------------------- TEXT GENERATOR ------------------------------- #

#Text Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letter = [choice(letters) for _ in range(randint(1, 1))]
    password_letter = "".join(password_letter)
    return(password_letter)

# ---------------------------- SAVE PASSWORD ------------------------------- #

run_program = True
starting_string = ""

while run_program:
    temp_char = generate_password()
    starting_string = starting_string + temp_char
    time.sleep(0.1)
    print(starting_string)