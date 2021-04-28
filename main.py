import matplotlib.pyplot as plt
import numpy as np
import random

def find_fix_point(a, x0):
    for i in range(0, 100): # As the convergence point can be approximated after 100 iterations, a for loop which loops through the equation above 100 times is set up
        x = a * x0 * (1 - x0)
        x0 = x

    return x # The function returns the convergence point, x


def scatterPlot(a_init, a_final):  # This has been done as a function as later questions require the same code with different arguments to be ran
    a_vls = np.linspace(a_init, a_final, 1000)  # The a_vls array generates 1000 equally spaced data points between the given initial and final value
    x_vls = [random.uniform(0, 1) for x in range(50)]  # The elements in x_vls are randomly generated using list comprehension
    x_star = np.zeros((50, 1000))  # A 0 matrix with 50 rows and 1000 columns is created to store all x* values; every row corresponds to a different x_0 value and every column is a different a value
    star_lst = []  # star_lst will be used to temporarily hold the x* values

    i = 0  # i is initialised as 0 and will serve as a counter variable

    for x in x_vls:  # The nested for loop ensure that initially the code loops through every one of the 50 x values, but then for each one of those it loops through the a values first. This is done because x* is effectively a multivariable function of both a and x_0. By nesting the loops, one of those variables (x) is made constant, which is helpful as the graph to be plotted will be x*(a, x_0) vs a.
        for a in a_vls:
            star_lst.append(find_fix_point(a, x))  # Finds the convergence point for the given a and x_0 values it is looping though and then appends it to the star_lst list

        x_star[i] = star_lst  # After all 1000 x* values have been found for a fixed x_0 value, they are used to replace the i-th row of the x_star array

        star_lst = []  # The star_lst is cleared, to avoid dimensional errors and/or duplication of rows
        i += 1  # The counter is increased by 1

    for row in x_star:
        plt.plot(a_vls, row, 'o', markersize=0.2, color='b')  # The graph of x* vs a is then plotted

    plt.xlabel('Growth rate')  # And the axes labelled
    plt.ylabel('Convergence point')

    plt.grid()

    plt.show()


scatterPlot(1.5, 4)