import pytest
from one_hot_encoder import fit_transform


def test_equal():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(cities)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_exception():
    with pytest.raises(TypeError):
        fit_transform()
        

def test_empty():
    assert fit_transform([]) == []

    
if __name__ == '__main__':
    pytest.main()
    
