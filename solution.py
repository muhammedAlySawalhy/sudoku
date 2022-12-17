from utilities import *


def search(values):
    "Using depth-first search and propagation, try all possible values."
    """The code is a function that uses depth-first search and propagation to try all possible values.
    The first step is to reduce the puzzle using the previous function, which takes in an array of integers as input and returns False if there are no solutions.
    If all of the boxes have only one value, then it's solved!
    Otherwise, choose one of the unfilled squares with the fewest possibilities (the min() function) by choosing n=min(len(boxes), s).
    Now use recurrence to solve each one of these resulting sudokus by calling this function on each element in new_sudoku.
    The code starts off by creating a list called values that contains all possible values for our puzzle.
    It then reduces this list down into smaller lists based on how many boxes we have left over from earlier reductions: values = reduce_puzzle(values) If there are still more than two boxes left over after reducing them down, then we'll need to find another solution for those remaining boxes.
    We do so by finding out what box has fewer numbers in it than any other box (using len()): if len(boxes) > 1: n, s = min((len(boxes
The code has a recursive function that will search through all the values in the list of boxes, and if it finds a solution, return True."""
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False  # Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values  # Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt
