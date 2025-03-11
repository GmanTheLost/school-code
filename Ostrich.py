import random

def problem_1():
    animal_name = input("Please name an animal! ").lower()

    animal_letter = input("Please pick a letter in the animals name. ").lower()
    if animal_letter in animal_name:
        index = animal_name.index(animal_letter)

        print(f"The letter {animal_letter} is the #{index + 1} letter in {animal_name}!")
    else:  
        print(f"Sorry, the letter '{animal_letter}' is not in '{animal_name}'. ")


def collect_items():
    items = []  
    
    while True:
        item = input("Enter an item (or type 'exit' to stop): ")
        
        if item.lower() == 'exit':  
            break
        else:
            items.append(item)  
        print(f"Your current list{items}")

    if items:  
        print(f"First item: {items[0]}")
        print(f"Last item: {items[-1]}")
    else:
        print("No items were entered.")


# collect_items()
    
def Guess_number():
    Number_to_guess = random.randint(1, 10)
    guesses = 5

    while guesses > 0:
        try:
            User_guesse = int(input("Enter your Guess (1-10): "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        if User_guesse < Number_to_guess:
            guesses -= 1
            print(f"Too Low Try Again! Guesses Remaining: {guesses}!")
        elif User_guesse > Number_to_guess:
            guesses -= 1
            print(f"Too High Try Again! Guesses Remaining: {guesses}!")
        elif User_guesse == Number_to_guess:
            print(f"Congratulations you guessed correctly! You guessed right with {guesses} guesses remaining! ")
            break
    
        
    if guesses == 0:
        print(f"Ran out of Guesses You lose! Loser! Stinky loser! The answer was {Number_to_guess} BTW!") 

# Guess_number()