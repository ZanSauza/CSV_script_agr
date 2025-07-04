import csv
import operator


def parse_aggregate(file, column_name, cond, val):
    ops = {
        '=': operator.eq,
    }


    result =  [
        [val]
    ]

    count = 0

    val_list = []

    result_value = 0


    with open(file, 'r', encoding="utf-8") as csvfile:
        column_reader = csv.DictReader(csvfile, delimiter=";")
        try:
            if val == "avg":
                for row in column_reader:
                    cell_val = row[column_name]
                    cell = cell_value(cell_val)

                    result_value += cell
                    count += 1
                result_value /= count

                result.append([result_value])


            if val == "max":
                for row in column_reader:
                    cell_val = row[column_name]
                    cell = cell_value(cell_val)
                    if type(cell) == str:
                        raise TypeError
                    val_list.append(cell)


                result.append([max(val_list)])

            if val == "min":
                for row in column_reader:
                    cell_val = row[column_name]
                    cell = cell_value(cell_val)
                    if type(cell) == str:
                        raise TypeError
                    val_list.append(cell)

                result.append([min(val_list)])

            else:
                print(val)
                print('fssdffsd')

        except TypeError:
            print("Столбец должен иметь числовое значение!")
        except ValueError:
            print("неверное значение введите: avg, min или max")

    return result



def cell_value(cell_v):
    try:
        cell_v = float(cell_v)
    except ValueError:
        cell_v = cell_v

    return cell_v
