# brutto = 1
# while brutto > 0:
 
i = 0
while i in range (1000000):

    print('*** Gehaltsberechnung ***\n')
    
    
    brutto = float(input('Geben Sie den Bruttobgehalt ein: '))

    steuern = brutto * 0.25
    krankenversicherung = brutto * (0.146/2 + 0.02)
    krankenversicherung_arbeitgeber = brutto * (0.146/2)
    pflegeversicherung = brutto * 0.035/2
    rentenversicherung = brutto * 0.186/2
    arbeitslosenversicherung = brutto * 0.026/2

    netto = brutto - krankenversicherung - pflegeversicherung - rentenversicherung - arbeitslosenversicherung - steuern
            
    print(f"Nettogehalt:   {netto:10.2f} €")
    print(f"Arbeitgeberkosten: {brutto + krankenversicherung_arbeitgeber + pflegeversicherung + rentenversicherung + arbeitslosenversicherung}")
    if brutto == 0:
       break
