def check_inputs(player1, player2, p1_inp, p2_inp):
    if p1_inp == "rock":
        if p2_inp == "paper":
            print("{} (Player 2): You won.".format(player2.name))
            return "p2"
        elif p2_inp == p1_inp:
            print("{} (Player 1) and {} (Player 2): You tied.".format(player1.name, player2.name))
        else:
            print("{} (Player 1): You won.".format(player1.name))
            return "p1"

    elif p1_inp == "paper":
        if p2_inp == "scissors":
            print("{} (Player 2): You won.".format(player2.name))
            return "p2"
        elif p2_inp == p1_inp:
            print("{} (Player 1) and {} (Player 2): You tied.".format(player1.name, player2.name))
        else:
            print("{} (Player 1): You won.".format(player1.name))
            return "p1"

    elif p1_inp == "scissors":
        if p2_inp == "rock":
            print("{} (Player 2): You won.".format(player2.name))
            return "p2"
        elif p2_inp == p1_inp:
            print("{} (Player 1) and {} (Player 2): You tied.".format(player1.name, player2.name))
        else:
            print("{} (Player 1): You won.".format(player1.name))
            return "p1"
