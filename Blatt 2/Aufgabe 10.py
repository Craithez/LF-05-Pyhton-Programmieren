einheit = str(input("Bitte geben sie die Einheit an! In KB,MB oder GB. "))
dateiGröße = input("Bitte geben sie die Dateigröße an (in ihrer Einheit): ")
übertragungsRate = input("Bitte geben sie ihre Übertragungsrate an (in MB/s): ")
transferZeit = 0
KB = str("KB")
MB = str("MB")
GB = str("GB")
match einheit:
    case 1 if einheit == KB:
        transferZeit = (dateiGröße/1000)/übertragungsRate
        print("Es dauert: ", transferZeit, "s")
    case 2 if einheit == MB:
        transferZeit = dateiGröße/übertragungsRate
        print("Es dauert: ", transferZeit, "s")
    case 3 if einheit == GB:        
        transferZeit = (dateiGröße*1000)/übertragungsRate
        print("Es dauert: ", transferZeit, "s")

