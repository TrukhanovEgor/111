import logging
import unittest


logging.basicConfig(level=logging.INFO, filemode="a", filename="runner_tests.log", encoding='utf-8',
                        format="%(asctime)s:%(levelname)s:%(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            n1 = Runner('Mike', -4)
            for i in range(10):
                n1.walk()
            self.assertEqual(n1.distance, 50)

            logging.info(f'"test_walk" выполнен успешно')

        except ValueError as err:
            logging.error(f"Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            n1 = Runner({}, 7)
            for i in range(10):
                n1.run()
            self.assertEqual(n1.distance, 100)

            logging.info(f'"test_run" выполнен успешно')

        except TypeError as err:
            logging.error(f"Неверный тип данных для обьекта Runner", exc_info=True)


if __name__ == '__main__':

    unittest.main()