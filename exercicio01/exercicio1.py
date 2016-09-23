# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

class Function():
    '''
    Dictionary for function parameters:

    a0: start
    a1: end
    step: discrete step used between real values
    k: theta multiplier parameter for sine function

    **important**: subfunctions are plotted from a0 to (a1-step)
    '''

    def __init__(self, step):
        self.step = step
        self.x = []
        self.y = []

    def add_ramp(self, a0, a1):
        x_list = np.arange(a0, a1, self.step).tolist()
        k = 1/len(x_list)
        y_list = [k*(i+1)-k for i in range(len(x_list))]
        self.x += x_list
        self.y += y_list

    def add_plateau(self, a0, a1):
        x_list = np.arange(a0, a1, self.step).tolist()
        y_list = [1/(a1-a0) for i in x_list]
        self.x += x_list
        self.y += y_list

    def add_sin(self, a0, a1, k=1.0):
        x_list = np.arange(a0, a1, self.step).tolist()
        y_list = [np.sin(k*x) for x in x_list]
        self.x += x_list
        self.y += y_list

    def add_pulse(self, a0):
        self.x += [a0]
        self.y += [1.0]

    def add_flat(self, a0, a1):
        x_list = np.arange(a0, a1, self.step).tolist()
        y_list = [0.0 for i in x_list]
        self.x += x_list
        self.y += y_list

    def clear_function(self):
        self.function = {'x': [], 'y': []}


class Plotter():
    '''
    Plots either:
    - a function as itself
    - a convolution between two 1-D functions
    - a correlation between two 1-D functions
    '''

    def __init__(self):
        pass

    def plot_function(self, function):
        plt.plot(function.x, function.y)
        plt.show()

    def plot_convolution(self, g, h):
        y_list = np.convolve(g.y, h.y)
        x_list = np.arange(0, len(y_list)/10.0, 0.1).tolist()
        plt.plot(x_list, y_list)
        plt.show()

    def plot_correlation(self, g, h):
        y_list = np.correlate(g.y, h.y, "full")
        x_list = np.arange(0, len(y_list)/10.0, 0.1).tolist()
        plt.plot(x_list, y_list)
        plt.show()


'''
main program
------------
Testing multiple combinations:-)
'''

if __name__ == "__main__":
    #creating signals
    #================

    #creating signal h
    h = Function(0.1)
    h.add_flat(0, 1)
    h.add_pulse(1)
    h.add_flat(1.1, 2)
    h.add_pulse(2)
    h.add_flat(2.1, 4)
    h.add_plateau(4, 6)
    h.add_flat(6, 7)
    h.add_ramp(7, 9)
    h.add_flat(9, 12)
    h.add_sin(12, np.pi*2 + 10.9, 3)
    h.add_flat(np.pi*2 + 11, 18)

    #creating signal g1
    g1 = Function(0.1)
    g1.add_ramp(0, 2)
    g1.add_flat(2, 18)

    #creating signal g2
    g2 = Function(0.1)
    g2.add_flat(0, 0.2)
    g2.add_plateau(0.2, 2.2)
    g2.add_flat(2.2, 18)

    #creating signal g3
    g3 = Function(0.1)
    g3.add_flat(0, 0.1)
    g3.add_pulse(0.1)
    g3.add_flat(0.2, 18)

    #creating signal g4
    g4 = Function(0.1)
    g4.add_sin(0, np.pi*2, 3)
    g4.add_flat(np.pi*2 + 0.1, 18)


    #plotting signals
    #================
    plotter = Plotter()
    plotter.plot_function(h)
    plotter.plot_function(g1)
    plotter.plot_function(g2)
    plotter.plot_function(g3)
    plotter.plot_function(g4)

    #plotting convolutions
    plotter.plot_convolution(h, g1)
    plotter.plot_convolution(g1, h)
    plotter.plot_convolution(h, g2)
    plotter.plot_convolution(g2, h)
    plotter.plot_convolution(h, g3)
    plotter.plot_convolution(g3, h)
    plotter.plot_convolution(h, g4)
    plotter.plot_convolution(g4, h)

    #plotting correlations
    plotter.plot_correlation(h, g1)
    plotter.plot_correlation(g1, h)
    plotter.plot_correlation(h, g2)
    plotter.plot_correlation(g2, h)
    plotter.plot_correlation(h, g3)
    plotter.plot_correlation(g3, h)
    plotter.plot_correlation(h, g4)
    plotter.plot_correlation(g4, h)
