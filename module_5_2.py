class House:
    def __init__(self,name,num):
        self.name = name
        self.number_of_floors = num
    def go_to (self,new_floor):
        self.new_floor = new_floor
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            for floor in range(1,new_floor +1):
                print(floor)
        if new_floor < 1 or new_floor > self.number_of_floors:
                print("Такого этажа не существует")
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return self.name


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(f'Название:{h1},кол-во этажей:{len(h1)}')
print(f'Название:{h2},кол-во этажей:{len(h2)}')
print(len(h1))
print(len(h2))