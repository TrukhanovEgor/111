def add_everything_up(a, b):
    try:
        return a+b
    except:
        return str(a) + str(b)


def start():
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))

if __name__ == '__main__':
    start()