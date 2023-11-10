#!/usr/bin/env python3


# Main
def main():
    #print("Hello world")
    #nome = input("come ti chiami? \n")
    #print("ciao " + nome)
    #if(nome == "mionome"):
    #    print("bentornato, come stai?")
    #else:
    #    print("non ti conosco")

    while True:
        print("Seleziona un'operazione:")
        print("1. Somma")
        print("2. Sottrazione")
        print("3. Moltiplicazione")
        print("4. Divisione")
        print("5. Esci")

        scelta = input("Inserisci il numero corrispondente all'operazione desiderata: ")

        if scelta == '5':
            print("Grazie per aver usato la calcolatrice, arrivederci")
            break

        if scelta not in ('1', '2', '3', '4'):
            print("Scelta non valida, selezionare un'opzione valida")
            continue

        try:
            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))
        except:
            print("Errore, inserire numeri validi")
            continue

        if scelta == '1':
            risultato = num1 + num2
        elif scelta == '2':
            risultato = num1 - num2
        elif scelta == '3':
            risultato = num1 * num2
        elif scelta == '4':
            if num2 == 0:
                print("Errore: divisione per zero")
                continue
            else:
                risultato = num1 / num2

        print("Risultato: ", risultato)


# Execute
if __name__ == '__main__':
    main()

