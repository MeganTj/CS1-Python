# Name: Megan Tjandrasuwita
# CMS cluster login name: mtjandra

'''
Solves a Dissembler puzzle given a puzzle in the form of a one-line string.

'''

import string
import random
from utils import *

# ---------------------------------------------------------------------- 
# Global data.
# ---------------------------------------------------------------------- 

# A list of dissembler puzzles.
# Each puzzle is represented as a single string.
# Blank squares are indicated by '.' and colored squares
# are indicated by a single lowercase letter.
# The letters have no meaning (they aren't short for a specific color).
# The blanks in the string are used to separate different rows of the
# puzzle.

puzzles = [
  'aababb',
  'aa. b.. abb',
  'a.. aba bab ..b',
  'abba a..b b..a abba',
  '.aa. ..b. baab .b.. .aa.',

  'a...a babab a...a',
  '....a ababa b.... a.aba b.a.b a...a babab',
  'aabb .ba. .ac. .cd. ddcd',
  'ababc d...b ad.ec .f.c. fd.eg f...e hhghg',
  'aabaa bbcbb ccdcc ddedd eeaee',

  '.aabb. .c..c. ca..bc d....d cdccdc .cddc.',
  '..aab .ccda .b.cb db.db da.d. cbaa. dcc..',
  'abbcbc adaddc dccbcb dadaab',
  'ababb b.b.a a.a.a a.b.b bbaba',
  '.ab. .ba. .ab. abab a..b',

  # Harder puzzles:

  '...a... ..bac.. .bdbad. cca.dee .afbeb. ..afb.. ...f...',
  'aaaaab cbdcdb cbeadb cabfeb cafefb cddddd',
  'abcdded adb.ecd abcccad afggged agf.bad afbbgad',
  'abcacc daedfe dbgfef ccbhhi gjcijh gfjffi',
  'aabcbcb c.a.d.b cbcdcaa d.a.a.b adcabda d.b.d.b acadcdd'
]

# ---------------------------------------------------------------------- 
# Helper functions.
# ---------------------------------------------------------------------- 

def is_adjacent(loc1, loc2):
    '''
    Arguments:
      loc1, loc2 -- (row, column) locations

    Return value: 
      True if two locations are orthogonally adjacent, otherwise False.
    '''

    assert is_loc(loc1)
    assert is_loc(loc2)
    
    x_adj = abs(loc1[0] - loc2[0]) == 1 
    y_adj = abs(loc1[1] - loc2[1]) == 1
    if (abs(loc1[0] - loc2[0]) == 1 and loc1[1] == loc2[1]) or \
       (abs(loc1[1] - loc2[1]) == 1 and loc1[0] == loc2[0]):
        return True
    return False

def adjacent_to_any(loc, locset):
    '''
    Arguments:
      loc -- a (row, column) location
      locset -- a set of locations

    Return value:
      True if `loc` is not in `locset` and at least one location 
      in `locset` is adjacent to `loc`, otherwise False.

    The set `locset` is not altered.
    '''

    assert is_loc(loc)
    assert is_locset(locset)
    
    if loc not in locset:
        for loc2 in locset:
            if is_adjacent(loc, loc2):
                return True
    return False

def collect_adjacent(locset, target_set):
    '''
    Arguments:
      locset -- a set of (row, column) locations
      target_set -- another set of (row, column) locations

    Return value: 
      A set of all the locations in `locset` that are adjacent 
      to any location in `target_set`.

    The sets `locset` and `target_set` are not altered.
    '''

    assert is_locset(locset)
    assert is_locset(target_set)

    adj = set()
    for loc in locset:
        if adjacent_to_any(loc, target_set):
            adj.add(loc)
    return adj

def collect_connected(loc, locset):
    '''
    Arguments:
      loc -- a (row, column) location
      locset -- a set of locations

    Return value: 
      A set of all the locations in `locset` which are connected to `loc` 
      via a chain of adjacent locations. Include `loc` in the resulting set.

    The set `locset` is not altered.
    '''

    assert is_loc(loc)
    assert is_locset(locset)

    connected = set([loc])
    orig = locset.copy()
    adj = collect_adjacent(orig, connected)
    adj.add(loc)
    while len(adj.difference(connected)) > 0:
        connected = connected.union(adj)
        for i in adj:
            if i in orig:
                orig.remove(i)
        adj = adj.union(collect_adjacent(orig, connected))
    return connected

def partition_connected(locset):
    '''
    Partition a set of locations based on being connected via a chain of
    adjacent locations.  The original locset is not altered.
    Return a list of subsets.  The subsets must all be disjoint i.e.
    the intersection of any two subsets must be the empty set.

    Arguments:
      locset -- a set of (row, column) locations

    Return value: 
      The list of partitioned subsets.

    The set `locset` is not altered.
    '''

    assert is_locset(locset)
    orig = locset.copy()
    lst = []
    lst2 = []
    while len(orig) > 0:
        lst.append(orig.pop())
    while len(lst) > 0:
        adj = collect_connected(lst[0], locset)
        lst2.append(adj)
        for x in adj:
            lst.remove(x)
    return lst2

