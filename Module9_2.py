def start():
    first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
    second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

    first_result = [len(item) for item in first_strings if len(item) >= 5]
    print(first_result)

    second_result = [(first, second)
                     for first in first_strings
                     for second in second_strings
                     if len(first) == len(second)]
    print(second_result)

    third_result = [(string, len(string))
                    for string in first_strings + second_strings
                    if len(string) % 2 == 0]
    print(third_result)


if __name__ == '__main__':
    start()