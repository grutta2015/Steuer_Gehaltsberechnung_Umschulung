# Programm Kapertragsteuer / zur Ermittlung der Kapitalertragsteuer und Zinsen
# inputl: Kapital, zinssatz, familienStand, freibetrag, kirchensteuer.
# return: zinsen, steuern

def ziffern_anfordern(mensaje, tipo=int):
    while True:
        try:
            return tipo(input(mensaje))
        except ValueError:
            print(' ✗ Error: Bitte nur Ziffern eingeben')

def ja_nein_anfordern(mensaje):
    while True:
        entrada = input(mensaje).lower().strip()
        if entrada in ('j', 'n'):
            return entrada
        print(' ✗ Error: Bitte nur J/N eingeben')


kapital = ziffern_anfordern('Kapital: ', float)
zinssatz = ziffern_anfordern('Zinssatz: ', float)
familienstand = ja_nein_anfordern('Verheiratet J/N: ')
kirchensteuer = ja_nein_anfordern('Kirchensteuerpflicht J/N: ')

freibetrag = 1000

zinsen = kapital * zinssatz / 100

steuern = 0


if familienstand == 'j':
    freibetrag = freibetrag * 2
        
    if zinsen > freibetrag:
        if kirchensteuer == 'j':
           steuern = (zinsen - freibetrag) * 0.2445 * (1 + 0.09)
        else:
            steuern = (zinsen - freibetrag) * 0.25
    
zinsen -= steuern

print('Beim  einem Kapital von ', kapital,
       '€ erhalten Sie eine Zinssatz von', zinssatz,'%,', zinsen, '€ Zinsen und zahlen', steuern,
      '€ Steuern.')
