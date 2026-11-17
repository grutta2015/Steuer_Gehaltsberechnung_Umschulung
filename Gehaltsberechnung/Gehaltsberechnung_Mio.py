class Sozialversicherungen:
    def __init__(self):
        self.kv = 14.6
        self.pv = 3.5
        self.rv = 18.6
        self.av = 2.6

# 1. Definición de funciones (deben estar antes de ser llamadas)

def rechnen_sozial_arbeitgeber(brutto, sv):
    arbeitgeber_kv = brutto * (sv.kv / 200)
    arbeitgeber_pv = brutto * (sv.pv / 200)
    arbeitgeber_rv = brutto * (sv.rv / 200)
    arbeitgeber_av = brutto * (sv.av / 200)
   
    return arbeitgeber_kv + arbeitgeber_pv + arbeitgeber_rv + arbeitgeber_av

def rechnen_sozial_arbeitnehmer(brutto, sv):
    arbeitnehmer_kv = brutto * ((sv.kv / 200) + 0.02)
    arbeitnehmer_pv = brutto * (sv.pv / 200)
    arbeitnehmer_rv = brutto * (sv.rv / 200)
    arbeitnehmer_av = brutto * (sv.av / 200)
    return arbeitnehmer_kv + arbeitnehmer_pv + arbeitnehmer_rv + arbeitnehmer_av

def rechnen_steuern(brutto, steuern):    
    return brutto * steuern / 100

def rechnen_netto(brutto, steuern, sozialversicherungen):
    return brutto - steuern - sozialversicherungen

def validar_numero(numero_ingresado):
    while True:
        validar = input(numero_ingresado).strip() # .strip() elimina espacios accidentales al inicio/final
        try:
            return float(validar)
        except ValueError:
            print("Error: Por favor, ingresa solo números (usa punto para decimales).")
            
# 2. Inicio del programa

sozialversicherung = Sozialversicherungen()

print(' ' * 5 + '*** Gehaltsberechnung ***\n')
print("+" + "-" * 35 + "+")
print(f"| {'Sozialversicherungen':^32}  |")
print("|" + "-" * 35 + "|")
print(f"| Krankenversicherung      {sozialversicherung.kv:>7}% |")
print(f"| Pflegeversicherung       {sozialversicherung.pv:>7}% |")
print(f"| Rentenversicherung       {sozialversicherung.rv:>7}% |")
print(f"| Arbeitslosenversicherung {sozialversicherung.av:>7}% |")
print("+" + "-" * 35 + "+")

brutto_ingresado = validar_numero('Geben Sie den Bruttobgehalt ein: ')
steuern_ingresado = validar_numero('Geben Sie den Steuernbetrag ein: (en %): ')

# 3. Asignación de resultados a variables para poder imprimirlas
# Usamos el objeto 'sozialversicherung' que creamos arriba
sozialversicherungen_rechnen = rechnen_sozial_arbeitnehmer(brutto_ingresado, sozialversicherung)
steuern_rechnen = rechnen_steuern(brutto_ingresado, steuern_ingresado)
netto_rechnen = rechnen_netto(brutto_ingresado, steuern_rechnen, sozialversicherungen_rechnen)

# Cálculos opcionales para el empleador si los necesitas imprimir:
total_arbeitgeber = rechnen_sozial_arbeitgeber(brutto_ingresado, sozialversicherung)

print('\n')
print(f'Brutto:               {brutto_ingresado:>10.2f} €\n')
print(f'Steuern:              {steuern_rechnen:>10.2f} €')
print(f'Sozialversicherungen: {sozialversicherungen_rechnen:>10.2f} €')
print('-' * 40)
print(f'Netto:                {netto_rechnen:>10.2f} €')