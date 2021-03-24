# coinwar

Connor Williams 2021

This program runs the game Coin War (two-player game inspired by the card game War), which plays two armies against each other until one is left standing or both tie. Armies are defined by a list of five coins flipped to either side heads or tails. Each army starts with an empty prisoners list. Heads beats tails and winner takes opponents coin, then adds it to their army list. Ties (heads vs. heads or tails vs. tails) takes players' coins and adds them into the each respective prisoners list. Armies can be created randomly, manually, or by reading text files from the command line (test game text files included). The program returns a winner or a tie (0 - tie, 1 - player 1, 2 - player 2).

This was created as a homework assignment for my CS 161 - Introduction to Programs and Problem Solving class at Portland State University.
