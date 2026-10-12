import random #import is used to import librararies
#list is used to store mutiple string, variables 



def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissor)") #variable create 
    options = ["rock", "paper", "scissor"] 
    computer_choice = random.choice(options) #random.choice is used to select a random value from a list
    #function is a only code when only runs when called
    choices = {"player": player_choice, "computer": computer_choice} #create a tuple with no values and store ina variable called choices
    return choices


###def greeting():
    return "hi"
# hi is being retured through a variable called response
###response = greeting() # greting fucntion is beeing called and the return value is being storred in a variable callled repsonse 
###print(response) #prints in the console ###

#choices = get_choices() #calling the fucntiona nd storing the return value ina variable called choices 
#print(choices)

def check_win(player, computer): #function is being created with 2 peices of data
    print("You chose " + player + ", computer chose " + computer)
    if player == computer:
        return "Its a tie"
    elif player == "rock":
        if computer == "scissors":
            return "you win"
        else:
            return "you lose"
    elif player == "paper":
        if computer == "rock":
            return "you win"
        else:
            return "you lose"
    elif player == "scissors":
        if computer == "paper":
            return "you win"
        else:
            return "you lose"

#check_win("rock", "scissors") #calling the function and passing 2 values to it
choices = get_choices() #calling a variable and storing the return value in a avriable get_choices
result = check_win(choices["player"], choices["computer"]) 
print(result)