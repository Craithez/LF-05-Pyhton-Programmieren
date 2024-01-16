geschwindigkeitsLimit = float(input("Geschwindkeitslimit: "))
geschwindigkeit = float(input("Geschwindigkeit: "))
unterschied = 0
if geschwindigkeit < geschwindigkeitsLimit:
    print("Passt, fahr schneller.")
    exit()
elif geschwindigkeit < 100:
    verändereGeschwindigkeit = geschwindigkeit -((geschwindigkeit/100)*3)
else:
    verändereGeschwindigkeit = geschwindigkeit -((geschwindigkeit/100)*5) 
    veränderung = geschwindigkeitsLimit - verändereGeschwindigkeit
    if verändereGeschwindigkeit < 20:  
        print("Glück gehabt! Du warst ", verändereGeschwindigkeit, "zu schnell")
    elif verändereGeschwindigkeit >= 20:
        print("Du warst ", verändereGeschwindigkeit, "zu schnell, 30 Euro.")
    elif verändereGeschwindigkeit >= 30 and verändereGeschwindigkeit < 50:
        print("Du warst ", verändereGeschwindigkeit, "zu schnell, 120 Euro.")
    else:
        print("Du warst VIEL", verändereGeschwindigkeit, "zu schnell, 240 Euro.")        
    print("Glück gehabt!")

