import argparse
from tabulate import tabulate

from headers.create_tables import create_table, create_table_where
from headers.filter_values import filter_values
from headers.parse_aggregate import parse_aggregate
from headers.parse_where import parse_where



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str)
    parser.add_argument('--where',  type=str)
    parser.add_argument('--aggregate', type=str)

    args = parser.parse_args()

    file_path = args.file
    arg_filter = args.where
    arg_aggregate = args.aggregate

    if file_path and not arg_filter and not arg_aggregate:
        table_1 = create_table(file_path)

        print(tabulate(table_1, headers="firstrow", tablefmt="grid"))


    if arg_filter:
        filtered_where = filter_values(arg_filter)
        parsed_where = parse_where(file_path, filtered_where[0], filtered_where[1], filtered_where[2])
        table_2 = create_table_where(parsed_where)

        print(tabulate(table_2, headers="firstrow", tablefmt="grid"))


    if arg_aggregate:
        filtered_aggregate = filter_values(arg_aggregate)
        parsed_aggregate = parse_aggregate(file_path, filtered_aggregate[0], filtered_aggregate[1], filtered_aggregate[2])
        print(parsed_aggregate)
        table_3 = tabulate(parsed_aggregate, headers="firstrow", tablefmt="grid")

        print(table_3)




if __name__ == '__main__':
    main()