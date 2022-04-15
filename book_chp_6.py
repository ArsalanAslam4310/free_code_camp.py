def largest_string(arr):
    max_length = 0
    max_index = 0
    for i in range(len(arr)):
        if len(arr[i]) > max_length:
            max_length = len(arr[i])
            max_index = i
    return arr[max_index]


def print_table(table):
    col_widths = [len(largest_string(x)) for x in table]

    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(col_widths[j]), end=' ')
        print()


table_data = [['apples', 'oranges', 'cherries', 'banana'], [
    'Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]
print(print_table(table_data))
