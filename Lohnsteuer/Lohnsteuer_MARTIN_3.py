# Programm zur Ermittulng der Lohnsteuer, des Solidartitätsbeitrags und der
# Bemmessunggrundlage Kirchensteuer für 2026.

# Eingangsparameter
# import math
# import decimal
# 
# 
# AF = AJAHR = ALTER1 = ALV = F = JFREIB = JHINZU = JRE4 = JRE4ENT = JVBEZ = 0
# KRV = LZZFREIB = LZZHINZU = PVS = PVA = 0
# MBV = PKPV = PKPVAGZ = PKV = R = RE4 = SONSTB = SONSTENT = STERBE = 0 
# VBEZ = VBEZM = VBEZS = VBS = VJAHR = ZKF = ZMVB = 0
# STKL = 1 # lo cambie por 1
# LZZ = 1
# PVZ = 0 # era 0
# KVZ = 2.90 # era 0
# 
# 
# 
# # Interne Variablen
# ALTE = ANP = ANTEIL1 = AVSATZAN= BBGKVPV = BBGRVALV = BMG = DIFF = EFA = 0
# FVB = FVBSO = FVBZSO = FVBZ = GFB = HBALTE = HFVB = HFVBZ = HFVBZSO = HOCH = 0
# J = JBMG = JLFREIB = JLHINZU = JW = K = KFB = KVSATZAN = KZTAB = LSTJAHR = 0
# LSTOSO = LSTSO = MIST = PKPVAGZJ = PVSATZAN = RVSATZAN = RW = SAP = 0
# SOLZFREI = SOLZJ = SOLZMIN = SOLZSBMG = SOLZSZVE = ST = ST1 = ST2 = 0
# VBEZB = VBEZBSO = VERGL = VSPHB = VSP = VSPN = VSPALV = VSPKVPV = 0
# VSPR = W1STKL5 = W2STKL5 = W3STKL5 = X = Y = ZRE4 = ZRE4J = ZRE4VP = 0
# ZRE4VPR = ZTABFB = ZVBEZ =ZVBEZJ = ZVE = ZX = ZZX = 0
# VFRB = WVFRB = VFRBS1 = VFRBS2 = WVFRBO = 0
# 
# 
# # Ausgabeparameter
# BK = BKS = LSTLZZ = SOLZLZZ = SOLZS = STS = WVFRBM = 0 #BKS =? necesito?

# Programm zur Ermittlung der Lohnsteuer, des Solidiaritätsbeitrags und der Bemessungsgrundlage Kirchensteuer für 2026
#import
import math

# Eingangsparameter
AF, AJAHR, ALTER1, ALV = 0, 0, 0, 0
F = 0
JFREIB, JHINZU, JRE4, JRE4ENT, JVBEZ = 0, 0, 0, 0, 0
KRV, KVZ = 0, 0
LZZ, LZZFREIB, LZZHINZU = 0, 0, 0
MBV = 0
PKPV, PKPVAGZ, PKV, PVA,PVS, PVZ = 0, 0, 0, 0, 0, 0
R, RE4 = 0, 0
SONSTB, SONSTENT, STERBE, STKL = 0, 0, 0, 0
VBEZ, VBEZM, VBEZS , VBS, VJAHR = 0, 0, 0, 0, 0
ZKF, ZMVB = 0, 0

