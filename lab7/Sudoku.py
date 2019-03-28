'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuLoadError(SudokuError):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        '''Creates a Sudoku object that contains the board as a field. The 
        board, a 9 x 9 grid of numbers is represented as a list of lists of
        numbers (a list of 9 lists of length 9). An empty square is represented
        by the number 0. Also has a list of moves as a field.'''
        self.board = []
        for i in range(9):
            self.board.append([0 for j in range(9)])
        self.moves = []

    def load(self, filename):
        '''Takes in a file name and tries to load the contents of that file into 
        the representation of the Sudoku board. The file must have 9 lines, each
        of which have 9 numbers in the range 0 to 9.'''
        f = open(filename, 'r')
        lines = f.readlines()
        if len(lines) != 9:
            raise SudokuLoadError('File has wrong number of lines.')
        for i in range(9):
            line = lines[i]
            if len(line) != 10:
                raise SudokuLoadError('Line is not 9 characters long.')
            for j in range(9):
                char = line[j]
                if char < '0' or char > '9':
                    raise SudokuLoadError('All characters must be digits.')
                digit = int(char)
                self.board[i][j] = digit

    def save(self, filename):
        '''Takes in a file names and saves the contents of the board in the file
        in the same format that the load method can read: 9 lines of 9 digits
        with no spaces.'''
        f = open(filename, 'w')
        for lst in self.board:
            line = ''
            for i in lst:
                line += str(i)
            line += '\n'
            f.write(line)

    def show(self):
        '''Pretty-print the current board representation.'''
        print()
        print('   1 2 3 4 5 6 7 8 9 ')
        for i in range(9):
            if i % 3 == 0:
                print('  +-----+-----+-----+')
            print(f'{i + 1} |', end='')
            for j in range(9):
                if self.board[i][j] == 0:
                    print(end=' ')
                else:
                    print(f'{self.board[i][j]}', end='')
                if j % 3 != 2 :
                    print(end=' ')
                else:
                    print('|', end='')
            print() 
        print('  +-----+-----+-----+')
        print()

    def move(self, row, col, val):
        '''Takes in the row coordinate, the column coordinate, and a number to
        place at these coordinates. All three are integers that range from 1
        to 9. If the inputs are valid and the move is a valid move, the move
        is executed by writing the value into the board representation. The
        move is also appended into the list of moves stored on the object.'''
        if row < 1 or row > 9: 
            raise SudokuMoveError('Row coordinate must be between 1 and 9.')
        if col < 1 or col > 9: 
            raise SudokuMoveError('Column coordinate must be between 1 and 9.') 
        if val < 1 or val > 9: 
            raise SudokuMoveError('Value at a location must be between 1 \
            and 9.') 
        adj_row = row - 1
        adj_col = col - 1
        if self.board[adj_row][adj_col] != 0:
            raise SudokuMoveError('The location ({0}, {1}) is ' 
                                  'occupied.'.format(row, col))
        for i in range(9):
            if self.board[adj_row][i] == val:
                raise SudokuMoveError('There is a row conflict with '
                                      'location ({0}, {1}).'.format(row, i + 1))
        for i in range(9):
            if self.board[i][adj_col] == val:
                raise SudokuMoveError('There is a column conflict with '
                                    'location ({0}, {1}).'.format(i + 1, col)) 
        start_x = 0
        start_y = 0
        if adj_row >= 3 and adj_row < 6:
            start_x = 3
        if adj_row >= 6:
            start_x = 6
        if adj_col >= 3 and adj_col < 6:
            start_y = 3
        if adj_col >= 6:
            start_y = 6 
        for i in range(3):
            for j in range(3):
                a = i + start_x
                b = j + start_y
                if self.board[a][b] == val:
                    raise SudokuMoveError('There is a box conflict ({0}, {1}) '
                                          'with location'.format(a + 1, b + 1))
        self.moves.append((row, col, val))
        self.board[adj_row][adj_col] = val 


    def undo(self):
        '''Removes the last entery in the stored lists of moves and erases the
        contents of the board at the at the coordinates of the last move.'''
        if len(self.moves) > 0:
            move = self.moves.pop()
            self.board[move[0] - 1][move[1] - 1] = 0

    def solve(self):
        '''Handles the user playing the game. Runs an infinite loop in which it
        asks the user for a command and executes a command.'''
        done = False
        while done == False:
            try:
                command = input('Enter a command: ')
                if command == 'q':
                    done = True
                elif command == 'u':
                    self.undo()
                    self.show()
                elif len(command) > 2 and command[:2] == 's ':
                    filename = command[2:]
                    self.save(filename)
                elif len(command) == 3:
                        for i in range(3): 
                            if command[i] < '0' or command[i] > '9':
                                raise SudokuCommandError('{0} is a bad ' 
                                                   'command.'.format(command))
                        self.move(int(command[0]), int(command[1]), 
                             int(command[2]))
                        self.show()
                                
                else:
                    raise SudokuCommandError('{0} is a bad '
                                             'command.'.format(command))
            except SudokuCommandError as err:
                print('Invalid command: {0} Please try again.'.format(err))
            except SudokuMoveError as err:
                print('Invalid move: {0} Please try again.'.format(err))            
            
           

if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except FileNotFoundError as e:
            print(e)
        except SudokuLoadError as e:
            print(e)

    s.show()
    s.solve()

