geschwindigkeitsLimit = float(input("Geschwindkeitslimit: "))
geschwindigkeit = float(input("Geschwindigkeit: "))
if geschwindigkeit <= geschwindigkeitsLimit:
    print("Passt, fahr schneller.")
    exit()

if geschwindigkeit < 100:
    geschwindigkeit = geschwindigkeit -((geschwindigkeit/100)*3)
else:
    geschwindigkeit = geschwindigkeit -((geschwindigkeit/100)*5) 
unterschied = geschwindigkeit - geschwindigkeitsLimit
if unterschied < 20:  
    print("Glück gehabt! Du warst nur ", unterschied, "zu schnell")
elif unterschied > 20 and unterschied < 30:
    print("Du warst ", unterschied, "zu schnell, 30 Euro.")
elif unterschied > 30 and unterschied < 50:
    print("Du warst ", unterschied, "zu schnell, 120 Euro.")
else:
    print("Du warst VIEL", unterschied, "zu schnell, 240 Euro.")        

