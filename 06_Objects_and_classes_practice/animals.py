list_animals = []
count_talking_animals = 0
list_talking_animals = []


data = input()


#from operator import attrgetter


class Dog:
    def __init__(self, name, age, number_of_legs):
        self.name = name
        self.age = age
        self.number_of_legs = number_of_legs

    def produce_sound(self):
        print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")


class Cat:
    def __init__(self, name, age, intelligence_quotient):
        self.name = name
        self.age = age
        self.intelligence_quotient = intelligence_quotient

    def produce_sound(self):
        print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")


class Snake:
    def __init__(self, name, age, cruelty_coefficient):
        self.name = name
        self.age = age
        self.cruelty_coefficient = cruelty_coefficient

    def produce_sound(self):
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")


while data != "I'm your Huckleberry":

    list_data = data.split()
    class_animal = list_data[0]

    if class_animal != "talk":
        name_animal = list_data[1]
        age_animal = list_data[2]
        parameter = list_data[3]

        if class_animal == "Dog":
            number_of_legs = parameter
            current_animal = Dog(name_animal, age_animal, number_of_legs)

        elif class_animal == "Cat":
            intelligence_quotient = parameter
            current_animal = Cat(name_animal, age_animal, intelligence_quotient)

        elif class_animal == "Snake":
            cruelty_coefficient = parameter
            current_animal = Snake(name_animal, age_animal, cruelty_coefficient)

        list_animals.append(current_animal)

    else:
        talking_animal_name = list_data[1]
        count_talking_animals += 1
        for item in list_animals:
            if talking_animal_name == item.name:
                list_talking_animals.append(item)

    data = input()

for item in list_talking_animals:
    item.produce_sound()

num = 0
n = len(list_animals)

for num in range(0, n-1):
    for i in range(n-1, 0, -1):
        if isinstance(list_animals[i], Dog) and not isinstance(list_animals[i-1], Dog):
            list_animals[i], list_animals[i-1] = list_animals[i-1], list_animals[i]



for item in list_animals:
    if isinstance(item, Dog):
        print(f"Dog: {item.name}", end=", ")
        print(f"Age: {item.age}",  end=", ")
        print(f"Number Of Legs: {item.number_of_legs}")
    if isinstance(item, Cat):
        print(f"Cat: {item.name}", end=", ")
        print(f"Age: {item.age}",  end=", ")
        print(f"IQ: {item.intelligence_quotient}")
    if isinstance(item, Snake):
        print(f"Snake: {item.name}", end=", ")
        print(f"Age: {item.age}",  end=", ")
        print(f"Cruelty: {item.cruelty_coefficient}")
