# Dragging from one box to another
# Print error messages
# Animate removing boxes
# Show number of moves played
# Splash screen when player wins

from tkinter import *


def draw_square(canvas, start, end, color):
    '''Takes in four arguments: the canvas to draw the line on, the
    starting location, the ending location, and the color of the line. Draws a
    line given these parameters. Returns the handle of the line that was drawn
    on the canvas.'''
    start_x, start_y = start
    end_x, end_y = end
    return canvas.create_rectangle(start_x, start_y, end_x, end_y, fill = color,
                              outline = color)    

def print_error(root):
    messageBox.showwarning('Sorry! This ain\'t allowed')
    return

class DissemblerWidgets:
    def __init__(self, master):
        g_frame = Frame(master, row = 0, column = 0)
        g_frame.grid(row = 0, column = 1, rowspan = 2)
        
        
        
        c_frame = Frame(master, width = 400, height = 600)
        c_frame.grid(row = 0, column = 0)
        
        canvas = Canvas(g_frame, width = 800, height = 800)
        canvas.pack()        
        
        m_frame = Frame(master, width = 400, height = 200)
        lbl = Label(m_frame, text = 'Number of Moves')        
        m_frame.grid(row = 1, column = 0)

if __name__ == '__main__':
    root = Tk()
    root.title('Dissembler')
    root.geometry('1200x800')
    #outer = LabelFrame(root, width = 1200, height = 800, text = 'Dissembler')
    #outer.pack()
    
    widgets = DissemblerWidgets(root)
    
    move_var = StringVar()
    
    
    #possible_moves = set()
    #options = []
    #for i in possible_moves:
        #options.append()
    #options.append('Undo')
    #opt_menu = OptionMenu(frame, move_var, moves)
    #opt_menu.pack(side = LEFT)
        
    #root.geometry('1200x800')
    
    root.mainloop()