def filter_locset(locset):
    '''
    Given a locset, partition it into subsets which are connected via a
    chain of adjacent locations.  Compute two sets:
      -- the union of all partitions whose length is < 3 
      -- the union of all partitions whose length is >= 3 
    and return them as a tuple of two sets (in that order).  

    Arguments:
      locset -- a set of (row, column) locations

    Return value:
      The two sets as described above.

    The set `locset` is not altered.
    '''

    assert is_locset(locset)

    lst = partition_connected(locset)
    all_less = set()
    all_three = set()
    for i in lst:
        if len(i) >= 3:
            all_three.update(i)
        else:
            all_less.update(i)
    return (all_less, all_three)

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
    
    Precondition: loc1 and loc2 are adjacent locations.

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
        short, connected = filter_locset(locset)
        discard[i] = connected
        keep[i] = short
    return (revert_rep(keep), revert_rep(discard))   

class DissemblerSolver:
    
    def __init__(self, puzzle):
        self.nrows = 0
        self.ncols = 0   
        self.puzzle = puzzle
        self.rep = {}
        self.load(self.puzzle)      
        #a list that stores all the possible moves of a subtree as lists
        self.possible = [self.possible_moves()]
        #self.rand = 0
        self.parent = []
        self.moves = []
        self.history = []
        self.level = 0
        self.count = []
        
    
    def solve_puzzle(self):
        '''Depth-first traversal. Check subtrees of possible moves from left
        to right. If there are no possible moves, undo a move. When making a
        move, save all the possible moves at the current step.
        
        Returns True if the puzzle is solvable; otherwise False.'''          
        
        while self.level >= 0:         
            if len(self.rep) == 0:
                return True
            possible = self.possible[self.level]
            if len(possible) == 0:
                self.possible.pop()
                self.undo()
            else:
                rand = random.randint(0, len(possible) -1)
                move = possible[rand]
                self.make_move(move)
        return False
        
        
    def make_move(self, move):
        '''Takes in one argument, a move. Makes the given move, assuming that
        it is valid. Saves the board before the move is made and saves the move
        itself. Also saves the new set of possible moves and updates the level
        of the subtree.'''
        self.history.append(self.rep.copy())
        self.rep = swap_locations(self.rep, move[0], move[1])
        (self.rep, removed) = remove_connected_groups(self.rep) 
        self.moves.append(move)
        self.possible.append(self.possible_moves())
        self.level += 1
        
    def undo(self):
        '''Undos the previous move and returns the board to its previous state.
        Deletes the move that was undone from the list of possible moves and
        updates the level of the subtree.'''
        if self.history != []:
            self.rep = self.history.pop()  
            move = self.moves.pop()                
            self.possible[self.level - 1].remove(move)
        self.level -= 1    
    
    def give_solution(self):
        '''Prints out the solution as a list of moves. If the puzzle is 
        unsolvable, prints out that there is no solution.'''
        if self.solve_puzzle():
            for i in self.moves:
                print('({0}, {1})'.format(i[0], i[1]), end = ' ')
        else:
            print('No solution :(') 
        
    def load(self, puzzle):
        '''
        Load a puzzle from a string representation of the puzzle.
        Convert the string representation into a dictionary representation
        mapping (row, column) coordinates to colors.

        Arguments:
          puzzle -- a string representing the puzzle

        Return value: none
        '''

        rep = {}
        lines = puzzle.split()
        self.nrows = len(lines)
        self.ncols = len(lines[0])

        for row in lines:
            assert len(row) == self.ncols

        for row in range(self.nrows):
            for col in range(self.ncols):
                color = lines[row][col]
                if color == '.':
                    continue
                rep[(row, col)] = color
        self.rep = rep
        
    def possible_moves(self):
        '''
        Compute and return all the possible moves as a list.  A "possible move"
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
        rep = self.rep
        nrows = self.nrows
        ncols = self.ncols
        assert type(nrows) is int and type(ncols) is int
        assert nrows > 0 and ncols > 0    
        adj = self.adjacent_moves(nrows, ncols)
        possible = []
        for i in adj:
            if i[0] in rep and i[1] in rep:
                new_rep = swap_locations(rep, i[0], i[1])
                kept, discarded = remove_connected_groups(new_rep)
                if len(discarded) >= 3:
                    possible.append(i)
        return possible
    
    def adjacent_moves(self, nrows, ncols):
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
      
        
if __name__ == '__main__':
    puzzle = input("Enter a Dissembler puzzle to be solved: ")
    solver = DissemblerSolver(puzzle)
    solver.give_solution()