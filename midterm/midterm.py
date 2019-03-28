# Name: Megan Tjandrasuwita
# CMS cluster login name: mtjandra
# Midterm exam for Fall 2018 (solution set).
#

import random, sys, time

# Part 1: Pitfalls.

# Problem 1.1: There should not be single quotes around the argument n. The 
# multi-line docstring should be in three single (or double) quotes, not just 
# one. There is a missing colon after "while True". "i % j = 0" should have a
# double equal sign instead of one, since "=" is an assignment operator. The 
# indentation level of the last three lines of the function is not consistent
# with that of the while loop.

# Problem 1.2: enumerate returns a tuple, so you cannot unpack it with just 
# "for n in ...". There is no variable named "hist", so "n in hist" will not 
# work. "==" should not be used to assign hist[n] to 1 as "=" is the
# assignment operator. In the second for loop, "hist" should be replaced with
# "hist.items()", which retrieves the key and corresponding value. There are
# curly braces in the print in the second for loop, but there is no format
# method acting on the string. 

# Problem 1.3: The name of the function, "pa", and the names of all the 
# variables are bad names since they are hard to understand. The function does
# not have a docstring. There are no spaces around operators such as in "tt=0",
# "xx+1", and "2*xxx-1". Within the for loop, the indentation level is not four 
# spaces. There is no comment space in "#4".  

# ---------------------------------------------------------------------- 
# Part 2: Simple functions.
# ---------------------------------------------------------------------- 

import random, sys

#
# Problem 2.1
#

def draw_tictactoe(n):
    '''
    Takes one argument: a positive integer. Returns a string that draws a
    tictactoe-like "board" onto the terminal.
    '''
    assert n > 0
    mid = '{0}{1}{0}{1}\n'.format(' ' * n, '|')
    split = '{0}{1}{0}{1}{0}\n'.format('-' * n, '+')
    return '\n{0}{1}{0}{1}{0}\n'.format(mid * n, split)

def test_draw_tictactoe():
    print(draw_tictactoe(1))
    print(draw_tictactoe(2))
    print(draw_tictactoe(3))
    print(draw_tictactoe(4))
    print(draw_tictactoe(5))

#
# Problem 2.2
#

def rps(player1, player2):
    '''
    Takes in two arguments that represent the choices of two players in a game 
    of rock/paper/scissors. Both arguments one-character strings that are 
    either 'R', 'P', or 'S', denoting rock, paper, and scissors respectively.
    Returns 0 if the two arguments are the same, 1 if the first is the winner,
    and 2 if the second is the winner.
    '''
    assert player1 in ['R', 'P', 'S']
    assert player2 in ['R', 'P', 'S']
    win = {'R': 'S', 'S': 'P', 'P': 'R'}
    if not (player1 == player2):
        if player2 == win[player1]:
            return 1
        return 2
    return 0

def rpslk(player1, player2):
    '''
    Takes in two arguments that represent the choices of two players in a game 
    of rock/paper/scissors/lizard/spock. Both arguments one-character strings
    that are either 'R', 'P', 'S', 'L', or 'K', denoting rock, paper, scissors,
    lizard, and spock respectively. Returns 0 if the two arguments are the same,
    1 if the first is the winner, and 2 if the second is the winner.
    '''
    assert player1 in ['R', 'P', 'S', 'L', 'K']
    assert player2 in ['R', 'P', 'S', 'L', 'K']
    win = {'S': ('P', 'L'), 'P': ('R', 'K'), 'R': ('L', 'S'), 'L': ('P', 'K'), 
           'K': ('S','R')}
    if not (player1 == player2):
        if player2 in win[player1]:
            return 1
        return 2
    return 0    

def rpslk2(player1, player2):
    '''
    Takes in two arguments that represent the choices of two players in a game 
    of rock/paper/scissors/lizard/spock. Returns the winner of the game. 
    
    We write possible choices as a string 'SRKPL'. This string maps to
    'PLSRK' in that every choice in 'SRKPL' is defeats the choice with
    the same index and the choice with the same index + 1 in 'PLSRK'. Because
    'PLSRK' is 'SRKPL' except shifted to the right by three indexes, you can
    test whether player1 defeats player2 by seeing if player2 is at either  
    player1's index + 3 or player1's index + 4.
    
    '''
    str = 'SRKPL'   #maps to'PLSRK'
    if player1 == player2:
        return 0
    if str.index(player2) == (str.index(player1) + 3) % 5 or \
       str.index(player2) == (str.index(player1) + 4) % 5:
        return 1
    return 2
    

#
# Problem 2.3
#

### Supplied to students.

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ['S', 'H', 'D', 'C']

