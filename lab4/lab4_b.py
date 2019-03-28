import random

#Ex B.1:

def random_size(small, large):
    '''Takes in two arguments, two non-negative even integers. The first 
    argument must be smaller than the sedond. Returns a random even integer >=
    the lower number and <= the upper number.'''
    assert small >= 0 and large >= 0, 'negative input numbers'
    assert small % 2 == 0 and large % 2 == 0, 'odd input numbers'
    assert small < large, 'first argument not less than second'
    rand = random.randint(small, large/2) * 2
    assert rand % 2 == 0, 'output not even'
    return rand

#Ex B.2:

def random_position(max_x, max_y):
    '''Takes in two integer arguments that are both >= 0. Returns a random
    (x, y) pair with both x and y >= 0 and with x <= max_x and y <= max_y.'''
    assert max_x >= 0 and max_y >= 0, 'negative maximums'
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    return (x, y)

#Ex B.3: 

def random_color():
    '''Generates random color values in the format recognized by the tkinter
    graphics package, of the form #RRGGBB'''
    seq = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
           'd', 'e', 'f']
    rand = '#'
    for i in range(6):
        rand += random.choice(seq)
    return rand

#Ex B.4:

def count_values(dict):
    '''Takes a dictionary as an argument and returns a count of the number of 
    distinct values it contains'''
    val = dict.values()
    unique = []
    for i in val:
        if i not in unique:
            unique.append(i)
    return len(unique)

#Ex B.5:

def remove_value(dict, item):
    '''Takes a dictionary and an item that could be a value in the dictionary.
    Removes all key/value pairs from the dictionary which have that value. If 
    the value is not in the dictionary, nothing is done.'''
    remove = []
    for k, v in dict.items():
        if v == item:
            remove.append(k)
    for i in remove:
        del dict[i]
        
#Ex B.6:

def split_dict(dict):
    '''Takes in an argument, a dictionary that uses strings as keys and returns 
    a tuple of two dictionaries whose pairs are from the original dictionary: 
    those whose keys start with the letters a-m (lower or uppercase) and those
    whose keys start with the letter n-z (lower or uppercase).'''
    dict_1 = {}
    dict_2 = {}
    for k, v in dict.items():
        if (k >= 'a' and k <= 'm') or (k >= 'A' and k <= 'M'):
            dict_1[k] = v
        if (k >= 'n' and k <= 'z') or (k >= 'N' and k <= 'Z'):
            dict_2[k] = v   
    return (dict_1, dict_2)

#Ex B.7:

def count_duplicates(dict):
    '''Takes a dictionary as an argument and returns the number of values that 
    appear two or more times.'''
    unique = []
    repeated = []
    for k, v in dict.items():
        if v in unique:
            if v not in repeated:
                repeated.append(v)
        else:
            unique.append(v)
    return len(repeated)
    
    
    