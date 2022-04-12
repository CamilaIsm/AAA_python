import unittest
from typing import List, Tuple


def fit_transform(*args: list) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    unique_categories = set(categories)
    bin_format = f'{{0:0{len(unique_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class Test_one_coder(unittest.TestCase):
    def test_empty(self):
        """
        Проверка на пустое значение
        """
        input = fit_transform([])
        expected = []

        self.assertEqual(input,
                         expected)  # тип исключения, выбрасываемый при несовпадении ожидаемого и реального результатов

    def test_basic(self):
        """
        Проверка корректной работы fit transform
        """
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_not_equal(self):
        """
        Проверка несоответствия задаваемых значений ожидаемым результатам
        """
        test_input = fit_transform(['Moscow', 'Moscow', 'London'])
        expected_result = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]

        self.assertNotEqual(test_input, expected_result)


if __name__ == '__main':
    unittest.main()
