orario = float(input("Che ore sono? "))
if orario < 12:
    print("Buongiorno!")
else:
    if orario < 18:
        print("Buon pomeriggio!")
    else:
        if orario <23:
            print("Buona sera!")
        else:
            print("Buona notte!")