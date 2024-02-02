temperaturen = []
for i in range (3):
    temmperatur = float(input(f"Geben sie die {i+1} Temperatur eingeben: "))
    temperaturen.append(temmperatur)
durchschnitt = round(sum(temperaturen)/ len(temperaturen),2)
if durchschnitt <= 30:
    print(f"{durchschnitt}°: Temperatur ist normal! ")
elif 30 < durchschnitt < 40:
    print(f"{durchschnitt}°: Temperatur ist höher als normal!")
else:
    print(f"{durchschnitt}°: Temperatur ist viel zu hoch!")



