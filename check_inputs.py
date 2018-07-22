"""
MIT License

Copyright (c) 2018 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
