class House:
    houses_history = []  # Атрибут класса для хранения истории домов

    def __new__(cls, *args, **kwargs):
        # Добавляем название дома в историю
        cls.houses_history.append(args[0])  # args[0] - название дома
        return super(House, cls).__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2
del h3

print(House.houses_history)  # ['ЖК Эльбрус']