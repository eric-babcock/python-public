# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 00:23:46 2023

@author: calic
"""

import random

options = ["rock", "paper", "scissors"]


def get_player_choice():
    player_choice = input("Enter a choice(rock, paper, scissors: ")
    return str(player_choice)

def check_input(user_input):
    if user_input == "rock" or user_input =="paper" or user_input =="scissors":
        return str(user_input)            
    else:     
        print("Try again!")
        return False

def check_loop():
    choice = str(get_player_choice())
    check = check_input(choice)
    if check == False:
        check_loop()
    else:
        return str(choice)


    
def get_choices():
    player_choice = str(check_loop())
    computer_choice = random.choice(options)
    choices = {"player": str(player_choice), "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:

        return "It's a tie"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! You Lose!"
        else:# computer =="paper":
            return"Scissors cut paper! You Win!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You Win!"
        else:# if computer =="paper":
            return"Paper wraps rock! You Lose!"
    elif player == "paper":
        if computer == "rock":
            return "Paper wraps rock! You Win!"
        else:# if computer =="scissors":
            return"Scissors cut paper! You Lose!"
            
           

def main():
    choices = get_choices()
    #check_win(choices["player"],choices["computer"])
    
    return(check_win(
        str(choices["player"]),
        choices["computer"])
    )


    
    
    
    
    
    
    