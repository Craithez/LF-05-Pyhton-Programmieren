a = "KB"
b = "MB"
c = "GB"

def einheitencheck(einheit):
    if einheit == a:
        dateiGröße = float(input("Bitte geben sie die Dateigröße an (in ihrer Einheit): "))
        übertragungsRate = float(input("Bitte geben sie ihre Übertragungsrate an (in MB/s): "))
        transferZeit = (dateiGröße / 1000) / übertragungsRate /  3600
        print("Es dauert:", transferZeit, "stunden")
    elif einheit == b:
        dateiGröße = float(input("Bitte geben sie die Dateigröße an (in ihrer Einheit): "))
        übertragungsRate = float(input("Bitte geben sie ihre Übertragungsrate an (in MB/s): "))
        transferZeit = dateiGröße / übertragungsRate /  3600
        print("Es dauert:", transferZeit, "stunden")
    elif einheit == c:
        dateiGröße = float(input("Bitte geben sie die Dateigröße an (in ihrer Einheit): "))
        übertragungsRate = float(input("Bitte geben sie ihre Übertragungsrate an (in MB/s): "))
        transferZeit = (dateiGröße * 1000) / übertragungsRate / 3600
        print("Es dauert:", transferZeit, "stunden")
    else:
        print("Ungültige Einheit!")

einheit = input("Bitte geben sie die Einheit an! In a(KB), b(MB) oder c(GB) an: ")
einheitencheck(einheit)

#Klappt, wohlgemerkt nur SI Einheiten! Kein MBit/s oder MiB/s etc.