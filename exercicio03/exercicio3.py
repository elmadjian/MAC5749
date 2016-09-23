import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

class Fourier_Derivative():

    def __init__(self, y_list, T):
        self.f = y_list
        self.F = self._fourier_transform()
        self.T = T

    def derivative_f(self, degree):
        f_list = np.arange(len(self.F))/self.T
        f_list = self._D_a(f_list, degree) * self.F
        return self._inverse_fourier_transform(f_list)

    def _D_a(self, freq, a):
        return (2 * np.pi * 1j * freq)**a

    def _fourier_transform(self):
        F = fft.fft(self.f)
        return fft.fftshift(F)

    def _inverse_fourier_transform(self, f_list):
        f_list = fft.ifftshift(f_list)
        return fft.ifft(f_list)


#-----------------------
def func(a_0, a_1):
    return [i**4 for i in np.arange(a_0, a_1, 0.05)]


#------------------------
if __name__ == "__main__":
    y_list = func(-20, 20)
    F = Fourier_Derivative(y_list, len(y_list))
    plt.plot(y_list)
    plt.show()
    derivative = F.derivative_f(1)
    plt.plot(derivative)
    plt.show()
