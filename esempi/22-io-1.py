print("Questo programma permette di calcolare l'energia contenuta in corpo,\ncome dimostrato dalla teoria della relatività di Einstein.\nLa formula che useremo è:\n\t Energia = massa * velocità_luce^2")
massa = float(input("Quanto vale la massa del corpo in kg? "))
vel_luce = 300000000
energia = massa * vel_luce**2
risposta = f"L'energia contenuta in un corpo di massa {massa:.2E} kg è {energia:.2E} Joule"
print(risposta)