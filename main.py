import csv
import matplotlib.pyplot as plt
employees = []


class Person:
    def __init__(self, id, firstName, lastName, age, email, gender, ipaddr):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.email = email
        self.gender = gender
        self.ipaddr = ipaddr

with open('MOCK_DATA.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(spamreader)
    for row in spamreader:
        employees.append(Person(row[0], row[1], row[2], row[3], str(row[4]), row[5], str(row[6])))


def listEmployees(attr):
    if attr == 'quick':
        for Person in employees:
            printPerson(Person)
    if attr == 'edu':
        for Person in employees:
            if '.edu' in Person.email:
                printPerson(Person)


def printPerson(Person):
    print(Person.firstName + " " + str(Person.age) + ' ' + str(Person.email) + ' ' + str(Person.ipaddr))

def graph():
    names = ['Female', 'Male']
    femaleCount = 0
    maleCount = 0
    for Person in employees:
        if Person.gender == 'Female':
            femaleCount = 1 + femaleCount
        if Person.gender == 'Male':
            maleCount = 1 + maleCount
    values = [femaleCount, maleCount]
    print(values)
    plt.bar(names, values)
    plt.figure(100)
    plt.show()


listEmployees('quick')
graph()
