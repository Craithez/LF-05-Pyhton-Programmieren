while True:

    print("1 Festplatte formatieren ")
    print("2 Festplatte waschen ")
    print("3 Festplatte trocknen ")
    print("4 Programm beenden ")

    auswahl = input("Eingabe? ")
    auswahl = auswahl.strip()

    if (auswahl == "1"):
        print("Festplatte wurde formatiert.")
    elif (auswahl == "2"):
        print("Festplatte wurde gewaschen.")
    elif (auswahl == "3"):
        print("Festplatte wurde getrocknet.")
    elif print(auswahl == "4"):
        print("Programm wird beendet.")
        exit
    else:
        print("Ungültige Eingabe.")    