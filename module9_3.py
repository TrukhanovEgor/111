def start():
    first = ['Strings', 'Student', 'Computers']
    second = ['Строка', 'Урбан', 'Компьютер']

    first_result = ((abs(len(x) - len(y))) for x, y in zip(first, second) if len(x) != len(y))
    print(list(first_result))

    second_result = (first[i] == second[i] for i in range(len(first)))
    print(list(second_result))


if __name__ == '__main__':
    start()