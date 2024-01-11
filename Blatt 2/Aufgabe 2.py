betrag = float(input("Betrag eingeben: "))
if betrag >= 100:
    versandkosten1 = 0
    print("Keine Versandkosten")
    print ("Sie bezahlen: ", betrag)
elif betrag < 100:
    print("Bestellwert zu gering")
    versandkosten2 = 10
    gesamtpreis = betrag+versandkosten2
    print("Sie bezahlen: ", gesamtpreis)
else:
    print("Richtige Werte eintragen")

