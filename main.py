#!user/bin/env python3


# Main
def main():
    print("fine programma")



a = False
while (a != True):
    a = False
    try:
        scelta = input("quale operazione vuoi fare?")
    except:
        print("errore")
    try:
        n1 = (float)(input("digita il primo  numero"))
        n2 = (float)(input("digita il secondo numero"))
    except:
        print("è stato inserito un carattere errato")
    if (scelta == "addizione"):
        print(n1 + n2)
    elif (scelta == "sottrazione"):
        print(n1 - n2)
    elif (scelta == "moltiplicazione"):
        print(n1 * n2)
    elif (scelta == "divisione"):
        print(n1 / n2)
    else:
        print("operazione non gestita")
    s = input("vuoi continuare?")
    if (s == "no"):
        a = True
        break
    else:
        a = False









# Execute
if __name__ == '__main__':
    main()



