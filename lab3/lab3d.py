'''
lab3c.py
Simple L-system simulator.
'''

# References: 
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math

# ---------------------------------------------------------------------- 
# Example L-systems.
# ---------------------------------------------------------------------- 

# Koch snowflake.
koch = { 'start' : 'F++F++F', 
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1', 
              '+' : 'R 60', 
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A', 
             'A'     : '-BF+AFA+FB-' , 
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1', 
                 '-' : 'L 90', 
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G', 
               'F'     : 'F-G+F+G-F', 
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1', 
                    'G' : 'F 1', 
                    '+' : 'L 120', 
                    '-' : 'R 120' }

plant = { 'start' : 'X', 
          'X'     : 'F-[[X]+X]+F[+FX]-X', 
          'F'     : 'FF' }

plant_draw = { 'F' : 'F 1', 
               '-' : 'L 25', 
               '+' : 'R 25' }

# ---------------------------------------------------------------------- 
# L-systems functions.
# ---------------------------------------------------------------------- 

def update(dict, str):
    '''Takes in two arguments. The first is a a dictionary that specifies the
    starting string and the update rules for a particular L-system. The second
    is an L-system string. Generates the next version of the L-system string and
    returns it.'''
    new_str = ''
    for i in range(len(str)):
        if str[i] in dict.keys():
            new_str += dict[str[i]]
        else:
            new_str += str[i]
    return new_str

def iterate(lsys, n):
    '''Takes in two arguments. The first is a dictionary that specifies the
    starting string and the update rules for a particular L-system. The second
    is an integer n which should be 0 or greater. 
    
    Returns the string which results from starting with the starting string of
    that L-system and updating n times.'''
    new_str = lsys['start']
    for i in range(n):
        new_str = update(lsys, new_str)
    return new_str

def lsystemToDrawingCommands(draw, s):
    '''Takes in two arguments. The first is a dictionary whose keys are
    characters in L-system strings and whose values are drawing commands. The
    second is an L-system string. 
    
    Returns the list of drawing commands needed to draw the figure corresponding
    to the L-system string.'''
    commands = []
    post = []
    current = (0.0, 0.0, 0)
    for i in range(len(s)):        
        if s[i] in draw.keys():
            commands.append(draw[s[i]])
            current = nextLocation(current[0], current[1], current[2], 
                                   draw[s[i]])
        elif s[i] == '[':
            post.append(current)
        elif s[i] == ']':
            restored = post.pop()
            cmd = 'G {0} {1} {2}'.format(restored[0], restored[1],
                                                     restored[2])
            commands.append(cmd)
            current = nextLocation(current[0], current[1], current[2], 
                                   cmd)
            
    return commands   

def bounds(cmds):
    '''Takes in one argument: a list of drawing commands. Computes the bounding
    coordinates of the resulting drawing, or in other words, the minimum and
    maximum x and y coordinates achieved by the turtle to make the drawing. 
    
    Returns a tuple of the minimum x, maximum x, minimum y, and maximum y 
    coordinates, where each coordinate is a float.'''
    xmin, ymin, xmax, ymax = 0.0, 0.0, 0.0, 0.0
    current_x, current_y, current_angle = 0.0, 0.0, 0
    for str in cmds:
        current_x, current_y, current_angle = nextLocation(current_x, current_y, 
                                               current_angle, str)
        if xmin > current_x:
            xmin = current_x
        if ymin > current_y:
            ymin = current_y  
        if xmax < current_x:
            xmax = current_x  
        if ymax < current_y:
            ymax = current_y        
    return (xmin, xmax, ymin, ymax)

def nextLocation(x, y, angle, cmd):
    '''Takes in four arguments. The first is the current x coordinate value of 
    the turtle. The second is the current y coordinate value of the turtle. The
    third is the current direction (angle from the horizontal) the turtle is 
    facing. The fourth is a drawing command.
    
    Generates the next location and direction of the turtle after that drawing
    command has executed. Returns a tuple of the next x coordinate, the next y
    coordinate, and the next angle of the turtle, where the coordinates are 
    floating-point numbers while the angle is an integer.'''
    coord = cmd.split()
    letter = coord[0]
    number = coord[1:]
    new_x = x
    new_y = y
    new_angle = angle
    rad = angle * (math.pi/180)
    if letter == 'F':
        new_x += float(number[0]) * math.cos(rad)
        new_y += float(number[0]) * math.sin(rad)
    elif letter == 'L':
        new_angle = (new_angle + int(number[0])) % 360
    elif letter == 'R':
        new_angle -= int(number[0])
        if new_angle < 0:
            new_angle += 360 
    else:
        new_x = float(number[0])
        new_y = float(number[1])
        new_angle = int(number[2])
    return (new_x, new_y, new_angle)
         
def saveDrawing(filename, bounds, cmds):
    '''Takes in three arguments. The first is a filename to write to. The 
    second is the bounds of the resulting drawing, as a tuple of the floats
    minimum x, maximum x, minimum y, maximum y coordinates. The third is a list
    of drawing commands. 
    
    Writes to a file corresponding to the given filename the bounds information
    on a single line and then the drawing commands, one per line.'''
    file = open(filename, 'w')
    file.write('{0} {1} {2} {3} \n'.format(bounds[0], bounds[1], bounds[2],
                                           bounds[3]))
    for str in cmds:
        file.write(str +'\n')
    file.close()

def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print('Making drawings for {}...'.format(name))
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    makeDrawings('koch', koch, koch_draw, 0, 6)
    makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)
    makeDrawings('plant', plant, plant_draw, 1, 7)
    
    

