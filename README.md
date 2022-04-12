# AAA_python
Avito analytics academy python course


# testing: 

issue 01:
Тестирование с помощью доктестов. Импортировать библиотеку doctest: import doctest. Run file morse.py.
issue 02:
Тестирование с помощью параметрического теста, используя декоратор @pytest.mark.parametrize. Импортировать библиотеку pytest: import pytest. Run file test_issue02.py. Исходный код в файле morse.py
issue 03:
Тесты с использованием unittest: проверка на пустое значение, проверка корректной работы fit tranform, проверка несоответствия задаваемых значений ожидаемым реузльтатам. Импортировать библиотеку unittest. Run file one_hot_encoder.py
issue 04:
Тесты с использованием pytest. Run file test_OHE_pytest.py. Исходный код в файле file one_hot_encoder.py.
issue 05:
Для запуска требуется установка pytest, pytest-cov:
pip install pytest
pip install pytest-cov
Запуск из терминала с информацией о покрытии: python -m pytest what_year_is_now.py --cov
Чтобы получить html отчет о покрытии: python -m pytest what_year_is_now.py --cov --cov-report html
