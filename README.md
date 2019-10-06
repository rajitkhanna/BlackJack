# BlackJack
Console-based BlackJack Card Game in Python. Oodles of Fun.

Run the file in your console with the command

python3 BlackJack.py

to experience this classic card game!

I stored the cards and card values in a dictionary called Cards. I stored the suits in a list called suits. In the beginning, I generate a generic deck of cards of thirteen values and four suits. I shuffle a list called mask in my function deal_cards to create a unique deck each time the code is run. To shuffle this list, I instantiate an object from python's random library because it's easy and convenient to. use. 

The edge case that was most problematic to account for was the fact that aces have the value of 1 and 11. I added several if-families to deal with this case.

The functions dealer_action and player_action drive the gameplay. dealer_action determines the dealer's score, and player_action allows the player to hit - build up their point total - to reach 21. 

I hope you enjoy playing!

