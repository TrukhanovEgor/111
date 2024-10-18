import random

def test():
    first = 'Мама мыла раму'
    second = 'Рамена мало было'

    result = list(map(lambda x, y: x == y, first, second))
    print(result)

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(str(data) + '\n')

    return write_everything

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


def start():
    test()

    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
    #get_advanced_writer('example.txt') ('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())



if __name__ == '__main__':
    start()