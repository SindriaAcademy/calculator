#!/user/bin/env python3

# Main
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
        return "Impossibile dividere per zero"
def main():
    while True:
        print("Seleziona un'operazione:")
        print("1. Somma")
        print("2. Sottrazione")
        print("3. Moltiplicazione")
        print("4. Divisione")
        print("5. Esci")
        try:
            scelta = input("Inserisci il numero corrispondente all'operazione desiderata: ")
            if scelta in ('1', '2', '3', '4'):
                numero1 = float(input("Inserisci il primo numero: "))
                numero2 = float(input("Inserisci il secondo numero: "))

                if scelta == '1':
                    print("Risultato:", somma(numero1, numero2))
                elif scelta == '2':
                    print("Risultato:", sottrazione(numero1, numero2))
                elif scelta == '3':
                    print("Risultato:", moltiplicazione(numero1, numero2))
                elif scelta == '4':
                    print("Risultato:", divisione(numero1, numero2))
            elif scelta == '5':
                print("Chiusura della calcolatrice.")
                break
            else:
                print("Selezione non valida. Riprova.")
        except:
            print('errore! inserire valori numerici')



# Execute
if __name__ == '__main__':
    main()
