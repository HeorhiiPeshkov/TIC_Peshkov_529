import collections
import math
import matplotlib.pyplot as plt

N_sequence = 100

with open("sequence.txt", "r") as file:
    lines = file.readlines()
    original_sequences = [sequence.strip("\n") for sequence in lines]


def encode_rle(sequence):
    count = 1
    result = []
    for i in range(len(sequence)):
        if i == 0:
            continue
        if sequence[i] == sequence[i - 1]:
            count += 1
        else:
            result.append((sequence[i - 1], count))
            count = 1
    result.append((sequence[len(sequence) - 1], count))
    encoded = []
    for item in result:
        encoded.append(f"{item[1]}{item[0]}")
    return "".join(encoded), result


def decode_rle(sequence):
    decode_result = []
    for item in sequence:
        decode_result.append(item[0] * item[1])
    return "".join(decode_result)


def encode_lzw(sequence):
    result = []
    dictionary = {}
    total = 0
    for i in range(65536):
        dictionary[chr(i)] = i
    current = ""
    for c in sequence:
        new_str = current + c
        if new_str in dictionary:
            current = new_str
        else:
            result.append(dictionary[current])
            dictionary[new_str] = len(dictionary)
            element_bits = 16 if dictionary[current] < 65536 else math.ceil(math.log2(len(dictionary)))
            current = c
            with open("results_rle_lzw.txt", "a+", encoding="utf-8") as file:
                file.write(f"Code: {dictionary[current]}, Element: {current}, bits: {element_bits}\n")
            file.close()
            total = total + element_bits
    last_bits = 16 if dictionary[current] < 65536 else math.ceil(math.log2(len(dictionary)))
    total = total + last_bits
    result.append(dictionary[current])
    with open("results_rle_lzw.txt", "a+", encoding="utf-8") as file:
        file.write(f"Code: {dictionary[current]}, Element: {current}, Bits: {last_bits}\n")
        # file.write(f"Закодована LZW послідовність: {''.join(map(str, result))}\n")
        # file.write(f"Розмір закодованої LZW послідовності: {total} bits\n")
    file.close()
    if total > 0:
        compression_ratio_LZW = round((len(sequence) * 16 / total), 2)
    else:
        compression_ratio_LZW = 0
    return result, total, compression_ratio_LZW, dictionary


def decode_lzw(encode_sequence):
    dictionary = {}
    for i in range(65536):
        dictionary[i] = chr(i)
    result = ""
    previous = None
    for code in encode_sequence:
        if code in dictionary:
            current = dictionary[code]
            result += current
            if previous is not None:
                dictionary[len(dictionary)] = previous + current[0]
            previous = current
        else:
            current = previous + previous[0]
            result += current
            dictionary[len(dictionary)] = current
            previous = current
    return result


i = 1
results = []
with open("results_rle_lzw.txt", "w", encoding="utf-8") as results_rle_lzw:
    for sequence in original_sequences:
        print('----------')
        print(f'Ітерація циклу: {i}')
        i += 1
        counts = collections.Counter(sequence)
        probability = {symbol: count / len(sequence) for symbol, count in counts.items()}
        entropy = -sum(p * math.log2(p) for p in probability.values())
        print(f"Послідовність {sequence}")
        print(f"Кількість відліків {counts}")
        print(f"Ймовірність послідовності {probability}")
        print(f"Ентропія {entropy}")
        encoded_sequence, encoded = encode_rle(sequence)
        print(f"Закодована послідовність {encoded}")
        CR1 = len(sequence) / len(encoded_sequence)
        CR2 = (1 - (len(encoded_sequence) / len(sequence))) * 100
        print(f"Ефективність стиснення {CR1}")
        print(f"Ефективність стиснення {CR2} у відсотках")
        compression_ratio_RLE = round((len(sequence) / len(encoded_sequence)), 2)
        if compression_ratio_RLE < 1:
            compression_ratio_RLE = '-'
        else:
            compression_ratio_RLE = compression_ratio_RLE
        print(f"Результат стиснення RLE{compression_ratio_RLE}")
        print_decode_rle = decode_rle(encoded)
        with open("results_rle_lzw.txt", "a+", encoding="utf-8") as results_rle_lzw:
            results_rle_lzw.write("//////////////////////////////////////////\n")
            results_rle_lzw.write(f"Оригінальна послідовність: {sequence}\n")
            results_rle_lzw.write(f"Розмір оригінальної послідовності: {len(sequence) * 16} bits\n")
            results_rle_lzw.write(f"Ентропія: {round(entropy, 4)}\n")
            results_rle_lzw.write("___________Кодування RLE___________\n")
            results_rle_lzw.write(f"Закодована послідовність: {encoded_sequence}\n")
            results_rle_lzw.write(f"Розмір закодованої послідовності: {len(encoded_sequence)} bits\n")
            results_rle_lzw.write(f"Декодована: {decode_rle(encoded)}\n")
            results_rle_lzw.write(f"Коефіцієнт стиснення RLE: {compression_ratio_RLE}\n")
            results_rle_lzw.write("___________Кодування LZW___________\n")
            # compression_ratio_LZW = encode_lzw(sequence)
        results_rle_lzw.close()
        lzw_encoded, lzw_size, compression_ratio_LZW, lzw_dict = encode_lzw(sequence)
        results.append([round((entropy), 2), compression_ratio_RLE, compression_ratio_LZW])

        with open("results_rle_lzw.txt", "a+", encoding="utf-8") as results_rle_lzw:
            # results_rle_lzw.write(f"Словник: {lzw_dict}\n")
            results_rle_lzw.write(f"Закодована послідовність: {"".join(map(str, lzw_encoded))}\n")
            results_rle_lzw.write(f"Розмір закодованої: {lzw_size} bits\n")
            results_rle_lzw.write(f"Декодована: {decode_lzw(lzw_encoded)}\n")
            results_rle_lzw.write(f"Коефіцієнт стиснення LZW: {compression_ratio_LZW}\n\n")
        results_rle_lzw.close()

fig, ax = plt.subplots(figsize=(14 / 1.54, len(results) / 1.54))
headers = ['Ентропія', 'КС RLE', 'КС LZW']
row = [f'Послідовність {i + 1}' for i in range(len(results))]
ax.axis('off')
table = ax.table(cellText=results, colLabels=headers, rowLabels=row,
                 loc='center', cellLoc='center')
table.set_fontsize(14)
table.scale(0.8, 2)
fig.savefig("TableResults.png")
plt.show()
