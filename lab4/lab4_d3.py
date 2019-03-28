from tkinter import *
import random

def draw_square(canvas, color, length, center):
    '''Takes in four arguments: the canvas to draw the square on, the color of
    the square, the length of the sides of the square, and the center of the 
    square. Draws a square given these parameters. Returns the handle of the
    square that was drawn on the canvas.'''
    center_x, center_y = center
    handle = canvas.create_rectangle(center_x - length/2, center_y - length/2,
                                     center_x + length/2, center_y + length/2, 
                                     fill = color, outline = color)
    return handle
    
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

def random_position(max_x, max_y):
    '''Takes in two integer arguments that are both >= 0. Returns a random
    (x, y) pair with both x and y >= 0 and with x <= max_x and y <= max_y.'''
    assert max_x >= 0 and max_y >= 0, 'negative maximums'
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    return (x, y) 

def random_color():
    '''Generates random color values in the format recognized by the tkinter
    graphics package, of the form #RRGGBB'''
    seq = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
           'd', 'e', 'f']
    rand = '#'
    for i in range(6):
        rand += random.choice(seq)
    return rand

def exit_python(event):
    '''Exits Python when the event 'event' occurs.'''
    quit()

if __name__ == '__main__':
    '''Draws 50 squares of random colors, random sizes ranging from 20 to 150 
    pixels, and random positions on an 800 by 800 pixel canvas.'''
    root = Tk()
    root.geometry('800x800')    
    c = Canvas(root, width = 800, height = 800)
    c.pack() 
    for i in range(50):
        color = random_color()
        size = random_size(20, 150)
        position = random_position(800, 800)
        draw_square(c, color, size, position)
    root.bind('<q>', exit_python)
    input('Press <q> to quit. \n')
    root.mainloop()
    
