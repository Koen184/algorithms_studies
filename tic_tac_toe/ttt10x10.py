import tkinter as tk


# Create window
def create_window(window):
    window.title('Tick Tack Toe 10x10')
    window.geometry('600x880')

    # Create grid
    rows = 13
    columns = 10

    for row in range(rows):
        tk.Grid.rowconfigure(window, row, weight=1)

    for column in range(columns):
        tk.Grid.columnconfigure(window, column, weight=1)

    label_up = tk.Label(window, text="Insert 'x' or 'o' to start ^^", font=('Helvetica', 13, 'italic'), fg='#656363')
    label_up.grid(row=10, column=0, columnspan=10, sticky='nsew')

    label_down = tk.Label(window, font=('Helvetica', 18))
    label_down.grid(row=11, column=0, columnspan=10, sticky='nsew')

    # Create entry fields
    entry_fields = []

    button = tk.Button(window, text='Reset game', font=('Helvetica', 14), bg='#FCCACA',
                       command=lambda: clear_board(entry_fields, label_up, label_down))
    button.grid(row=12, column=0, columnspan=10)

    for row in range(10):
        for column in range(10):
            entry = tk.Entry(window)
            entry.grid(row=row, column=column, sticky='nsew')
            entry.configure(font=('Helvetica', 48), justify='center')
            entry.bind('<KeyRelease>',
                       lambda event, entry=entry: on_entry_change(event, entry, entry_fields, label_up, label_down))
            entry_fields.append(entry)


# I think the names of the functions are clear enough that they do not require additional comments
# In addition to the algorithms responsible for the operation of the game,
# they pass labels to each other in order to communicate with the players
def on_entry_change(event, entry, entry_fields, label_up, label_down):
    check_input(entry, entry_fields, label_up, label_down)


def check_input(entry, entry_fields, label_up, label_down):
    value = entry.get()

    if value == 'x':
        entry.configure(state="disabled")
        show_turn(label_up, value)
        check_win(entry_fields, label_down, label_up, 'x')
    elif value == 'o':
        entry.configure(state="disabled")
        show_turn(label_up, value)
        check_win(entry_fields, label_down, label_up, 'o')
    else:
        label_up.configure(text="Wrong marker, please pick 'x' or 'o'")
        entry.delete(0, tk.END)

    check_end(entry_fields, label_down)


def check_win(entry_fields, label1, label2, letter):
    for i in range(0, 91, 10):
        flag = 0
        for j in range(10):
            if entry_fields[i + j].get() == letter:
                flag += 1

                if flag == 5:
                    label1.configure(text='The winner is: ' + letter + ' !')
                    label2.configure(text="It's end of the game")
                    block_board(entry_fields)
                    break

            else:
                flag = 0

    for i in range(10):
        flag = 0
        for j in range(0, 91, 10):
            if entry_fields[i + j].get() == letter:
                flag += 1

                if flag == 5:
                    label1.configure(text='The winner is: ' + letter + ' !')
                    label2.configure(text="It's end of the game")
                    block_board(entry_fields)
                    break
            else:
                flag = 0

    flag = 0
    for i in range(6):
        for j in range(6):
            if all(entry_fields[(i + k) * 10 + j + k].get() == letter for k in range(5)):
                flag = 1
                break
        if flag == 1:
            break

    if flag == 0:
        for i in range(9, 3, -1):
            for j in range(6):
                if all(entry_fields[(i - k) * 10 + j + k].get() == letter for k in range(5)):
                    flag = 1
                    break
            if flag == 1:
                break

    if flag == 1:
        label1.configure(text='The winner is: ' + letter + ' !')
        label2.configure(text="It's end of the game")
        block_board(entry_fields)


def check_end(entry_fields, label):
    for entry in entry_fields:
        if entry.get() == '':
            return False
    label.configure(text='No ones win - tie :c')


def clear_board(entry_fields, label1, label2):
    for entry in entry_fields:
        entry.configure(state='normal')
        entry.delete(0, tk.END)

    label1.configure(text='')
    label2.configure(text='')


def block_board(entry_fields):
    for entry in entry_fields:
        entry.configure(state="disabled")


def show_turn(label, letter):
    if letter == 'x':
        label.configure(text="It's now 'o' turn")
    elif letter == 'o':
        label.configure(text="It's now 'x' turn")


# MAIN
window = tk.Tk()
create_window(window)

window.mainloop()