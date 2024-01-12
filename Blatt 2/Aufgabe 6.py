#ip = str(input("IP eingeben : "))
#octets = 0
#octets == ip
#number = 0
#number == ip
#def check_ip(ip):
#        octets = ip.split(".")
#        if len(octets)!=4:
#            print("Keine richtige IP Adresse!")
#            return "Ungültige IP"
#for number in octets:
#    if not number==str:
#        print("Keine richtige IP Adresse!")
#    if str(number)<0 or int(number)>255:
#        print("Keine richtige IP Adresse!")
#    else:
#        print("IP Adresse ist gültig!")

#def validIP(inp):
#    if inp.find('/') == -1:
#        return False
#    ips,mask = inp.split('/')
#    if not mask.isdigit():
#        return False
#    if ips.isnumeric()>255:
#        return False
#    if ips.isnumeric()<0:
#        return False
#    if ips.count('.') > 3:
#        return False
#    for ip in ips.split('.'):
#        if not ip.isdigit():
#            return False
#    return True
#print("Starte!")

#IPv4 = ''
#while not validIP(IPv4):
#    IPv4 =input("Bitte gültige IP Adresse eingeben (#.#.#.#:####):")
#    print(IPv4)
#print ("valid:", IPv4)

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
                elif a>255:
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
