#!/usr/bin/env python3
import os


# Main
def main():

    while True:
        os.system('cls')
        utente = "+"
        print("Benvenuto")
        while True:
            print("Che operazione desideri fare?")
            print("1) +\n2) -\n3) *\n4) /")
            utente = input()
            if not (utente == "+" or utente == "-" or utente == "*" or utente == "/"):
                print("input non valido inserire nuovamente")
            else:
                break

        while True:
            try:
                numero1 = int(input("Inserire primo numero:\t\t"))
                break
            except ValueError:
                print("Input non valido. Inserisci un numero intero.")
        while True:
            try:
                numero2 = int(input("Inserire secondo numero:\t\t"))
                break
            except ValueError:
                print("Input non valido. Inserisci un numero intero.")

        if utente == "+":
            numero1 += numero2
            print("Il risultato è:\t" + str(numero1))
        if utente == "-":
            numero1 -= numero2
            print("Il risultato è:\t" + str(numero1))
        if utente == "*":
            numero1 = numero1 * numero2
            print("Il risultato è:\t" + str(numero1))
        if utente == "/":
            numero1 = numero1 / numero2
            print("Il risultato è:\t" + str(numero1))
        input("\n\npremere per continuare ...")





# Execute
if __name__ == '__main__':
    main()


