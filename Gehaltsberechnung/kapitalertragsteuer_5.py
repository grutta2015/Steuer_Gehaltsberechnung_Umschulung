import tkinter as tk


#### Configuración de la ventana principal
root = tk.Tk()
root.title('Kapitalertragssteuer')
root.geometry('450x450')
root.configure(bg='light grey')

#### Funcion Principal

def berechnen():
    # 1. CAPTURA DE DATOS Y LIMPIEZA
    # Obtenemos el texto de los campos de entrada
    val_kapital = entry_kapital.get()
    val_zinssatz = entry_zinssatz.get()

    # 2. VALIDACIÓN INICIAL
    # Verificamos si los campos están vacíos
    if val_kapital == "" or val_zinssatz == "":
        lbl_resultado.config(text='✗ Fehler: Bitte Werte eingeben.', fg='red')
        return

    # 3. INICIALIZACIÓN POR SEGURIDAD (Buena práctica)
    # Definimos valores base para que las variables existan siempre.
    #  Captura (val_kapital): Primero guardamos lo que el usuario escribió en una variable de texto.
    #  Inicialización (kapital = 0.0): Aquí creamos la variable numérica con un valor de seguridad.
    #  Conversión (kapital = float(...)): Inmediatamente después, sobrescribimos ese 0.0
    #  con el valor real que el usuario ingresó.
    kapital = 0.0
    zinssatz = 0.0
    zinsen = 0.0
    steuern = 0.0
    freibetrag = 1000  # Valor base de exención

    try:
        # Reemplazamos coma por punto y convertimos a número decimal
        kapital = float(val_kapital.replace(',', '.'))
        zinssatz = float(val_zinssatz.replace(',', '.'))
    except ValueError:
        # Si el usuario ingresó letras, salimos del cálculo
        lbl_resultado.config(text='✗ Error: Bitte nur Ziffern eingeben', fg='red')
        return

    # 4. LÓGICA DE CÁLCULO
    familienstand = var_verheiratet.get()
    kirchensteuer = var_kirche.get()
    
    # Calculamos el interés bruto
    zinsen = kapital * zinssatz / 100

    # Ajustamos la exención si está casado
    if familienstand == 'J':
        freibetrag *= 2

    # Solo calculamos impuestos si los intereses superan la exención
    if zinsen > freibetrag:
        interes_imponible = zinsen - freibetrag
        
        if kirchensteuer == 'J':
            # Tasa con impuesto eclesiástico
            steuern = interes_imponible * 0.2445 * 1.09
        else:
            # Tasa estándar (25%)
            steuern = interes_imponible * 0.25

    # Calculamos el interés neto (lo que realmente recibe el usuario)
    zinsen_netto = zinsen - steuern

    # 5. MOSTRAR RESULTADO
    # Usamos :.2f para mostrar solo 2 decimales
    lbl_resultado.config(
        text=f'Bei einem Kapital von {kapital:.2f} € erhalten Sie '
             f'{zinsen_netto:.2f} € Zinsen und zahlen {steuern:.2f} € Steuern.',
        fg='black'
    )
    

#### Título
lbl_titulo = tk.Label(root, text='Kapitalertragssteuer', font=('Arial', 16, 'bold'), bg='light grey')
lbl_titulo.pack(pady=20)

#### Contenedor principal de campos
frame_campos = tk.Frame(root, bg='light grey')
frame_campos.pack(anchor='w', padx=30)

#### Campo: Kapital
tk.Label(frame_campos, text="Kapital (€):", bg='light grey').grid(row=0, column=0, sticky="w", pady=10)
entry_kapital = tk.Entry(frame_campos, width=25)
entry_kapital.grid(row=0, column=0, sticky="w", padx=77, pady=10)

#### Campo: Zinssatz
tk.Label(frame_campos, text="Zinssatz (%):", bg='light grey').grid(row=1, column=0, sticky="w", pady=10)
entry_zinssatz = tk.Entry(frame_campos, width=25)
entry_zinssatz.grid(row=1, column=0, sticky="w", padx=77, pady=10)

#### Campo: Verheiratet
tk.Label(frame_campos, text='Verheiratet:', bg='light grey').grid(row=2, column=0, sticky="w", pady=10)
frame_verheiratet = tk.Frame(frame_campos, bg='light grey')
frame_verheiratet.grid(row=2, column=0, sticky='w', padx=160)

var_verheiratet = tk.StringVar(value='N')
tk.Radiobutton(frame_verheiratet, text='J', variable=var_verheiratet, value='J', 
               bg='light grey', activebackground='light grey', selectcolor='white').pack(side='left')
tk.Radiobutton(frame_verheiratet, text='N', variable=var_verheiratet, value='N', 
               bg='light grey', activebackground='light grey', selectcolor='white').pack(side='left')

#### Campo: Kirchensteuer
tk.Label(frame_campos, text='Kirchensteuerpflicht:', bg='light grey').grid(row=3, column=0, sticky="w", pady=10)
frame_kirche = tk.Frame(frame_campos, bg='light grey')
frame_kirche.grid(row=3, column=0, sticky='w', padx=160)

var_kirche = tk.StringVar(value='N')
tk.Radiobutton(frame_kirche, text='J', variable=var_kirche, value='J', 
               bg='light grey', activebackground='light grey', selectcolor='white').pack(side='left')
tk.Radiobutton(frame_kirche, text='N', variable=var_kirche, value='N', 
               bg='light grey', activebackground='light grey', selectcolor='white').pack(side='left')

#### Botón de cálculo
btn_berechnen = tk.Button(
    root, text='Berechnen',
    bg='#949494', fg='black',
    activebackground='#B8B6B6', activeforeground='#1F1F1F',
    command=berechnen
)
btn_berechnen.pack(pady=20)

#### Etiqueta de resultado
lbl_resultado = tk.Label(root, text='', wraplength=380, justify="left", bg='light grey', font=('Arial', 10))
lbl_resultado.pack(padx=20, fill='x')

root.mainloop()