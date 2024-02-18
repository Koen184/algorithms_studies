from tkinter import *


class BinaryTree:
    def __init__(self, numbers):
        self.numbers = numbers
        self.build_heap()

    def build_heap(self):
        start_index = len(self.numbers) // 2 - 1
        end_index = len(self.numbers)

        nodes = range(start_index, -1, -1)

        for node in nodes:
            self.heapify(node, end_index)

    def heapify(self, parent_index, end_index):
        largest_index = parent_index
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2

        if left_child_index < end_index and self.numbers[left_child_index] > self.numbers[largest_index]:
            largest_index = left_child_index

        if right_child_index < end_index and self.numbers[right_child_index] > self.numbers[largest_index]:
            largest_index = right_child_index

        if largest_index != parent_index:
            self.swap(parent_index, largest_index)
            self.heapify(largest_index, end_index)

    def swap(self, i, j):
        self.numbers[i], self.numbers[j] = self.numbers[j], self.numbers[i]

    def get_tree(self):
        return self.numbers

    def get_children(self):
        parent = int(input('Insert parent value: '))

        val_array = self.get_tree()

        if parent in val_array:
            index = val_array.index(parent)
            children = []

            if 2 * index + 2 < len(val_array):
                children.append(val_array[2 * index + 1])
                children.append(val_array[2 * index + 2])
                print('Inserted value has two children: ', children)

            elif 2 * index + 1 < len(val_array):
                children.append(val_array[2 * index + 1])
                print('Inserted value has one child: ', children)

            else:
                print('Inserted value does not have children')
        else:
            print('Inserted value does not exist in the tree')

    def get_parent(self):
        child = int(input('Insert child value: '))

        val_array = self.get_tree()

        if child in val_array:
            index = val_array.index(child)

            if index % 2 == 0 and index != 0:
                parent = val_array[int((index - 2)/2)]
                print('Inserted value has parent: ', parent)

            elif index % 2 == 1:
                parent = val_array[int((index - 1)/2)]
                print('Inserted value has parent: ', parent)

            else:
                print('Value does not have parent - it is a root')
        else:
            print('Inserted value does not exist in the tree')

    def print_tree(self):
        val_array = self.get_tree()

        border_value = len(val_array)
        buffer_value = len(val_array)
        line = 1
        level = 0
        elements_in_line = 1
        index = 0

        # creating simple window
        window = Tk()
        window.title('Binary Tree')
        window.geometry('300x400')

        label = Label(window, text='Binary Tree:\n')
        label.pack()

        while index < border_value:
            missing = BinaryTree.calculate_full_layer_size(self, level)

            values = '  '.join(str(value) for value in val_array[index:index + elements_in_line])

            if missing > 0:
                values += '  ' + ('    ' * missing)

            buffer_value -= elements_in_line

            new_label = Label(window, text=values)
            new_label.pack()

            if buffer_value >= 0 and line >= elements_in_line:
                lines = '   '.join(['/ \\'] * line)

                new_label = Label(window, text=lines)
                new_label.pack()

            index += elements_in_line
            level += 1
            elements_in_line *= 2
            line *= 2

        window.mainloop()

    def calculate_full_layer_size(self, level):
        val_array = self.get_tree()
        tree_size = len(val_array)

        nodes_in_prev_layers = 2 ** level
        nodes_in_last_layer = tree_size - nodes_in_prev_layers

        if nodes_in_last_layer >= 2 ** level:
            return 0
        else:
            return 2 ** level - nodes_in_last_layer - 1
