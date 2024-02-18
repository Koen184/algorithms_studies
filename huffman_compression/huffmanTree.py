class HuffmanCode:
    def __init__(self, probability, symbol=None,  left=None, right=None):
        self.probability = probability
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

    # inserting symbols into tree - building a tree
    @staticmethod
    def insertion(dictionary):
        nodes = [HuffmanCode(probability, symbol) for symbol, probability in dictionary.items()]
        while len(nodes) > 1:
            nodes.sort(key=lambda node: node.probability)

            left = nodes.pop(0)
            right = nodes.pop(0)

            parent = HuffmanCode(left.probability + right.probability, left=left, right=right)
            nodes.append(parent)

        return nodes[0]

    # counting probability for text
    @staticmethod
    def count_symbols(string):
        symbols_count = {}

        for symbol in string:
            if symbol in symbols_count:
                symbols_count[symbol] += 1
            else:
                symbols_count[symbol] = 1

        symbols_count = dict(sorted(symbols_count.items(), key=lambda item: item[1]))
        return symbols_count

    # counting probability for text from file
    @staticmethod
    def count_symbols_file(file_name):
        symbols_count = {}

        with open(file_name, 'r') as file:
            text = file.read()

            for symbol in text:
                if symbol in symbols_count:
                    symbols_count[symbol] += 1
                else:
                    symbols_count[symbol] = 1

        symbols_count = dict(sorted(symbols_count.items(), key=lambda item: item[1]))
        return symbols_count

    # create statistics for compression - size of text, taken bits by text and compressed code and rate between
    @staticmethod
    def compression_rate(file_name, code):

        with open(file_name, 'r') as file:
            text = file.read()

        size = len(text)

        bits_count_text = len(text) * 8
        bits_count_code = len(code)

        rate = (bits_count_code / bits_count_text) * 100
        rate = round(rate, 2)

        results = [size, bits_count_text, bits_count_code, rate]

        return results

    # creating codes for every symbol in tree
    def generate_codes(self):
        if self.left is not None:
            self.left.code = self.code + '0'
            self.left.generate_codes()

        if self.right is not None:
            self.right.code = self.code + '1'
            self.right.generate_codes()

    # displaying codes and probability for every symbol
    def show_codes(self):
        if self.symbol is not None:
            print(f"{self.symbol}: {self.code}, {self.probability}")

        if self.left is not None:
            self.left.show_codes()

        if self.right is not None:
            self.right.show_codes()

    # saving codes and probability for every symbol in array
    def save_codes_array(self, array):
        if self.symbol is not None:
            info = [self.symbol, self.code, self.probability]
            array.append(info)

        if self.left is not None:
            self.left.save_codes_array(array)

        if self.right is not None:
            self.right.save_codes_array(array)

        return array

    # encoding a text using created codes
    def encode(self, text):
        encoded_text = ""
        for symbol in text:
            node = self.find_node_by_symbol(symbol)
            encoded_text += node.code
        return encoded_text

    # encoding a text from file using created codes
    def encode_file(self, filename):
        encoded_text = ""
        with open(filename, "r") as file:
            text = file.read()
            for symbol in text:
                node = self.find_node_by_symbol(symbol)
                encoded_text += node.code
        return encoded_text

    # decoding a encoded text
    def decode(self, encoded_text):
        decoded_text = ""
        node = self
        for bit in encoded_text:
            if bit == '0':
                node = node.left
            elif bit == '1':
                node = node.right

            if node.symbol is not None:
                decoded_text += node.symbol
                node = self

        return decoded_text

    # auxiliary function - used in encode process
    def find_node_by_symbol(self, symbol):
        if self.symbol == symbol:
            return self

        node = None
        if self.left is not None:
            node = self.left.find_node_by_symbol(symbol)
        if node is None and self.right is not None:
            node = self.right.find_node_by_symbol(symbol)
        return node

    # not my code, only using to show bst to better understand how it works and looks
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.symbol
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.symbol
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.symbol
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.symbol
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    # end of not my code

# # TEST
#
# # text = 'Hello World!'
# # dict_symbols = HuffmanCode.count_symbols(text)
#
# dict_symbols = HuffmanCode.count_symbols_file('3_wersy.txt')
# print(dict_symbols)
#
# huffman_tree = HuffmanCode.insertion(dict_symbols)
#
# huffman_tree.display()
# huffman_tree.generate_codes()
# huffman_tree.show_codes()
#
# # Code
# # encoded_text = huffman_tree.encode(text)
# encoded_text = huffman_tree.encode_file('3_wersy.txt')
# print(encoded_text)
#
# # Compression rate
# results = HuffmanCode.compression_rate('3_wersy.txt', encoded_text)
# print(results)
#
# # Decode
# decoded_text = huffman_tree.decode(encoded_text)
# print(decoded_text)
