from Entrys.login_loops import Login
from jsons.data import JSON
from classes.person import *

class AdminEntry(Login):
    def Loop(self, personList, customerList, workerList, person):
        print(f"Login Successful. Hello Boss.\n")
        while True:
            print("1 - Hire Worker")
            print("2 - Fire Worker")
            print("3 - Show Workers")
            print("4 - Show Animals")
            print("9 - Exit")
            command = input(">: ")

            if command == "9": break
            elif command == "1":
                HireWorker(personList, workerList)
                JSON.UpdatePersonsJson(JSON, personList)

def HireWorker(personList, workerList):
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    salary = input("Enter the salary: ")

    w = Worker(username, password, salary)
    personList.append(w)
    workerList.append(w)

def FireWorker(personList, workerList):
    pass