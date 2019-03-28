# Name: Megan Tjandrasuwita
# CMS cluster login name: mtjandra

'''
The CS 1 final exam, Fall 2018, part 1.

Functions on locations and sets of locations.
'''

import string
from utils import *

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
    

