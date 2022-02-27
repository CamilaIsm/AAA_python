import sys


output = './function_output.txt'


def redirect_output(filepath):
    def wrapper(function):
        def inner_wrapper(*args, **kwargs):
            sys.stdout = open(filepath, 'w')
            return function(*args, **kwargs)
        return inner_wrapper
    return wrapper


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    print('Результат выполнения находится в файле function_output.txt')
    calculate()
    
