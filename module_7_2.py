import os.path


def custom_write(file_name, strings):
    strings_positions = {}

    if len(strings) > 0:

        if not os.path.isfile(file_name):
            file = open(file_name, "x", encoding='utf-8')
            file.close()
            lines = 0

        else:
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = sum(1 for line in file)

        line_ = lines
        with open(file_name, 'a+', encoding='utf-8') as file:
            for item in strings:
                line_ += 1
                start_byte = file.tell()
                file.write(f"{item}\n")
                strings_positions[(line_, start_byte)] = item

    return strings_positions


def start():
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)


if __name__ == '__main__':
    start()