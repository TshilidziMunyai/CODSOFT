import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

def decor(func):
  def wrap():
    print("==========================================")
    func()
    print("==========================================")
  return wrap

@decor
def print_text():
    print(f"\033[38;5;46m WELCOME TO THE ROCK, PAPER, SCISSORS GAME \033[0m")
    print("         YOU GET THREE CHANCES        ")
print_text()

choice = {0: "Rock", 1: "Paper", 2: "Scissors"}
game_is_on = True
score = 0
turns = 3
while game_is_on:
    computer_choice = random.randint(0,2)
    user_choice = input("\033[1;36m\nWhat do you choose?\nType 0 for Rock, 1 for Paper and 2 for Scissors\033[0m\n")

    if not user_choice.isdigit():
        print("Enter a valid number")
        print("--------------------")
        continue
    user_choice = int(user_choice)
    if user_choice >= 3 or user_choice < 0:
        print("you entered an invalid number".capitalize())
        print("------------------------------")
        continue
    
    else:
        print(f"You chose: {choice[user_choice]}")
        print(game_images[user_choice])
        print (f"The computer chose: {choice[computer_choice]}")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("\033[37;42mYOU WIN!\033[0m")
            score +=1

        elif computer_choice == 0 and user_choice == 2:
            print("\033[37;41mYOU LOSE!\033[0m")
            
        elif computer_choice > user_choice:
            print("\033[37;41mYOU LOSE!\033[0m")

        elif user_choice > computer_choice:
            print("\033[37;42mYOU WIN!\033[0m")
            score +=1

        elif user_choice == computer_choice:
            print("\033[38;5;46;48;5;208mIT'S A DRAW!\033[0m")


    if not user_choice == computer_choice:
        turns -= 1
    print(f"You have: {turns} turns remaining.")
    print("-------------- ")
    if turns == 0:
        game_is_on = False
        if score < 2:
            # print("\033[36mSORRY YOU LOST THE GAME!\033[0m")
            print("\033[37;41mSORRY, YOU LOST THE GAME!\033[0m")

        else:
            print("\033[37;42mCONGRATULATIONS YOU WON THE GAME!\033[0m")

