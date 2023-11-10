#!/usr/bin/env python3


# Main
def main():
    print("Calcolatrice")


    while True:

        try:
         v1 = float(input("Inserisci il primo valore\n"))
         v2 = float(input("Inserisci il secondo valore \n"))


         operatore = input("Inserisci l'operatore\n - 1 +\n - 2 -\n - 3 x \n - 4 :\n")

         if (operatore == "+"):
            print("Il risultato dell'Addizione è: ", str(v1 + v2))

         elif (operatore == "-"):
            print("Il risultato della Sottrazione è: ", str(v1 - v2))

         elif (operatore == "x"):
            print("Il risultato della Moltiplicazione è: ", str(v1 * v2))

         elif (operatore == ":"):
            if v2 == 0: print(" Impossibile fare la Divisione con 0")
            else: print("Il risultato della Divisione è: ", str(v1 / v2))

         else: print("operatore invalido")



        except ValueError:
         print("Errore: Valore non numerico")
         print("Riprova")


    #if (nome == "lorenzo"):
     #print("Bentornato " + nome)
    #else: print("Non ti conosco")

# Execute
if __name__ == '__main__':
    main()
