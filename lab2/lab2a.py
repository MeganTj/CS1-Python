import random

#Ex B.1:

def complement(dna):
    '''Takes in one argument, a string representing a DNA string, and
    returns another string that is the complement of the original string.'''
    comp = '';
    for b in range(len(dna)):
        if dna[b] == 'A':
            comp +='T'
        elif dna[b] == 'T':
            comp += 'A'    
        elif dna[b] == 'G':
            comp += 'C'       
        else:
            comp += 'G'  
    return comp

#Ex B.2:

def list_complement(dna):
    '''Takes in one argument, a list representing the individual bases of
    a DNA sequence, and modifies the list so that it represents the complement
    of the original sequence.'''
    for b in range(len(dna)):
        if dna[b] == 'A':
            dna[b] = 'T'
        elif dna[b] == 'T':
            dna[b] = 'A'    
        elif dna[b] == 'G':
            dna[b] = 'C'       
        else:
            dna[b] = 'G'  

#Ex B.3:  

def product(num_list):
    '''Takes in one argument, a list of numbers, and returns the product of 
    the entire list.'''
    product = 1
    for num in num_list:
        product *= num
    return product

#Ex B.4

def factorial(num):
    '''Takes in an argument, a number, and returns the factorial of that 
    integer.'''
    return product(range(1, num + 1))

#Ex B.5

def dice(m, n):
    '''Takes in two arguments: the 'sidedness' of the dice (m) and the 
    number of dice rolled (n). Returns the sum of the values of all the
    dice rolled.'''
    sum = 0;
    for i in range(n):
        sum += random.choice(range(1, m + 1))
    return sum

#Ex B.6

def remove_all(list_int, value):
    '''Takes in two arguments: a list of integers and an integer value. 
    Modifies the list by removing all copies of the integer value from
    the list.'''
    while list_int.count(value) > 0:
        list_int.remove(value)
        
#Ex B.7

def remove_all2(list_int, value):
    '''Takes in two arguments: a list of integers and an integer value. 
    Modifies the list by removing all copies of the integer value from
    the list. Counts the number of values to be removed once, and then 
    uses the remove method that many times.'''
    total = list_int.count(value)
    for i in range(total):
        list_int.remove(value)

def remove_all3(list_int, value):
    '''Takes in two arguments: a list of integers and an integer value. 
    Modifies the list by removing all copies of the integer value from
    the list. Counts the number of values to be removed once, and then 
    uses the remove method that many times.'''    
    while value in list_int:
        list_int.remove(value)

#Ex B.8

def any_in(l1, l2):
    '''Takes two lists as arguments and returns True if any of the
    elements of the first are qeualy to any in the scecond.'''
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                return True
    return False

#Ex C.1.a: The problem is a = 0 in the if statement. To write a boolean
#expression, you must use == instead of =.

#Ex C.1.b: The problem is the argument of add_suffix. There can never be quotes
#in the arguments when defining a function. You would define add_suffix as
#add_suffix(s).

#Ex C.1.c: The problem is the 's' in the return statement. You don't put quotes
#around a variable that is already a string, so you would just have s in the 
#return statement.

#Ex C.1.d: The problem is with the concatenation in the last line. The
#concatenation operator does not work with two different types of objects, so
#you could put 'bam' in a list, like ['bam'], or use the append method,
#like lst.append('bam').

#Ex C.1.e: The problem is trying to set a variable equal to reverse acting on a 
#list and returning using the method append. The methods reverse and append only
#modify a list and do not return anything. You would not set a variable to
#lst.reverse() and you would not try to return lst.append(0).

#Ex C.1.f: The problem is trying to append a list to a list. The method append
#is not overloaded such that you can pass a list to append. You would use a for
#loop to append each element of the list str to list. Also, there is a problem
#with using list as the name as one of the arguments, as list is also a function
#that converts an iterable, str, to a list. Thus you would rename the list 
#parameter to some other name.

#Ex C.2: At the time when c = b + a is evaluated, the value of a is 10
#and that of b is 20. The assignment of a to 30 is done after c = b + a and
#thus does not matter in evaluation.

#Ex C.3: Printing a result translates a string to standard output and displays 
#it for human viewing. On the other hand, returning a result sends the result 
#directly to the caller, which the caller can pass to another function, store,
#etc.

#Ex C.4: The first works as the function takes in arguments that a programmer
#will pass when the function is called. When values are gotten interactively,
#the programmer doesn't call a function with arguments beforehand; instead,
#in the body of the function, the values are obtained from the user.

#Ex C.5: This function won't work because strings are immutable, meaning 
#that you cannot modify them.

#Ex C.6: The item that is retrieved from list is like a return value. When
#you multiply item by 2, you are doubling the current variable item, but you
#are not actually changing the contents of the list. In essence, item does not
#point to the element in the list.


    



