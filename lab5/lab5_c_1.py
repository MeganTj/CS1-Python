from tkinter import *
import random

# Graphics commands.

def draw_random_circle(canvas, x, y, color):
    '''Takes in four arguments: the canvas to draw the circle on, the
    x-coordinate of the center of the circle, the y-coordinate of the center of
    the circle, and the color of the circle. Draws a circle given these
    parameters and with a randomly chosen diameter between 10 to 50 pixels. 
    Returns the handle of the circle that was drawn on the canvas.'''
    d = random.randint(10, 50)
    return canvas.create_oval(x - d/2, y - d/2, x + d/2, y + d/2, fill = color,
                              outline = color)    

def random_color():
    '''Generates random color values in the format recognized by the tkinter
    graphics package, of the form #RRGGBB'''
    seq = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
           'd', 'e', 'f']
    rand = '#'
    for i in range(6):
        rand += random.choice(seq)
    return rand

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    global circles
    global color
    key = event.keysym
    if key == 'q':
        exit_python(event)
    if key == 'c':
        color = random_color()
    if key == 'x':
        for circle in circles:
            canvas.delete(circle)
        circles = []       

def button_handler(event):
    '''Handle left mouse button click events.'''
    global circles
    circle = draw_random_circle(canvas, event.x, event.y, color)
    circles.append(circle)

def exit_python(event):
    '''Exit Python.'''
    quit()

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    circles = []
    color = random_color()

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()