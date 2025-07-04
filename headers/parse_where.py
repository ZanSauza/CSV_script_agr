import csv
import operator


def parse_where(file, column_name, cond, val):
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