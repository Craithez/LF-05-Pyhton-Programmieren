def bin_2_dez(num):

    bits = list(str(num))
    dez = 0
    zaehler = 0

    for i in reversed(bits):
        #print(bits) für Stellen einzusehen
        dez += 2**zaehler * int(i)
        zaehler+=1
    print(dez)

if __name__ == '__main__':

    # Binär Value
    bin_val = int(input("Binaerzahl eingeben: "))
     
    # Funktion aufrufen
    bin_2_dez(bin_val)