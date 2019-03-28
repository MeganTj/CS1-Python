from tkinter import *
import random
import math

# Graphics commands.

def draw_line(canvas, start, end, color):
    '''Takes in four arguments: the canvas to draw the line on, the
    starting location, the ending location, and the color of the line. Draws a
    line given these parameters. Returns the handle of the line that was drawn
    on the canvas.'''
    start_x, start_y = start
    end_x, end_y = end
    return canvas.create_line(start_x, start_y, end_x, end_y, fill = color,
                              width = 3)    

def draw_star(canvas, n, center, color):
    '''Takes in four arguments: the canvas to draw the line on, the number of
    points that the star has (a positive odd integer no smaller than 5), the
    center of the star, and the color of the star. Draws a star pointed
    vertically upwards given these parameters  and with a randomly chosen radius
    between 50 to 100 pixels. Returns a list of the handles of all the lines
    drawn.'''    
    points = []
    lines = []
    r = random.randint(50, 100)
    center_x, center_y = center
    theta = (2 * math.pi) / n
    for p in range(n):
        x = r * math.cos(theta * p)
        y = r * math.sin(theta * p)
        points.append((y + center_x, -x + center_y))
    increment = int((n - 1) / 2)
    for l in range(n):
        end_index = (l + increment) % n
        lines.append(draw_line(canvas, points[l], points[end_index], color))
    return lines

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
    global stars
    global color
    global n
    key = event.keysym
    if key == 'q':
        exit_python(event)
    if key == 'c':
        color = random_color()
    if key == 'plus':
        n += 2
    if key == 'minus':
        if n >= 7:
            n -= 2
    if key == 'x':
        for lines in stars:
            for line in lines:
                canvas.delete(line)
        stars = []       

def button_handler(event):
    '''Handle left mouse button click events.'''
    global stars
    lines = draw_star(canvas, n, (event.x, event.y), color)
    stars.append(lines)

def exit_python(event):
    '''Exit Python.'''
    quit()

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    stars = []
    color = random_color()
    n = 5

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()