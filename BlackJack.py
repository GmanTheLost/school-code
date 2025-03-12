import random  # import a package/module
import sys
import time

hand = []  # a list

dealer = []  # Dealers hand now a list



def is_win():
    print("Dealers hand is = ", sum(dealer))
    print("Your hand is = ", sum(hand))

    if sum(hand) > 21:
        print("BUST!!! You lose!")

    elif sum(hand) == sum(dealer):
        print("Push! Bet returned to player try again.")

    elif sum(dealer) > 21:
        print("Dealer busts! YOU WIN!!!")

    elif sum(hand) > sum(dealer) and sum(hand) <= 21:
       print("You win!!!!")

    else:
        print("Ah! Tough luck this time luck try again later.")
    sys.exit(0)

# Make a fake card game
hand.append(random.randint(1, 11))
hand.append(random.randint(1, 11))

print("Starting hand is:", hand, "=", sum(hand), )

dealer.append(random.randint(1, 11))
dealer.append(random.randint(1, 11))

print("Dealer's Starting hand is:", dealer, "=", sum(dealer))

if sum(hand) == 21:
    is_win()
if sum(dealer) == 21:
    is_win()

    
while True:
    user_input = input("Do you want to hit or stay (N/y): ").lower()

    if user_input == "y":
        hand.append(random.randint(1, 11))
        print("Your current hand: ", hand, "=", sum(hand), "\n")
        if sum(hand) == 21:
            print("BLACK JACK!!! \n")
            break
        elif sum(hand) > 21:
            is_win()
            break
    elif user_input == "n":
        print("You stay.\n")
        break

time.sleep(1)    
while True:
    if sum(dealer) <= 16:
       print ("Dealer hits!\n")
       dealer.append(random.randint(1, 11))
       print("Dealer's hand: ", dealer, "=", sum(dealer), "\n")
    elif sum(dealer) == 21:
        print
        is_win()
        break
    else: 
        print ("Dealer stands!\n")
        break
    time.sleep(1.5)
is_win()

