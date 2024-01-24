total = input("Einkaufswert eingeben: ")
country = input(str("Zielland eingeben: "))
shipping = None

if country == "Japan":
    if total <= 50:
        shipping = 50
    elif total <= 100:
        shipping = 25
    elif total >= 180:
        shipping = 0
    else:
        shipping = 5
elif country == "Australien":
    if total <= 50:
        shipping = 40
    else:
        shipping = 15
print ("Ihre Kosten Lieferkosten betragen ",shipping,"$")
#Funktioniert noch nicht

