from random import randint
from threading import Thread
from time import sleep
from queue import Queue


# Стол, хранит информацию о находящемся за ним гостем (Guest)
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

# Гость, поток, при запуске которого происходит задержка от 3 до 10 секунд
class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

#  Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей
#  (guest_arrival) и их обслуживания (discuss_guests)
class Cafe:
    list_thr = []

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        len_list_guests = len(list(guests))
        min_guests_tables = min(len_list_guests, len(self.tables))

        for i in range(min_guests_tables):
            self.tables[i].guest = guests[i]
            thr1 = guests[i]
            thr1.start()
            Cafe.list_thr.append(thr1)

            print(f'{list(guests)[i].name} сел(-а) за стол номер {self.tables[i].number}')

        if len_list_guests > min_guests_tables:
            for i in range(min_guests_tables, len_list_guests):
                self.queue.put(guests[i])
                print(f'{list(guests)[i].name} в очереди')

    def discuss_guests(self):
        while not (self.queue.empty()) or Cafe.check_table(self):
                for table in self.tables:
                    if not (table.guest is None) and not (table.guest.is_alive()):
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None

                if (not (self.queue.empty())) and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thr1 = table.guest
                    thr1.start()
                    Cafe.list_thr.append(thr1)

    def check_table(self):
        for table in self.tables:
            if table.guest is not None:
                return True
        return False


def start():
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]

    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'    ]

    # Создание гостей
    guests = [Guest(name) for name in guests_names]

    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()

    for thr in Cafe.list_thr:
        thr.join()


if __name__ == '__main__':
    start()