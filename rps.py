# All the imports required to make this thing work as nicely as it does.
from os import system as sys
from check_inputs import check_inputs
from time import time as unixtime
from datetime import datetime
from dateutil.relativedelta import *

class Player:
    def __init__(self, name, number):
        self.name = name
        self.matches_won = 0
        self.number = number

"""
The rules of Rock, Paper, Scissors are as follows:
Rock eliminates Scissors
Paper eliminates Rock
Scissors eliminates Paper
"""

player1 = Player(input("Player 1: Please enter a name: "), 1)
player2 = Player(input("Player 2: Please enter a name: "), 2)
started = unixtime()

def getInput(player):
    prefix = "{} (Player {})".format(player.name, player.number)
    inp = input("{}: Please input 'Rock', 'Paper' or 'Scissors': ".format(prefix)).lower()

    if inp not in ["rock", "paper", "scissors"]:
        print("{}: Try again.".format(prefix))
        getInput(player)
    
    return inp

while True:
    p1_inp = getInput(player1)
    sys("cls")
    p2_inp = getInput(player2)

    winner = check_inputs(player1, player2, p1_inp, p2_inp)

    if winner == "p1": player1.matches_won += 1
    elif winner == "p2": player2.matches_won += 1

    try_again = input("Do you want to try again or both player's statistics? Enter 'Yes' to try again, 'viewstats' to view your statistics and anything else to exit. ").lower()

    if try_again == "yes":
        print("Starting a new game!")
        continue
    elif try_again == "viewstats":
        date1 = datetime.fromtimestamp(started)
        date2 = datetime.fromtimestamp(unixtime())
        rd = relativedelta(date2, date1)
        print("-== STATISTICS ==-\nPlayer 1 ({}): Won {} games.\n\nPlayer 2 ({}): Won {} games.\n\nPlayed for: {} years, {} months, {} days, {} hours, {} minutes and {} seconds.".format(player1.name, player1.matches_won, player2.name, player2.matches_won, rd.years, rd.months, rd.days, rd.hours, rd.minutes, rd.seconds))
        new_try_again = input("Do you want to go back to playing now, or exit? Enter 'Yes' to try again, and anything else to exit. ").lower()
        if new_try_again == "yes":
            print("Starting a new game!")
            continue
        else:
            break
    else:
        break

print("Thank you for playing. Final statistics:\n\nPlayer 1 ({}): Won {} games.\n\nPlayer 2 ({}): Won {} games.\n\nPlayed for: {} years, {} months, {} days, {} hours, {} minutes and {} seconds".format(player1.name, player1.matches_won, player2.name, player2.matches_won, rd.years, rd.months, rd.days, rd.hours, rd.minutes, rd.seconds))