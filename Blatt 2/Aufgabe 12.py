note = int(input("Note eingeben! "))
if note >= 1 and note < 7:
    match note:
        case 1 if note == 1:
            print("Sehr gut!")
        case 2 if note == 2:
            print("Gut!")
        case 3 if note == 3:
            print("Befriedigend!")
        case 4 if note == 4:
            print("Ausreichend!")
        case 5 if note == 5:
            print("Mangelhaft!")
        case 6 if note == 6:
            print("Ungenügend!")
else:
    print("Ungültige Eingabe!")