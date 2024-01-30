def ip_classcheck(ip):
        oktets=ip.split(".")
        if len(oktets)<4 or len(oktets)>4:
            return "IP sollte aus 4 Oktets bestehen! "
        else:
            while len(oktets)== 4:
                a=int(oktets[0])
                b=int(oktets[1])
                c=int(oktets[2])
                d=int(oktets[3])
                if a >= 0 and b >= 0 and c >= 0 and d >= 0 and a <= 127 and b <= 255 and c <= 255 and d <= 255:
                    return "Klasse A - 255.0.0.0"
                elif a >= 128 and b >= 0 and c >= 0 and d >= 0 and a <= 191 and b <= 255 and c <= 255 and d <= 255:
                    return "Klasse B - 255.255.0.0" 
                elif a >= 192 and b >= 0 and c >= 0 and d >= 0 and a <= 232 and b <= 255 and c <= 255 and d <= 255:
                    return "Klasse C - 255.255.255.0"                      
                elif a >= 224 and b >= 0 and c >= 0 and d >= 0 and a <= 239 and b <= 255 and c <= 255 and d <= 255:
                    return "Klasse D - Multicast-Anwendungen "
                elif a >= 240 and b >= 0 and c >= 0 and d >= 0 and a <= 255 and b <= 255 and c <= 255 and d <= 255:
                    return "Klasse E - reserviert für zukünftige Anwendungen "
                else:
                    return "Ungültige IP Adresse ", ip
        
ip=(input("IP Adresse eingeben! "))
print(ip_classcheck(ip))


