import argparse
import csv
import operator
from tabulate import tabulate

def create_table(data):
    table = []

    for elems in data:
        if not table:
            table.append([key for key in elems.keys()])
            table.append([value for value in elems.values()])
        else:
            table.append([value for value in elems.values()])






    return table



def parse_columns(file, column_name, cond, val):
    ops = {
        '>': operator.gt,
        '>=': operator.ge,
        '<': operator.lt,
        '<=': operator.le,
        '=': operator.eq,
        '!=': operator.ne
    }

    try:
        val = float(val)
    except ValueError:
        pass

    result = []
    with open(file, 'r', encoding="utf-8") as csvfile:
        column_reader = csv.DictReader(csvfile, delimiter=";")
        for row in column_reader:
            cell_val = row[column_name]

            try:
                cell_val = float(cell_val)
            except ValueError:
                cell_val = cell_val

            if cond in ops:
                if ops[cond](cell_val, val):
                    result.append(row)


    return result



def filter_values(filter_value):
    column = ""
    condition = ""
    value = ""

    for i in filter_value:
        if i.isalpha() and condition == "":
            column+=i
        if not i.isalpha() and not i.isdigit():
            condition+=i
        if (i.isalpha() or i.isdigit()) and condition != "":
            value+=i

    return column, condition, value






def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str)
    parser.add_argument('--where',  type=str)

    args = parser.parse_args()

    file_path = args.file
    arg_filter = args.where


    filtered_rows = filter_values(arg_filter)

    parsed_columns = parse_columns(file_path, filtered_rows[0], filtered_rows[1], filtered_rows[2])

    table = create_table(parsed_columns)

    print(tabulate(table, headers="firstrow", tablefmt="grid"))


    # print(parsed_columns)
    #
    # print("----------------------------------------")
    #
    # print("----------------------------------------")
    # print(table)

    # print(parsed_columns)




    return filtered_rows



if __name__ == '__main__':
    main()