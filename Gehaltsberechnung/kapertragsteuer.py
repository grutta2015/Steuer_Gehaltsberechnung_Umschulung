# Programm Kapertragsteuer / zur Ermittlung der Kapitalertragsteuer und Zinsen
# inputl: Kapital, zinssatz, familienStand, freibetrag, kirchensteuer.
# return: zinsen, steuern

kapital = float(input('Kapital: '))
zinssatz = float(input('Zinssatz: '))
familienstand = input('Verheiratet j/n: ').lower().strip()
kirchensteuer = input('Kirchensteuerpflicht j/n: ').lower().strip()


freibetrag = 1000

zinsen = kapital * zinssatz / 100

if familienstand == 'j':
    if zinsen > (freibetrag * 2):
        if kirchensteuer == 'j':
           steuer = (zinsen - freibetrag * 2) * 0.2445 * (1 + 0.09)
        else:
           steuer = (zinsen - freibetrag * 2) * 0.25
    else:
        steuer = 0
else:
    if zinsen > freibetrag:
        if kirchensteuer == 'j':
           steuer = (zinsen - freibetrag) * 0.2445 * (1 + 0.09)
        else:
            steuer = (zinsen - freibetrag) * 0.25
    else:
        steuer = 0
        
zinsen -= steuer

print('Beim  einem Kapital von ', kapital,
       '€ erhalten Sie eine Zinssatz von', zinssatz,'%,', zinsen, '€ Zinsen und zahlen', steuer,
      '€ Steuern.')
