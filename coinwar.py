# HW6: Coin War
# Connor Williams 2021

import sys
import random

# This program plays the game, Coin War. You can select your army
# manually, randomly, or by reading a text file from the command
# line. The program then returns a winner or a tie.

# For the purpose of this program, it will typically loop throughout
# a range of 5, assigned to initial_size.
initial_size = range(5)

# Player 1 and Player 2 are assigned empty lists for their
# respective armies.
player1_army = []
player2_army = []

# Heads and tails side of a coin are assigned characters and
# grouped into a list.
heads = 'H'
tails = 'T'
coin_side = [heads, tails]

# Player 1 and Player 2 are assigned empty lists for their
# respective prisoners (prisoners1 for Player 1 and
# prisoners2 for Player 2).
prisoners1 = []
prisoners2 = []

# Function defined for user to choose whether to select player
# armies randomly or "positionally" (manually or by reading a
# text file on the command line).
def army_selection():

    # For loop reads standard input line-by-line.
    # Code adapted from Video Lecture 11 - linecount.py and
    # from online resource, JournalDev:
    # https://www.journaldev.com/32137/read-stdin-python#1-using-sysstdin-to-read-from-standard-input
    for line in sys.stdin:

        # If the line being read is not blank.
        if line.rstrip() != "":

            # If user types 'random' or program reads 'random'
            # from first line of inputted text file,
            # random_select() function is called.
            if "random" == line.rstrip().lower():
                print("Random selected.\n")
                random_select()
                break

            # If user types 'position' or program reads 'position'
            # from first line of inputted text file,
            # position_select() function is called.
            elif "position" == line.rstrip().lower():
                print("Position selected.\n")
                position_select()
                break

        # Otherwise user needs to try inputting a choice again.
        else:
            print("Try again. Enter random or position.")

# Function defined for user to "positionally" choose each player's
# army (manually or by reading a text file on the command line).
def position_select():

    # Player 1 and Player 2 are assigned users input - or
    # the next two lines of a text file are inputted from
    # the command line - to their respective armies
    # (position1 for Player 1 and position2 for Player 2).
    position1 = input()
    position2 = input()

    # Both positions entered get a list length split at any spaces
    # assigned to these variables (army_size1 for Player 1
    # and army_size2 for Player 2). This is to check that the list
    # length is 1.
    army_size1 = len(position1.split(' '))
    army_size2 = len(position2.split(' '))

    # Game start message and players starting positions printed.
    print("------------------ Begin Battle ------------------\n")
    print(position1.upper())
    print(position2.upper())

    # For loop appends every nth index of Player 1's and Player 2's
    # respective inputted position to their respective armies.
    for n in initial_size:

        # If the positions entered are not blank.
        if position1 != "" and position2 != "":

            # If the lengths of the lists created from the positions
            # are also equal to 1.
            if army_size1 == 1 and army_size2 == 1:
                player1_army.append(position1[n].upper())
                player2_army.append(position2[n].upper())

        # Otherwise, the positions entered are blank
        # making the armies incorrectly positioned.
        else:
            break

# Function defined to randomly select armies for both
# Player 1 and Player 2.
def random_select():

    # For loop creates a random army for Player 1 and Player 2
    # of range(5) (initial_size).
    for n in initial_size:

        # coin_side list element randomly chosen and
        # appended to each players army.
        player1_army.append(random.choice(coin_side))
        player2_army.append(random.choice(coin_side))

    # Game start message and players starting positions printed.
    print("------------------ Begin Battle ------------------\n")
    print(''.join(player1_army))
    print(''.join(player2_army))

