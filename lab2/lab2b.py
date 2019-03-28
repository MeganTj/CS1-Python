import random

def make_random_code():
    '''Returns a string of four characters, each randomly selected to be either 
    'R', 'G', 'B', 'Y', 'O', or 'W' '''
    chars = ['R', 'G', 'B', 'Y', 'O', 'W']
    str = '';
    for i in range(4):
        str += random.choice(chars)
    return str

def count_exact_matches(str1, str2):
    '''Takes in two arguments, both strings of length 4, and returns number
    of places where two strings have the exact same letters at the same
    locations.'''
    num_matches = 0
    for i in range(4):
        if str1[i] == str2[i]:
            num_matches += 1
    return num_matches

def count_letter_matches(str1, str2):
    '''Takes in two arguments, both strings of length 4, and returns number
    of letters of the strings that are the same regardless of order'''  
    list1 = list(str1)
    list2 = list(str2)
    num_matches = 0
    counter = 0
    for i in range(4):
        if list1[i] in list2:
            counter += 1
            list2.remove(list1[i])
    return counter

def compare_codes(code, guess):
    '''Takes in two arguments, both strings of length 4, the first representing
    the secred code chosen by the code maker and the second representing the
    guess of the codebreaker. Outputs a string of length 4 only consisting of 
    the characters 'b', 'w', and '-', which represent key pegs.'''
    black_pegs = count_exact_matches(code, guess)
    white_pegs = count_letter_matches(code, guess) - black_pegs
    blank_pegs = 4 - black_pegs - white_pegs
    out = black_pegs * 'b' + white_pegs * 'w' + blank_pegs * '-'
    return out

def run_game():
    '''Runs the game by selecting a secret code, prompting the user to guess,
    evaluating how well the guess matches the stored code, repeating the process
    if the secret code is not guessed. Tells the user how many moves it took
    to guess the code.'''
    print('New game.')
    code = make_random_code()
    feedback = '';
    counter = 0
    while True:
        guess = input('Enter your guess: ')
        counter += 1
        feedback = compare_codes(code, guess)
        print('Result:', feedback)
        if feedback == 'bbbb':
            print('Congratulations! You cracked the code in', counter, 'moves!')
            break
        
    
  
        
    
            