# interne Variablen
ALTE, ANP, ANTEIL1, AVSATZAN = 0, 0, 0, 0
BBGKVPV, BBGRVALV, BMG = 0, 0, 0
DIFF = 0
EFA = 0
FVB, FVBSO, FVBZ, FVBZSO = 0, 0, 0, 0
GFB = 0
HBALTE, HFVB, HFVBZ, HFVBZSO, HOCH = 0, 0, 0, 0, 0
J, JBMG, JLFREIB, JLHINZU, JW = 0, 0, 0, 0, 0
KFB, KVSATZAN, KZTAB = 0, 0, 0
LSTJAHR, LSTOSO, LSTSO = 0, 0, 0
MIST = 0
PKPVAGZJ, PVSATZAN, RVSATZAN = 0, 0, 0
RW = 0
SAP, SOLZ, SOLZFREI, SOLZJ, SOLZMIN, SOLZSBMG, SOLZSZVE, ST, ST1, ST2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
VBEZB, VBEZBSO, VERGL, VSPHB, VSP, VSPN, VSPALV, VSPKVPV, VSPR = 0, 0, 0, 0, 0, 0, 0, 0, 0
W1STKL5, W2STKL5, W3STKL5 = 0, 0, 0
X = 0
Y = 0
ZRE4, ZRE4J, ZRE4VP, ZRE4VPR, ZTABFB, ZVBEZ, ZVBEZJ, ZVE, ZX, ZZX = 0, 0, 0, 0, 0, 0, 0, 0, 0,0

# Ausgangsparameter
BK, BKS = 0, 0
LSTLZZ = 0
SOLZLZZ, SOLZS, STS = 0, 0, 0
WVFRBM = 0

def date_anfordern(mensaje, tipo=int):
    while True:
        try:
            # Intentamos convertir al tipo de dato pedido (int o float)
            return tipo(input(mensaje))
        except ValueError:
            print(' ✗ Error: Bitte nur Ziffern eingeben')



def eingeben(): #STKL, RE4, ZKF, R
   
#     global R, RE4, ZKF, STKL, LZZ
    global RE4, STKL, LZZ, ZKF, R
    global KVZ, ALV, KRV, PKV, PVZ, PVS, PVA
    global LZZFREIB, LZZHINZU
    
    r = 50
    print('┌' + '─' * r + '┐')
    print('│' + '  Lohnsteuerberechnung 2026'.center(r) + '│')
    print('└' + '─' * r + '┘')
    w = 35

    # Ahora pides cada dato de forma independiente
    # Si el error ocurre en LZZ, solo repetirá LZZ
    RE4  = int(date_anfordern('  ' + 'Bruttogehalt (Euro):'.ljust(w), float) * 100)
    STKL = date_anfordern('  ' + 'Steuerklasse (1-6):'.ljust(w))
    LZZ  = date_anfordern('  ' + 'Zeitraum (1=J 2=M 3=W 4=T):'.ljust(w))
    ZKF  = date_anfordern('  ' + 'Kinderfreibetrag (0, 0.5...):'.ljust(w), float)
    R    = date_anfordern('  ' + 'Kirchensteuer (0=Nein 1=Ja):'.ljust(w))
    
    KVZ = 2.90
    if STKL ==2:
        PVZ = 0
    else:
        PVZ = 1
    AF = 0
    F = 1
    
    
def ausgeben(): #LSTLZZ, SOLZLZZ, BK
    global LSTLZZ, SOLZLZZ, BK
    
    KiSt = BK / 100 * 0.09
#     print('Lohnsteuer für 2026:    ', LSTLZZ / 100)
#     print('Soli für 2026:          ', SOLZLZZ / 100)
#     print('Bemessungsgrundlage:    ', BK / 100)

   
    l1 = 'Lohnsteuer 2026:'
    l2 = 'Solidaritätszuschlag:'
    l3 = 'Bemessungsgrundlage KiSt:'
    l4 = 'Kirchensteuer Berlin (9%):'
    v1 = f'{LSTLZZ/100:.2f}'
    v2 = f'{SOLZLZZ/100:.2f}'
    v3 = f'{BK/100:.2f}'
    v4 = f'{KiSt:.2f}'
    
    w = 50
    print()
    print('┌' + '─' * w + '┐')
    print('│' + ' Lohnsteuerberechnung 2026 '.center(w) + '│')
    print('├' + '─' * w + '┤')
    print('│  ' + l1.ljust(w-len(v1)-7) + v1 + ' €   │')
    print('│  ' + l2.ljust(w-len(v2)-7) + v2 + ' €   │')
    print('│  ' + l3.ljust(w-len(v3)-7) + v3 + ' €   │')
    print('│  ' + l4.ljust(w-len(v4)-7) + v4 + ' €   │')
    print('└' + '─' * w + '┘')

