orario = float(input("Che ore sono? "))
if orario < 12:
    print("Buongiorno!")
elif orario < 18:
    print("Buon pomeriggio!")
elif orario <23:
    print("Buona sera!")
else:
    print("Buona notte!")