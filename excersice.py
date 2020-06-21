import json
from itertools import product, groupby
from pprint import pprint


class TooMuchParametersException(Exception):

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return 'Достигнуто предельное количество возможных вариантов: более 100'


def read_json(filename: str) -> dict:
    with open(filename) as file:
        return json.load(file)


planet_data = read_json('test3.json')


def calculate(data: dict) -> list:

    pairs_set = list()

    for key, val in data.items():
        temp_list = list()
        for el in product([key], val):
            temp_list.append(el)
        pairs_set.append(temp_list)

    result_gen = product(*pairs_set)
    result_list = list()

    variation_counter = 0
    for el in result_gen:
        result_list.append(dict(el))
        variation_counter += 1
        if variation_counter > 100:
            raise TooMuchParametersException

    return result_list


pprint(calculate(planet_data))









