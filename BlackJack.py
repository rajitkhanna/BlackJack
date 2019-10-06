import random

# Our Deck of Cards
deck_of_cards = []

# Dict of card values
Cards = {
    "TWO" : 2,
    "THREE" : 3,
    "FOUR" : 4,
    "FIVE" : 5,
    "SIX" : 6,
    "SEVEN" : 7,
    "EIGHT" : 8,
    "NINE" : 9,
    "TEN" : 10,
    "JACK" : 10,
    "QUEEN" : 10,
    "KING" : 10,
    "ACE" : (11,1),
}
    
# List of suits
Suit = [
    "SPADES",
    "CLUBS",
    "HEARTS",
    "DIAMONDS"
]

# Generates a deck of cards with numbers from 1 - 14 and suits in order spades, clubs, hearts, diamonds
for suit in Suit:
    for card in Cards:
        deck_of_cards.append((card, suit))

# Generate dealer and player cards
def deal_cards():
    num_decks = 1 # specifies the number of decks we are using
    mask = list(range(52*num_decks))  # Generate ints [0 .. 51] representing pack of cards
    rng = random.Random()    # Black box object that generates random numbers
    rng.shuffle(mask)       # Shuffle the pack

    dealer_cards = []
    for i in mask[:2]: # grab the top two cards for dealer's hand
        dealer_cards.append(deck_of_cards[i])
        mask.pop(0)
    print("Dealer has X & the {0} of {1}.".format(dealer_cards[1][0], dealer_cards[1][1]))

    player_cards = []
    for j in mask[:2]: # grab the next two cards for player's hand
        player_cards.append(deck_of_cards[j])
        mask.pop(0)

    ## ACE appears in the players hand - multiple possible sums
    if player_cards[0][0] == "ACE" and player_cards[1][0] == "ACE": # Both cards are ACES
        print("You have the {0} of {1} and the {0} of {2}.".
        format(player_cards[0][0], player_cards[0][1], player_cards[1][1]))
        validInput = False
        while not validInput:
            print("Your two possible sums are 2 and 12.", end= " ")
            answer = int(input("Please enter which you would like: "))
            if answer == 2:
                player_total = answer
                validInput = True
            elif answer == 12:
                player_total = answer
                validInput = True
            else:
                print("Please enter a valid input.")

    elif player_cards[0][0] == "ACE": # The first card is an ACE
        if check_total(Cards[player_cards[1][0]] + 11):
            player_total = 1 + Cards[player_cards[1][0]]
            print("You have {0} with the {1} of {2} and the {3} of {4}.".
        format(player_total, player_cards[0][0], player_cards[0][1], player_cards[1][0], player_cards[1][1]))
        else:
            print("You have the {0} of {1} and the {2} of {3}.".
            format(player_cards[0][0], player_cards[0][1], player_cards[1][0], player_cards[1][1]))

            validInput = False
            while not validInput:
                print("Your two possible sums are {0} and {1}.".
                format(Cards[player_cards[1][0]] + 1, Cards[player_cards[1][0]] + 11))
                answer = int(input("Please enter which one you would like: "))
                if answer == Cards[player_cards[1][0]] + 1:
                    player_total = Cards[player_cards[1][0]] + 1
                    validInput == True
                elif answer == Cards[player_cards[1][0]] + 11:
                    player_total = Cards[player_cards[1][0]] + 11
                    validInput = True
                else:
                    print("Please enter a valid input.")
    
    elif player_cards[1][0] == "ACE": # The second card is an ACE
        if check_total(Cards[player_cards[0][1]] + 11):
            player_total = 1 + Cards[player_cards[0][1]]
            print("You have {0} with the {1} of {2} and the {3} of {4}.".
        format(player_total, player_cards[0][0], player_cards[0][1], player_cards[1][0], player_cards[1][1]))

        else:
            print("You have the {0} of {1} and the {2} of {3}.".
            format(player_cards[0][0], player_cards[0][1], player_cards[1][0], player_cards[1][1]))

            validInput = False
            while not validInput:
                print("Your two possible sums are {0} and {1}.".
            format(Cards[player_cards[0][1]] + 1, Cards[player_cards[0][1]] + 11))
                answer = int(input("Please enter which one you would like: "))
                if answer == Cards[player_cards[0][1]] + 1:
                    player_total = Cards[player_cards[0][1]] + 1
                    validInput == True
                elif answer == Cards[player_cards[0][1]] + 11:
                    player_total = Cards[player_cards[0][1]] + 11
                    validInput = True
                else:
                    print("Please enter a valid input.")
            
    
    else: # Neither cards are ACES - majority of instances
        player_total = Cards[player_cards[0][0]] + Cards[player_cards[1][0]]
        print("You have {0} with the {1} of {2} and the {3} of {4}.".
        format(player_total, player_cards[0][0], player_cards[0][1], player_cards[1][0], player_cards[1][1]))

    return (mask, dealer_cards, player_cards, player_total)

