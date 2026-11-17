import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Kapitalertragssteuer')
root.geometry('450x400') 
root.configure(bg='light grey')
ttk.Style().configure('TLabel', background='light grey')
ttk.Style().configure('TFrame', background='light grey')

# --- ESTO SOLUCIONA EL MOVIMIENTO ---
# Reservamos espacio para la fila 6 (donde va el resultado) 
# y evitamos que el resto de filas cambien de tamaño.
root.rowconfigure(6, minsize=80) 

lbl_titulo = ttk.Label(root, text='Kapitalertragssteuer', font=('Arial', 16, 'bold'))
lbl_titulo.grid(row=0, column=0, columnspan=3, pady=20, padx=(125, 5))

# --- CAMPOS DE ENTRADA ---
ttk.Label(root, text="Kapital (€):").grid(row=1, column=0, sticky="w", padx=(10, 5))
entry_kapital = tk.Entry(root, width=25)
entry_kapital.grid(row=1, column=0, padx=(70, 5), pady=10)

ttk.Label(root, text="Zinssatz (%):").grid(row=2, column=0, sticky="w", padx=(10, 5))
entry_zinssatz = tk.Entry(root, width=25)
entry_zinssatz.grid(row=2, column=0, padx=(70, 5), pady=10)

# --- Sección de Verheiratet ---
lbl_verheiratet = ttk.Label(root, text='Verheiratet:')
lbl_verheiratet.grid(row=3, column=0, padx=(10, 5), pady=10, sticky='w')

frame_verheiratet = ttk.Frame(root)
frame_verheiratet.grid(row=3, column=0, padx=(100, 5))
var_verheiratet = tk.StringVar(value='N')

tk.Radiobutton(frame_verheiratet, text='J', variable=var_verheiratet, value='J', 
               bg='light grey', activebackground='light grey', 
               selectcolor='white').pack(side='left')

tk.Radiobutton(frame_verheiratet, text='N', variable=var_verheiratet, value='N', 
               bg='light grey', activebackground='light grey', 
               selectcolor='white', padx=2).pack(side='left')

# --- Sección de Kirchensteuer ---
lbl_kirche = ttk.Label(root, text='Kirchensteuerpflicht:')
lbl_kirche.grid(row=4, column=0, padx=(10, 5), pady=10, sticky='w')

frame_kirche = ttk.Frame(root)
frame_kirche.grid(row=4, column=0, padx=(100, 5))
var_kirche = tk.StringVar(value='N')

tk.Radiobutton(frame_kirche, text='J', variable=var_kirche, value='J', 
               bg='light grey', activebackground='light grey', 
               selectcolor='white').pack(side='left')

tk.Radiobutton(frame_kirche, text='N', variable=var_kirche, value='N', 
               bg='light grey', activebackground='light grey', 
               selectcolor='white', padx=2).pack(side='left')

def berechnen():
    val_kapital = entry_kapital.get()
    val_zinssatz = entry_zinssatz.get()

    if val_kapital == "" or val_zinssatz == "":
        lbl_resultado.config(text='✗ Fehler: Bitte Werte eingeben.')
        return
        
    try:
        kapital = float(entry_kapital.get())
        zinssatz = float(entry_zinssatz.get())
    except ValueError:
        lbl_resultado.config(text='✗ Error: Bitte nur Ziffern eingeben')
        return

    familienstand = var_verheiratet.get()
    kirchensteuer = var_kirche.get()

    freibetrag = 1000
    zinsen = kapital * zinssatz / 100
    steuern = 0

    if familienstand == 'J':
        freibetrag = freibetrag * 2
        if zinsen > freibetrag:
            if kirchensteuer == 'J':
                steuern = (zinsen - freibetrag) * 0.2445 * (1 + 0.09)
            else:
                steuern = (zinsen - freibetrag) * 0.25

    zinsen -= steuern
    lbl_resultado.config(text=f'Bei einem Kapital de {kapital} € erhalten Sie {zinsen:.2f} € Zinsen und zahlen {steuern:.2f} € Steuern.')

btn_berechnen = tk.Button(
    root, 
    text='Berechnen', 
    bg='#949494', 
    fg='black', 
    activebackground='#B8B6B6', 
    activeforeground='#1F1F1F',
    command=berechnen
)
btn_berechnen.grid(row=5, column=0, columnspan=3, pady=15, padx=(110, 5))


lbl_resultado = ttk.Label(root, text='', wraplength=300, justify="left")

lbl_resultado.grid(row=6, column=0, columnspan=3, pady=1, padx=10, sticky='w')

root.mainloop()