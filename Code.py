import random
import time

print("You are in the Kingdom of Dragons. In front of you, you see two caves.")
print("In one cave, the dragon is friendly and will share his treasure with you.")
print("The other dragon is hungry and will eat you on sight!")

def get_user_choice():
    while True:
        try:
            user_choice = int(input("Enter 1 or 2: "))
            if user_choice in (1, 2):
                return user_choice
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")


    
def Cave():
    user_choice = get_user_choice()

print("You approach a cave...")
time.sleep(2)
print("a large dragon jumps in front of you")
time.sleep(1)
print("He opens up his jaws and ....")
time.sleep(2)

    # Generate a random outcome based on user's choice   
    if user_choice == 1:
        outcome = random.choice("Gobbles you down")
    else:
        outcome = random.choice("Greets you and shares his treasure")

    print(outcome)

    
