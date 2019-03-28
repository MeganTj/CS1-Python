import math

# Ex A.1:

class Point:
    '''Represents a three-dimensional Euclidian space with real-valued coord-
    inates.'''
    
    def __init__(self, x, y, z):
        '''Takes in the x, y, and z coordinates of the point and constructs a
        Point object. '''
        self.x = x
        self.y = y
        self.z = z
        
    def distanceTo(self, p):
        '''Takes in another Point and computes the distance between that Point 
        and the Point being acted on.'''
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2 + 
                          (self.z - p.z) ** 2)
    
# Ex A.2:

class Triangle:
    '''Represents a Triangle in a three-dimensional Euclidian space with 
    real-valued coordinates.'''
    
    def __init__(self, p1, p2, p3):
        '''Takes in three Point objects that represent the vertices of the
        triangle.'''
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
    def area(self):
        '''Finds the area of the Triangle object being acted on using Heron's
        formula.'''
        a = self.p1.distanceTo(self.p2)
        b = self.p2.distanceTo(self.p3)
        c = self.p3.distanceTo(self.p1)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Ex A.3:

class Averager:
    '''Stores a list of numbers and performs various operations on it.'''
    
    def __init__(self):
        '''Constructs an Averager class that stores the current list of numbers,
        the sum of the current list, and how many numbers are in the current 
        list.'''
        self.nums = []
        self.total = 0
        self.n = 0
    
    def getNums(self):
        '''Returns a copy of the list of numbers stored so far.'''
        return self.nums[:]
    
    def append(self, new_num):
        '''Takes in a new number and appends this number to the list.'''
        self.nums.append(new_num)
        self.total += new_num
        self.n += 1
        
    def extend(self, new_list):
        '''Takes in a list of numbers and appends it to the existing list.'''
        for i in new_list:
            self.nums.append(i)
            self.total += i
            self.n += 1            
    
    def average(self):
        '''Returns the average of the stored list as a floating-point value.'''
        if self.total == 0:
            return 0.0
        return float(self.total / self.n)
    
    def limits(self):
        '''Returns the minimum and maximum of the stored list as a tuple.'''
        if self.total == 0:
            return (0, 0)
        return (min(self.nums), max(self.nums))
            
# Ex B.1: Returning the conditional evaluates it and returns the result.

def is_positive(x):
    '''Test if x is positive.'''
    return x > 0

# Ex B.2: There is no need for the "found" and "location" variables. When
# "item == x" is true, you can return the index of item. Since we know that if x
# is within the list, the program will return a location in the for loop, if the
# program exits the for loop, x is not within the list and we can simply return
# -1.

def find(x, lst):
    '''Returns the index into a list where x is found, or -1 otherwise.
    Assume that x is found at most once in the list.'''
    for i, item in enumerate(lst):
        if item == x:
            return i
    return -1
    
# Ex B.3: Within the if statements, the program should return the categorization
# so that it doesn't have to unnecessarily check the other conditions before 
# returning. For the third if statement, we only need to check if "x < 10" as 
# we already know that x is greater than 0 if the program reaches that point.
# The fourth if statement is unnecessary.

def categorize(x):
    '''Return a string categorizing the number 'x', which should be
    an integer.'''
    if x < 0:
        return 'negative'
    if x == 0:
        return 'zero'
    if x < 10:
        return 'small'
    return 'large'

# Ex B.4: The if statements are unnecessary as the for loop will handle all of
# those situations. There is also no need for the "answer" method.

def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''

    total = 0
    for item in lst:
        total += item
    return total