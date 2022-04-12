import json
import urllib.request
import pytest
from unittest.mock import patch
from io import StringIO

API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год
    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


def test_incorrect_index():
    """
    Тест на некорректный формат даты (без нулей)
    """
    exp_response = '{"currentDateTime": "5.7.2021T13:52Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_response)):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_format_dd_mm_yyyy():
    """
    Тест на корректную работу с датой в формате 'DD.MM.YYYY'
    """
    exp_response = '{"currentDateTime": "07.12.2021T00:10Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_response)):
        actual = what_is_year_now()
    expected = 2021
    assert actual == expected


def test_format_yyyy_mm_dd():
    """
    Тест на корректную работу с датой в формате 'YYYY-MM-DD'
    """
    exp_response = '{"currentDateTime": "2021-12-07T00:10Z"}'
    with patch('urllib.request.urlopen', return_value=StringIO(exp_response)):
        actual = what_is_year_now()
    expected = 2021
    assert actual == expected
 
