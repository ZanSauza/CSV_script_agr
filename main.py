import argparse
import csv
import operator
from tabulate import tabulate



def create_table(file):
    table_1 = []

    with open(file, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            table_1.append(row)

    return table_1


def create_table_arg(data):
    table_2 = []

    for elems in data:
        if not table_2:
            table_2.append([key for key in elems.keys()])
            table_2.append([value for value in elems.values()])
        else:
            table_2.append([value for value in elems.values()])


    return table_2



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

    if file_path and not arg_filter:
        table_1 = create_table(file_path)
        print(tabulate(table_1, headers="firstrow", tablefmt="grid"))


    if arg_filter:
        filtered_rows = filter_values(arg_filter)
        parsed_columns = parse_columns(file_path, filtered_rows[0], filtered_rows[1], filtered_rows[2])

        table_2 = create_table_arg(parsed_columns)

        print(tabulate(table_2, headers="firstrow", tablefmt="grid"))





if __name__ == '__main__':
    main()