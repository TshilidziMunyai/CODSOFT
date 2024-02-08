import random
def decor(func):
  def wrap():
    print("\033[1;37m* * * * * * * * * * * * * * * * * *\033[0m")
    func()
    print("\033[1;37m* * * * * * * * * * * * * * * * * *\033[0m")

  return wrap

@decor
def print_text():
    print(f"\033[38;5;46m WELCOME TO THE PASSWORD GENERATOR \033[0m")
print_text()

ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '[', ']']



def get_letters():
    while True:
        user_alphabets = input("\033[1;36m\nHow many letters would you like in your password?\033[0m\n")
        if user_alphabets.isdigit():
           return int(user_alphabets)
        else:
           print("Please enter a valid number.")


def get_numbers():
   while True:
    user_numbers = input("\033[1;36mHow many numbers would you like in your password?\033[0m\n")
    if user_numbers.isdigit():
       return int(user_numbers)
    else:
        print("Please enter a valid number.")


def get_symbols():
   while True:
    user_symbols = input("\033[1;36mHow many symbols would you like in your password?\033[0m\n")
    if user_symbols.isdigit():
       return int(user_symbols)
    else:
        print("Please enter a valid number.")
       
         
def generate_password(user_alphabets, user_numbers, user_symbols):
    password = ""

    for char in range(1, user_alphabets + 1):
        password += random.choice(ALPHABETS)

    for number in range(1, user_numbers +1):
        password += random.choice(NUMBERS)

    for symbol in range(user_symbols):
        password += random.choice(SYMBOLS)

    password = list(password)
    random.shuffle(password)
    password = ''.join(password)
    return password


def decor(func):
  def wrap(password):
    print("**************")
    func(password)
    print("**************")
  return wrap

@decor
def print_password(password):
    print(f"\033[38;5;46m{password}\033[0m")



if __name__=="__main__":
    user_alphabets = get_letters()
    user_numbers = get_numbers()
    user_symbols = get_symbols()

    while True:

        password = generate_password(user_alphabets, user_numbers, user_symbols)
        print("\033[1m\nYour password is:\033[0m")
        print_password(password)

        regenerate = input("Would you like to regenerate a new password? (yes/no)\n").lower()
        while regenerate != 'yes' and regenerate != 'no':
            print("invalid response")
            regenerate = input("Would you like to regenerate a new password? (yes/no)\n").lower()
         
        if regenerate == 'yes':
            continue
        else:
            print("THANK YOU 😀")
            break
           

