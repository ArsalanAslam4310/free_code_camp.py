def print_table(table):
    col_widths = [0] * len(table)

    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(col_widths[j]), end=' ')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]
print(print_table(table_data))