def TAB1(J):
    if J < 17:
        return (0.400 - (J -1) * 0.016)
    if J > 16 and J < 19: # 17 und 18
        return (0.160 - (J -16) * 0.008)
    if J > 18:
        return (0.144 - (J -18) * 0.004)
    
def TAB2(J):
    if J < 17:
        return (3000 - (J -1) * 120)
    if J > 16 and J < 19: # 17 und 18
        return (1200 - (J -16) * 60)
    if J > 18:
        return (1080 - (J -18) * 30)
    
def TAB3(J):
    if J < 17:
        return (900 - (J -1) * 36)
    if J > 16 and J < 19: # 17 und 18
        return (360 - (J -16) * 18)
    if J > 18:
        return (324 - (J -18) * 9)
    
def TAB4(K):
    if K < 17:
        return (0.400 - (K -1) * 0.016)
    if K > 16 and J < 19: # 17 und 18
        return (0.160 - (K -16) * 0.008)
    if K > 18:
        return (0.144 - (K -18) * 0.004)
def TAB5(K):
    if K < 17:
        return(1900 - (K - 1) * 76)
    if K > 16 and K < 19: # NUR 17 und 18
        return(760 - (K - 16) * 38)
    if K > 18:
        return(684 - (K - 18)* 19)

def UPTAB26():
    global X, GFB, ST, RW, Y, KZTAB
    
    GFB = 12348 # Ajustado al valor de tu MPARA
    
    if X < GFB + 1:
        ST = 0
    else:
        if X < 17800:
            Y = (X - GFB) / 10000
            RW = Y * 914.51
            RW = RW + 1400
            ST = math.floor(RW * Y)
        elif X < 69879:
            Y = (X - 17799) / 10000
            RW = Y * 173.1
            RW = RW + 2397
            RW = RW * Y
            ST = math.floor(RW + 1034.87)
        elif X < 277826:
            ST = math.floor(X * 0.42 - 11135.63)
        else:
            ST = math.floor(X * 0.45 - 19470.38)
            
    ST = ST * KZTAB
        
def MRE4SONST():
    global FVB, FVBSO, ZRE4VP, MBV, JRE4ENT, FVBZ, FVBZSO, SONSTENT, VFRBS2, ANP, VFRBS1
    
    MRE4()
    FVB = FVBSO
    MRE4ABZ()
    ZRE4VP = ZRE4VP + MBV / 100 - JRE4ENT / 100 - SONSTENT / 100 
    FVBZ = FVBZSO
    MZTABFB()
    VFRBS2 = (ANP + FVB + FVBZ) * 100 - VFRBS1
        
def MOSONST():
    global ZRE4J, ZVBEZJ, JLFREIB, JLHINZU, ZRE4VP, VFRBS1, WVFRBO, LSTOSO
    
    ZRE4J = JRE4 / 100
    ZVBEZJ = JVBEZ / 100
    JLFREIB = JFREIB / 100
    JLHINZU = JHINZU / 100
    
    MRE4()
    MRE4ABZ()
    
    ZRE4VP = ZRE4VP - JRE4ENT / 100
    MZTABFB()
    
    VFRBS1 = (ANP + FVB + FVBZ) * 100
    MLSTJAHR()
    
    WVFRBO = (ZVE - GFB) * 100
    
    if WVFRBO < 0:
        WVFRBO = 0
        
    LSTOSO = ST * 100

def MSOLZSTS():
    global ZKF, KFB, SOLZSZVE, ZVE, X, KZTAB, STKL, SOLZSBMG, ST, F, SOLZFREI, SOLZS, STS
    
    if ZKF > 0:
        SOLZSZVE = ZVE - KFB
    else:
        SOLZSZVE = ZVE
    
    if SOLZSZVE < 1:
        SOLZSZVE = 0
        X = 0
    else:
        X = math.floor(SOLZSZVE / KZTAB)
    
    if STKL < 5:
        UPTAB26()
    else:
        MST5_6()
    
    SOLZSBMG = math.floor(ST * F)
    
    if SOLZSBMG > SOLZFREI:
        SOLZS = math.floor(STS * 5.5 / 100)
    else:
        SOLZS = 0

