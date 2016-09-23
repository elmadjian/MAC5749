import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

class Fourier():

    def __init__(self, g, L):
        self.g = g  #function
        self.L = L  #period

    def a_0(self):
        const = 1 / (2*self.L)
        integral = integrate.quad(self.g, -self.L, self.L)
        return integral[0] * const

    def a_n(self, n):
        const = 1 / self.L
        integral = integrate.quad(self._cos_integrand, -self.L, self.L, args=(n))
        return integral[0] * const

    def b_n(self, n):
        const = 1 / self.L
        integral = integrate.quad(self._sin_integrand, -self.L, self.L, args=(n))
        return integral[0] * const

    def _cos_integrand(self, t, n):
        g = self.g(t)
        cos = self._cos_npit(t, n)
        return g * cos

    def _sin_integrand(self, t, n):
        g = self.g(t)
        sin = self._sin_npit(t, n)
        return g * sin

    def _cos_npit(self, t, n):
        return np.cos((n * np.pi * t)/self.L)

    def _sin_npit(self, t, n):
        return np.sin((n * np.pi * t)/self.L)

    def build_g(self, t, n):
        a_0 = self.a_0()
        total_sum = 0
        for i in range(1, n+1):
            a_n = self.a_n(i)
            b_n = self.b_n(i)
            total_sum += a_n * self._cos_npit(t,i) + b_n * self._sin_npit(t,i)
        return a_0 + total_sum

#-------------------
def g_func(t):
    if -1 <= t < 1:
        return 1
    return 0


#--------------------
if __name__ == "__main__":
    F = Fourier(g_func, 2)
    x_list = np.arange(-1.5, 1.5, 0.01).tolist()
    y_list = []

    user_input = input("Enter the N for the Fourier series: ")
    while user_input != 'q':
        n = int(user_input)
        for i in x_list:
            y_list.append(F.build_g(i,n))
        plt.plot(x_list, y_list)
        plt.show()
        user_input = input("Enter the N for the Fourier series: ")
        plt.close('all')
        y_list = []
