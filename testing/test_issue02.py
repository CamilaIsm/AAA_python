from morse import decode
import pytest


@pytest.mark.parametrize('morse_message, expected_output', [
    ('.- .- .-', 'AAA'),
    ('... --- ...', 'SOS'),
    ('.... ..','HI')
])
def test_decode(morse_message, expected_output):
    assert decode(morse_message) == expected_output


if __name__ == '__main__':
    pytest.main()
    
