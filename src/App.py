import random
import string

# Password Generator 

def passwod_generator(length=12, include_numbers=True, include_special_chars=True):
    letters = string.ascii_letters
    digits = string.digits if include_numbers else ''
    special_chars = string.punctuation if include_special_chars else ''

    all_chars = letters + digits + special_chars

    if length < 1:
        raise ValueError("Password Length should be at least 5")
    password =''.join(random.choice(all_chars) for _ in range(length)) 

    return password 
   
def main():
    print("Please enter the values for below and get the password ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("---------------------------")

    try:
      length = int(input("Enter the desired password length : "))
      include_digits = input("Include digits ? (y/n) : ").lower() == 'y'
      include_special_chars = input("Include special characters? (y/n) :").lower() == 'y'

      password = passwod_generator(length, include_digits, include_special_chars)

      print(f"Generated Password : {password}")

    except ValueError as e :
        print(f"Error : {e}")

if __name__ == "__main__":
  main()

        
          
    
