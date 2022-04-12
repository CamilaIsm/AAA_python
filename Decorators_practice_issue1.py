import sys
from datetime import datetime

original_write = sys.stdout.write


def my_write(string_text):
    if string_text != '\n':
        date_time = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        output = f'[{date_time}]: {string_text}'
        original_write(output)


if __name__ == '__main__':
    sys.stdout.write = my_write
    print('1, 2, 3')
    sys.stdout.write = original_write
    
