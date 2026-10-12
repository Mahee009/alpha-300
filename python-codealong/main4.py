

suits = ["spades", "hearts", "diamonds", "clubs"]
'''suit = suits[2]
rank = "k"
value = 10
print("your card is :" + rank + " of " + suit)
suits.append("snakes")
for suit in suits:
    print(suit)'''

import random 

class Card:
    def __init__(self, suit, rank): # constructor to create a new obj from the class self is used to point to the current obj instance
        self.suit = suit
        self.rank = rank

    def __str__(self): #  used to return a string representation of the object when we print the object
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [] # empty list to store all the cards
        suits = ["spades", "clubs", "hearts", "diamonds"] # all 4 suits in a deck
        ranks = [
                {"rank": "A", "value": 11}, # it is a list of dict where rank and valur is represented 
                {"rank": "2", "value": 2},
                {"rank": "3", "value": 3},
                {"rank": "4", "value": 4},
                {"rank": "5", "value": 5},
                {"rank": "6", "value": 6},
                {"rank": "7", "value": 7},
                {"rank": "8", "value": 8},
                {"rank": "9", "value": 9},
                {"rank": "10", "value": 10},
                {"rank": "J", "value": 10},
                {"rank": "Q", "value": 10},
                {"rank": "K", "value": 10},
            ]
        for suit in suits: # go through each suit
            for rank in ranks: # go through each rank
                self.cards.append(Card(suit, rank)) # add a new card obj to the list of cards deck

    def shuffle(self):
        if len(self.cards) > 1: #count number of cards and if if greater than 1 shuffle
            random.shuffle(self.cards) # random shuffle

    def deal(self, number=1):
        if len(self.cards) > 0: # check if there are cards left in the deck
            cards_delt = [] # empty list to store the cards we give out
            for x in range(number): # repeat this for the number of cards needed
                card = self.cards.pop() # remove last item # remove last item
                cards_delt.append(card) # append card to list of cards delt
            return cards_delt # return the cards we delt

class Hand:
    def __init__(self, dealer=False):
        self.cards = [] # stores the cards in the hand
        self.value = 0 # total value of the cards
        self.dealer = dealer # check fi hand belogs to dealer or player

    def add_card(self, card_list):
        self.cards.extend(card_list) # add a list to hand 

    def calculate_value(self):
        self.value = 0 # reset value 
        has_ace = False #if hand has ace chck if greatert than 21

        for card in self.cards: # go through all the cards in the hand
            card_value = int(card.rank["value"]) # get the value of the card
            self.value += card_value # add card value to total

        if has_ace and self.value > 21: # if ace is there and value is above 21
            self.value -= 10 # reduce ace value by 10

    def get_value(self):
        self.calculate_value() # calculate the total value
        return self.value # return the final value

    def is_blackjack(self):
        return self.get_value() == 21 # check if the hand value is 21

    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''') # print whose hand it is
        for index, card in enumerate(self.cards): # go through each card with its index
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack(): # hide dealers first card
                print("hidden") # show hidden instead of the card
            else:
                print(card) # print the card

        if not self.dealer: # only show value for the player
            print("Value:", self.get_value())
        print() 

class Game:
    def play(self):
        game_number = 0 
        games_to_play = 0 

        while games_to_play <= 0: # keep asking until valid
            try:
                games_to_play = int(input("How many games do you want to play?: ")) 
            except:
                print("You must enter a number.") 

        while game_number < games_to_play: # keep playing till all games are done
            game_number += 1 # increase game count by 1

            deck = Deck() 
            deck.shuffle() 

            player_hand = Hand() 
            dealer_hand = Hand(dealer=True) # create dealers hand

            for i in range(2): # both player and dealer get 2 cards
                player_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())

            print() # leave some space
            print("*" * 30) # print a line of stars
            print(f"Game {game_number} of {games_to_play}") # show current game number
            print("*" * 30) # print another line of stars
            player_hand.display() # display players cards
            dealer_hand.display() # display dealers cards

            if self.check_winner(player_hand, dealer_hand): # check if anyone already won
                continue # move to next game

            choice = "" # store players choice
            while choice not in ["s", "stand"] and player_hand.get_value() < 21: # keep asking till player stands or reaches 21
                choice = input("Please choose 'Hit' or 'Stand': ").lower() # take choice and convert to lowercase
                print()
                while choice not in ["h", "s", "hit", "stand"]: 
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S) ").lower() # ask again if invalid
                    print()
                if choice in ["hit", "h"]: # if player wants another card
                    player_hand.add_card(deck.deal()) # give player one more card
                    player_hand.display() 

            if self.check_winner(player_hand, dealer_hand):
                continue 

            player_hand_value = player_hand.get_value() # store players final value
            dealer_hand_value = dealer_hand.get_value() # store dealers current value

            while dealer_hand_value < 17: # dealer to keep taking cards till 17
                dealer_hand.add_card(deck.deal()) # give dealer another card
                dealer_hand_value = dealer_hand.get_value() # update dealers value

            dealer_hand.display(show_all_dealer_cards=True) 

            if self.check_winner(player_hand, dealer_hand): # check if anyone has won
                continue 

            print("Final Results") 
            print("Your hand:", player_hand_value)
            print("Dealer's hand:", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True) # compare both hands to decide 
            
        print("\nThanks for playing!") 

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over: # check for winner before comparing final scores
            if player_hand.get_value() > 21: # player value above 21 means bust
                print("You busted. Dealer wins! 😭")
                return True # game is over
            elif dealer_hand.get_value() > 21: # dealer value above 21 means bust
                print("Dealer busted. You win! 😄")
                return True # game is over
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack(): # both have blackjack
                print("Both players have blackjack! Tie! 🤨")
                return True
            elif player_hand.is_blackjack(): # check if player has blackjack
                print("You have blackjack! You win! 😄")
                return True
            elif dealer_hand.is_blackjack(): # check if dealer has blackjack
                print("Dealer has blackjack! Dealer wins! 😭")
                return True
        else: # compare scores when game is over
            if player_hand.get_value() > dealer_hand.get_value(): # player has higher value
                print("You win! 😄")
            elif player_hand.get_value() == dealer_hand.get_value(): # both have same value
                print("Tie! 🤨")
            else: # dealer has higher value
                print("Dealer wins! 😭")

            return True # game over

        return False # no winner yet so continues

g = Game() # create game obj
g.play() # start playing