def STSMIN():
    global BKS, STS, LSTLZZ, SOLZLZZ, BK, SOLZS, MBV, R
    
    if STS < 0:
        if MBV == 0:
            pass
        else:
            LSTLZZ = LSTLZZ + STS
            if LSTLZZ < 0:
                LSTLZZ = 0
            SOLZLZZ = math.floor(SOLZLZZ + STS * 5.5 / 100) #### esta bien?
            
            if SOLZLZZ < 0:
                SOLZLZZ = 0
                
            BK = BK + STS
            if BK < 0:
                BK = 0
                
            STS = 0
            SOLZS = 0
    else:
        MSOLZSTS()
    
    if R > 0:
        BKS = STS
    else:
        BKS = 0
        
def MSONST():
    global ZMVB, SONSTB, MBV, LSTSO, STS, SOLZS, BKS, LZZ
    global ZRE4J, ZVBEZJ, JVBEZ, JRE4, VBS, VBEZBSO, STERBE, WVFRBM, ST
    
    LZZ = 1
    if ZMVB == 0:
        ZMVB = 12
    if SONSTB == 0 and MBV == 0:
        LSTSO = 0
        STS = 0
        SOLZS = 0
        BKS = 0
    else:
        MOSONST()
        ZRE4J = (JRE4 + SONSTB) / 100
        ZVBEZJ = (JVBEZ + VBS) / 100
        VBEZBSO = STERBE
        MRE4SONST()
        MLSTJAHR()
        WVFRBM = (ZVE - GFB) * 100
        
    if WVFRBM < 0:
        WVFRBM = 0
    
    LSTSO = ST * 100
    STS = math.floor((LSTSO - LSTOSO) * F) 
    if STS < 0: # esto lo puse yo
        STS = 0 # esto lo puse yo
    STSMIN()
    
def UPANTEIL():
    global ANTEIL1, JW, LZZ #
    
    if LZZ == 1:
        ANTEIL1 = JW
    elif LZZ == 2: 
        ANTEIL1 = math.floor(JW / 12)
    elif LZZ == 3: 
        ANTEIL1 = math.floor(JW * 7 / 360)
    else: 
        ANTEIL1 = math.floor(JW / 360)
    
def MSOLZ():
    global SOLZFREI, KZTAB, JBMG, SOLZJ, SOLZMIN, JW, SOLZLZZ, ANTEIL1, R, BK
    
    SOLZFREI = SOLZFREI * KZTAB
    
    if JBMG > SOLZFREI:
        SOLZJ = math.floor(JBMG * 5.5 / 100)
        SOLZMIN = (JBMG - SOLZFREI) * 11.9 / 100
        if SOLZMIN < SOLZJ:
            SOLZJ = SOLZMIN
        JW = SOLZJ * 100
        UPANTEIL()
        SOLZLZZ = ANTEIL1
        
    else:
        SOLZLZZ = 0
        
    if R > 0:
        JW = JBMG * 100
        UPANTEIL()
        BK = ANTEIL1
    else:
        BK = 0
    
def UP5_6():
    global X, ST, ST1, ST2, DIFF, MIST
    
    X = math.floor(ZX * 1.25)
    UPTAB26()
    ST1 = ST
    X = math.floor(ZX * 0.75)
    UPTAB26()
    ST2 = ST
    DIFF = (ST1 - ST2) * 2
    MIST = math.floor(ZX * 0.14)
    
    if MIST > DIFF:
        ST = MIST
    else:
        ST = DIFF
    
