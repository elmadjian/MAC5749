import numpy as np
import scipy.fftpack as fft
import matplotlib.pyplot as plt

class Fourier_Derivative():

    def __init__(self, y_list):
        self.f = y_list
        self.F = self._fourier_transform()

    def derivative_f(self, degree):
        f_list = []
        for f in range(len(self.F)):
            df = self._D_a(f, degree)
            f_list.append(df * self.F[f])
        return self._inverse_fourier_transform(f_list)

    def _D_a(self, freq, a):
        return (2 * np.pi * 1j * freq)**a

    def _fourier_transform(self):
        return fft.fft(self.f)

    def _inverse_fourier_transform(self, f_list):
        return fft.ifft(f_list)


#-----------------------
def func(a_0, a_1):
    return [i**2 for i in range(a_0, a_1)]


#------------------------
if __name__ == "__main__":
    y_list = func(-20, 20)
    F = Fourier_Derivative(y_list)
    plt.plot(y_list)
    plt.show()
    derivative = F.derivative_f(1)
    plt.plot(derivative)
    plt.show()
