import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Kapitalertragssteuer')
root.geometry('450x400')
root.configure(bg='light grey')
ttk.Style().configure('TLabel', background='light grey')
ttk.Style().configure('TFrame', background='light grey')

root.rowconfigure(6, minsize=80)

lbl_titulo = ttk.Label(root, text='Kapitalertragssteuer', font=('Arial', 16, 'bold'))
lbl_titulo.pack(pady=20)

frame_campos = ttk.Frame(root)
frame_campos.pack(anchor='w', padx=30)

# Kapital
ttk.Label(frame_campos, text="Kapital (€):").grid(row=0, column=0, sticky="w", pady=10)
entry_kapital = tk.Entry(frame_campos, width=25)
entry_kapital.grid(row=0, column=0, sticky="w", padx=(80,0), pady=10)

# Zinssatz
ttk.Label(frame_campos, text="Zinssatz (%):").grid(row=1, column=0, sticky="w", pady=10)
entry_zinssatz = tk.Entry(frame_campos, width=25)
entry_zinssatz.grid(row=1, column=0, sticky="w", padx=(80,0), pady=10)

# Verheiratet
ttk.Label(frame_campos, text='Verheiratet:').grid(row=2, column=0, sticky="w", pady=10)
frame_verheiratet = ttk.Frame(frame_campos)
frame_verheiratet.grid(row=2, column=0, sticky='w', padx=(115,0), pady=10)
var_verheiratet = tk.StringVar(value='N')
tk.Radiobutton(frame_verheiratet, text='J', variable=var_verheiratet, value='J',
               bg='light grey', activebackground='light grey',
               selectcolor='white').pack(side='left')
tk.Radiobutton(frame_verheiratet, text='N', variable=var_verheiratet, value='N',
               bg='light grey', activebackground='light grey',
               selectcolor='white', padx=2).pack(side='left')

# Kirchensteuer
ttk.Label(frame_campos, text='Kirchensteuerpflicht:').grid(row=3, column=0, sticky="w", pady=10)
frame_kirche = ttk.Frame(frame_campos)
frame_kirche.grid(row=3, column=0, sticky='w', padx=(115,0), pady=10)
var_kirche = tk.StringVar(value='N')
#Botones
tk.Radiobutton(frame_kirche, text='J', variable=var_kirche, value='J',
               bg='light grey', activebackground='light grey',
               selectcolor='white').pack(side='left')
tk.Radiobutton(frame_kirche, text='N', variable=var_kirche, value='N',
               bg='light grey', activebackground='light grey',
               selectcolor='white', padx=2).pack(side='left')

def berechnen():
    # 1. Obtener los valores como texto
    val_kapital = entry_kapital.get()
    val_zinssatz = entry_zinssatz.get()

    if val_kapital == "" or val_zinssatz == "":
        lbl_resultado.config(text='✗ Fehler: Bitte Werte eingeben.')
        return

    try:
        # 2. Reemplazar comas por puntos antes de la conversión
        val_kapital = val_kapital.replace(',', '.')
        val_zinssatz = val_zinssatz.replace(',', '.')
        
        # 3. Convertir a float
        kapital = float(val_kapital)
        zinssatz = float(val_zinssatz)
        
    except ValueError:
        lbl_resultado.config(text='✗ Error: Bitte nur Ziffern eingeben')
        return


    familienstand = var_verheiratet.get()
    kirchensteuer = var_kirche.get()
    freibetrag = 1000
    zinsen = kapital * zinssatz / 100
    steuern = 0

    if familienstand == 'J':
        freibetrag *= 2
        if zinsen > freibetrag:
            if kirchensteuer == 'J':
                steuern = (zinsen - freibetrag) * 0.2445 * 1.09
            else:
                steuern = (zinsen - freibetrag) * 0.25

    zinsen -= steuern
    lbl_resultado.config(
        text=f'Bei einem Kapital von {kapital} € erhalten Sie '
             f'{zinsen:.2f} € Zinsen und zahlen {steuern:.2f} € Steuern.'
    )

btn_berechnen = tk.Button(
    root, text='Berechnen',
    bg='#949494', fg='black',
    activebackground='#B8B6B6', activeforeground='#1F1F1F',
    command=berechnen
)
btn_berechnen.pack(pady=15)

lbl_resultado = ttk.Label(root, text='', wraplength=350, justify="left")
lbl_resultado.pack(padx=10, anchor='w')

root.mainloop()