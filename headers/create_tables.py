import csv


def create_table(file):
    table_1 = []

    with open(file, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            table_1.append(row)

    return table_1



def create_table_where(data):
    table_2 = []
    try:
        for elems in data:
            if not table_2:
                table_2.append([key for key in elems.keys()])
                table_2.append([value for value in elems.values()])
            else:
                table_2.append([value for value in elems.values()])
    except AttributeError:
        print("неверное названеи столбца")



    return table_2
