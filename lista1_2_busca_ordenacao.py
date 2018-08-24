# -*- coding: utf-8 -*-
import random
import math

class Person:

    def __init__(self, registration, type, cash):
        self.registration = registration
        self.type = type
        self.cash = cash

    def has_cash(self, price):
        return self.cash - price >= 0

    def meal_price(self):

        meal_prices = {
            'Employee': 13.00,
            'Student': 5.20,
        }

        return meal_prices[self.type]

    def breakfast_price(self):

        breakfast_prices = {
            'Employee': 13.00,
            'Student': 5.20,
        }

        return breakfast_prices[self.type]

    def discount_meal_price(self):

        if self.has_cash(self.meal_price()):
            self.cash -= self.meal_price()

        else:
            print("\nDINHEIRO INSUFICIENTE!!! OPERAÇÃO CANCELADA\n")

    def discount_breakfast_price(self):

        if self.has_cash(self.breakfast_price()):
            self.cash -= self.breakfast_price()

        else:
            print("\nDINHEIRO INSUFICIENTE!!!  OPERAÇÃO CANCELADA\n")

    def insert_cash(self, cash):
        self.cash += cash



def generate_people():

    people = []

    for i in range(5000):
        registration = random.randint(100000001, 180000001)
        cash = random.randint(1, 100)
        types  = ['Employee', 'Student']
        type = random.choice(types)
        people.append(Person(registration, type, cash))

    return people


def insertionSort(people):
    for index in range(1,len(people)):

        current_person = people[index]
        current_registration = people[index].registration
        position = index

        while position > 0 and people[position-1].registration > current_registration:
            people[position] = people[position-1]
            position = position-1

        people[position] = current_person


def remove_duplicates(people):
    seen = set()
    seen_add = seen.add
    return [x for x in people if not (x.registration in seen or seen_add(x.registration))]


def write_to_file(people):
    file = open("matriculas.txt","w")
    for p in people:
        file.write(str(p.registration) + " " + p.type + " " + str(p.cash) + "\n")
    file.close()


def search(registration, people_list):

    lower_index = 0
    upper_index = people_list.__len__() - 1

    while lower_index <= upper_index:

        middle_index = math.floor((upper_index + lower_index) / 2)

        current_person =  people_list[middle_index]

        if current_person.registration == registration:
            return  current_person

        elif current_person.registration > registration:
            upper_index = middle_index - 1

        else:
            lower_index = middle_index + 1

    return None


##################################################################

people = generate_people() # generates random students and employess
#people.sort(key=lambda p: p.registration, reverse=False)
insertionSort(people) #ordenate by registration
people = remove_duplicates(people) # remove people with the same registrarion
write_to_file(people) # writes the people data to matriculas.txt

while True:
    registration = int(input("Digite a matricula do estudante/funcionário: "))
    person = search(registration, people) #binary search by registration

    if person is not None:

        print("\nMatrícula encontrada! Tipo: " + person.type + "\n")

        while True:

            option = int(input("\nO que deseja fazer?\n(1)Ver saldo\n(2)Inserir créditos\n(3)Descontar café da manhã\n(4)Descontar almoço/jantar\n(5)Sair do registro de " + str(person.registration) + "\n"))

            if option == 1:
                print("\nSaldo atual: " + str(person.cash))

            elif option == 2:
                cash = float(input("Digite o valor a ser inserido: "))

                print("\nSaldo anterior: " + str(person.cash))
                person.insert_cash(cash)

                print("\nSaldo atual: " + str(person.cash))
                write_to_file(people)

            elif option == 3:

                print("\nSaldo anterior: " + str(person.cash))
                person.discount_breakfast_price()

                print("\nSaldo atual: " + str(person.cash))
                write_to_file(people)

            elif option == 4:

                print("\nSaldo anterior: " + str(person.cash))
                person.discount_meal_price()

                print("\nSaldo atual: " + str(person.cash))
                write_to_file(people)

            elif option == 5:
                break

            else:
                print("Opção inexistente! Tente novamente")

    else:
        print("Matrícula não encontrada!")


    option = input("Deseja fazer uma nova busca (s)/(n)?")

    if option == "n":
        break
