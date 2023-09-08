import numpy
import math
from collections import defaultdict

def draw_plot(fn, x0, x1, x_step, y0, y1, y_step, rows, cols):
    """
    A method to print graph of mathematical function y = f(x) 
    of a single (real) variable using an ancient line printer.
    
    Attributes
    ----------
    fn : math function
        Mathmatical function that take x value and output y value
    x0 : int
        Lowest x coordinate
    x1 : int
        Highest x coordinate
    x_step : int
        number of step for x value to advance when insert to function
    y0 : int
        Lowest y coordinate
    y1 : int
        Highest y coordinate
    y_step : int
        number of step for y value to advance when check x in function
    row : int
        number of row that will print in output
    cols: int
        number of column that will print in output
    
    """
    coordinate = defaultdict(list)
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')
    for i in numpy.arange(x0, x1+x_step, x_step): # get all the x value that can insert to function
        
        for j in numpy.arange(y0, y1+y_step, y_step): # get all the y valye that is close to the fn(x)
            if abs(j-fn(i)) < 0.1:
                coordinate[round(j, 2)].append(round(i, 2)) # When y-fn(x) is close to precision of 0.1, add that to dictionary

                # Record min and max for x and y points for the function
                min_x = min(min_x, round(i, 2))
                min_y = min(min_y, round(j, 2))
                max_x = max(max_x, round(i, 2))
                max_y = max(max_y, round(j, 2))


    # Create a out_list for printing
    out_list = [["" for i in range(cols)] for j in range(rows)]

    # Get the range to move the x, y coordinate to cols row format
    y_range = max_y - min_y
    x_range = max_x - min_x

    # Sort the dictionary to make sure y start with highest number so it should appear at top
    for y, x in sorted(coordinate.items(), reverse=True):

        # We want to flip y as row 0 is the highest, the following will give for each row, at 
        # what position should be convert to * instead of empty string.
        # For instance, at row 0, index 57, 59, 61 should have * and every other range in col have
        # empty string 

        key = round((y_range*(rows-1) - (y+abs(min_y))*(rows-1))/y_range, 0)

        for value in (x+abs(min_x))*(cols-1)/x_range:

            out_list[int(key)][int(value)] = "*"
  

    return out_list

# Line function
def line(x): return x


def main():
    plot = draw_plot(math.sin, -math.pi, math.pi, math.pi/16, -1.1, 1.1, 0.1, 25, 80)
    
    # since the output is list, we want join the point to string and print them
    for points in plot:
        print(' '.join(points))
    
    # Same for line function
    plot = draw_plot(line, -10, 10, 0.1, -10, 10, 0.1, 25, 80)

    for points in plot:
        print(' '.join(points))

if __name__=="__main__":
    main()