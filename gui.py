from utilities import *
from solution import *
import tkinter as tk


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.gridEntry = []
        self.gridValues = ''

    def great(self):
        self.root.title('Sudoku Solver')

    def createEntries(self):
        """The code creates a grid of 9 rows and columns.
        The first row is numbered 0, the second row is numbered 1, etc.
        Each entry in the grid has a width of 3 pixels.
        The code creates an Entry object for each column and then appends it to the root node with borderwidth=2 so that it will be on top of any other entries in that column.
        Then it sets its width to 3 pixels so that all three sides are equal size.
        The code creates nine entries in a grid.
        The first line of the code assigns a value to the variable i.
        The next line of the code assigns a value to the variable j.
        The third line of the code appends an entry to the list of entries in self.gridEntry with an ID of root and borderwidth=2, width=3.
        The fourth line iterates through all nine lines and places each iteration's row number and column number into self.gridEntry[-1].
        This is done because there are nine iterations and -1 is used as a placeholder for iteration 0 (the last iteration).
        """
        for i in range(9):
            for j in range(9):
                self.gridEntry.append(
                    tk.Entry(self.root, borderwidth=2, width=3))
                self.gridEntry[-1].grid(row=i, column=j)

        return self.gridEntry

    def getGrid(self):
        """he code is trying to get the grid values.
        If an item is not found in the list, then it will return a '.'.
        Otherwise, it will return the value of that item.
        The code returns a list with all of the items in it and their respective values if they are found or else just a '.'
        for any other case.
        The code returns a list of strings, each string representing the value of the grid entry.
        The code is used to return a list of values from the grid.
        """
        self.gridValues = ['.' if not item.get()
                           else item.get() for item in self.gridEntry]
        return self.gridValues

    def solve_sudoku(self):
        """The code starts by creating a grid of 9x9 squares.
        The next line creates a canvas and sets it to the size of 300x300 pixels.
        Next, we create a text object that will display the values in our grid.
        Finally, we use search() to find all possible solutions for each row and column in our grid.
        The code creates a canvas with the dimensions of 300x300.
        The code then creates a grid on the canvas with 9 rows and 9 columns.
        The code then places text on the canvas to display the solved grid.
        """
        values = grid_values(self.getGrid())

        solvedgrid = search(values)

        x = 10
        y = 15
        canvas = tk.Canvas(self.root, width=350, height=400, bg="blue3")
        canvas.grid(row=11, column=0, columnspan=10, rowspan=9)
        for key, value in solvedgrid.items():
            canvas.create_text(x, y, text=value, width=3, fill="white")
            x += 40
            if x == 370:
                x = 10
                y += 30
        return canvas

    def perform(self):
        """The code starts by creating a new tk.Button object called "button" and setting its text to "Solve".
        The code then creates a function that will be executed when the button is clicked, which calls the solve_sudoku() function.
        This function sets up an empty grid with nine rows and columns in it, then adds the button to this grid at row 9, column 0.
        The main loop of the program starts here because we have not yet added any other code to it.
        The code attempts to create a button that when clicked, will call the function solve_sudoku() which will be defined in the following code.
        def solve_sudoku(): print('Solve') return True"""
        button = tk.Button(self.root, text='Solve',
                           command=lambda: self.solve_sudoku())
        button.grid(row=9, column=0, columnspan=9)

        self.root.mainloop()


if __name__ == '__main__':
    gui = GUI()
    gui.great()
    gui.createEntries()
    gui.perform()
