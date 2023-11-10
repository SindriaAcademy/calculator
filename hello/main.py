#!/usr/bin/env python3


def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b != 0:
        return a / b
    else:
        return "Errore: Divisione per zero"


# Main
def calcolatrice():
    continua = True

    while continua:
        print("Seleziona l'operazione:")
        print("1. Somma")
        print("2. Sottrazione")
        print("3. Moltiplicazione")
        print("4. Divisione")
        print("0. Esci")

        scelta = input("Inserisci il numero dell'operazione desiderata: ")

        if scelta == '0':
            continua = False
            print("Arrivederci!")

        elif scelta in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Inserisci il primo numero: "))
                num2 = float(input("Inserisci il secondo numero: "))
            except ValueError:
                print("ERRORE: Inserire numeri validi.\n")
                continue

            if scelta == '1':
                print(f"{num1} + {num2} = {somma(num1, num2)}")

            elif scelta == '2':
                print(f"{num1} - {num2} = {sottrazione(num1, num2)}")

            elif scelta == '3':
                print(f"{num1} * {num2} = {moltiplicazione(num1, num2)}")

            elif scelta == '4':
                risultato = divisione(num1, num2)
                if isinstance(risultato, str):
                    print(risultato)
                else:
                    print(f"{num1} / {num2} = {risultato}")

        elif scelta != '0':
            print("SCELTA NON VALIDA!\n")

# Execute
calcolatrice()



