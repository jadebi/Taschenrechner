def addieren(a, b):
    return a + b
def subtraktion(a, b):
    return a - b

def multiplizieren(a,b):
    return a * b

def dividieren(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "ERROR: division by zero"

def main():
    print("Taschenrechner")
    print("1 fuer Addition")
    print("2 fuer Subtraktion")
    print("3 fuer Multiplikation")
    print("4 fuer Division")

    wahl = input("Wahl eingeben: ")

    match wahl:
        case "1":
            print("Resultat: {}".format(addieren(2,3)))
            # Hier Funktion für Addition einfügen
        case "2":("Resultat: {}".format(subtraktion(5,2)))
            # Hier Funktion für die Subtraktion einfügen
        case "3":
            print("Resultat: {}".format(multiplizieren(2, 3)))
        case "4":
            print("Resultat: {}".format(dividieren(2, 3)))
        case _:
            print("Falsche Auswahl, das Programm wird beendet.")

if __name__ == "__main__":
    main()
