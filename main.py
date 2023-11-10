#!/usr/bin/env python3


# Main
def main():
    print("Hello, World!")
    while True:
        operazione = input("Inserisci il numero 1 Somma 2 Sottrazione 3 Moltiplicazione 4 Divisione ")
        if (operazione != "1" or "2" or "3" or "4"):
            print("Scelta non valida")
            input("Inserisci il numero 1 Somma 2 Sottrazione 3 Moltiplicazione 4 Divisione ")

        n1 = float(input("Inserisci il Primo Numero -> "))
        if(n1<0):
            print("Scelta non valida")
            input("Inserisci il Primo Numero -> ")
        n2 = float(input("Inserisci il Secondo Numero -> "))
        if (n2 < 0):
            print("Scelta non valida")
            input("Inserisci il Secondo Numero -> ")

        if operazione == "1":
            print("Il risultato  è: ", (n1 + n2))
        elif operazione == "2":
            print("Il risultato  è: ", (n1 - n2))
        elif operazione == "3":
            print("Il risultato  è: ", (n1 * n2))
        elif operazione == "4":
            print("Il risultato  è: ", (n1 / n2))

        new_action = input("\nDesideri continuare ad utilizzare l'Applicazione? S/N ")
        if new_action == "N" or new_action == "n":
            print("A presto!\n")
            break



        print("Sto tornando al menù principale!\n")



    pass

# Execute
if __name__ == '__main__':
    main()