def validate_hand(hand):
    '''
    Validate a Poker hand.  If the hand is invalid, an assertion violation occurs.
    '''

    assert type(hand) is list
    assert len(hand) == 5
    for card in hand:
        assert type(card) is tuple
        assert len(card) == 2
        assert card[0] in ranks
        assert card[1] in suits

def random_hand():
    '''
    Return a randomly-generated Poker hand.

    Cards are represented as (rank, suit) tuples.
    Ranks are 2-10, or 'J', 'Q', 'K', 'A'
    Suits are one of 'S', 'H', 'D', 'C'
    '''

    # This uses a "list comprehension", which we haven't seen yet.
    deck = [(r, s) for r in ranks for s in suits]
    random.shuffle(deck)
    hand = deck[:5]
    # This uses "lambda", which we haven't seen yet.
    hand.sort(key=lambda c: ranks.index(c[0]))
    validate_hand(hand)
    return hand

def test_random_hand():
    '''
    Create a random hand, print it, and print its Poker rank.
    '''
    hand = random_hand()
    print(hand, poker_rank(hand))

def find_hand(p_rank):
    '''
    Print the first random hand that has a particular poker rank.
    Argument:
      p_rank: a poker rank
    '''
    count = 0
    while True:
        count += 1
        hand = random_hand()
        pr = poker_rank(hand)
        if pr == p_rank:
            print()
            break
        else:
            print('.', end='')
            sys.stdout.flush()
    print(hand, pr, count)

### End supplied to students.

# Helper functions for 'poker_rank' function go here.

def poker_rank(hand):
    '''
    Takes a five-card Poker hand represented as a list of cards, where cards are
    represented as a tuple of the card rank, either an integer or a one- 
    character string, and the suit, which is a one-character string. Returns 
    the ranking of the poker hand.
    '''
    validate_hand(hand)
    h_ranks = {}
    h_suits = {}
    for r, s in hand:
        if not (r in h_ranks):
            h_ranks[r] = 1
        else:
            h_ranks[r] += 1
        if not (s in h_suits):
            h_suits[s] = 1
        else:
            h_suits[s] += 1
    flush = test_flush(h_ranks, h_suits)
    straight = test_straight(h_ranks, h_suits)
    if flush and straight:
        return 'SF'
    pairs = count_pairs(h_ranks, h_suits)
    if len(h_ranks) == 2:
        if not pairs == 1:
            return '4K'
        return 'FH'
    if flush:
        return 'FL'
    if straight:
        return 'ST'
    if test_three(h_ranks, h_suits):
        return '3K'
    if pairs == 2:
        return '2P'
    if pairs == 1:
        return '1P'
    return 'NP' 

def test_straight(h_ranks, h_suits):
    '''Takes in two histograms for a hand. The first is the histogram of the
    ranks, where the keys are ranks and the values are the count of the ranks.
    The second is the histogram of suits, where the keys are suits and the
    values are the count of the suits. Returns True if the hand
    is a straight; otherwise, False.'''  
    if len(h_ranks) == 5:
        ranks_int = []
        for rank in h_ranks.keys():
            ranks_int.append(ranks.index(rank)) #converts ranks to integers
        ranks_int.sort()
        #taking care of special case with Ace in the straight
        if ranks_int == [0, 1, 2, 3, 12]: 
            return True 
        #checking for straight normally
        counter = ranks_int[0]
        for j in ranks_int:
            if not (counter == j):
                return False
            counter += 1
        return True
    return False

def test_flush(h_ranks, h_suits):
    '''Takes in two histograms for a hand. The first is the histogram of the
    ranks, and the second is the histogram of suits. Returns True if the hand
    is a flush; otherwise, False.'''
    if len(h_suits) == 1:
        return True
    return False

def test_three(h_ranks, h_suits):
    '''Takes in two histograms for a hand. The first is the histogram of the
    ranks, and the second is the histogram of suits. Returns True if the hand
    is a three of a kind; otherwise, False.'''  
    for v in h_ranks.values():
        if v == 3:
            return True   
    return False

def count_pairs(h_ranks, h_suits):
    '''Takes in two histograms for a hand. The first is the histogram of the
    ranks, and the second is the histogram of suits. Returns the number of 
    pairs in the hand''' 
    count = 0
    for v in h_ranks.values():
        if v == 2:
            count += 1  
    return count    
        

# ---------------------------------------------------------------------- 
# Miniproject: Game of Life.
# ---------------------------------------------------------------------- 

def make_empty_board(nrows, ncols):
    '''
    Takes two arguments: the first is the number of rows and the second is the 
    number of columns. Both arguments must be positive. Returns an empty Life 
    board containing a list of lists containing only zeros.
    '''
    board = []
    for i in range(nrows):
        board.append([])
        for j in range(ncols):
            board[i].append(0)
    return board

