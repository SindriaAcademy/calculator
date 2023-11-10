#!/usr/bin/env python3
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
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
        raise ValueError("Errore: Divisione per zero")

while True:
    try:
        clearConsole()
        operazione = input("Scegli un'operazione (sum, sub, m, div) o 'esc' per uscire: ")


        if operazione == 'esc':
            break

        num1 = float(input("Inserisci il primo numero: "))
        num2 = float(input("Inserisci il secondo numero: "))

        if operazione == 'sum':
            risultato = somma(num1, num2)
        elif operazione == 'sub':
            risultato = sottrazione(num1, num2)
        elif operazione == 'm':
            risultato = moltiplicazione(num1, num2)
        elif operazione == 'div':
            risultato = divisione(num1, num2)
        else:
            print("Errore: Operazione non valida")
            continue

        print("Risultato:", risultato)

    except ValueError as e:
        print(f"Errore: {e}")
    except Exception as e:
        print(f"Errore imprevisto: {e}")



