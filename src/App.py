import random
import string

# Password Generator 

def passwod_generator(length=12, include_numbers=True, include_spl_character=True):
    letters = string.ascii_letters
    digits = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_spl_character else ''

    all_chars = letters + digits + special_chars

    if length < 1:
        raise ValueError("Password Length should be at least 5")
    password =''.join(random.choice(all_chars) for _ in range(length)) 

    return password    