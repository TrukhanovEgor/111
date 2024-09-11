class House:
    def __init__(self, name, number_of_rooms):
        self.name = name
        self.number_of_rooms = number_of_rooms

    def go_to(self, new_floop):
        if new_floop < 1 or new_floop > self.number_of_rooms:
            print("Такого этожа не существует")
        else:
            for floop in range(1, new_floop + 1):
                print(floop)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)