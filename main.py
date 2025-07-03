import argparse
from tabulate import tabulate


def filter_table(table, column_name, filter_value):
    try:
        column_index = table[0].index(column_name)
    except ValueError:
        print(f"Ошибка: Столбец с именем '{column_name}' не найден в таблице.")
        return []

    filtered_rows = [row for row in table[1:] if row[column_index] == filter_value]
    return filtered_rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str)
    parser.add_argument('--where',  type=str)


    args = parser.parse_args()

    file_path = args.file

    arg_filter = args.where

    data = []

    with open(file_path, 'r', encoding="utf-8") as f:
        content = f.readlines()
        for i in content:
            data.append(i.split(";"))

    filtered_rows = filter_table(data, args.where)

    if filtered_rows:
        print("Результаты фильтрации:")
        for row in filtered_rows:
            print(row)

    # print(tabulate(arg_filter if arg_filter in data else "None"))

        # print(tabulate(data, headers="firstrow", tablefmt="grid"))


if __name__ == '__main__':
    main()