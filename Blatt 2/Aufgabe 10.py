einheit = str(input("Bitte geben sie die Einheit an! In a(KB),b(MB) oder c(GB) an."))
a = "KB"
b = "MB"
c = "GB"
def einheitencheck(einheit):
    match einheit:
        case 1 if einheit == a:
            dateiGröße = input("Bitte geben sie die Dateigröße an (in ihrer Einheit): ")
            übertragungsRate = input("Bitte geben sie ihre Übertragungsrate an (in MB/s): ")
            transferZeit = None
            transferZeit = (dateiGröße/1000)/übertragungsRate
            print("Es dauert: ", transferZeit, "s")
        case 2 if einheit == b:
            dateiGröße = input("Bitte geben sie die Dateigröße an (in ihrer Einheit): ")
            übertragungsRate = input("Bitte geben sie ihre Übertragungsrate an (in MB/s): ")
            transferZeit = None
            transferZeit = dateiGröße/übertragungsRate
            print("Es dauert: ", transferZeit, "s")
        case 3 if einheit == c:       
            dateiGröße = input("Bitte geben sie die Dateigröße an (in ihrer Einheit): ")
            übertragungsRate = input("Bitte geben sie ihre Übertragungsrate an (in MB/s): ")
            transferZeit = None
            transferZeit = (dateiGröße*1000)/übertragungsRate
            print("Es dauert: ", transferZeit, "s")
    print(transferZeit)
#Funktioniert noch nicht

