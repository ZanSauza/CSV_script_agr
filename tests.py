import pytest

from headers.filter_values import filter_values
from headers.parse_where import parse_where
from headers.parse_aggregate import parse_aggregate


file_path = "products.csv"

filter_values_lst_1 = ["price<0", "price>0", "price=0", "brand=apple"]
filter_values_lst_2 = [("price", "<", "0"), ("price", ">", "0"), ("price", "=", "0"), ("brand", "=", "apple")]

parse_where_lst_1 = [("price", "<", "0"), ("price", ">", "0"), ("price", "=", "0"), ("brand", "=", "apple")]
parse_where_lst_2 = [
    [],
    [{'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
    {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
    {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'},
    {'name': 'poco x5 pro', 'brand': 'xiaomi', 'price': '299', 'rating': '4.4'}],
    [],
    [{'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'}]
                     ]

parse_aggregate_lst_1 = [("rating", "=", "min"), ("price", "=", "avg"), ("price", "=", "max"), ("rating", "=", "ABCDEFGYTABBC")]
parse_aggregate_lst_2 = [
    [['min'], [4.4]],
    [['avg'], [674.0]],
    [['max'], [1199.0]],
    [['ABCDEFGYTABBC']]



]


def test_filter_values():
    count = 0
    for i in filter_values_lst_1:
        assert filter_values(i) == filter_values_lst_2[count]
        count += 1



def test_parse_where():
    count = 0
    for i in parse_where_lst_1:
        assert parse_where(file_path, parse_where_lst_1[count][0],
                           parse_where_lst_1[count][1], parse_where_lst_1[count][2]) == parse_where_lst_2[count]
        count += 1


def test_parse_aggregate():
    count = 0
    for i in parse_aggregate_lst_1:
        assert parse_aggregate(file_path, parse_aggregate_lst_1[count][0],
                               parse_aggregate_lst_1[count][1],parse_aggregate_lst_1[count][2]) == parse_aggregate_lst_2[count]
        count += 1




if __name__ == '__main__':
    test_filter_values()
    test_parse_where()
    test_parse_aggregate()