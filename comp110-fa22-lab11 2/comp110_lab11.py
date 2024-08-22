"""
Module: comp110_lab11

Lab 11: A flash card program.
"""
import random


def get_flash_cards(filename):
    """
    Creates a dictionary of flash card questions and answers.

    Parameters:
    filename (type: string) - The name of the file containing flash card Q's/A's

    Returns:
    (type: dictionary) - A dictionary that associates questions with answers.
    """

    card_file = open(filename, 'r')
    flash_cards = {}
    for line in card_file:
        line = line.strip()
        question, answer = line.split("|")
        flash_cards[question] = answer

    return flash_cards 


    
def quiz(cards,target_score):
    """Parameters:
    cards: This is a dictionary with the questions and answers for the flash cards. In other words, it’s a dictionary that would have been returned by the get_flash_cards function.
    target_score: An integer that will determine how many cards the user will be shown."""
    questions = list(cards.keys())
    score = 0 
    num_questions = 0 

    while score != target_score:
        num_questions+=1
        x = random.choice(questions)
        print(x)
        answer = input("Type in answer: ")
        if answer == cards[x]:
            print ("Correct!")
            score += 1
        else: 
            print ("Incorrect!")
    

    return (score/num_questions)*100





def main():
    print ("Welcome to flash cards")
    file = input("Enter the name of a file: ")
    cards = get_flash_cards(file)
    target = int(input("Enter target score: "))
    x = quiz(cards,target)
    print(x)
    

""" DO NOT MODIFY ANYTHING BELOW THIS LINE! """
if __name__ == "__main__":
    main()
