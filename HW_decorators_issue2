import sys
from datetime import datetime


def timed_output(function):

    def wrapper(*args, **kwargs):

        original_write = sys.stdout.write

        def my_write(string_text):
            if string_text != '\n':
                date_time = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
                output = f'[{date_time}]: {string_text}'
                original_write(output)

        sys.stdout.write = my_write
        result = function(*args, **kwargs)
        sys.stdout.write = original_write

        return result

    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting('Camila')
    