def MST5_6():
    global ZZX, X, ZX, W2STKL5, W2STKL, ST, W1STKL5, W3STKL5, VERGL, HOCH
    
    ZZX = X
    
    if ZZX > W2STKL5:
        ZX = W2STKL5
        UP5_6()
        if ZZX > W3STKL5:
            ST = math.floor(ST + (W3STKL5 - W2STKL5) * 0.42)
            ST = math.floor(ST + (ZZX - W3STKL5) * 0.45)
        else:
            ST = math.floor(ST + (ZZX - W2STKL5) * 0.42)
    else:
        ZX = ZZX
        UP5_6()
        if ZZX > W1STKL5:
            VERGL = ST
            ZX = W1STKL5
            UP5_6()
            HOCH = math.floor(ST + (ZZX - W1STKL5) * 0.42)
            if HOCH < VERGL:
                ST = HOCH
            else:
                ST = VERGL
    
def MVSPHB():
    global VSPN, VSP, VSPHB, ZRE4VP, BBGRVALV, ZRE4VPR, AVSATZAN, VSPALV, VSPKVPV, VSPR
    
    if ZRE4VP > BBGRVALV:
        ZRE4VPR = BBGRVALV
    else:
        ZRE4VPR = ZRE4VP
        
    VSPALV = AVSATZAN * ZRE4VPR
    
    VSPHB = VSPALV + VSPKVPV
    
    if VSPHB > 1900:
        VSPHB = 1900
        
    VSPN = math.ceil(VSPR + VSPHB)
    
    if VSPN > VSP:        
        VSP = VSPN
        
  #  VSP = VSPN  # ← reemplazar el if VSPN > VSP
        
def MVSPKVPV():
    global ZRE4VPR, VSPKVPV, VSP, PKPVAGZJ
    
    if ZRE4VP > BBGKVPV:
        ZRE4VPR = BBGKVPV
    else:
        ZRE4VPR = ZRE4VP
    
    if PKV > 0:
        if STKL == 6:
            VSPKVPV = 0
        else:
            PKPVAGZJ = PKPVAGZ * 12 / 100
            VSPKVPV = PKPV * 12 / 100
            VSPKVPV = VSPKVPV - PKPVAGZJ
            
            if VSPKVPV < 0:
                VSPKVPV = 0    
    else:
        VSPKVPV = ZRE4VPR * (KVSATZAN + PVSATZAN)
    
    VSP = math.ceil(VSPKVPV + VSPR)

def UPEVP():
    global VSPR, ZRE4VPR, KRV, ZRE4VP, BBGRVALV, RVSATZAN, ALV, STKL
    
    if KRV == 1:
        VSPR = 0
    else:
        if ZRE4VP > BBGRVALV:
            ZRE4VPR = BBGRVALV
        else:
            ZRE4VPR = ZRE4VP
        
        VSPR = ZRE4VPR * RVSATZAN
    
    MVSPKVPV()
    
    if ALV == 1:
        pass  # El diagrama va directo al ENDE (Ja)
    else:
        if STKL == 6:
            pass  # El diagrama va directo al ENDE (Ja)
        else:
            MVSPHB() # Se llama a la subrutina

def UPMLST():
    global ZVE, X, STKL, KZTAB, ST
    
    if ZVE < 1:
        ZVE = 0
        X = 0
    else:
        X = math.floor(ZVE / KZTAB) # esta bien?
        
    if STKL < 5:
        UPTAB26()
    else:
        MST5_6()

def UPLSTLZZ():
    global JW, LSTLZZ, ANTEIL1, LSTJAHR
    
    JW = LSTJAHR * 100 
    UPANTEIL()
    LSTLZZ = ANTEIL1
    
def MLSTJAHR():
    
    global ZVE, ZRE4, ZTABFB, VSP
        
    UPEVP()
    ZVE = ZRE4 -ZTABFB - VSP
    UPMLST ()


