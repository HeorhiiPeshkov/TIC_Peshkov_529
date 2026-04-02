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

# discrete_signals = []
# discrete_spectrums = []
# f_r_parameters = []
# var_signal_varriance = []
# varriences = []
# corrs = []
# for Dt in [2, 4, 8, 16]:
#     discrete_signal = numpy.zeros(n)
#     for i in range(0, round(n/Dt)):
#         discrete_signal[i*Dt]=y[i*Dt]
#     discrete_signals.append(list(discrete_signal))
#     discrete_spectrum = scipy.fft.fft(discrete_signal)
#     symmetric_spectrum = numpy.abs(scipy.fft.fftshift(discrete_spectrum))
#     discrete_spectrums.append(list(symmetric_spectrum))
#     discrete_counts = scipy.fft.fftfreq(n, 1/n)
#     final_discrete_counts = scipy.fft.fftshift(discrete_counts)
#     w = F_filter / (Fs / 2)
#     r_parameter = scipy.signal.butter(3, w, 'low', output='sos')
#     f_r_parameter = scipy.signal.sosfiltfilt(r_parameter, discrete_signal)
#     f_r_parameters.append(list(f_r_parameter))
#     E1 = f_r_parameters - y
#     variance_E = numpy.var(E1)
#     varriences.append(variance_E)
#     print(varriences)
#     corr = numpy.var(y)/numpy.var(E1)
#     corrs.append(corr)
#
# x = [2, 4, 8, 16]
# fig, ax = plt.subplots(figsize=(21*cm, 14*cm))
# ax.plot(x, corrs, linewidth = 1)
# ax.set_xlabel("Крок дискретизації", fontsize=14)
# ax.set_ylabel("ССШ", fontsize=14)
# plt.title("Залежність співвідношення сигнал-шум від кроку дискретизації")
# plt.show()
# fig.savefig("correlation2.jpeg")


q_signals_array = [] #збереження квантованих сигналів
varrience_array = [] #збереження значень дисперсії
q_levels = []
correlation_array = [] #значення співвідношення сигнал-шум
for M in [4, 16, 64, 256]:
    bits_array = [] #змінна для збереження бітів
    signal_from_bits_array = [] #змінна для збереження сигналу сформованого з бітів
    delta = (numpy.max(y) - numpy.min(y))/(M-1) #крок квантування
    quantize_signal = delta * numpy.round(y/delta) #отриманий цифровий сигнал
    q_signals_array.append(quantize_signal)
    quantize_levels = numpy.arange(numpy.min(quantize_signal), numpy.max(quantize_signal)+1, delta) #список дискретних відліків амплітуди сигналу з кроком delta
    q_levels.append(quantize_levels)
    quantize_bit = numpy.arange(0, M) #діапазон генерації
    quantize_bit = [format(bits_array, '0' + str(int(numpy.log(M)/numpy.log(2))) + 'b') for bits_array in quantize_bit] #
    quantize_table = numpy.c_[quantize_levels[:M], quantize_bit[:M]]
    fig,ax = plt.subplots(figsize=(14/2.54, M/2.54))
    table = ax.table(cellText=quantize_table, colLabels=["Значення сигналу", "Кодова послідовність"], loc='center')
    table.set_fontsize(14)
    table.scale(1,2)
    ax.axis('off')
    fig.savefig(f'Table{M}', dpi=600)
    # plt.plot(varrience_array, len(q_levels))
    # plt.show()
    for signal_value in quantize_signal:
        for index, value, in enumerate(quantize_levels[:M]):
            if numpy.round(numpy.abs(signal_value - value), 0) == 0:
                bits_array.append(quantize_bit[index])
                break
    bits_array = [int(item) for item in list(''.join(bits_array))]
    fig, ax = plt.subplots(figsize=(21/2.54, 14/2.54))
    x = numpy.arange(0, len(bits_array))
    ax.step(x, bits_array, linewidth=0.1)
    fig.savefig(f'Sequence{M}')
    # E2 = quantize_signal - y
    # varr = numpy.var(E2)
    # varrience_array.append(varr)
    # corre = numpy.var(y)/numpy.var(E2)
    # correlation_array.append(corre)
    # fig, axes = plt.subplots(2, 2, figsize=(21*cm, 14*cm))
#     axes.plot(M, )
#
# M_list = [4, 16, 64, 256]
# M1 = 0
# figure, ax = plt.subplots(2, 2, figsize=(21/2.54, 14/2.54))
# for i in range(0, 2):
#     for j in range(0, 2):
#         ax[i][j].plot(numpy.arange(500) / 1000, q_signals_array[M1], linewidth=1)
#         M1+=1
# figure.suptitle("Цифрові сигнали з рівнями квантування (4, 16, 64, 256)")
# figure.supxlabel("Час(секунди)")
# figure.supylabel("Амплітуда сигналу")
# figure.show()
# figure.savefig("signals_with_levels")

# M = [4, 16, 64, 256]
# fig, ax = plt.subplots(figsize=(21*cm, 14*cm))
# ax.plot(M, varrience_array, linewidth = 1)
# ax.set_xlabel("Кількість рівнів квантування", fontsize=14)
# ax.set_ylabel("Дисперсія", fontsize=14)
# plt.title("Залежність дисперсії від кількості рівнів квантування")
# plt.show()
# fig.savefig("var_lvl.jpeg")

# M = [4, 16, 64, 256]
# fig, ax = plt.subplots(figsize=(21*cm, 14*cm))
# ax.plot(M, correlation_array, linewidth = 1)
# ax.set_xlabel("Кількість рівнів квантування", fontsize=14)
# ax.set_ylabel("ССШ", fontsize=14)
# plt.title("Залежність співвідношення сигнал-шум від кількості рівнів квантування")
# plt.show()
# fig.savefig("correlation42.jpeg")


# for signal_value in quantize_signal:
#     for index, value, in enumerate(quantize_levels[:M]):
#         if numpy.round(numpy.abs(signal_value - value), 0) == 0:
#             bits_array.append(quantize_bit[index])
#             break
# bits_array = [int(item) for item in list(''.join(bits_array))]
# fig, ax = plt.subplots(figsize=(21/2.54, 14/2.54))
# x = numpy.arange(0, len(bits_array))
# ax.step(x, bits_array, linewidth=0.1)
# fig.savefig('Sequence')
