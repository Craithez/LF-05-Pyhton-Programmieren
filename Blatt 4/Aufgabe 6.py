def dez_2_bin(num):
     
    if num >= 1:
        dez_2_bin(num // 2)
    print(num % 2, end = '')
 
if __name__ == '__main__':
     
    # Dezimal Value
    dez_val = int(input("Dezimalzahl eingeben: "))
     
    # Funktion aufrufen
    dez_2_bin(dez_val)
