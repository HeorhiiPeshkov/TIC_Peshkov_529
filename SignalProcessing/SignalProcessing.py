#номер варианта 11
import numpy as numpy
import scipy
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig

Fs = 1000
F_max = 23
cm = 1/2.54
a = 0 #середнє значення розподілу
b = 10.0 #стандартне відхилення розподілу
n = 500 #кількість згенерованих елементів чисел

y = numpy.random.normal(a, b, n)
x = numpy.arange(n)/Fs
w = F_max/(Fs/2)
parameters_filter = scipy.signal.butter(3, w, 'low', output='sos')
y = scipy.signal.sosfiltfilt(parameters_filter, y)
fig, ax = plt.subplots(figsize=(21*cm, 14*cm))
ax.plot(x, y, linewidth = 1)
ax.set_xlabel("Час(секунди)", fontsize=14)
ax.set_ylabel("Амплітуда сигналу", fontsize=14)
plt.title("Сигнал з максимальною частотою F_max=23")
plt.show()
fig.savefig("max_signal.jpeg")

spectrum = scipy.fft.fft(y)
symmetric_spectrum = numpy.abs(scipy.fft.fftshift(spectrum))
counts = scipy.fft.fftfreq(n, 1/n)
final_counts = scipy.fft.fftshift(counts)
figure, ax = plt.subplots(figsize=(21*cm, 14*cm))
ax.plot(final_counts,symmetric_spectrum, linewidth = 1)
ax.set_xlabel("Частота (Гц)", fontsize=14)
ax.set_ylabel("Амплітуда спектру", fontsize=14)
plt.title("Сигнал з максимальною частотою F_max=23")
plt.show()
figure.savefig("specter.jpeg")