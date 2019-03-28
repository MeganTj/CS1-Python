# Ex A.1.1:

def union(set1, set2):
    '''Takes two sets and computes and returns their union as another set.'''
    union = set([])
    for i in set1:
        union.add(i)
    for j in set2:
        union.add(j)
    return union

# Ex A.1.2:

def intersection(set1, set2):
    '''Takes two sets and computes and returns their intersection as another
    set.'''
    inter = set([])
    for i in set1:
        if i in set2:
            inter.add(i)
    return inter

# Ex A.1.3:

def difference(set1, set2):
    '''Takes two sets and computes and returns the difference of the two sets 
    as another set.'''
    diff = set([])
    for i in set1:
        if i not in set2:
            diff.add(i)
    return diff 

# Ex A.2:

def mySum(*args):
    '''Takes an arbitrary number of arguments, all of which should be integers
    greater than zero. Returns the sum of these integers.'''
    sum = 0
    for i in args:
        if not isinstance(i, int):
            raise TypeError('All arguments must be integers.')
        if i < 1:
            raise ValueError('All arguments must be greater than zero.')
        sum += i
    return sum

# Ex A.3:

def myNewSum(*args):
    '''Takes in a single list of positive integers as its only argument or an
    arbitrary number of individual values. Returns the sum of the integers.'''
    sum = 0
    if len(args) == 1 and isinstance(args[0], list):
        for i in args[0]:
            if not isinstance(i, int):
                raise TypeError('All list elements must be integers.')
            if i < 1:
                raise ValueError('All list elements must be greater than 0.')
            sum += i
        return sum
    for i in args:
        if not isinstance(i, int):
            raise TypeError('All arguments must be integers.')
        if i < 1:
            raise ValueError('All list elements must be greater than 0.')   
        sum += i
    return sum

# Ex A.4:

def myOpReduce(lst, **op):
    '''Takes one required argument, a list of integers, and one keyword argument
    called op, whose value should be a string. The string should either be '*', 
    '+', or 'max'.'''
    if len(op) == 0:
        raise ValueError('No keyword argument.')
    if len(op) > 1:
        raise ValueError('Too many keyword arguments.')
    if 'op' not in list(op.keys()):
        raise ValueError('Invalid keyword argument.')
    oper = op['op']
    if not isinstance(oper, str):
        raise TypeError('Value for keyword argument \'op\' must be a string.')
    if oper != '*' and oper != '+' and oper != 'max':
        raise ValueError('Invalid keyword argument.')
    ans = 0
    if oper == '+':
        for i in lst:
            ans += i
    if oper == '*':
        ans = 1
        for i in lst:
            ans *= i  
        return ans
    for i in lst:
        ans = max(ans, i)
    return ans
            
# Ex B.1: On catching the KeyError, the program aborts entirely and does not 
# handle the exception. 

import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError as err:   
        print('KeyError: The key {0} does not exist'.format(err))

# Ex B.2: The program does not specify what kind of error was found and it 
# doesn't specify what key doesn't exist. 

import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError as err:   # raised if a key isn't in a dictionary
        print('KeyError: The key {0} does not exist'.format(err),
              file=sys.stderr)
        
# Ex B.3: The program raises an exception in an except block, which is supposed
# to handle the exception.

import sys

def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and 
    key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError as err:   # raised if a key isn't in a dictionary
        print('KeyError: The key {0} does not exist'.format(err))
    
# Ex B.4: The program prints out the traceback, which is not preferrable. It
# also prints out the missing key, but it does not give an error message. 

import sys
    
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and 
    key2.'''
    match1 = False
    while not match1:
        try:
            val1 = dict[key1]
            match1 = True
        except KeyError as e:  
            print('The first key doesn\'t exist.')
            key1 = input('Enter a new key: ')
    match2 = False
    while not match2:
        try:
            val2 = dict[key2]
            match2 = True
        except KeyError as e:
            print('The second key doesn\'t exist.')
            key2 = input('Enter a new key: ')

    return val1 + val2

# Ex B.5: The program attempts to raise an exception with a message, but it 
# cannot do so by having print() after raising the ValueError.

import sys

def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0', file=sys.stderr)
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)


# Ex B.6: The program prints the error message before the Traceback, so the 
# error message does not appear in the correct location. 

import sys

def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0', file=sys.stderr)
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)

# Ex B.7: The error should not be a TypeError but rather a ValueError, as x is
# the right type but does not have the correct value.

from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0.0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if x <= 0.0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)

# Ex B.8: The program should raise specific types of Exceptions so that the 
# exception is caught and handled properly. The first exception is raised when
# x is not the correct type while the second is raised when x is not the correct
# value, so the two exceptions should be TypeError and ValueError respectively.

from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0.0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if type(x) is not float:
        raise TypeError('x must be a float')
    elif x <= 0.0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)


