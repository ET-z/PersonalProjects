import random

i = "true"

def game():
    choice = input("Pick between Rock(r), Paper(p), or Scissors(s): ")
    choice.lower()
    bot = random.randint(1, 3)
    
    if choice == "r":
        print("You chose Rock")
        if bot == 1:
            print("Bot chose Rock")
            print("You tied!")
        if bot == 2:
            print("Bot chose Paper")
            print("You lose!")
        if bot == 3:
            print("Bot chose Scissors")
            print("You win!")
            
    elif choice == "p":
        print("You chose Paper")
        if bot == 1:
            print("Bot chose Rock")
            print("You win!")
        if bot == 2:
            print("Bot chose Paper")
            print("You tied!")
        if bot == 3:
            print("Bot chose Scissors")
            print("You lose!")
            
    elif choice == "s":
        print("You chose Scissors")
        if bot == 1:
            print("Bot chose Rock")
            print("You lose!")
        if bot == 2:
            print("Bot chose Paper")
            print("You win!")
        if bot == 3:
            print("Bot chose Scissors")
            print("You tied!")
            
    else:
        print("Your choice is invalid")
        game()

while i == 'true':
    game()

game()
