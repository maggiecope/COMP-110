"""
Module: game_of_sticks

Implementation of the Game of Sticks, including an AI that learns the game,
either by playing against a human, or by pre-training against another AI.

Authors:
1) Ella Fahrendorf - efahrendorf@sandiego.edu
2) Maggie Cope - mcope@sandiego.edu
"""

import random


def get_player_selection(player_number, sticks_left):
    """
    Instructs the user to pick how many sticks to take in a given range. Returns the valid number of sticks.
    Parameter: 
    player_number- either 1 or 2
    sticks_left- the number of sticks remaining on the board

    Returns:
    number- integer
    """
    #sets valif orginally to false
    valid = False 
    while valid == False:
        if sticks_left >= 3:
    #uses input to get the players selection of how many sticks they take 
            number = int(input("Player " + str(player_number) + ": How many sticks do you take (1-3)? "))
    #validates the users input and continously asks the user to enter a valid input until valid = True 
            while number!=1 and number!=2 and number!=3:
                print ("Please enter a number between 1 and 3")
                number = int(input("Player " + str(player_number) + ": How many sticks do you take (1-3)? "))
            #when the user enters a valid number, valid is set to true 
            valid = True 
    
        elif sticks_left ==2:
            number = int(input("Player " + str(player_number) + ": How many sticks do you take (1-2)? "))
            while number!=1 and number!=2:
                print ("Please enter a number between 1 and 2")
                number = int(input("Player " + str(player_number) + ": How many sticks do you take (1-2)? ")) 
            valid  = True 
        else: 
            number = int(input("Player " + str(player_number) + ": How many sticks do you take (1-1)? "))
            while number!=1:
                print ("Please enter a number between 1 and 1")
                number = int(input("Player " + str(player_number) + ": How many sticks do you take (1-1)? "))
            valid  = True 
        #Returns the valid number(int)
        return (number)
    

def player_vs_player(num_sticks):
    """
    This function will alternate between player 1 and player 2, print out how many sticks are left on the board, and ask the player to make a selection>
    The game will run until there are not any sticks left. It will print out a message saying which player won.
   
    Paramter:
    num_sticks- number of sticks to start with (int)

    """
    #sets the first turn to player 1 
    player = 1 
    #checks to see if there are sticks still left on the board 
    while num_sticks >0:
        if num_sticks > 1:
            print("")
            print("There are " + str(num_sticks) + " on the board.")
            num_sticks = num_sticks - int(get_player_selection(int(player), num_sticks))
            if player == 1:
                player = 2
            else: 
                player = 1
        #player selection when there is only one stick left
        elif num_sticks == 1:
            print("There is 1 stick on the board.")
            num_sticks = num_sticks - int(get_player_selection(int(player), num_sticks))
            #if it is player 1s turn when their is only 1 stick left, player 1 loses
            if player == 1:
                print("Player 1, you lose.")
            #likewise, if it is player 2's turn and there is only 1 stick left, player 2 loses
            else: 
                print("Player 2, you lose.")
            #removes the last stick from num_sticks and now num_sticks is 0 and the while loop ends 
            num_sticks = num_sticks - 1

       


def initialize_hats(num_sticks):
    """
    Creates a hat list with only the valid number of sticks. 
    Parameter: num_sticks- int
    Return: hats- dictionary that associates the hat number with the hat contents

    """
    #create empty dictionary called hats 
    hats = {}

    
    for stick in range(1,num_sticks+1):
        #adds the hat number and its associated hat conects to the hats dictionary 
        if stick == 1:
            hats[stick] = [1]
        elif stick == 2:
            hats[stick] = [1,2]
        else:
            hats[stick] = [1,2,3]
    #returns the hat dictionary 
    return hats

def update_hats(hats, besides, ai_won):
    """
    This function adds the besides value to the hat if the AI wins. 
    If the AI loses, it removes the besides value from the hat, unless there is only one. 
    Parameters: 
    hats- dictionary
    besdies- dictionary
    ai_won- Boolean value
    
    """
    #If the AI won, adds two balls to all hats that have a ball beside them. 
    if ai_won == True:
        for balls in besides:
            hats[balls].append(besides[balls])
            hats[balls].append(besides[balls])
    #If the AI lost, adds a ball to a hat to avoid having no balls with one of the numbers in a hat.
    else:
        for balls in besides:
            if besides[balls] not in hats[balls]:
                hats[balls].append(besides[balls])

        
def get_ai_selection(sticks_left, hats, besides):
    """
    Prompts the AI to choose a random value from hats, then returns the choice after removing it from the hat.
    Parameter:
    sticks_left- the number of sticks left (int)
    hats- dictionary 
    besides- dictionary

    Return:
    choice- the number that was randomly picked (int)

    """
    #randomly pick and remove a ball (choice) from the hat associated with the number of sticks remaining. 
    choice = random.choice(hats[sticks_left]) 
    hats[sticks_left].remove(choice)
    #add the removed ball to the besides dictionary 
    # to save which ball was chosen with the given number of sticks remaining. 
    besides[sticks_left]= choice
    #returns the number that was randomly picked.(choice)
    return choice

