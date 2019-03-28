# Ex A.1:

def list_reverse(lst):
    '''Takes in an argument, a list, and returns the reverse of the list without
    changing the original list.'''
    lst2 = lst[:]
    lst2.reverse()
    return lst2

# Ex A.2

def list_reverse2(lst):
    '''Takes in an argument, a list, and returns the reverse of the list without
    changing the original list. Uses the range function and for loop.'''
    lst2 = []
    for i in range(len(lst), 0, -1):
        lst2.append(lst[i-1])
    return lst2

# Ex A.3

def file_info(txt):
    '''Takes in an argument, a string representing the name of a text file.
    Returns the number of lines, the number of words, the number of characters,
    in the file as a tuple with three components (line count, word count, 
    character count).'''
    file = open(txt, 'r')
    num_line = 0
    num_word = 0
    num_char = 0
    for line in file:
        num_line += 1
        x = line.split()
        num_word += len(x)
        num_char += len(line)
    file.close()
    return (num_line, num_word, num_char)

# Ex A.4

def file_info2(txt):
    '''Takes in an argument, a string representing the name of a text file.
    Returns a dictionary containing the line count, word count, and character
    count.'''    
    num_line, num_word, num_char = file_info(txt)
    return {'lines': num_line, 'words': num_word, 'characters': num_char}

# Ex A.5

def longest_line(txt):
    '''Takes in an argument, the name of a text file and returns the length of
    the longest line of the file in addition to the line itself as a tuple. '''
    file = open(txt, 'r')
    longest = ''
    for line in file:
        if len(line) > len(longest):
            longest = line
    file.close()
    return (len(longest), longest)

# Ex A.6

def sort_words(str):
    '''Takes in an argument, a string, splits the string into a list of words,
    and sorts the string.'''
    list = str.split()
    list.sort()
    return list

# Ex A.7: 11011010 --> 
# 0 * 2^0 + 1 * 2^1 + 0 * 2^2 + 1 * 2^3 + 1 * 2^4 + 0 * 2^5 + 1 * 2^6 + 1 * 2^7
# = 218
# The largest eight-digit binary number = 
# 2^0 + 2^1 + 2^2 + 2^3 + 2^4 + 2^5 + 2^6 + 2^7 = 255

# Ex A.8

def binaryToDecimal(lst):
    '''Takes in an argument, a binary number represented as a list of 0s and 1s,
    and returns it as a Python integer.'''
    sum = 0
    for i in range(len(lst)):
        sum += 2 ** (len(lst) - i -1) * lst[i]
    return sum

# Ex A.9: 

def decimalToBinary(num):
    '''Takes in an argument, a Python integer, and returns it into a list of 
    0's and 1's representing the binary equivalent. We assume that the integer
    is greater than 0.''' 
    if num < 1:
        return [0]
    largest = largestPowerTwo(num)
    num -= 2 ** (largest)
    binary = [0] * (largest + 1)
    binary[0] = 1
    while num > 1:
        largest = largestPowerTwo(num)
        num -= 2 ** (largest)
        binary[len(binary) - 1 - largest] = 1
    if num == 1:
        binary[len(binary) - 1] = 1
    return binary
         
def largestPowerTwo(num):
    '''Takes in an argument, a Python integer, and returns the largest power of
    two exponent that fits into the integer.'''    
    power = 0
    # the power of two we compare to the integer
    comp = 1
    while True:
        comp *= 2
        if comp > num:
            break
        power += 1
    return power
        
# Ex B.2.1: The three kinds of mistakes are bad function name, no space 
# after commas, and no spaces before and after the operators.

def sum_cubes(a, b, c):
    return a * a * a + b * b * b + c * c * c

# Ex B.2.2: The four kinds of mistakes are bad names, not leaving a space after 
# the open-comment sign, bad grammar in the comment, and a line longer than 80
# characters.

def sum_of_cubes(argument_a, argument_b, argument_c, argument_d):
    # Return the sum of cubes of argument_a, argument_b, argument_c, and 
    # argument_d
    return argument_a * argument_a * argument_a + argument_b * argument_b * \
           argument_b + argument_c * argument_c * argument_c

# Ex B.2.3: The two kinds of mistakes are lack of blank lines and inconsistent
# indentation levels.

def sum_of_square(x, y):
    return x * x + y * y

def sum_of_three_cubes(x, y, z):
    return x * x * x + y * y * y + z * z * z






