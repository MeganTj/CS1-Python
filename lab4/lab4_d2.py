from tkinter import *

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
                                
    
if __name__ == '__main__':
    '''Draws four squares of size 100x100 on an 800x800 canvas in each corner.
    The square in the upper-left is red, that in the upper-right is green, that
    in the lower-left is blue, and the remaining in the lower-right is yellow.
    '''    
    root = Tk()
    root.geometry('800x800')    
    c = Canvas(root, width = 800, height = 800)
    c.pack()  
    draw_square(c, 'red', 100, (50,50))
    draw_square(c, 'green', 100, (750,50))
    draw_square(c, 'blue', 100, (50,750))
    draw_square(c, 'yellow', 100, (750,750))
    root.bind('<q>', quit)
    root.mainloop()
    