def MZTABFB():
    
    global ANP, ZVBEZ, FVBZ, FVBZSO, ZRE4, KZTAB, STKL, SAP, KFB, ZKF, STKL, EFA, ZTABFB
    
    ANP = 0
    EFA = 0    # ← TRAMPA esto no esta en el programmablaufplan
    SAP = 0    # ← TRAMPA esto no esta en el programmablaufplan
    
    if ZVBEZ >= 0:
        if ZVBEZ < FVBZ:
            FVBZ = ZVBEZ    
    if STKL < 6:
        if ZVBEZ > 0:
            if ZVBEZ - FVBZ < 102:
                ANP = math.ceil(ZVBEZ - FVBZ) # esta bien esto?
            else:
                ANP = 102   
    else:
        FVBZ = 0
        FVBZSO = 0
        
    if STKL < 6:
        if ZRE4 > ZVBEZ:
            if ZRE4 - ZVBEZ < 1230:
                ANP = math.ceil(ANP + ZRE4 - ZVBEZ) # esta bien esto?
            else:
                ANP = ANP + 1230    
    KZTAB = 1
    
    if STKL == 1:
        SAP = 36
        KFB = ZKF * 9756
    else:
        if STKL == 2:
            EFA = 4260
            SAP = 36
            KFB = ZKF * 9756
        elif STKL == 3:
            KZTAB = 2
            SAP = 36
            KFB = ZKF * 9756
        elif STKL == 4:
            SAP = 36
            KFB = ZKF * 4878
        elif STKL == 5:
            SAP = 36
            KFB = 0
        else:
            KFB = 0
        
    ZTABFB = EFA + ANP + SAP + FVBZ



def MBERECH():
    global ZTABFB, KFB, VFRB, ANP, FVB, FVBZ, ZVE, GFB, WVFRB, LSTJAHR, ST, F, JBMG
    
    MZTABFB()
    VFRB = (ANP + FVB + FVBZ) * 100
    MLSTJAHR()
    WVFRB = (ZVE - GFB) * 100
    
    if WVFRB < 0:
        WVFRB = 0
        
    LSTJAHR = ST * F
    UPLSTLZZ()
    
    if ZKF > 0:
        ZTABFB = ZTABFB + KFB
        MRE4ABZ()
        MLSTJAHR()
        JBMG = ST * F
    else:
        JBMG = LSTJAHR
        
    MSOLZ()

        
def MRE4ABZ():
    global ZRE4, ZRE4J, FVB, ALTE, JLFREIB, JLHINZU, ZRE4VP, ZVBEZ, ZVBEZJ
    
    ZRE4 = ZRE4J - FVB - ALTE - JLFREIB + JLHINZU
    
    if ZRE4 < 0:
        ZRE4 = 0
    
    ZRE4VP = ZRE4J
    ZVBEZ = ZVBEZJ - FVB
    
    if ZVBEZ < 0:
        ZVBEZ = 0
             
# def MRE4ALTE():
#     global K, ALTE, BMG, ALTER1, AJAHR, BMG, ZRE4J, ZVBEZJ, HBALTE, 
#     
#     if ALTER1 == 0:
#         ALTE = 0
#     else:
#         if AJAHR < 2006:
#             K = 1
#         elif AJAHR < 2058:
#             K = AJAHR - 2004
#         else:
#             K = 54
#     
#     BMG = ZRE4J - ZVBEZJ
#     ALTE = math.ceil(BMG * TAB4(K)) ############ eurito? cent?
#     
#     HBALTE = TAB5(K)
#     
#     if ALTE > HBALTE:
#         ALTE = HBALTE
def MRE4ALTE():
    global K, ALTE, BMG, ALTER1, AJAHR, ZRE4J, ZVBEZJ, HBALTE
    
    if ALTER1 == 0:
        ALTE = 0
    else:
        if AJAHR < 2006:
            K = 1
        elif AJAHR < 2058:
            K = AJAHR - 2004
        else:
            K = 54
        
        BMG = ZRE4J - ZVBEZJ          # ← indentado dentro del else
        ALTE = math.ceil(BMG * TAB4(K))
        HBALTE = TAB5(K)
        if ALTE > HBALTE:
            ALTE = HBALTE
            

