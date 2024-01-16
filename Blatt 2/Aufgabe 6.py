#Man kann die Okets wohl zusammen packen und nur eine Bedingung für alle Fälle definieren.

def ip_checkv4(ip):
        oktets=ip.split(".")
        if len(oktets)<4 or len(oktets)>4:
            return "IP sollte aus 4 Oktets bestehen! "
        else:
            while len(oktets)== 4:
                a=int(oktets[0])
                b=int(oktets[1])
                c=int(oktets[2])
                d=int(oktets[3])
                if a<= 0 or a == 127 :
                    return "ungültige IP Adresse "
                elif d == 0:
                    return " " 
                elif a>255 or a<0:
                    return "Sollte nicht größer als 255 und nicht kleiner als 0 sein! "
                elif b>255 or b<0: 
                    return "Sollte nicht größer als 255 und nicht kleiner als 0 sein! "
                elif c>255 or c<0:
                    return "Sollte nicht größer als 255 und nicht kleiner als 0 sein! "
                elif d>255 or c<0:
                    return "Sollte nicht größer als 255 und nicht kleiner als 0 sein! "
                else:
                    return "Gültige IP Adresse ", ip
        
ip=(input("IP Adresse eingeben! "))
print(ip_checkv4(ip))