def player_vs_ai(initial_num_sticks, training_rounds):
    """
    Checks if the AI needs to be trained, if it does, then trains the AI. Then the AI is run against
    the player, and learns from each game.
    Parameter:
    initial_num_sticks

    """
    #sets player equal to 1, which means its the humans turn, when player is 2 it is the AI's turn
    player = 1 

    playing = 1 

    #pretains ai - if its player v Ai training rounds = 0, if its trained computer training rounds = 1000
    hats = pretrain_ai(initial_num_sticks, training_rounds)
    #write_hat_contents specifying the file name after intializing the number of hats 
    write_hat_contents(hats, "hat-contents.txt")

    #determines if the user wants to play/ keep playing 
    while playing == 1: 
        besides = {}
        num_sticks = initial_num_sticks

        while num_sticks > 0:
            #if there are more than 1 sticks on the board
            if num_sticks > 1:
                print("")
                print("There are " + str(num_sticks) + " sticks on the board.")
                #if its the players turn, gets the players stick selection and subtracts from num_sticks
                #switches the turn to AI 
                if player == 1:
                    num_sticks = num_sticks - int(get_player_selection(int(player), num_sticks))
                    player = 2
                #if its the AI's turn, gets and prints the AI stick selection and subtracts from num_sticks
                else:
                    ai_selection = int(get_ai_selection(num_sticks, hats, besides))
                    num_sticks = num_sticks - ai_selection
                    print ("AI selects " + str(ai_selection))
                    player = 1
            #when there is only 1 stick left on the board prints that and takes the player or AI's selection and switches turns 
            else:
                print("There is 1 stick on the board.")
                if player == 1: 
                    num_sticks = num_sticks - int(get_player_selection(int(player), num_sticks))
                    player = 2

                else: 
                    ai_selection = (get_ai_selection(num_sticks, hats, besides))
                    num_sticks = num_sticks - ai_selection
                    player = 1
        #determines who won the game based on whose turn it was (player or AI)            
        if player == 1:
            print("AI loses.")
            win = False
        else:
            print("You lose.")
            win = True

        #updates hats after each round 
        update_hats(hats, besides, win)
       
        #asks the user if they want to play again after each round if the user inputs 1 a new round will begin 
        # if the user inputs 0 the game will end 
        playing = int(input("Play again (1 = yes, 0 = no)? "))
       #makes sure the user enters 1 or 0 
        while playing != 1 and playing !=0:
            playing = int(input("Please enter 1 or 0"))



def pretrain_ai(initial_num_sticks, num_rounds):
    """
    This function runs 2 AI against each other for a given number of rounds, and after all the rounds, returns player two's hats.
    Parameters:
    initial_num_sticks- integer
    num_rounds- integer

    Returns:
    hats_2 - dictionary
    """
    ai = 1
    #creates two separate dictionaries for the two AI 
    hats_1 = initialize_hats(initial_num_sticks)
    hats_2 = initialize_hats(initial_num_sticks)

    #loops through the number of times specified in the parameter num_rounds 
    for rounds in range(num_rounds):
        #creates to seperate besides dictionaries for the two AI 
        besides_1 = {}
        besides_2 = {}
 
        num_sticks = initial_num_sticks

        #while there are sticks on the board
        while num_sticks > 0:
    
            if ai == 1:
                num_sticks = num_sticks - int(get_ai_selection(num_sticks, hats_1, besides_1))
                ai = 2
            else:
                num_sticks = num_sticks - int(get_ai_selection(num_sticks, hats_2, besides_2))
                ai = 1
        #when there are no sticks left on the board the AI whose turn it was loses
        if ai == 1: 
            update_hats(hats_1, besides_1, True)
            update_hats(hats_2, besides_2, False)
        else:
            update_hats(hats_1, besides_1, False)
            update_hats(hats_2, besides_2, True)

    #returns the contents dictionary for the 2nd AI 
    return hats_2
                

def write_hat_contents(hats, filename):
    """
    write a summary of how many of each of each ball number there are
    Parameter:
    hats- dictionary
    filename- file
    """
    #opens the file in the write method 
    f = open(filename,'w')
    f.write("Hat Number: (1's, 2's, 3's)" + "\n")
    for i in hats:
        #uses the count method to get the number of time an item occurs in a list and prints the contents of all the hats 
        f.write(str(i) + ": " + str((hats[i].count(1), hats[i].count(2), hats[i].count(3))) + "\n")
    #closes file when done 
    f.close()
    
def main():
    """
    welcomes the user to the game, prompts the user to chose how many sticks to start with and then to chose the game mode
    """
    
    print("Welcome to the Game of Sticks!")
   #prompts user to input how many sticks they want to start on the table
    num_sticks = int(input("How many sticks are there on the table initially (10-100)? "))
    #makes sure the user entered a number between 10 and 100 for the number of sticks on the table 
    while num_sticks<10 or num_sticks>100:
        print("Please enter a number between 10 and 100")
        num_sticks = int(input("How many sticks are there on the table initially (10-100)? "))
    
    print ("Options:")
    print(" Play against a friend (1)")
    print(" Play against the computer (2)")
    print(" Play against the trained computer (3)")
    #prompts the user to chose a game mode 
    game_mode = int(input("Which option do you take (1-3)? "))
    #makes sure the user entered a valid option for the game mode 
    while game_mode!=1 and game_mode!=2 and game_mode!=3:
        game_mode = int(input("Which option do you take (1-3)? "))
    
    if game_mode == 1:
        player_vs_player(num_sticks)
    elif game_mode == 2:
        player_vs_ai(num_sticks, 0)
    else:
        print("Training AI, please wait...")
        player_vs_ai(num_sticks, 1000)

if __name__ == "__main__":
    main()

