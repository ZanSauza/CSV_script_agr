import argparse
from tabulate import tabulate


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

    print(tabulate(arg_filter if arg_filter in data else "None"))

        # print(tabulate(data, headers="firstrow", tablefmt="grid"))


if __name__ == '__main__':
    main()