def MRE4():
    global ZVBEZJ, VJAHR, J, LZZ, VBEZM, ZMVB, VBEZS, VBEZB, HFVB, FVBZ, FVB, VBEZBSO, FVBSO, HFVBZSO, FVBZSO, HFVBZ

    if ZVBEZJ == 0:
        FVBZ = 0
        FVB = 0
        FVBZSO = 0
        FVBSO = 0
    else:
        # Determinación de J
        if VJAHR < 2006:
            J = 1
        elif VJAHR < 2058:
            J = VJAHR - 2004
        else:
            J = 54
        
        # Rama LZZ
        if LZZ == 1:
            VBEZB = VBEZM * ZMVB + VBEZS
            HFVB = math.ceil(TAB2(J) / 12 * ZMVB)  # Euro ↑
            FVBZ = math.ceil(TAB3(J) / 12 * ZMVB)  # Euro ↑
        else:
            VBEZB = VBEZM * 12 + VBEZS
            HFVB = TAB2(J)
            FVBZ = TAB3(J)
            
        # Cálculo de FVB (Cent ↑)
        FVB = math.ceil(VBEZB * TAB1(J) / 100)

        
        if FVB > HFVB:
            FVB = HFVB
        
        if FVB > ZVBEZJ:
            FVB = ZVBEZJ
        
        # Cálculo de FVBSO (Cent ↑)
        FVBSO = math.ceil(FVB + VBEZBSO * TAB1(J) / 100)

        
        if FVBSO > TAB2(J):
            FVBSO = TAB2(J)
            
        HFVBZSO = (VBEZB + VBEZBSO) / 100 - FVBSO
        FVBZSO = math.ceil(FVBZ + VBEZBSO / 100) # Euro ↑
        
        if FVBZSO > HFVBZSO:
            FVBZSO = math.ceil(HFVBZSO) # Euro ↑
            
        if FVBZSO > TAB3(J):
            FVBZSO = TAB3(J)
            
        HFVBZ = VBEZB / 100 - FVB
        
        if FVBZ > HFVBZ:
            FVBZ = math.ceil(HFVBZ) # Euro ↑

    # MRE4ALTE se ejecuta siempre antes del ENDE, sin importar el valor de ZVBEZJ
    MRE4ALTE()
    
    

def MRE4JL():
    global LZZ, ZVBEZJ, ZRE4J, JLFREIB, JLHINZU, ZVBEZJ, F, LZZFREIB, LZZHINZU, RE4, VBEZ, AF

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
    global BBGRVALV, AVSATZAN, RVSATZAN, BBGKVPV, KVSATZAN, PVSATZAN, W1STKL5, W2STKL5, W3STKL5, GFB, SOLZFREI
    
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


   

####################            Hauptprogramm
eingeben()

MPARA()
MRE4JL()
VBEZBSO = 0
MRE4()
MRE4ABZ() 
MBERECH() 
MSONST() 

# print("--- DEBUG DETALLADO ---")
# print('X', X)
# print("ZRE4J=", ZRE4J)
# print("ZRE4=", ZRE4)
# print("ZTABFB=", ZTABFB)
# print("ANP=", ANP)
# print("FVB=", FVB)
# print("FVBZ=", FVBZ)
# print("SAP=", SAP)
# print("EFA=", EFA)
# print("VSP=", VSP)
# print("VSPR=", VSPR)
# print("VSPKVPV=", VSPKVPV)
# print("VSPHB=", VSPHB)
# print("VSPALV=", VSPALV)
# print("VSPN=", VSPN)
# print("BBGRVALV=", BBGRVALV)
# print("BBGKVPV=", BBGKVPV)
# print("RVSATZAN=", RVSATZAN)
# print("KVSATZAN=", KVSATZAN)
# print("PVSATZAN=", PVSATZAN)
# print("AVSATZAN=", AVSATZAN)
# print("ZRE4VP=", ZRE4VP)
# print("ZRE4VPR=", ZRE4VPR)
# print("JBMG=", JBMG)
# print("SOLZFREI=", SOLZFREI)
# print("LSTJAHR=", LSTJAHR)
# print("LSTLZZ=", LSTLZZ)

ausgeben()

