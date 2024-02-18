from huffmanTree import HuffmanCode
from matplotlib import pyplot as plt
from tabulate import tabulate
import time

# creating lists of files names
files_names = ['1_wers.txt', '3_wersy.txt', '10_wersow.txt', '25_wersow.txt', '50_wersow.txt']

# creating list of results
results_all = []
results_time_code = []
results_time_decode = []

# the main loop of the algorithm
for file in files_names:
    dict_symbols = HuffmanCode.count_symbols_file(file)
    huffman_tree = HuffmanCode.insertion(dict_symbols)

    start = time.perf_counter_ns()
    huffman_tree.generate_codes()
    encoded_text = huffman_tree.encode_file(file)
    finish = time.perf_counter_ns()
    results_time_code.append(round((finish - start) / 1_000_000_000, 5))

    results_all.append(HuffmanCode.compression_rate(file, encoded_text))

    codes = []
    headers = ['Symbol', 'Code', 'Probability']

    huffman_tree.save_codes_array(codes)

    with open('results_' + file, 'w') as result_file:
        result_file.write(tabulate(codes, headers=headers))

    start = time.perf_counter_ns()
    huffman_tree.decode(encoded_text)
    finish = time.perf_counter_ns()
    results_time_decode.append(round((finish - start) / 1_000_000_000, 5))

    print('Performed compression for :', files_names[files_names.index(file)])


print(results_all)
print(results_time_code)
print(results_time_decode)


# creating first graph
plt.subplot(1, 3, 1)

plt.plot([value[0] for value in results_all], [value[1] for value in results_all],
         label='Before compression', color='#E39DE3')
plt.plot([value[0] for value in results_all], [value[2] for value in results_all],
         label='After compression', color='#A8EAFC')

# editing the graph
plt.title('Taken bits before and after compression')
plt.xlabel('Size of text')
plt.ylabel('Taken bits')
plt.legend()


# creating second graph
plt.subplot(1, 3, 2)

plt.plot([value[0] for value in results_all], results_time_code,
         label='Compression', color='#E39DE3')
plt.plot([value[0] for value in results_all], results_time_decode,
         label='Decompression', color='#A8EAFC')

# editing the graph
plt.title('Time used to compression and decompression')
plt.xlabel('Size of text')
plt.ylabel('Time [s]')
plt.legend()


# creating third graph
plt.subplot(1, 3, 3)

plt.plot([value[0] for value in results_all], [value[3] for value in results_all],
         label='Compression rate', color='#E39DE3')

# editing the graph
plt.title('Compression rate')
plt.xlabel('Size of text')
plt.ylabel('Compression rate [%]')
plt.ylim((0, 100))
plt.legend()


# showing the graph
plt.show()

