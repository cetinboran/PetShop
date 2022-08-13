from Entrys.workerEntry import WorkerEntry
from Entrys.customerEntry import CustomerEntry

def Login(personList):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for person in personList:
        if person.type == "Worker" and person.username == username and person.password == password:
            return [WorkerEntry, person]
        elif person.type == "Customer" and person.username == username and person.password == password:
            return [CustomerEntry, person]

    print("username or password is incorrect")
    return [False,False]