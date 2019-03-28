# Name: Megan Tjandrasuwita
# CMS cluster login name: mtjandra

'''
The CS 1 final exam, Fall 2018, part 2.

The Dissembler puzzle game.
'''

from utils import *
import locset as ls

# ---------------------------------------------------------------------- 
# Functions on board representations.
# ---------------------------------------------------------------------- 

def invert_rep(rep):
    '''
    Invert the board representation which maps locations to colors.
    The inverted representation will map colors to sets of locations.

    Arguments:
      rep -- a dictionary mapping locations to one-character strings
             representing colors

    Return value:
      a dictionary mapping one-character strings (representing colors)
      to sets of locations

    The input dictionary 'rep' is not altered.
    '''

    assert is_rep(rep)
    colors = list(rep.values())
    locations = list(rep.keys())
    loc = []
    unique = []
    for i in range(len(colors)):
        if colors[i] in unique:
            index = unique.index(colors[i])
            loc[index].add(locations[i])
        else:
            unique.append(colors[i])
            loc.append({locations[i]})
    inv = {}
    for i in range(len(unique)):
        inv[unique[i]] = loc[i]
    return inv   

def revert_rep(inverted):
    '''
    Invert the board representation which maps colors to sets of 
    locations.  The new representation will map locations to colors.

    Arguments:
      inverted -- a dictionary mapping one-character strings 
                  (representing colors) to sets of locations

    Return value:
      a dictionary mapping locations to one-character strings
      representing colors

    The input dictionary 'inverted' is not altered.
    '''

    assert is_inverted_rep(inverted)

    locations = list(inverted.values())
    colors = list(inverted.keys())
    rev = {}
    for i in range(len(locations)):
        loc_set = locations[i].copy()
        while len(loc_set) > 0:
            rev[loc_set.pop()] = colors[i]
    return rev

def swap_locations(rep, loc1, loc2):
    '''
    Exchange the contents of two locations.

    Arguments:
      rep -- a dictionary mapping locations to one-character strings
             representing colors
      loc1, loc2 -- adjacent locations which are in the board rep

    Return value:
      a new dictionary with the same structure of 'rep' with the
      specified locations having each others' contents

    The input dictionary 'rep' is not altered.
    '''

    assert is_rep(rep)
    assert is_loc(loc1)
    assert is_loc(loc2)
    assert ls.is_adjacent(loc1, loc2)
    assert loc1 in rep
    assert loc2 in rep
    
    new_rep = rep.copy()
    color1 = new_rep[loc1]
    new_rep[loc1] = new_rep[loc2]
    new_rep[loc2] = color1
    return new_rep

def remove_connected_groups(rep):
    '''
    Remove all connected color groups covering at least three squares
    from a board representation.

    Arguments: 
      rep -- a dictionary mapping locations to one-character strings
             representing colors

    Return value:
      a tuple of two dictionaries of the same kind as the input
      (i.e. a mapping between locations and color strings);
      the first contains the remaining locations only, 
      and the second contains the removed locations only 

    The input dictionary 'rep' is not altered.
    '''

    assert is_rep(rep)

    inv = invert_rep(rep)
    colors = list(inv.keys())
    keep = {}
    discard = {}
    for i in colors:
        locset = inv[i]
        short, connected = ls.filter_locset(locset)
        discard[i] = connected
        keep[i] = short
    return (revert_rep(keep), revert_rep(discard)) 
    
def adjacent_moves(nrows, ncols):
    '''
    Create and return a set of all moves on a board with 'nrows' rows and
    'ncols' columns.  The moves consist of two adjacent (row, column)
    locations.

    Arguments:
      nrows -- the number of rows on the board
      ncols -- the number of columns on the board

    Return value:
      the set of moves, where each move is a pair of adjacent locations
      and each location is a (row, column) pair; also the two locations
      are ordered in the tuple (the "smallest" comes first)

    Note that the moves are independent of the contents of any board
    representation; we aren't considering whether the moves would actually 
    change anything on a board or whether the locations of each move are 
    occupied by color squares.
    '''

    assert type(nrows) is int and type(ncols) is int
    assert nrows > 0 and ncols > 0
    
    moves = set()
    for i in range(nrows):
        for j in range(ncols):
            current = (i, j)
            top = (i - 1, j)
            bottom = (i + 1, j)
            left = (i, j - 1)
            right = (i, j + 1)
            if i - 1 >= 0:
                if (top, current) not in moves:
                    moves.add((current, top))
            if i + 1 < nrows:
                if (bottom, current) not in moves:
                    moves.add((current, bottom))
            if j - 1 >= 0:
                if (left, current) not in moves:
                    moves.add((current, left))
            if j + 1 < ncols:
                if (right, current) not in moves:
                    moves.add((current, right)) 
    return moves
            

def possible_moves(rep, nrows, ncols):
    '''
    Compute and return a set of all the possible moves.  A "possible move"
    is a move where:
    -- both locations of the move are adjacent
    -- both locations on the board rep are occupied by colors 
    -- making the move will cause some locations to be vacated

    Arguments: 
      rep -- a dictionary mapping locations to one-character strings
             representing colors
      nrows -- the number of rows on the board
      ncols -- the number of columns on the board

    Return value: 
      the set of possible moves

    The input dictionary 'rep' is not altered.
    '''

    assert is_rep(rep)
    assert type(nrows) is int and type(ncols) is int
    assert nrows > 0 and ncols > 0

    adj = adjacent_moves(nrows, ncols)
    possible = set()
    for i in adj:
        if i[0] in rep and i[1] in rep:
            new_rep = swap_locations(rep, i[0], i[1])
            kept, discarded = remove_connected_groups(new_rep)
            if len(discarded) >= 3:
                possible.add(i)
    return possible

