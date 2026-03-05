#номер варианта 11
import numpy as numpy
import scipy
import matplotlib.pyplot as plt
# from matplotlib.pyplot import savefig

Fs = 1000
F_max = 23
cm = 1/2.54
a = 0 #середнє значення розподілу
b = 10.0 #стандартне відхилення розподілу
n = 500 #кількість згенерованих елементів чисел
F_filter = 30

y = numpy.random.normal(a, b, n)
x = numpy.arange(n)/Fs
w = F_max/(Fs/2)
parameters_filter = scipy.signal.butter(3, w, 'low', output='sos')
y = scipy.signal.sosfiltfilt(parameters_filter, y)
# fig, ax = plt.subplots(figsize=(21*cm, 14*cm))
# ax.plot(x, y, linewidth = 1)
# ax.set_xlabel("Час(секунди)", fontsize=14)
# ax.set_ylabel("Амплітуда сигналу", fontsize=14)
# plt.title("Сигнал з максимальною частотою F_max=23")
# plt.show()
# fig.savefig("max_signal.jpeg")

# spectrum = scipy.fft.fft(y)
# symmetric_spectrum = numpy.abs(scipy.fft.fftshift(spectrum))
# counts = scipy.fft.fftfreq(n, 1/n)
# final_counts = scipy.fft.fftshift(counts)
# figure, ax = plt.subplots(figsize=(21*cm, 14*cm))
# ax.plot(final_counts,symmetric_spectrum, linewidth = 1)
# ax.set_xlabel("Частота (Гц)", fontsize=14)
# ax.set_ylabel("Амплітуда спектру", fontsize=14)
# plt.title("Сигнал з максимальною частотою F_max=23")
# plt.show()
# figure.savefig("specter.jpeg")

discrete_signals = []
discrete_spectrums = []
f_r_parameters = []
var_signal_varriance = []
varriences = []
corrs = []
for Dt in [2, 4, 8, 16]:
    discrete_signal = numpy.zeros(n)
    for i in range(0, round(n/Dt)):
        discrete_signal[i*Dt]=y[i*Dt]
    discrete_signals.append(list(discrete_signal))
    discrete_spectrum = scipy.fft.fft(discrete_signal)
    symmetric_spectrum = numpy.abs(scipy.fft.fftshift(discrete_spectrum))
    discrete_spectrums.append(list(symmetric_spectrum))
    discrete_counts = scipy.fft.fftfreq(n, 1/n)
    final_discrete_counts = scipy.fft.fftshift(discrete_counts)
    w = F_filter / (Fs / 2)
    r_parameter = scipy.signal.butter(3, w, 'low', output='sos')
    f_r_parameter = scipy.signal.sosfiltfilt(r_parameter, discrete_signal)
    f_r_parameters.append(list(f_r_parameter))
    E1 = f_r_parameters - y
    variance_E = numpy.var(E1)
    varriences.append(variance_E)
    print(varriences)
    corr = numpy.var(y)/numpy.var(E1)
    corrs.append(corr)

x = [2, 4, 8, 16]
fig, ax = plt.subplots(figsize=(21*cm, 14*cm))
ax.plot(x, corrs, linewidth = 1)
ax.set_xlabel("Крок дискретизації", fontsize=14)
ax.set_ylabel("ССШ", fontsize=14)
plt.title("Залежність співвідношення сигнал-шум від кроку дискретизації")
plt.show()
fig.savefig("correlation2.jpeg")




# fig, ax = plt.subplots(2, 2, figsize=(21*cm, 14*cm))
# s = 0
# for i in range(0, 2):
#     for j in range(0, 2):
#         ax[i][j].plot(x, f_r_parameters[s], linewidth=1)
#         s+=1
# fig.supxlabel("Амплітуда сигналу", fontsize = 14)
# fig.supylabel("Час(секунди)", fontsize = 14)
# fig.suptitle("Сигнал з кроком дискретизації Dt=(2,4,8,16)")
# fig.set_dpi(600)
# fig.savefig("return_discrete.jpeg")
# fig.show()


# figure, ax = plt.subplots(2, 2, figsize=(21*cm, 14*cm))
# ax.plot(final_discrete_counts,symmetric_spectrum, linewidth = 1)
# ax.set_xlabel("Частота (Гц)", fontsize=14)
# ax.set_ylabel("Амплітуда спектру", fontsize=14)
# plt.title("Сигнал з максимальною частотою F_max=23")
# plt.show()
# figure.savefig("specter.jpeg")

# fig, ax = plt.subplots(2, 2, figsize=(21*cm, 14*cm))
# s = 0
# for i in range(0, 2):
#     for j in range(0, 2):
#         ax[i][j].plot(final_discrete_counts, discrete_spectrums[s], linewidth=1)
#         s+=1
# fig.supxlabel("Амплітуда сигналу", fontsize = 14)
# fig.supylabel("Час(секунди)", fontsize = 14)
# fig.suptitle("Сигнал з кроком дискретизації Dt=(2,4,8,16)")
# fig.set_dpi(600)
# fig.savefig("WithDt_specter.png")
# fig.show()


# fig, ax = plt.subplots(2, 2, figsize=(21*cm, 14*cm))
# s = 0
# for i in range(0, 2):
#     for j in range(0, 2):
#         ax[i][j].plot(x, discrete_spectrums[s], linewidth=1)
#         s+=1
# fig.supxlabel("Амплітуда сигналу", fontsize = 14)
# fig.supylabel("Час(секунди)", fontsize = 14)
# fig.suptitle("Сигнал з кроком дискретизації Dt=(2,4,8,16)")
# fig.set_dpi(600)
# # fig.savefig("WithDt.png")
# fig.show()

# ax.plot(x, discrete_signals, linewidth = 1)
# ax.set_xlabel("Час(секунди)", fontsize=14)
# ax.set_ylabel("Амплітуда сигналу", fontsize=14)
# plt.title("Сигнал з максимальною частотою F_max=23")
# plt.show()