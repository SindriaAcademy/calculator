#!/usr/bin/env python3
import sys

def plus(num1, num2):
    return num1+num2

def minum(num1, num2):
    return num1-num2

def product(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

# Main
def main():
    global ris
    scelta = ""
    while scelta != "exit":

        try:
            num1 = input("insersci primo numero \n")
            num1 = float(num1)
            segno = input("inserisci segno \n")
            num2 = input("inserisci secondo numero \n")
            num2 = float(num2)
            if segno == "+":
                ris = plus(num1,num2)
            elif segno == "-":
                ris = minum(num1,num2)
            elif segno == "*":
                ris = product(num1, num2)
            elif segno == "/":
                try:
                    ris = divide(num1,num2)
                except:
                    ris = "divisione impossibile"
            else:
                ris = "segno sbagliato"

            if (type(ris) == "float"):
                print("risultato: ")
                print(ris)
            else:
                print(ris)
        except:
            print("inserisci un numero")
        print()
        scelta = input("Scrivere exit per uscire \n")


# Execute
if __name__ == '__main__':
    main()
