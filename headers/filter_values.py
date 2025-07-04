

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
