#!/usr/bin/env python3

def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        raise ValueError("Impossibile dividere per zero SCEMO")
    return a / b

def main():
    while True:
        print("\nCalcolatrice Scurrile")
        print("1. Somma")
        print("2. Sottrazione")
        print("3. Moltiplicazione")
        print("4. Divisione")
        print("5. Esci")

        try:
            scelta = int(input("Seleziona un'operazione (1-5): "))
            if scelta not in range(1, 6):
                raise ValueError("Scelta non valida. Inserisci un numero tra 1 e 5 TESTA DI MINCHIA.")
        except ValueError as e:
            print(f"Errore: {e}")
            continue

        if scelta == 5:
            print("CIAONE COIONE!!")
            break

        try:
            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))
        except ValueError:
            print("Errore: Inserisci numeri validi COGLIONE.")
            continue

        if scelta == 1:
            risultato = somma(num1, num2)
        elif scelta == 2:
            risultato = sottrazione(num1, num2)
        elif scelta == 3:
            risultato = moltiplicazione(num1, num2)
        elif scelta == 4:
            try:
                risultato = divisione(num1, num2)
            except ValueError as e:
                print(f"Errore: {e}")
                continue
        else:
            print("Errore: Scelta non valida. Riprova PIRLA.")
            continue

        print(f"Risultato: {risultato}")

if __name__ == "__main__":
    main()