# Dealer Action
def dealer_action(mask, dealer_cards, player_total):

    # Determines how to deal w dealer receiving an ACE
    if dealer_cards[0][0] == "ACE" and dealer_cards[1][0] == "ACE": # Both cards are ACES
        dealer_total = 12
    elif dealer_cards[0][0] == "ACE": # The first card is an ACE
        if check_total(Cards[player_cards[1][0]] + 11):
            dealer_total = 1 + Cards[dealer_cards[1][0]]
        else:
            dealer_total =  Cards[dealer_cards[1][0]] + 11 
    elif dealer_cards[1][0] == "ACE": # The second card is an ACE
        if check_total(Cards[dealer_cards[0][1]] + 11):
            dealer_cards = 1 + Cards[dealer_cards[0][1]]
            
        else:
            dealer_total = Cards[dealer_cards[0][1]] + 11

    else: ## gets the dealer_total
        dealer_total = Cards[dealer_cards[0][0]] + Cards[dealer_cards[1][0]]
    
    return dealer_total

# Player Action
def player_action(mask, player_cards, player_total):
    answer = ""
    while not check_total(player_total) and player_total != 21:
        validInput = False
        while not validInput:
            answer = input("Would you like to hit? (y/n) ")
            if answer == 'y':
                player_cards.append(deck_of_cards[mask[0]])
                # If dealer receives an ACE
                if deck_of_cards[mask[0]][0] == "ACE":
                    if check_total(player_total + 11):
                        player_total += 1
                    else:
                        player_total += 11
                else:
                    player_total += Cards[deck_of_cards[mask[0]][0]]
                mask.pop(0)
                validInput = True

                # Display player's cards
                for j in range(len(player_cards)):
                    if j == 0:
                        print("You now have {0} with the {1} of {2}".format(player_total, player_cards[j][0], player_cards[j][1]), end = "")
                    elif j == len(player_cards) - 1:
                        print(" and the {0} of {1}. ".format(player_cards[j][0], player_cards[j][1]))
                    else:
                        print(", the {0} of {1},".format(player_cards[j][0], player_cards[j][1]), end = "")
                
            elif answer == 'n':
                validInput = True
                return player_total
            else:
                print("Please enter a valid input.")

    return player_total

def check_total(total):
    if total > 21:
        return True
    return False

if __name__ == '__main__':
    play = True
    while play:
        mask, dealer_cards, player_cards, player_total = deal_cards()
        dealer_total = dealer_action(mask, dealer_cards, player_total)
        player_total = player_action(mask, player_cards, player_total)

        if check_total(player_total):
            print("You have busted. You lose :(.")
        else:
            # If the dealer has 16 or less it will draw another card
            while dealer_total < 17:
                dealer_cards.append(deck_of_cards[mask[0]])
                # If dealer receives an ACE
                if deck_of_cards[mask[0]][0] == "ACE":
                    if check_total(dealer_total + 11):
                        dealer_total += 1
                    else:
                        dealer_total += 11
                else:
                    dealer_total += Cards[deck_of_cards[mask[0]][0]]
                mask.pop(0)

            if player_total == 21 and dealer_total != 21:
                print("You have BLACKJACK! You win!") 
            elif check_total(dealer_total):
                print("Dealer has busted! You win!")

            else:
                # Display the dealer's cards
                for i in range(len(dealer_cards)):
                    if i == 0:
                        print("The dealer has {0} with the {1} of {2}".format(dealer_total, dealer_cards[i][0], dealer_cards[i][1]), end = "")
                    elif i == len(dealer_cards) - 1:
                        print(" and the {0} of {1}.".format(dealer_cards[i][0], dealer_cards[i][1]))
                    else:
                        print(", the {0} of {1},".format(dealer_cards[i][0], dealer_cards[i][1]), end = "")

                # Display player's cards
                for j in range(len(player_cards)):
                    if j == 0:
                        print("You have {0} with the {1} of {2}".format(player_total, player_cards[j][0], player_cards[j][1]), end = "")
                    elif j == len(player_cards) - 1:
                        print(" and the {0} of {1}.".format(player_cards[j][0], player_cards[j][1]))
                    else:
                        print(", the {0} of {1},".format(player_cards[j][0], player_cards[i][1]), end = "")

                # Check to see who has won
                if dealer_total > player_total:
                    print("You lose :(.")
                elif dealer_total == player_total:
                    print("You and the dealer have tied.")
                elif dealer_total == 21:
                    print("The Dealer has Blackjack. You lose :(.")
                elif player_total > dealer_total:
                    print("You win!")

        validInput = False
        while not validInput:
            answer = input("Would you like to play again? (y/n) ")
            if answer == 'n':
                print("Thank you for playing!")
                validInput = True
                play = False
            elif answer == 'y':
                print("Let's see if we can't get you that chicken dinner :)!")
                validInput = True
            else:
                print("Please enter a valid input.")

