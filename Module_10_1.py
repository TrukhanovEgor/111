from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name): # где word_count - количество записываемых слов,
    # file_name - название файла, куда будут записываться слова.
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write( f'Какое-то слово №  {i+1}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')


def start():
    # Взятие текущего времени
    time_start = datetime.now()

    # Запуск функций с аргументами из задачи
    # После создания файла вызовите 4 раза функцию wite_words
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')

    # Взятие текущего времени
    time_stop = datetime.now()
    time_res = time_stop - time_start

    # Вывод разницы начала и конца работы функций
    print(f'Время работы функций {time_res}')

    # После вызовов функций создайте 4 потока для вызова этой функции

    # Взятие текущего времени
    time2_start = datetime.now()

    # Создание и запуск потоков с аргументами из задачи
    thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
    thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
    thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
    thr_fourh = Thread(target=write_words, args=(100, 'example8.txt'))

    thr_first.start()
    thr_second.start()
    thr_third.start()
    thr_fourh.start()

    thr_first.join()
    thr_second.join()
    thr_third.join()
    thr_fourh.join()

    # Взятие текущего времени

    time2_stop = datetime.now()
    time2_res = time2_stop - time2_start
    print(f'Время работы потоков {time2_res}')

    # Вывод разницы начала и конца работы потоков
    print(f'Использование Потоков быстрее функций на {time_res - time2_res} секунд')


if __name__ == '__main__':
    start()