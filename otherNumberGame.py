import random

computer_choice=random.randint(1,100)
while True:
    user_choice=int(input("Enter your number(1 to 100):"))
    if user_choice>computer_choice:
        print("You guess Too High!!")
    elif user_choice<computer_choice:
        print("You guess Too Low!!")
    elif user_choice==computer_choice:
        print("Congrats,You won the game")
        break
    else:
        print("Invalid Input (please enter only number value)")
print("Bye")
        