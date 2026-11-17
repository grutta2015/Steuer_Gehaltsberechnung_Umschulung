# Programm zur Ermittulng der Lohnsteuer, des Solidartitätsbeitrags und der
# Bemmessunggrundlage Kirchensteuer für 2026.

# Eingangsparameter
AF = AJAHR = ALTER1 = ALV = F = JFREIB = JHINZU = JRE4 = JRE4ENT = JVBEZ = 0
KRV = KVZ = LZZFREIB = LZZHINZU = PVS = PVZ = PVA = 0
MBV = PKPV = PKPVAGZ = PKV = R = RE4 = SONSTB = SONSTENT = STERBE = 0 
VBEZ = VBEZM = VBEZS = VBS = VJAHR = ZKF = ZMVB = 0
STKL = 4
LZZ = 1


# Interne Variablen
ALTE =  0

# Ausgabeparameter
BK = LSTLZZ = SOLZLZZ = 0 #BKS =? necesito?

def eingeben(): #STKL, RE4, ZKF, R
    RE4 = int(input('Bruttogehalt:                             '))
    STKL = int(input('Steuerklasse 1-2:                        '))
    LZZ = int(input('Zeitraum (1-Jahr, 2_Monat, 3-Woche, 4-Tag)'))
    ZKF = float(input('Kinder 0.5, 1, 1.5...:                  '))
    R = int(input('Kirchensteuer 0-Nein 1-Ja :                 '))
    
def ausgeben(): #LSTLZZ, SOLZLZZ, BK
    print('Lohnsteuer für 2026:    ', LSTLZZ)
    print('Soli für 2026:          ', SOLZLZZ)
    print('Bemessungsgrundlage:    ', BK)

def MRE4():
    print(MRE4)

def MRE4JL():
    print(MRE4JL)
  
    if LZZ == 1:
        ZRE4J = RE4 / 100
        ZVBEZJ = VBEZ / 100
        JLFREIB = LZZFREIB / 100
        JLHINZU = LZZHINZU / 100        
    elif LZZ == 2:
        ZRE4J = RE4 * 12 / 100
        ZVBEZJ = VBEZ * 12 / 100
        JLFREIB = LZZFREIB * 12 / 100
        JLHINZU = LZZHINZU * 12 / 100
    elif LZZ == 3:
        ZRE4J = RE4 * 360 / 7 / 100
        ZVBEZJ = VBEZ * 360 / 7 / 100
        JLFREIB = LZZFREIB * 360 / 7 / 100
        JLHINZU = LZZHINZU * 360 / 7 / 100
    else:
        ZRE4J = RE4 * 360 / 100
        ZVBEZJ = VBEZ * 360 / 100
        JLFREIB = LZZFREIB * 360 / 100
        JLHINZU = LZZHINZU * 360 / 100

    if AF == 0:
        F = 1
     
    
def MPARA():
    global BBGRVALV
    global PVS
    global PVA
    BBGRVALV = 101400
    AVSATZAN = 0.0130
    RVSATZAN = 0.0930
    BBGKVPV = 69750
    KVSATZAN = KVZ / 2 / 100 + 0.07
    
    if PVS == 1:
        PVSATZAN = 0.023
    else:
        PVSATZAN = 0.018
    if PVZ == 1:
        PVSATZAN = PVSATZAN + 0.006
    else:
        PVSATZAN = PVSATZAN - PVA * 0.0025
    
    W1STKL5 = 14071
    W2STKL5 = 34939
    W3STKL5 = 222260
    GFB = 12348
    SOLZFREI = 20350

  

# Hauptprogramm
eingeben()

MPARA()
MRE4JL()
VBEZBSO = 0
MRE4()
# MRE4ABZ()
# MBERECH()
# MSONST()


ausgeben()