# Function defined to take 'army' as a parameter, plays out the
# Coin War game up until every possible comparative iteration
# has been made, and finalizes players army and prisoner lists.
def coinwar(army):

    # While loop true as long as army lists are not empty.
    while player1_army != [] and player2_army != []:

        # Alphabetical comparison. 'H' is checked by being
        # less than 'T' alphabetically. Alphabetically less than
        # means Player 1 wins the battle round.
        if player1_army[0] < player2_army[0]:

            # Player 1 first takes Player 2's 0th army list index
            # and adds it to the end of Player 1's army list, then
            # takes Player 1's 0th army list index and moves it to
            # the end of Player 1's army list.
            player1_army.append(player2_army.pop(0))
            player1_army.append(player1_army.pop(0))

            # As long as Player 2's prisoners list is not empty,
            # for loop iterates through the prisoners max possible
            # list length (initial_size) and appends each prisoner
            # to the end of Player 1's army list.
            for n in initial_size:
                if prisoners2 != []:
                    player1_army.append(prisoners2.pop(0))

            # As long as Player 1's prisoners list is not empty,
            # for loop iterates through the prisoners max possible
            # list length (initial_size) and appends each prisoner
            # to the end of Player 1's army list.
            for n in initial_size:
                if prisoners1 != []:
                    player1_army.append(prisoners1.pop(0))

        # Alphabetical comparison. 'H' is checked by being
        # less than 'T' alphabetically. Alphabetically less than
        # means Player 2 wins the battle round.
        elif player2_army[0] < player1_army[0]:

            # Player 2 first takes Player 1's 0th army list index
            # and adds it to the end of Player 2's army list, then
            # takes Player 2's 0th army list index and moves it to
            # the end of Player 2's army list.
            player2_army.append(player1_army.pop(0))
            player2_army.append(player2_army.pop(0))

            # As long as Player 1's prisoners list is not empty,
            # for loop iterates through the prisoners max possible
            # list length (initial_size) and appends each prisoner
            # to the end of Player 2's army list.
            for n in initial_size:
                if prisoners1 != []:
                    player2_army.append(prisoners1.pop(0))

            # As long as Player 2's prisoners list is not empty,
            # for loop iterates through the prisoners max possible
            # list length (initial_size) and appends each prisoner
            # to the end of Player 2's army list.
            for n in initial_size:
                if prisoners2 != []:
                    player2_army.append(prisoners2.pop(0))

        # Alphabetical comparison. Alphabetically equal
        # means the players tie during battle round.
        elif player1_army[0] == player2_army[0]:

            # If the length of either players army list is less
            # than 2, then only one army element can be popped and
            # appended to the prisoners list rather than two elements.
            if len(player1_army) < 2 or len(player2_army) < 2:

                # Player 1's 0th army index gets popped and
                # appended to prisoner1's list.
                prisoners1.append(player1_army.pop(0))

                # Player 2's 0th army index gets popped and
                # appended to prisoner2's list.
                prisoners2.append(player2_army.pop(0))
                break

            else:

                # For loop pops and appends from each players 0th army
                # list index to their respective prisoner lists, twice.
                for i in range(2):

                    # Player 1's 0th army index gets popped and
                    # appended to prisoner1's list.
                    prisoners1.append(player1_army.pop(0))

                    # Player 2's 0th army index gets popped and
                    # appended to prisoner2's list.
                    prisoners2.append(player2_army.pop(0))

        # Otherwise, assert False to check if their is any
        # improper code.
        else:
            assert False

# Function defined to take 'result' as a parameter and calculate
# which player has an army leftover or, if no army elements
# remain, which player has more coins with side 'heads' in
# prisoners list, determining the winner of Coin War.
def game_result(result):

    # Variables set to 0 for calculating how many 'heads' are
    # in each respective prisoner list.
    nheads_prisoners1 = 0
    nheads_prisoners2 = 0

    # For loop checks that a list is not empty and how many
    # 'heads' are in each list, adding the number to their
    # respective variable counters.
    for i in initial_size:
        if prisoners1 != [] and len(prisoners1) - 1 >= i:
            if prisoners1[i] == heads:
                nheads_prisoners1 = nheads_prisoners1 + 1
        if prisoners2 != [] and len(prisoners2) - 1 >= i:
            if prisoners2[i] == heads:
                nheads_prisoners2 = nheads_prisoners2 + 1

    # If only Player 1 has an army, then Player 1 wins.
    if player1_army != [] and player2_army == []:
        return 1

    # Else If only Player 2 has an army, then Player 2 wins.
    elif player2_army != [] and player1_army == []:
        return 2

    # Else If neither player has an army and Player 1 has
    # more 'heads' in their prisoners list, then
    # Player 1 wins.
    elif nheads_prisoners1 > nheads_prisoners2:
        return 1

    # Else If neither player has an army and Player 2 has
    # more 'heads' in their prisoners list, then
    # Player 2 wins.
    elif nheads_prisoners2 > nheads_prisoners1:
        return 2

    # Else If one or both armies are returned empty during a
    # manually entered game, the prisoners lists will also be
    # empty and the game will not operate correctly. This
    # prevents the program from calling it a tie.
    elif prisoners1 == [] and prisoners2 == []:
        return "Error: Teams not entered correctly. Game Over."

    # Otherwise it must be a tie.
    else:
        return 0

# Welcome message and prompt printed.
print("************** Welcome to Coin Wars **************\n")
print("How would you like to select each player's army?")
print("Random or Position?")

# game_result() function called with coinwar() function as its
# 'result' parameter called with army_selection() function as its
# 'army' parameter, all assigned to coinwar_game.
coinwar_game = game_result(coinwar(army_selection()))

# Print coinwar_game to see which result is returned.
# (Tie == 0, Player 1 wins == 1, Player 2 wins == 2)
print(coinwar_game)

# Exiting message printed.
print("\n****************** Exiting Game ******************")