def make_random_board(nrows, ncols, p):
    '''
    Takes three arguments: the first is the number of rows, the second is the 
    number of columns, and the third is the probability that any given cell is
    a 1. Returns a Life board where each cell is randomly 0 or 1 based on the
    given probability. 
    '''
    board = []
    for i in range(nrows):
        board.append([])
        for j in range(ncols):
            rand = random.random()
            if rand < p:
                board[i].append(1)
            else:
                board[i].append(0)
    return board    

def display_board(board):
    '''
    Takes one argument, a Life board. Returns a string that displays the Life
    board in a readable format when printed. Each sublist of the Life board is
    one row of the displayed board, 0s are represented as blank characters, 1s
    are represented as asterisks, and there is a box drawn around the board.
    '''
    display = '+' + '-' * len(board[0]) + '+\n'
    for i in board:
        display += '|'
        for j in i:
            if j == 0:
                display += ' '
            else:
                display += '*'
        display += '|\n'
    display += '+' + '-' * len(board[0]) + '+\n'
    return display

def board_sums(board):
    '''
    Takes one argument, a Life board. Returns a new list of lists containing the
    neighboring sums. Each location in the neighbor sums list of lists is the
    neighbor sum for the corresponding location in the original board.
    '''
    sums = []
    for x in range(len(board)):
        sums.append([])
        for y in range(len(board[x])): 
            sums[x].append(sum_neighbors(x, y, board))
    return sums

def sum_neighbors(x, y, board):
    '''
    Takes three arguments. The first two are the x and y-coordinates of the 
    location to find the neighboring sum for. The third argument is the Life
    board. Returns the neighboring sum of the corresponding location.
    ''' 
    sum = 0
    for a in range(x-1, x+2):
        for b in range(y-1, y+2):
            if a == len(board):
                a = 0
            if b == len(board[0]):
                b = 0
            sum += board[a][b]
    return sum - board[x][y]

def display_board_sums(board):
    '''
    Takes one argument, which is a Life board. Computes the neighbor sums and 
    returns a string that, when printed, gives a readable repersentation of the
    sums.
    '''
    sums = board_sums(board)
    display = '+' + '-' * len(sums[0]) + '+\n'
    for i in sums:
        display += '|'
        for j in i:
            display += str(j)
        display += '|\n'
    display += '+' + '-' * len(sums[0]) + '+\n'
    return display     

def board_update(board):
    '''
    Takes one argument, a Life board. Computes the next version of the board by
    using the neighbor sums and the original board values. Returns the next 
    version of the board.
    '''
    sums = board_sums(board)
    new_board = []
    for i in range(len(board)):
        new_board.append([])
        for j in range(len(board[i])):
            if board[i][j] == 0:
                if sums[i][j] == 3:
                    new_board[i].append(1)
                else:
                    new_board[i].append(0)
            else:
                if sums[i][j] == 2 or sums[i][j] == 3:
                    new_board[i].append(1)
                else:
                    new_board[i].append(0)
    return new_board       
    
def board_to_num(board):
    '''
    Takes a single argument, a Life board. Computes and returns an integer, 
    which is a compact representation of the board used to determine when
    to stop a Life simulation.
    '''
    num = 0
    counter = 0
    for i in board:
        for j in i:
            num += 2 ** (counter) * j
            counter += 1  
    return num

### Supplied to students:

def interact(nrows, ncols, p):
    '''
    Print the board and update it interactively until the user doesn't want
    to continue any more.  The user presses <return> to print the next
    generation to the terminal and enters "." to end the simulation.

    Arguments:
      nrows: number of rows (an integer > 0)
      ncols: number of columns (an integer > 0)
      p: a float in the range [0.0, 1.0]

    Return value: nothing
    '''

    answer = ''

    b = make_random_board(nrows, ncols, p)
    while True:
        print(display_board(b))
        answer = input()
        if answer == ".":
            break
        b = board_update(b)

def run_to_end(nrows, ncols, p, delay = 0.1):
    '''
    Print the board and update it non-interactively until the display repeats an
    earlier configuration, at which point the simulation stops.

    Arguments:
      nrows: number of rows (an integer > 0)
      ncols: number of columns (an integer > 0)
      p: a float in the range [0.0, 1.0]
      delay: time delay between printing of generations, in seconds

    Return value: nothing
    '''

    answer = ''
    seen = {}

    b = make_random_board(nrows, ncols, p)
    while True:
        print(display_board(b))
        time.sleep(delay)
        b = board_update(b)
        n = board_to_num(b)
        if n in seen:
            break
        seen[n] = 1

### End supplied to students.

