from tkinter import *


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    def insert(self, value):
        if self.value:
            if value > self.value:
                if self.left_child is None:
                    self.left_child = BinaryTree(value)
                else:
                    self.left_child.insert(value)

            elif value < self.value:
                if self.right_child is None:
                    self.right_child = BinaryTree(value)
                else:
                    self.right_child.insert(value)
        else:
            self.value = value

    def get_tree(self, val_list):
        if self.left_child:
            self.left_child.get_tree(val_list)

        val_list.append(self.value)

        if self.right_child:
            self.right_child.get_tree(val_list)

    def get_children(self):
        parent = int(input('Insert parent value: '))

        val_array = []
        self.get_tree(val_array)

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

        val_array = []
        self.get_tree(val_array)

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
        val_array = []
        self.get_tree(val_array)

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
        val_array = []
        self.get_tree(val_array)
        tree_size = len(val_array)

        nodes_in_prev_layers = 2 ** (level - 1)
        nodes_in_next_layer = tree_size - nodes_in_prev_layers + 1

        if nodes_in_next_layer >= 2 ** (level - 2):
            return 0
        else:
            return 2 ** (level - 1) - nodes_in_next_layer
