ip_adresse = input(str("Geben sie eine IPv4 Adresse ein: "))

Liste = ip_adresse.split(".")
Liste = list(map(int, Liste))
hexIP = []
#Zur Überprüfung mit entfernen von .
[hexIP.append(hex(int(x))[2:].zfill(2)) for x in ip_adresse.split('.')]
hexIP = "".join(hexIP)
print("Die IPv6 Adresse ist: " , hexIP)
#Ersetzt . und wandelt in : um
ip_adresseT = input(str("Geben sie eine IPv4 Adresse ein: "))
ListeT = ip_adresseT.replace(".",":")
print("Die IPv6 Adresse ist: " , ListeT)
