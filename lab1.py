# Ex C.1.1: 9 - 3 --> 6
# Ex C.1.2: 8 * 2.5 --> 20.0
# Ex C.1.3: 9 / 2 --> 4.5
# Ex C.1.4: 9 / -2 --> -4.5
# Ex C.1.5: 9 % 2 --> 1
# Ex C.1.6: 9 % -2 --> -1
# Ex C.1.7: -9 % 2 --> 1
# Ex C.1.8: 9 / -2.0 --> -4.5
# Ex C.1.9: 4 + 3 * 5 --> 19
# Ex C.1.10: (4 + 3) * 5 --> 35

# Ex C.2.1: x = 100 --> 100
# Ex C.2.2: x = x + 10 --> 110
# Ex C.2.3: x += 20 --> 130
# Ex C.2.4: x = x - 40 --> 90
# Ex C.2.5: x -= 50 --> 40
# Ex C.2.6: x *= 3 --> 120
# Ex C.2.7: x /= 5 --> 24.0
# Ex C.2.8: x %= 3 --> 0.0

#Ex C.3: First the right side of the assigment operator is evaluated, and as
#the value of x is 3, the right side would come out to 0. Next, this result
#is added to x, so the new value of x is 3 + 0, which is 3.

# Ex C.4.1.1: 1j + 2.4j --> 3.4j
# Ex C.4.1.2: 4j * 4j --> -16+0j
# Ex C.4.1.3: (1+2j) / (3+4j) --> 0.44+0.08j

# Ex C.4.2.1: (1+2j) * (1+2j) --> -3+4j
# Ex C.4.2.2: 1+2j * 1+2j --> 1+4j
#Ex C.4: The last two expressions gave different results because Python
#evaluates both using conventional order of operations. So in the 2nd
#expression, it multiplies 2j and 1 and adds that result to 1 and 2j, which is
#different from multiplying the expression 1+2j with itself. This tells us that
#the way Python handles complex numbers is the same as the way it handles
#real numbers.

# Ex C.5.1: cmath.sin(-1.0+2.0j) --> -3.165778513216168+1.9596010414216063j
# Ex C.5.2: cmath.log(-1.0+3.4j) --> 1.2652585805200263+1.856847768512215j
# Ex C.5.3: cmath.exp(-cmath.pi * 1.0j) -->-1-1.2246467991473532e-16j
#Ex C.5: It is a better idea to write import math and import cmath as from
#math import * and from cmath import * import all names from the math and cmath
#modules respectively, which could lead to name clashes as functions that share 
#the same names as the imported names become unusable.

# Ex C.6.1: "foo" + "bar" --> 'foobar'
# Ex C.6.2: "foo" 'bar' --> 'foobar'
#Ex C.6.3: 
#a = 'foo'
#b = "bar"
#a + b --> 'foobar' 

#Ex C.6.4: 
#a = 'foo'
#b = "bar"
#a b --> Traceback (most recent call last):
  #Python Shell, prompt 18, line 3
#Syntax Error: invalid syntax: <string>, line 3, pos 3 

# Ex C.7: 'A\nB\nC'

# Ex C.8: '-' * 80

# Ex C.9: 'first line\nsecond line\nthird line'

x = 3
y = 12.5

# Ex C.10.1:

print('The rabbit is {}.'.format(x))

# Ex C.10.2:

print('The rabbit is {} years old.'.format(x))

# Ex C.10.3:

print('{} is average.'.format(y))

# Ex C.10.4:

print('{0} * {1}'.format(y, x))

# Ex C.10.5:

print('{0} * {1} is {2}.'.format(y, x, y*x))

# Ex C.11

num = input("Enter a number: ")
num = float(num)
print(num)

# Ex C.12

def quadratic(a, b, c, x):
    return a*x**2 + b*x + c

# Ex C.13

def GC_content(dna):
    '''
    GC_content(dna) --> float 
    Input argument is a string representing a DNA sequence.
    
    Return the proportion of G and C characters, or "bases," in a string
    representing a DNA sequence.'''
    num_g = dna.count('G')
    num_c = dna.count('C')
    total_gc = num_g + num_c
    return total_gc / len(dna)
    