#!/usr/bin/env python3
import random


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def main():
    menu()


def menu():
    on = True
    tries = 0
    insults = ["Mongoloid", "Absolute garbage", "Midget", "Maggot"]

    while on:
        if tries >= 10:
            x = random.Random()
            print("You " + insults[x.randint(0, len(insults) - 1)] +
                  ", You failed the Baby IQ test " + str(tries) + " times\n"
                  "Shame on You, " + insults[x.randint(0, len(insults) - 1)])
            on = False
        else:
            try:
                command = int(input("--------------------------------------------\n"
                                    "Scegli Operazione\n"
                                    "0: Esci\n"
                                    "1: Addizione\n"
                                    "2: Sottrazione\n"
                                    "3: Moltiplicazione\n"
                                    "4: Divisione\n"
                                    "Scelta: "))
                if command == 0:
                    on = False
                elif command == 1:
                    print("risultato: " + str(add(int(input("Inserisci primo numero: ")),
                                                  int(input("Inserisci secondo numero: ")))))
                elif command == 2:
                    print("risultato: " + str(subtract(int(input("Inserisci primo numero: ")),
                                                       int(input("Inserisci secondo numero: ")))))
                elif command == 3:
                    print("risultato: " + str(multiply(int(input("Inserisci primo numero: ")),
                                                       int(input("Inserisci secondo numero: ")))))
                elif command == 4:
                    print("risultato: " + str(divide(int(input("Inserisci primo numero: ")),
                                                     int(input("Inserisci secondo numero: ")))))
                else:
                    print("--------------------------------------------\n"
                          "Comando inserito non disponibile")
                    tries += 1
            except ZeroDivisionError:
                print("--------------------------------------------\n"
                      "Divisione per Zero non eseguibile")
                tries += 1
            except ValueError:
                print("--------------------------------------------\n"
                      "Valore inserito non numerico")
                tries += 1


# Execute
if __name__ == '__main__':
    main()
