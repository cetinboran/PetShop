from Entrys.login_loops import Login
from classes.animals import Dog, Cat
from jsons.data import JSON

class WorkerEntry(Login):
    def Loop(self, personList, dogList, catList, animalsList, person):
        print(f"Login Successful. Hello {person.username}\n")
        while True:
            print("1 - Add Animal")
            print("2 - Update Animal")
            print("3 - Show Animals")
            print("9 - Exit")
            command = input(">: ")

            if command == "9": break
            elif command == "1":
                AddAnimal(animalsList, dogList, catList)
                JSON.UpdateAnimalsJson(JSON,animalsList)
            elif command == "2":
                UpdateAnimals(animalsList)
                JSON.UpdateAnimalsJson(JSON, animalsList)
            elif command == "3":
                ShowAnimals(animalsList)
                input("")


def AddAnimal(animalList, dogList, catList):
    name = input("Enter the name of the animal: ")
    rare = input("Enter the rare of the animal: ")
    cost = input("Enter the cost of the animal: ")
    type = input("Choose Type (Dog / Cat): ")
    if type.capitalize() == "Dog":
        d = Dog(name, rare, cost)
        animalList.append(d)
        dogList.append(d)
    elif type.capitalize() == "Cat":
        c = Cat(name, rare, cost)
        animalList.append(c)
        catList.append(c)
    else:
        input("There is no such type")

def UpdateAnimals(animalsList):
    ShowAnimals(animalsList)
    try:
        animalId = int(input("Choose From ID: "))

        for index,animal in enumerate(animalsList):
            if animal.animalId == animalId:
                input(animalsList[index].name)

                name = input("Enter the new name: ")
                rare = input("Enter the new rare: ")
                cost = input("Enter the new cost: ")

                animalsList[index].name = name
                animalsList[index].rare = rare
                animalsList[index].cost = cost
                input(animalsList[index].name)
    except:
        pass

def ShowAnimals(animalsList):
    animal_info = ""
    for animal in animalsList:
        animal_info += f"Animal Id: {animal.animalId}, Name: {animal.name}, Type: {animal.type}, Rare: {animal.rare}, Cost: {animal.cost}\n"
    print(animal_info)