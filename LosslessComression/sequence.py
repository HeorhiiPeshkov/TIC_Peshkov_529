import random
import string
import collections
import math
from enum import unique
from random import uniform
from numpy.ma.core import equal

N_sequence = 100

original_sequence1 = []
original_sequence2 = []
original_sequence3 = []
original_sequence4 = []
original_sequence5 = []
original_sequence6 = []
original_sequence7 = []
original_sequence8 = []

def original_sequence_1():
    list1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    list0 = []
    for i in range(0, 89):
        if i <= 89:
            list0.append(0)
            i += 1
        else:
            break
    list01 = list1 + [lisst for lisst in list0 if lisst not in list1]
    random.shuffle(list01)
    plist01 = ''.join(map(str, list01))
    random.shuffle(list01)
    unique_chars = set(list01)
    print(plist01)
    print(len(list01))
    print(len(unique_chars))
    original_sequence1.append(plist01)

def original_sequence_2():
    list1 = ["П", "є", "ш", "к", "о", "в"]
    list0 = []
    for i in range(0, N_sequence - len(list1)):
        if i <= N_sequence - len(list1):
                list0.append(0)
                i += 1
        else:
            break
    list01 = list1 + [lisst for lisst in list0 if lisst not in list1]
    plist01 = ''.join(map(str, list01))
    unique_chars = set(plist01)
    print(plist01)
    print(len(plist01))
    print(len(unique_chars))
    original_sequence2.append(plist01)

def original_sequence_3():
    list1 = ["П", "є", "ш", "к", "о", "в"]
    list0 = []
    for i in range(0, N_sequence - len(list1)):
        if i <= N_sequence - len(list1):
                list0.append(0)
                i += 1
        else:
            break
    list01 = list1 + [lisst for lisst in list0 if lisst not in list1]
    random.shuffle(list01)
    plist01 = ''.join(map(str, list01))
    unique_chars = set(plist01)
    print(plist01)
    print(len(plist01))
    print(len(unique_chars))
    original_sequence3.append(plist01)

def original_sequence_4():
    N_sequence = 100
    letters = ['П', 'є', 'ш', 'к', 'о', 'в', 5, 2, 9]
    len_letters = len(letters)
    repeats_letters = N_sequence/len_letters
    remainder_letters = N_sequence %len_letters
    list = letters * int(repeats_letters)
    list += letters[:remainder_letters]
    original_sequence_4 = ''.join(map(str,list))
    unique_chars = set(list)
    print(original_sequence_4)
    print(len(original_sequence_4))
    print(len(unique_chars))
    original_sequence4.append(original_sequence_4)

def original_sequence_5():
    list = ['П', 'є', 5, 2, 9]
    full_list = list * 20
    random.shuffle(full_list)
    print_list = ''.join(map(str,full_list))
    unique_chars = set(list)
    print(print_list)
    print(N_sequence)
    print(len(unique_chars))
    original_sequence5.append(print_list)

def original_sequence_6():
    letters = ['П', 'є']
    digits = [5, 2, 9]
    list100 = []
    n_letters = 70
    n_digits = 30
    for i in range(n_letters):
     list100.append(random.choice(letters))
    for i in range(n_digits):
     list100.append(random.choice(digits))
    random.shuffle(list100)
    print_list = ''.join(map(str, list100))
    unique_chars = set(list100)
    print(print_list)
    print(len(list100))
    print(len(unique_chars))
    original_sequence6.append(print_list)

def original_sequence_7():
    N_sequence = 100
    elements = string.ascii_lowercase + string.digits
    list100 = [random.choice(elements) for _ in range(N_sequence)]
    print_list = ''.join(map(str, list100))
    unique_chars = set(print_list)
    print(print_list)
    print(len(print_list))
    print(len(unique_chars))
    original_sequence7.append(print_list)

def original_sequence_8():
    N_sequence = 100
    one_list = []
    for i in range(0, N_sequence):
     if i <= N_sequence:
      one_list.append(1)
     else:
      break
    print_list = ''.join(map(str, one_list))
    unique_chars = set(print_list)
    print(print_list)
    print(len(print_list))
    print(len(unique_chars))
    original_sequence8.append(print_list)

original_sequence_1()
original_sequence_2()
original_sequence_3()
original_sequence_4()
original_sequence_5()
original_sequence_6()
original_sequence_7()
original_sequence_8()

original_sequences = [original_sequence1, original_sequence2, original_sequence3, original_sequence4, original_sequence5, original_sequence6, original_sequence7, original_sequence8]
for sequence in original_sequences:
    counts = collections.Counter(sequence)
    probability = {symbol: count/N_sequence for symbol, count in counts.items()}
    mean_probability = sum(probability.values())/len(probability)
    equal = all(abs(prob - mean_probability) < 0.05 * mean_probability for prob in probability.values())
    if equal:
        uniformity='Рівна'
    else:
        uniformity='Нерівна'
    entropy = -sum(p*math.log2(p) for p in probability.values())
    if unique_chars > 1:
        source_excess = 1 - entropy / math.log2(unique_chars)
    else:
        source_excess = 1
    probability_str = ', '.join([f"{symbol}={prob:.4f}" for symbol, prob in probability.items()])

