from tkinter import *
import math
import tkinter.messagebox


window = Tk()

window.geometry("1152x700")
window.title("Calculadora Geometrica")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.configure(bg = "#fade1b")

def showFrame(frame):
	frame.tkraise()

pi = math.pi

#========= DEFINITIONS
def pitagoras(Base, Altura):
    Cbas = Base
    Calt = Altura

    hip = math.sqrt((Cbas**2) + (Calt**2))
    return hip

def area_cercle(radi):
    area = pi * radi**2
    return area

def perimetre_cercle(radi):
    perimetre = 2 * pi * radi
    return perimetre

def btn_clicked():
    return True

def figuresPlanes():
    showFrame(f2_figuresPlanes)

def cossosGeometrics():
     showFrame(f3_figuresAmbVolum)

'''
CALCULATIONS FIGURES PLANES
'''
#region
def f4_calculate():
    f4_costat = float(f4_entry0.get())
    f4_perim = f4_costat * 4
    f4_area = f4_costat**2

    f4_canvas.create_text(
    863.0, 170.5,
    text = f4_perim,
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

    f4_canvas.create_text(
    863.0, 311.5,
    text = f4_area,
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

def f5_calculate():
    base = float(f5_entry0.get())
    altura = float(f5_entry1.get())

    perim = base*2 + altura*2
    area = base*altura

    f5_canvas.create_text(
        863.0, 170.5,
        text = perim,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f5_canvas.create_text(
        866.0, 311.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f7_calculate():
    base = float(f7_entry0.get())
    altura = math.sqrt(base**2 - (base/2)**2)

    #print(altura)

    perim = base*3
    area = base * altura / 2

    f7_canvas.create_text(
        863.0, 170.5,
        text = perim,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f7_canvas.create_text(
        866.0, 311.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f7_2_calculate():
    altura = float(f7_2_entry0.get())

    costat = (2*altura*(math.sqrt(3))) / 3

    #print(costat)

    perimetre = costat*3
    area = altura * costat / 2

    f7_2_canvas.create_text(
        863.0, 170.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f7_2_canvas.create_text(
        866.0, 311.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f8_1_calculate():
    altura = float(f8_1_entry0.get())
    base = float(f8_1_entry1.get())
    catet = pitagoras(base/2, altura)

    #print(altura, base, catet)

    perimetre = base + catet*2
    area = base * altura / 2

    #print(perimetre, area)

    f8_1_canvas.create_text(
        863.0, 170.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f8_1_canvas.create_text(
        866.0, 311.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f8_2_calculate():
    base = float(f8_2_entry1.get())
    catet = float(f8_2_entry0.get())

    altura = math.sqrt(catet**2 - (base/2)**2)
    #print(altura, base, catet)

    perimetre = catet*2 + base
    area = base * altura / 2

    f8_2_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f8_2_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f9_calculate():
    altura = float(f9_entry0.get())
    catet2 = float(f9_entry1.get())  
    catet1 = float(f9_entry2.get())
    base = float(f9_entry3.get())

    perimetre = catet1 + catet2 + base
    area = base * altura / 2

    f9_canvas.create_text(
        863.0, 170.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f9_canvas.create_text(
        866.0, 311.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))
def f11_calculate():
    num_costats = float(f11_entry0.get())    
    costat = float(f11_entry1.get())
    radi = float(f11_entry2.get())

    apotema = math.sqrt((radi**2)-((costat/2)**2))
    #print(apotema)

    if (num_costats <= 4):
        tkinter.messagebox.showerror(
            title="No és pentàgon!", message="Introdueix un valor igual o superior a 5.")
    else:
        perimetre = num_costats * costat
        area = costat*apotema/2*num_costats

        f11_canvas.create_text(
            863.0, 170.5,
            text = perimetre,
            fill = "#000000",
            font = ("ArchivoVFBeta-Regular", int(18.0)))

        f11_canvas.create_text(
            866.0, 311.5,
            text = area,
            fill = "#000000",
            font = ("ArchivoVFBeta-Regular", int(18.0)))

def f12_calculate():
    num_costats = float(f12_entry0.get())
    costat = float(f12_entry1.get())
    apotema = float(f12_entry2.get())

    if (num_costats <= 4):
        tkinter.messagebox.showerror(
            title="No és pentàgon!", message="Introdueix un valor igual o superior a 5.")
    else:
        perimetre = costat * num_costats
        area = costat*apotema/2*num_costats

        f12_canvas.create_text(
            863.0, 170.5,
            text = perimetre,
            fill = "#000000",
            font = ("ArchivoVFBeta-Regular", int(18.0)))

        f12_canvas.create_text(
            866.0, 311.5,
            text = area,
            fill = "#000000",
            font = ("ArchivoVFBeta-Regular", int(18.0)))

def f14_calculate():
    radi = float(f14_entry0.get())

    diametre = radi * 2
    area = pi * radi**2
    perimetre = 2 * pi * radi

    f14_canvas.create_text(
        863.0, 170.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f14_canvas.create_text(
        866.0, 311.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f14_canvas.create_text(
        866.0, 449.5,
        text = diametre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))


def f15_calculate():
    longitud = float(f15_entry0.get())

    radi = longitud / (2*pi)
    diametre = radi*2
    area = area_cercle(radi)
    perimetre = perimetre_cercle(radi)

    #print(perimetre, longitud)
    f15_canvas.create_text(
        863.0, 170.5,
        text = radi,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f15_canvas.create_text(
        866.0, 311.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f15_canvas.create_text(
        866.0, 449.5,
        text = diametre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f16_calculate():
    diametre = float(f16_entry0.get())

    radi = diametre/2
    area = area_cercle(radi)
    perimetre = perimetre_cercle(radi)

    f16_canvas.create_text(
        863.0, 170.5,
        text = radi,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f16_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f16_canvas.create_text(
        866.0, 449.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))


def f17_calculate():
    area = float(f17_entry0.get())

    radi = math.sqrt(area/pi)
    diametre = radi * 2
    perimetre = perimetre_cercle(radi)

    f17_canvas.create_text(
        863.0, 170.5,
        text = radi,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f17_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f17_canvas.create_text(
        866.0, 449.5,
        text = diametre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f18_calculate():    
    diagonal1 = float(f18_entry0.get())
    diagonal2 = float(f18_entry1.get())

    costat = pitagoras(diagonal1/2, diagonal2/2)

    area = diagonal1 * diagonal2 / 2
    perimetre = costat*4

    f18_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f18_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f20_calculate():
    h = float(f20_entry0.get())
    b = float(f20_entry1.get())
    a = float(f20_entry2.get())

    area = ((a + b)/2)*h
    costat = math.sqrt( ( (a-b) / 2)**2 + (h**2)  )
    perimetre = costat*2 + a + b

    f20_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f20_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f21_calculate():
    c = float(f21_entry0.get())
    d = float(f21_entry1.get())
    b = float(f21_entry2.get())
    a = float(f21_entry3.get())

    '''
    lista = [a, b, c, d]

    for x in lista:
        #print(x)

    a_menos_b = a-b

    #print(a_menos_b)

    ka = b**2 - a**2 - d**2 + c**2 + 2*a*b
    be = 2 * a_menos_b

    #print(str(ka) + "   " + str(be))

    x = ka / be

    h = math.sqrt(c**2 - x**2)

    #print(str(x) + "   " + str(h))
    '''
    
    altura = math.sqrt( c**2 - ( (c**2 - d**2 + (a-b)**2) / (2*(a-b)) )**2 )
    area = (a + b) / 2 * altura
    perimetre = a + b + c + d


    #print(altura)

    f21_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f21_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

#endregion

'''
CALCULATIONS FIGURES AMB VOLUM
'''
#region
def f30_calculate():
    costat = float(f30_entry0.get())

    volum = costat ** 3
    area = costat**2 * 6
    perimetre = costat * 12

    f30_canvas.create_text(
        863.0, 454.5,
        text = volum,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f30_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f30_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f31_calculate():
    base = float(f31_entry0.get())
    altura = float(f31_entry2.get())
    height = float(f31_entry1.get())

    volum = base * altura * height
    area = 2*(base*altura+base*height+altura*height)
    perimetre = 4*(base+altura+height)
    
    f31_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f31_canvas.create_text(
        866.0, 440.5,
        text = volum,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f31_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))    

def f33_calculate():
    diametre = float(f33_entry0.get())
    altura = float(f33_entry1.get())
    
    radi = diametre/2
    generatriu = math.sqrt((radi**2) + (altura**2))
    area = math.pi * radi * generatriu + math.pi * radi**2
    volum = math.pi * radi**2 * altura / 3
    perimetre = 2*math.pi*radi

    f33_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f33_canvas.create_text(
        866.0, 440.5,
        text = volum,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f33_canvas.create_text(
        866.0, 569.5,
        text = generatriu,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f33_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f34_calculate():
    generatriu = float(f34_entry0.get())
    altura = float(f34_entry1.get())

    radi = math.sqrt(generatriu**2 - altura**2)
    diametre = radi*2
    area = math.pi * radi * generatriu + math.pi * radi**2
    volum = math.pi * radi**2 * altura / 3
    perimetre = 2*math.pi*radi

    f34_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f34_canvas.create_text(
        866.0, 440.5,
        text = volum,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f34_canvas.create_text(
        866.0, 569.5,
        text = radi,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f34_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f35_calculate():
    generatriu = float(f35_entry0.get())
    diametre = float(f35_entry1.get())

    radi = diametre/2
    altura = math.sqrt(((generatriu) **2) - (radi**2))
    area = math.pi * radi * generatriu + math.pi * radi**2
    volum = math.pi * radi**2 * altura / 3
    perimetre = 2*math.pi*radi

    f35_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f35_canvas.create_text(
        866.0, 440.5,
        text = volum,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f35_canvas.create_text(
        866.0, 569.5,
        text = altura,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f35_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))


def f36_calculate():
    generatriu = float(f36_entry0.get())
    radi = float(f36_entry1.get())

    diametre = radi*2
    altura = math.sqrt(((generatriu) **2) - (radi**2))
    area = math.pi * radi * generatriu + math.pi * radi**2
    volum = math.pi * radi**2 * altura / 3
    perimetre = 2*math.pi*radi

    f36_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f36_canvas.create_text(
        866.0, 440.5,
        text = volum,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f36_canvas.create_text(
        866.0, 569.5,
        text = altura,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f36_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))


def f37_calculate():
    radi = float(f37_entry0.get())
    altura = float(f37_entry1.get())

    generatriu = math.sqrt((radi**2) + (altura**2))
    diametre = radi*2
    area = math.pi * radi * generatriu + math.pi * radi**2
    volum = math.pi * radi**2 * altura / 3
    perimetre = 2*math.pi*radi

    f37_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f37_canvas.create_text(
        866.0, 440.5,
        text = volum,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f37_canvas.create_text(
        866.0, 569.5,
        text = generatriu,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f37_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f39_calculate():
    altura = float(f39_entry0.get())
    radi = float(f39_entry1.get())

    area = 2*math.pi * radi**2 + (altura * (2*math.pi*radi))
    volum = math.pi * radi**2 * altura 
    perimetre = 2*math.pi*radi*2

    f39_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f39_canvas.create_text(
        866.0, 440.5,
        text = volum,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f39_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))


def f40_calculate():
    diametre = float(f40_entry0.get())
    altura = float(f40_entry1.get())
    
    radi = diametre / 2
    area = 2*math.pi * radi**2 + (altura * (2*math.pi*radi))
    volum = math.pi * radi**2 * altura 
    perimetre = 2*math.pi*radi*2

    f40_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f40_canvas.create_text(
        866.0, 440.5,
        text = volum,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f40_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f41_calculate():
    radi = float(f41_entry0.get())

    cercleInt = math.pi*radi**2
    area = cercleInt*4 
    volum = (4*math.pi*radi**3) / 3

    f41_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f41_canvas.create_text(
        866.0, 311.5,
        text = volum,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f43_calculate():
    ap = float(f43_entry0.get())
    h = float(f43_entry1.get())
    cost = float(f43_entry2.get())
    num_cost = float(f43_entry3.get())

    apB = math.sqrt(ap**2 - h**2)

    ab = apB * cost / 2 * num_cost
    al = (ap * cost) / 2 * num_cost
    gen = math.sqrt(  (cost/2)**2 + ap**2  )
    #print(gen)

    area = ab + al
    volum = 1 / 3 * ab * h
    perimetre = num_cost*gen + num_cost*cost

    f43_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f43_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f43_canvas.create_text(
        866.0, 438.5,
        text = volum,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f43_canvas.create_text(
        866.0, 559.5,
        text = apB,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))


def f44_calculate():
    apB = float(f44_entry0.get())
    h = float(f44_entry1.get())
    cost = float(f44_entry2.get())
    num_cost = float(f44_entry3.get())

    ap = math.sqrt(h**2 + apB**2)

    ab = apB * cost / 2 * num_cost
    al = (ap * cost) / 2 * num_cost
    gen = math.sqrt(  (cost/2)**2 + ap**2  )

    area = ab + al
    volum = 1 / 3 * ab * h
    perimetre = num_cost*gen + num_cost*cost

    f44_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f44_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f44_canvas.create_text(
        866.0, 438.5,
        text = volum,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f44_canvas.create_text(
        866.0, 559.5,
        text = ap,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

def f45_calculate():
    apB = float(f45_entry0.get())
    ap = float(f45_entry1.get())
    cost = float(f45_entry2.get())
    num_cost = float(f45_entry3.get())

    h = math.sqrt(ap**2 - apB**2)

    ab = apB * cost / 2 * num_cost
    al = (ap * cost) / 2 * num_cost
    gen = math.sqrt(  (cost/2)**2 + ap**2  )

    area = ab + al
    volum = 1 / 3 * ab * h
    perimetre = num_cost*gen + num_cost*cost

    f45_canvas.create_text(
        863.0, 170.5,
        text = area,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f45_canvas.create_text(
        866.0, 311.5,
        text = perimetre,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f45_canvas.create_text(
        866.0, 438.5,
        text = volum,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))

    f45_canvas.create_text(
        866.0, 559.5,
        text = h,
        fill = "#000000",
        font = ("ArchivoVFBeta-Regular", int(18.0)))


#endregion

#========= FRAMES
#region
f1_main = Frame(window)

f2_figuresPlanes = Frame(window)
f3_figuresAmbVolum = Frame(window)

f4_quadrat = Frame(window)

f5_quadrilater = Frame(window)

f6_triangles = Frame(window)

f7_equilaterChose = Frame(window)
f7_1_triangleEquilater_cat = Frame(window)
f7_2_triangleEquilater_alt = Frame(window)

f8_isoscelesChose = Frame(window)
f8_1_triangleIsosceles_alt = Frame(window)
f8_2_triangleIsosceles_bas = Frame(window)

f9_triangleEscale = Frame(window)

f10_pentagonChose = Frame(window)
f11_pentagonRadi = Frame(window)
f12_pentagonApotema = Frame(window)

f13_cercleChose = Frame(window)
f14_cercleRadi = Frame(window)
f15_cercleLongitud = Frame(window)
f16_cercleDiametre = Frame(window)
f17_cercleArea = Frame(window)

f18_rombe = Frame(window)

f19_trapeziChose = Frame(window)
f20_trapeziOpt1 = Frame(window)
f21_trapeziOpt2 = Frame(window)

f30_cub = Frame(window)

f31_prisme = Frame(window)

f32_conChose = Frame(window)
f33_diametreIaltura = Frame(window)
f34_alturaIgeneratriu = Frame(window)
f35_diametreIgeneratriu = Frame(window)
f36_radiIgeneratriu = Frame(window)
f37_radiIaltura = Frame(window)

f38_cilindreChose = Frame(window)
f39_altIradi = Frame(window)
f40_altIdiametre = Frame(window)

f41_esfera = Frame(window)

f42_piramChose = Frame(window)
f43_piramOpt1 = Frame(window)
f44_piramOpt2 = Frame(window)
f45_piramOpt3 = Frame(window)

frames=[f1_main , 
		f2_figuresPlanes, 
		f3_figuresAmbVolum,
		f4_quadrat,
        f5_quadrilater,
        f6_triangles,
        f7_equilaterChose,
        f7_1_triangleEquilater_cat,
        f7_2_triangleEquilater_alt,
        f8_isoscelesChose,
        f8_1_triangleIsosceles_alt,
        f8_2_triangleIsosceles_bas,
        f9_triangleEscale,
        f10_pentagonChose,
        f11_pentagonRadi,
        f12_pentagonApotema,
        f13_cercleChose,
        f14_cercleRadi,
        f15_cercleLongitud,
        f16_cercleDiametre,
        f17_cercleArea,
        f18_rombe,
        f19_trapeziChose,
        f20_trapeziOpt1,
        f21_trapeziOpt2,
        f30_cub,
        f31_prisme,
        f32_conChose,
        f34_alturaIgeneratriu,
        f35_diametreIgeneratriu,
        f33_diametreIaltura,
        f36_radiIgeneratriu,
        f37_radiIaltura,
        f38_cilindreChose,
        f39_altIradi,
        f40_altIdiametre,
        f41_esfera,
        f42_piramChose,
        f43_piramOpt1,
        f44_piramOpt2,
        f45_piramOpt3]

for frame in frames:
	frame.grid(row=0, column=0, sticky="nsew")

#endregion

'''
FRAMES FOR FIGURES PLANES
'''
#region
#========= FRAME 1 (Main Page)
f1_main.configure(bg = "#fade1b")

f1_canvas = Canvas(
    f1_main,
    bg = "#fade1b",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f1_canvas.place(x = 0, y = 0)

f1_img0 = PhotoImage(file = f"resources/f1_img0.png")
f1_b0 = Button(
	f1_canvas,
    image = f1_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = figuresPlanes,
    relief = "flat")

f1_b0.place(
    x = 689, y = 364,
    width = 315,
    height = 47)

f1_img1 = PhotoImage(file = f"resources/f1_img1.png")
f1_b1 = Button(
	f1_canvas,
    image = f1_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = cossosGeometrics,
    relief = "flat")

f1_b1.place(
    x = 689, y = 467,
    width = 314,
    height = 46)

f1_background_img = PhotoImage(file = f"resources/f1_background.png")
f1_background = f1_canvas.create_image(
    576.0, 337.0,
    image=f1_background_img)


#========= FRAME 2 (Figures Planes)

f2_figuresPlanes.configure(bg = "#fade1b")

f2_canvas = Canvas(
    f2_figuresPlanes,
    bg = "#fade1b",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f2_canvas.place(x = 0, y = 0)

f2_back_b0 = PhotoImage(file = f"resources/f8_2_img0.png")
f2_back_b0 = Button(
    f2_canvas,
    image = f2_back_b0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f1_main),
    relief = "flat")

f2_back_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)


f2_img0 = PhotoImage(file = f"resources/f2_img0.png")
f2_b0 = Button(
    f2_canvas,
    image = f2_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: showFrame(f6_triangles),
    relief = "flat")

f2_b0.place(
    x = 157, y = 314,
    width = 404,
    height = 76)

f2_img1 = PhotoImage(file = f"resources/f2_img1.png")
f2_b1 = Button(
    f2_canvas,
    image = f2_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f4_quadrat),
    relief = "flat")

f2_b1.place(
    x = 157, y = 216,
    width = 404,
    height = 77)

f2_img2 = PhotoImage(file = f"resources/f2_img2.png")
f2_b2 = Button(
    f2_canvas,
    image = f2_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f18_rombe),
    relief = "flat")

f2_b2.place(
    x = 591, y = 411,
    width = 405,
    height = 77)

f2_img3 = PhotoImage(file = f"resources/f2_img3.png")
f2_b3 = Button(
    f2_canvas,
    image = f2_img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f10_pentagonChose),
    relief = "flat")

f2_b3.place(
    x = 591, y = 314,
    width = 405,
    height = 76)

f2_img4 = PhotoImage(file = f"resources/f2_img4.png")
f2_b4 = Button(
    f2_canvas,
    image = f2_img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: showFrame(f5_quadrilater),
    relief = "flat")

f2_b4.place(
    x = 591, y = 216,
    width = 405,
    height = 77)

f2_img5 = PhotoImage(file = f"resources/f2_img5.png")
f2_b5 = Button(
    f2_canvas,
    image = f2_img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f19_trapeziChose),
    relief = "flat")

f2_b5.place(
    x = 374, y = 509,
    width = 404,
    height = 76)

f2_img6 = PhotoImage(file = f"resources/f2_img6.png")
f2_b6 = Button(
    f2_canvas,
    image = f2_img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f13_cercleChose),
    relief = "flat")

f2_b6.place(
    x = 157, y = 411,
    width = 404,
    height = 77)

f2_img7 = PhotoImage(file = f"resources/f2_img7.png")
f2_b7 = Button(
    f2_canvas,
    image = f2_img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f1_main),
    relief = "flat")

f2_b7.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f2_background_img = PhotoImage(file = f"resources/f2_background.png")
background = f2_canvas.create_image(
    593.5, 358.5,
    image=f2_background_img)


#========= FRAME 3 (Figures Amb Volum)

f3_figuresAmbVolum.configure(bg = "#fade1b")
f3_canvas = Canvas(
    f3_figuresAmbVolum,
    bg = "#fade1b",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f3_canvas.place(x = 0, y = 0)

f3_back_b0 = PhotoImage(file = f"resources/f8_2_img0.png")
f3_back_b0 = Button(
    f3_canvas,
    image = f3_back_b0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f1_main),
    relief = "flat")

f3_back_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f3_img0 = PhotoImage(file = f"resources/f3_img0.png")
f3_b0 = Button(
	f3_canvas,
    image = f3_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f42_piramChose),
    relief = "flat")

f3_b0.place(
    x = 157, y = 314,
    width = 404,
    height = 76)

f3_img1 = PhotoImage(file = f"resources/f3_img1.png")
f3_b1 = Button(
	f3_canvas,
    image = f3_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f30_cub),
    relief = "flat")

f3_b1.place(
    x = 157, y = 216,
    width = 404,
    height = 77)

f3_img2 = PhotoImage(file = f"resources/f3_img2.png")
f3_b2 = Button(
	f3_canvas,
    image = f3_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f41_esfera),
    relief = "flat")

f3_b2.place(
    x = 591, y = 411,
    width = 405,
    height = 77)

f3_img3 = PhotoImage(file = f"resources/f3_img3.png")
f3_b3 = Button(
	f3_canvas,
    image = f3_img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f32_conChose),
    relief = "flat")

f3_b3.place(
    x = 591, y = 314,
    width = 405,
    height = 76)

f3_img4 = PhotoImage(file = f"resources/f3_img4.png")
f3_b4 = Button(
	f3_canvas,
    image = f3_img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f31_prisme),
    relief = "flat")

f3_b4.place(
    x = 591, y = 216,
    width = 405,
    height = 77)

f3_img5 = PhotoImage(file = f"resources/f3_img5.png")
f3_b5 = Button(
	f3_canvas,
    image = f3_img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f38_cilindreChose),
    relief = "flat")

f3_b5.place(
    x = 157, y = 411,
    width = 404,
    height = 77)

f3_img6 = PhotoImage(file = f"resources/f3_img6.png")
f3_b6 = Button(
	f3_canvas,
    image = f3_img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f1_main),
    relief = "flat")

f3_b6.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f3_background_img = PhotoImage(file = f"resources/f3_background.png")
f3_background = f3_canvas.create_image(
    593.5, 358.5,
    image=f3_background_img)


#========= FRAME 4 (Quadrat)

f4_canvas = Canvas(
    f4_quadrat,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f4_canvas.place(x = 0, y = 0)

f4_background_img = PhotoImage(file = f"resources/f4_background.png")
f4_background = f4_canvas.create_image(
    612.5, 357.0,
    image=f4_background_img)

f4_img0 = PhotoImage(file = f"resources/f4_img0.png")
f4_b0 = Button(
    f4_canvas,
    image = f4_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f2_figuresPlanes),
    relief = "flat")

f4_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f4_img1 = PhotoImage(file = f"resources/f4_img1.png")
f4_b1 = Button(
    f4_canvas,
    image = f4_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f4_calculate,
    relief = "flat")

f4_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f4_entry0_img = PhotoImage(file = f"resources/f4_img_textBox0.png")
f4_entry0_bg = f4_canvas.create_image(
    355.5, 240.5,
    image = f4_entry0_img)

f4_entry0 = Entry(
    f4_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f4_entry0.place(
    x = 241.0, y = 216,
    width = 229.0,
    height = 47)

f4_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f4_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

#========= Frame 5 (Quadrilàter)
f5_quadrilater.configure(bg = "#36bd6d")
f5_canvas = Canvas(
    f5_quadrilater,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f5_canvas.place(x = 0, y = 0)

f5_background_img = PhotoImage(file = f"resources/f5_background.png")
f5_background = f5_canvas.create_image(
    612.5, 357.0,
    image=f5_background_img)

f5_img0 = PhotoImage(file = f"resources/f5_img0.png")
f5_b0 = Button(
    f5_quadrilater,
    image = f5_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f2_figuresPlanes),
    relief = "flat")

f5_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f5_img1 = PhotoImage(file = f"resources/f5_img1.png")
f5_b1 = Button(
    f5_quadrilater,
    image = f5_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f5_calculate,
    relief = "flat")

f5_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f5_entry0_img = PhotoImage(file = f"resources/f5_img_textBox0.png")
f5_entry0_bg = f5_canvas.create_image(
    355.5, 289.5,
    image = f5_entry0_img)

f5_entry0 = Entry(
    f5_quadrilater,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f5_entry0.place(
    x = 241.0, y = 265,
    width = 229.0,
    height = 47)

f5_entry1_img = PhotoImage(file = f"resources/f5_img_textBox1.png")
f5_entry1_bg = f5_canvas.create_image(
    355.5, 235.5,
    image = f5_entry1_img)

f5_entry1 = Entry(
    f5_quadrilater,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f5_entry1.place(
    x = 241.0, y = 211,
    width = 229.0,
    height = 47)


f5_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f5_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

#========= Frame 6 (Triangles)
f6_triangles.configure(bg = "#36bd6d")
f6_canvas = Canvas(
    f6_triangles,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f6_canvas.place(x = 0, y = 0)

f6_background_img = PhotoImage(file = f"resources/f6_background.png")
f6_background = f6_canvas.create_image(
    648.5, 357.0,
    image=f6_background_img)

f6_img0 = PhotoImage(file = f"resources/f6_img0.png")
f6_b0 = Button(
    f6_triangles,
    image = f6_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: showFrame(f2_figuresPlanes),
    relief = "flat")

f6_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f6_img1 = PhotoImage(file = f"resources/f6_img1.png")
f6_b1 = Button(
    f6_triangles,
    image = f6_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f9_triangleEscale),
    relief = "flat")

f6_b1.place(
    x = 201, y = 376,
    width = 241,
    height = 82)

f6_img2 = PhotoImage(file = f"resources/f6_img2.png")
f6_b2 = Button(
    f6_triangles,
    image = f6_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f7_equilaterChose),
    relief = "flat")

f6_b2.place(
    x = 201, y = 212,
    width = 241,
    height = 82)

f6_img3 = PhotoImage(file = f"resources/f6_img3.png")
f6_b3 = Button(
    f6_triangles,
    image = f6_img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f8_isoscelesChose),
    relief = "flat")

f6_b3.place(
    x = 201, y = 294,
    width = 241,
    height = 82)


f6_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f6_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

f6_canvas.create_text(
    863.0, 170.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f6_canvas.create_text(
    866.0, 311.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))


#========= Frame 7 (Triangle Equilater Chose)
f7_equilaterChose.configure(bg = "#36bd6d")
f7_0_canvas = Canvas(
    f7_equilaterChose,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f7_0_canvas.place(x = 0, y = 0)

f7_0_background_img = PhotoImage(file = f"resources/f7_0_background.png")
f7_0_background = f7_0_canvas.create_image(
    616.0, 357.0,
    image=f7_0_background_img)

f7_0_img0 = PhotoImage(file = f"resources/f7_0_img0.png")
f7_0_b0 = Button(
    f7_0_canvas,
    image = f7_0_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f6_triangles),
    relief = "flat")

f7_0_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f7_0_img1 = PhotoImage(file = f"resources/f7_0_img1.png")
f7_0_b1 = Button(
    f7_0_canvas,
    image = f7_0_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f7_2_triangleEquilater_alt),
    relief = "flat")

f7_0_b1.place(
    x = 234, y = 329,
    width = 241,
    height = 82)

f7_0_img2 = PhotoImage(file = f"resources/f7_0_img2.png")
f7_0_b2 = Button(
    f7_0_canvas,
    image = f7_0_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f7_1_triangleEquilater_cat),
    relief = "flat")

f7_0_b2.place(
    x = 234, y = 411,
    width = 241,
    height = 82)

f7_0_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f7_0_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

f7_0_canvas.create_text(
    863.0, 170.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f7_0_canvas.create_text(
    866.0, 311.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

#========= Frame 7_2 (Triangle Equilater Catet)
f7_1_triangleEquilater_cat.configure(bg = "#36bd6d")
f7_canvas = Canvas(
    f7_1_triangleEquilater_cat,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f7_canvas.place(x = 0, y = 0)

f7_background_img = PhotoImage(file = f"resources/f7_background.png")
f7_background = f7_canvas.create_image(
    612.5, 357.0,
    image=f7_background_img)

f7_img0 = PhotoImage(file = f"resources/f7_img0.png")
f7_b0 = Button(
    f7_1_triangleEquilater_cat,
    image = f7_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f7_equilaterChose),
    relief = "flat")

f7_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f7_img1 = PhotoImage(file = f"resources/f7_img1.png")
f7_b1 = Button(
    f7_1_triangleEquilater_cat,
    image = f7_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f7_calculate,
    relief = "flat")

f7_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f7_entry0_img = PhotoImage(file = f"resources/f7_img_textBox0.png")
f7_entry0_bg = f7_canvas.create_image(
    355.5, 235.5,
    image = f7_entry0_img)

f7_entry0 = Entry(
    f7_1_triangleEquilater_cat,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f7_entry0.place(
    x = 241.0, y = 211,
    width = 229.0,
    height = 47)


f7_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f7_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

#======== Frame 7_2 (Equilater Altura)
f7_2_triangleEquilater_alt.configure(bg = "#36bd6d")
f7_2_canvas = Canvas(
    f7_2_triangleEquilater_alt,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f7_2_canvas.place(x = 0, y = 0)

f7_2_background_img = PhotoImage(file = f"resources/f7_2_background.png")
f7_2_background = f7_2_canvas.create_image(
    612.5, 357.0,
    image=f7_2_background_img)

f7_2_img0 = PhotoImage(file = f"resources/f7_2_img0.png")
f7_2_b0 = Button(
    f7_2_canvas,
    image = f7_2_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f7_equilaterChose),
    relief = "flat")

f7_2_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f7_2_img1 = PhotoImage(file = f"resources/f7_2_img1.png")
f7_2_b1 = Button(
    f7_2_canvas,
    image = f7_2_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f7_2_calculate,
    relief = "flat")

f7_2_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f7_2_entry0_img = PhotoImage(file = f"resources/f7_2_img_textBox0.png")
f7_2_entry0_bg = f7_2_canvas.create_image(
    355.5, 235.5,
    image = f7_2_entry0_img)

f7_2_entry0 = Entry(
    f7_2_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f7_2_entry0.place(
    x = 241.0, y = 211,
    width = 229.0,
    height = 47)


f7_2_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f7_2_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")


#======= Frame 8 (Isosceles Chose)
f8_canvas = Canvas(
    f8_isoscelesChose,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f8_canvas.place(x = 0, y = 0)

f8_background_img = PhotoImage(file = f"resources/f8_background.png")
f8_background = f8_canvas.create_image(
    616.0, 357.0,
    image=f8_background_img)

f8_img0 = PhotoImage(file = f"resources/f8_img0.png")
f8_b0 = Button(
    f8_isoscelesChose,
    image = f8_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f6_triangles),
    relief = "flat")

f8_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f8_img1 = PhotoImage(file = f"resources/f8_img1.png")
f8_b1 = Button(
    f8_isoscelesChose,
    image = f8_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f8_1_triangleIsosceles_alt),
    relief = "flat")

f8_b1.place(
    x = 234, y = 329,
    width = 241,
    height = 82)

f8_img2 = PhotoImage(file = f"resources/f8_img2.png")
f8_b2 = Button(
    f8_isoscelesChose,
    image = f8_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f8_2_triangleIsosceles_bas),
    relief = "flat")

f8_b2.place(
    x = 234, y = 411,
    width = 241,
    height = 82)


f8_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f8_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

f8_canvas.create_text(
    863.0, 170.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f8_canvas.create_text(
    866.0, 311.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))


#======= Frame 8_1 (Isòsceles Altura)
f8_1_triangleIsosceles_alt.configure(bg = "#36bd6d")
f8_1_canvas = Canvas(
    f8_1_triangleIsosceles_alt,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f8_1_canvas.place(x = 0, y = 0)

f8_1_background_img = PhotoImage(file = f"resources/f8_1_background.png")
f8_1_background = f8_1_canvas.create_image(
    612.5, 357.0,
    image=f8_1_background_img)

f8_1_img0 = PhotoImage(file = f"resources/f8_1_img0.png")
f8_1_b0 = Button(
    f8_1_canvas,
    image = f8_1_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f8_isoscelesChose),
    relief = "flat")

f8_1_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f8_1_img1 = PhotoImage(file = f"resources/f8_1_img1.png")
f8_1_b1 = Button(
    f8_1_canvas,
    image = f8_1_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f8_1_calculate,
    relief = "flat")

f8_1_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f8_1_entry0_img = PhotoImage(file = f"resources/f8_1_img_textBox0.png")
f8_1_entry0_bg = f8_1_canvas.create_image(
    355.5, 289.5,
    image = f8_1_entry0_img)

f8_1_entry0 = Entry(
    f8_1_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f8_1_entry0.place(
    x = 241.0, y = 265,
    width = 229.0,
    height = 47)

f8_1_entry1_img = PhotoImage(file = f"resources/f8_1_img_textBox1.png")
f8_1_entry1_bg = f8_1_canvas.create_image(
    355.5, 235.5,
    image = f8_1_entry1_img)

f8_1_entry1 = Entry(
    f8_1_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f8_1_entry1.place(
    x = 241.0, y = 211,
    width = 229.0,
    height = 47)


f8_1_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f8_1_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")



#========= Frame 8_2 (Isosceles Catet)
f8_2_triangleIsosceles_bas.configure(bg = "#36bd6d")
f8_2_canvas = Canvas(
    f8_2_triangleIsosceles_bas,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f8_2_canvas.place(x = 0, y = 0)

f8_2_background_img = PhotoImage(file = f"resources/f8_2_background.png")
f8_2_background = f8_2_canvas.create_image(
    612.5, 357.0,
    image=f8_2_background_img)

f8_2_img0 = PhotoImage(file = f"resources/f8_2_img0.png")
f8_2_b0 = Button(
    f8_2_canvas,
    image = f8_2_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f8_isoscelesChose),
    relief = "flat")

f8_2_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f8_2_img1 = PhotoImage(file = f"resources/f8_2_img1.png")
f8_2_b1 = Button(
    f8_2_canvas,
    image = f8_2_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f8_2_calculate,
    relief = "flat")

f8_2_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f8_2_entry0_img = PhotoImage(file = f"resources/f8_2_img_textBox0.png")
f8_2_entry0_bg = f8_2_canvas.create_image(
    355.5, 289.5,
    image = f8_2_entry0_img)

f8_2_entry0 = Entry(
    f8_2_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f8_2_entry0.place(
    x = 241.0, y = 265,
    width = 229.0,
    height = 47)

f8_2_entry1_img = PhotoImage(file = f"resources/f8_2_img_textBox1.png")
f8_2_entry1_bg = f8_2_canvas.create_image(
    355.5, 235.5,
    image = f8_2_entry1_img)

f8_2_entry1 = Entry(
    f8_2_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f8_2_entry1.place(
    x = 241.0, y = 211,
    width = 229.0,
    height = 47)


f8_2_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f8_2_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")


#======== Frame 9 (Triangle Escalè)
f9_triangleEscale.configure(bg = "#36bd6d")
f9_canvas = Canvas(
    f9_triangleEscale,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f9_canvas.place(x = 0, y = 0)

f9_background_img = PhotoImage(file = f"resources/f9_background.png")
f9_background = f9_canvas.create_image(
    612.5, 357.0,
    image=f9_background_img)

f9_img0 = PhotoImage(file = f"resources/f9_img0.png")
f9_b0 = Button(
    f9_canvas,
    image = f9_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f6_triangles),
    relief = "flat")

f9_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f9_img1 = PhotoImage(file = f"resources/f9_img1.png")
f9_b1 = Button(
    f9_canvas,
    image = f9_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f9_calculate,
    relief = "flat")

f9_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f9_entry0_img = PhotoImage(file = f"resources/f9_img_textBox0.png")
f9_entry0_bg = f9_canvas.create_image(
    355.5, 289.5,
    image = f9_entry0_img)

f9_entry0 = Entry(
    f9_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f9_entry0.place(
    x = 241.0, y = 265,
    width = 229.0,
    height = 47)

f9_entry1_img = PhotoImage(file = f"resources/f9_img_textBox1.png")
f9_entry1_bg = f9_canvas.create_image(
    355.5, 397.5,
    image = f9_entry1_img)

f9_entry1 = Entry(
    f9_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f9_entry1.place(
    x = 241.0, y = 373,
    width = 229.0,
    height = 47)

f9_entry2_img = PhotoImage(file = f"resources/f9_img_textBox2.png")
f9_entry2_bg = f9_canvas.create_image(
    355.5, 343.5,
    image = f9_entry2_img)

f9_entry2 = Entry(
    f9_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f9_entry2.place(
    x = 241.0, y = 319,
    width = 229.0,
    height = 47)

f9_entry3_img = PhotoImage(file = f"resources/f9_img_textBox3.png")
f9_entry3_bg = f9_canvas.create_image(
    355.5, 235.5,
    image = f9_entry3_img)

f9_entry3 = Entry(
    f9_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f9_entry3.place(
    x = 241.0, y = 211,
    width = 229.0,
    height = 47)


f9_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f9_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

#======== Frame 10 (Pentagon Chose)

f10_pentagonChose.configure(bg = "#36bd6d")
f10_canvas = Canvas(
    f10_pentagonChose,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f10_canvas.place(x = 0, y = 0)

f10_background_img = PhotoImage(file = f"resources/f10_background.png")
f10_background = f10_canvas.create_image(
    616.0, 357.0,
    image=f10_background_img)

f10_img0 = PhotoImage(file = f"resources/f10_img0.png")
f10_b0 = Button(
    f10_canvas,
    image = f10_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f2_figuresPlanes),
    relief = "flat")

f10_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f10_img1 = PhotoImage(file = f"resources/f10_img1.png")
f10_b1 = Button(
    f10_canvas,
    image = f10_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f11_pentagonRadi),
    relief = "flat")

f10_b1.place(
    x = 234, y = 329,
    width = 241,
    height = 82)

f10_img2 = PhotoImage(file = f"resources/f10_img2.png")
f10_b2 = Button(
    f10_canvas,
    image = f10_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f12_pentagonApotema),
    relief = "flat")

f10_b2.place(
    x = 234, y = 411,
    width = 241,
    height = 82)


f10_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f10_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

f10_canvas.create_text(
    863.0, 170.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f10_canvas.create_text(
    866.0, 311.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

#========= Frame 11 (Pentagon Radi)
f11_pentagonRadi.configure(bg = "#36bd6d")
f11_canvas = Canvas(
    f11_pentagonRadi,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f11_canvas.place(x = 0, y = 0)

f11_background_img = PhotoImage(file = f"resources/f11_background.png")
f11_background = f11_canvas.create_image(
    648.5, 357.0,
    image=f11_background_img)

f11_img0 = PhotoImage(file = f"resources/f11_img0.png")
f11_b0 = Button(
    f11_canvas,
    image = f11_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f10_pentagonChose),
    relief = "flat")

f11_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f11_img1 = PhotoImage(file = f"resources/f11_img1.png")
f11_b1 = Button(
    f11_canvas,
    image = f11_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f11_calculate,
    relief = "flat")

f11_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)


f11_entry0_img = PhotoImage(file = f"resources/f11_img_textBox0.png")
f11_entry0_bg = f11_canvas.create_image(
    370.5, 235.5,
    image = f11_entry0_img)

f11_entry0 = Entry(
    f11_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f11_entry0.place(
    x = 271.0, y = 211,
    width = 199.0,
    height = 47)


f11_entry1_img = PhotoImage(file = f"resources/f11_img_textBox1.png")
f11_entry1_bg = f11_canvas.create_image(
    355.5, 351.5,
    image = f11_entry1_img)

f11_entry1 = Entry(
    f11_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f11_entry1.place(
    x = 241.0, y = 327,
    width = 229.0,
    height = 47)


f11_entry2_img = PhotoImage(file = f"resources/f11_img_textBox2.png")
f11_entry2_bg = f11_canvas.create_image(
    363.5, 293.5,
    image = f11_entry2_img)

f11_entry2 = Entry(
    f11_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f11_entry2.place(
    x = 257.0, y = 269,
    width = 213.0,
    height = 47)


f11_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f11_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")


#======== Frame 12 (Pentagon Apotema)
f12_pentagonApotema.configure(bg = "#36bd6d")
f12_canvas = Canvas(
    f12_pentagonApotema,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f12_canvas.place(x = 0, y = 0)

f12_background_img = PhotoImage(file = f"resources/f12_background.png")
f12_background = f12_canvas.create_image(
    612.5, 357.0,
    image=f12_background_img)

f12_img0 = PhotoImage(file = f"resources/f12_img0.png")
f12_b0 = Button(
    f12_canvas,
    image = f12_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f10_pentagonChose),
    relief = "flat")

f12_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f12_img1 = PhotoImage(file = f"resources/f12_img1.png")
f12_b1 = Button(
    f12_canvas,
    image = f12_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f12_calculate,
    relief = "flat")

f12_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f12_entry0_img = PhotoImage(file = f"resources/f12_img_textBox0.png")
f12_entry0_bg = f12_canvas.create_image(
    370.5, 235.5,
    image = f12_entry0_img)

f12_entry0 = Entry(
    f12_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f12_entry0.place(
    x = 271.0, y = 211,
    width = 199.0,
    height = 47)

f12_entry1_img = PhotoImage(file = f"resources/f12_img_textBox1.png")
f12_entry1_bg = f12_canvas.create_image(
    355.5, 351.5,
    image = f12_entry1_img)

f12_entry1 = Entry(
    f12_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f12_entry1.place(
    x = 241.0, y = 327,
    width = 229.0,
    height = 47)

f12_entry2_img = PhotoImage(file = f"resources/f12_img_textBox2.png")
f12_entry2_bg = f12_canvas.create_image(
    363.5, 293.5,
    image = f12_entry2_img)

f12_entry2 = Entry(
    f12_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f12_entry2.place(
    x = 257.0, y = 269,
    width = 213.0,
    height = 47)


f12_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f12_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")


#========= Frame 13 (Cercle Chose)
f13_cercleChose.configure(bg = "#36bd6d")
f13_canvas = Canvas(
    f13_cercleChose,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f13_canvas.place(x = 0, y = 0)

f13_background_img = PhotoImage(file = f"resources/f13_background.png")
f13_background = f13_canvas.create_image(
    616.0, 357.0,
    image=f13_background_img)

f13_img0 = PhotoImage(file = f"resources/f13_img0.png")
f13_b0 = Button(
    f13_canvas,
    image = f13_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f2_figuresPlanes),
    relief = "flat")

f13_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f13_img1 = PhotoImage(file = f"resources/f13_img1.png")
f13_b1 = Button(
    f13_canvas,
    image = f13_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f14_cercleRadi),
    relief = "flat")

f13_b1.place(
    x = 106, y = 291,
    width = 241,
    height = 82)

f13_img2 = PhotoImage(file = f"resources/f13_img2.png")
f13_b2 = Button(
    f13_canvas,
    image = f13_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f16_cercleDiametre),
    relief = "flat")

f13_b2.place(
    x = 106, y = 373,
    width = 241,
    height = 82)

f13_img3 = PhotoImage(file = f"resources/f13_img3.png")
f13_b3 = Button(
    f13_canvas,
    image = f13_img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f15_cercleLongitud),
    relief = "flat")

f13_b3.place(
    x = 362, y = 291,
    width = 241,
    height = 82)

f13_img4 = PhotoImage(file = f"resources/f13_img4.png")
f13_b4 = Button(
    f13_canvas,
    image = f13_img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f17_cercleArea),
    relief = "flat")

f13_b4.place(
    x = 362, y = 373,
    width = 241,
    height = 82)


f13_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f13_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

f13_canvas.create_text(
    863.0, 170.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f13_canvas.create_text(
    866.0, 311.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

#========= Frame 14 (Cercle Radi)
f14_cercleRadi.configure(bg = "#36bd6d")
f14_canvas = Canvas(
    f14_cercleRadi,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f14_canvas.place(x = 0, y = 0)

f14_background_img = PhotoImage(file = f"resources/f14_background.png")
f14_background = f14_canvas.create_image(
    648.5, 357.0,
    image=f14_background_img)

f14_img0 = PhotoImage(file = f"resources/f14_img0.png")
f14_b0 = Button(
    f14_canvas,
    image = f14_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f13_cercleChose),
    relief = "flat")

f14_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f14_img1 = PhotoImage(file = f"resources/f14_img1.png")
f14_b1 = Button(
    f14_canvas,
    image = f14_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f14_calculate,
    relief = "flat")

f14_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f14_canvas.create_text(
    166.5, 235.5,
    text = "Radi:",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(40.0)))

f14_entry0_img = PhotoImage(file = f"resources/f14_img_textBox0.png")
f14_entry0_bg = f14_canvas.create_image(
    355.5, 235.5,
    image = f14_entry0_img)

f14_entry0 = Entry(
    f14_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f14_entry0.place(
    x = 241.0, y = 211,
    width = 229.0,
    height = 47)


f14_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f14_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

f14_canvas.create_rectangle(
    740, 425, 740+251, 425+49,
    fill = "#c1da37",
    outline = "")


#======== Frame 15 (Cercle Longitud)
f15_cercleLongitud.configure(bg = "#36bd6d")
f15_canvas = Canvas(
    f15_cercleLongitud,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f15_canvas.place(x = 0, y = 0)

f15_background_img = PhotoImage(file = f"resources/f15_background.png")
f15_background = f15_canvas.create_image(
    648.5, 357.0,
    image=f15_background_img)

f15_img0 = PhotoImage(file = f"resources/f15_img0.png")
f15_b0 = Button(
    f15_canvas,
    image = f15_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f13_cercleChose),
    relief = "flat")

f15_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f15_img1 = PhotoImage(file = f"resources/f15_img1.png")
f15_b1 = Button(
    f15_canvas,
    image = f15_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f15_calculate,
    relief = "flat")

f15_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f15_canvas.create_text(
    166.5, 235.5,
    text = "Longitud:",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(40.0)))

f15_entry0_img = PhotoImage(file = f"resources/f15_img_textBox0.png")
f15_entry0_bg = f15_canvas.create_image(
    355.5, 235.5,
    image = f15_entry0_img)

f15_entry0 = Entry(
    f15_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f15_entry0.place(
    x = 241.0, y = 211,
    width = 229.0,
    height = 47)


f15_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f15_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

f15_canvas.create_rectangle(
    740, 425, 740+251, 425+49,
    fill = "#c1da37",
    outline = "")

#======== Frame 16 (Cercle Diàmetre)
f16_cercleDiametre.configure(bg = "#36bd6d")
f16_canvas = Canvas(
    f16_cercleDiametre,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f16_canvas.place(x = 0, y = 0)

f16_background_img = PhotoImage(file = f"resources/f16_background.png")
f16_background = f16_canvas.create_image(
    612.5, 357.0,
    image=f16_background_img)

f16_img0 = PhotoImage(file = f"resources/f16_img0.png")
f16_b0 = Button(
    f16_canvas,
    image = f16_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f13_cercleChose),
    relief = "flat")

f16_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f16_img1 = PhotoImage(file = f"resources/f16_img1.png")
f16_b1 = Button(
    f16_canvas,
    image = f16_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f16_calculate,
    relief = "flat")

f16_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f16_entry0_img = PhotoImage(file = f"resources/f16_img_textBox0.png")
f16_entry0_bg = f16_canvas.create_image(
    370.5, 237.5,
    image = f16_entry0_img)

f16_entry0 = Entry(
    f16_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f16_entry0.place(
    x = 271.0, y = 211,
    width = 199.0,
    height = 51)


#======== Frame 17 (Cercle Àrea)
f17_cercleArea.configure(bg = "#36bd6d")
f17_canvas = Canvas(
    f17_cercleArea,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f17_canvas.place(x = 0, y = 0)

f17_background_img = PhotoImage(file = f"resources/f17_background.png")
f17_background = f17_canvas.create_image(
    612.5, 357.0,
    image=f17_background_img)

f17_img0 = PhotoImage(file = f"resources/f17_img0.png")
f17_b0 = Button(
    f17_canvas,
    image = f17_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f13_cercleChose),
    relief = "flat")

f17_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f17_img1 = PhotoImage(file = f"resources/f17_img1.png")
f17_b1 = Button(
    f17_canvas,
    image = f17_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f17_calculate,
    relief = "flat")

f17_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f17_entry0_img = PhotoImage(file = f"resources/f17_img_textBox0.png")
f17_entry0_bg = f17_canvas.create_image(
    355.5, 235.5,
    image = f17_entry0_img)

f17_entry0 = Entry(
    f17_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f17_entry0.place(
    x = 241.0, y = 211,
    width = 229.0,
    height = 47)

#======== Frame 18 (Rombe)
f18_rombe.configure(bg = "#36bd6d")
f18_canvas = Canvas(
    f18_rombe,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f18_canvas.place(x = 0, y = 0)

f18_background_img = PhotoImage(file = f"resources/f18_background.png")
f18_background = f18_canvas.create_image(
    612.5, 357.0,
    image=f18_background_img)

f18_img0 = PhotoImage(file = f"resources/f18_img0.png")
f18_b0 = Button(
    f18_canvas,
    image = f18_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f2_figuresPlanes),
    relief = "flat")

f18_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f18_img1 = PhotoImage(file = f"resources/f18_img1.png")
f18_b1 = Button(
    f18_canvas,
    image = f18_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f18_calculate,
    relief = "flat")

f18_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f18_entry0_img = PhotoImage(file = f"resources/f18_img_textBox0.png")
f18_entry0_bg = f18_canvas.create_image(
    377.0, 235.5,
    image = f18_entry0_img)

f18_entry0 = Entry(
    f18_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f18_entry0.place(
    x = 284.0, y = 211,
    width = 186.0,
    height = 47)

f18_entry1_img = PhotoImage(file = f"resources/f18_img_textBox1.png")
f18_entry1_bg = f18_canvas.create_image(
    377.0, 304.5,
    image = f18_entry1_img)

f18_entry1 = Entry(
    f18_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f18_entry1.place(
    x = 284.0, y = 280,
    width = 186.0,
    height = 47)

#======== FRAME 19 (Trapezi Chose)
f19_canvas = Canvas(
    f19_trapeziChose,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f19_canvas.place(x = 0, y = 0)


f19_canvas.create_rectangle(
    700, 66, 700+411, 66+556,
    fill = "#ee6d33",
    outline = "")

f19_background_img = PhotoImage(file = f"resources/f19_background.png")
f19_background = f19_canvas.create_image(
    616.0, 357.0,
    image=f19_background_img)

f19_img0 = PhotoImage(file = f"resources/f19_img0.png")
f19_b0 = Button(
    f19_canvas,
    image = f19_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f2_figuresPlanes),
    relief = "flat")

f19_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)


f19_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f19_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

f19_canvas.create_text(
    863.0, 170.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f19_canvas.create_text(
    866.0, 311.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f19_img1 = PhotoImage(file = f"resources/f19_img1.png")
f19_b1 = Button(
    f19_canvas,
    image = f19_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f21_trapeziOpt2),
    relief = "flat")

f19_b1.place(
    x = 358, y = 298,
    width = 249,
    height = 84)

f19_img2 = PhotoImage(file = f"resources/f19_img2.png")
f19_b2 = Button(
    f19_canvas,
    image = f19_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f20_trapeziOpt1),
    relief = "flat")

f19_b2.place(
    x = 103, y = 294,
    width = 248,
    height = 88)

#======== FRAME 20 (Trapezi Opt1)
f20_canvas = Canvas(
    f20_trapeziOpt1,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f20_canvas.place(x = 0, y = 0)

f20_background_img = PhotoImage(file = f"resources/f20_background.png")
f20_background = f20_canvas.create_image(
    611.5, 357.0,
    image=f20_background_img)

f20_img0 = PhotoImage(file = f"resources/f20_img0.png")
f20_b0 = Button(
    f20_canvas,
    image = f20_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f19_trapeziChose),
    relief = "flat")

f20_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f20_img1 = PhotoImage(file = f"resources/f20_img1.png")
f20_b1 = Button(
    f20_canvas,
    image = f20_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f20_calculate,
    relief = "flat")

f20_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f20_entry0_img = PhotoImage(file = f"resources/f20_img_textBox0.png")
f20_entry0_bg = f20_canvas.create_image(
    261.5, 373.5,
    image = f20_entry0_img)

f20_entry0 = Entry(
    f20_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f20_entry0.place(
    x = 147.0, y = 349,
    width = 229.0,
    height = 47)

f20_entry1_img = PhotoImage(file = f"resources/f20_img_textBox1.png")
f20_entry1_bg = f20_canvas.create_image(
    261.5, 304.5,
    image = f20_entry1_img)

f20_entry1 = Entry(
    f20_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f20_entry1.place(
    x = 147.0, y = 280,
    width = 229.0,
    height = 47)

f20_entry2_img = PhotoImage(file = f"resources/f20_img_textBox2.png")
f20_entry2_bg = f20_canvas.create_image(
    261.5, 235.5,
    image = f20_entry2_img)

f20_entry2 = Entry(
    f20_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f20_entry2.place(
    x = 147.0, y = 211,
    width = 229.0,
    height = 47)


#======== FRAME 21 (Trapezi Opt2)
f21_canvas = Canvas(
    f21_trapeziOpt2,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f21_canvas.place(x = 0, y = 0)

f21_background_img = PhotoImage(file = f"resources/f21_background.png")
f21_background = f21_canvas.create_image(
    611.5, 357.0,
    image=f21_background_img)

f21_img0 = PhotoImage(file = f"resources/f21_img0.png")
f21_b0 = Button(
    f21_canvas,
    image = f21_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f19_trapeziChose),
    relief = "flat")

f21_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f21_img1 = PhotoImage(file = f"resources/f21_img1.png")
f21_b1 = Button(
    f21_canvas,
    image = f21_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f21_calculate,
    relief = "flat")

f21_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f21_entry0_img = PhotoImage(file = f"resources/f21_img_textBox0.png")
f21_entry0_bg = f21_canvas.create_image(
    261.5, 373.5,
    image = f21_entry0_img)

f21_entry0 = Entry(
    f21_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f21_entry0.place(
    x = 147.0, y = 349,
    width = 229.0,
    height = 47)

f21_entry1_img = PhotoImage(file = f"resources/f21_img_textBox1.png")
f21_entry1_bg = f21_canvas.create_image(
    262.5, 442.5,
    image = f21_entry1_img)

f21_entry1 = Entry(
    f21_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f21_entry1.place(
    x = 148.0, y = 418,
    width = 229.0,
    height = 47)

f21_entry2_img = PhotoImage(file = f"resources/f21_img_textBox2.png")
f21_entry2_bg = f21_canvas.create_image(
    261.5, 304.5,
    image = f21_entry2_img)

f21_entry2 = Entry(
    f21_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f21_entry2.place(
    x = 147.0, y = 280,
    width = 229.0,
    height = 47)

f21_entry3_img = PhotoImage(file = f"resources/f21_img_textBox3.png")
entry3_bg = f21_canvas.create_image(
    261.5, 235.5,
    image = f21_entry3_img)

f21_entry3 = Entry(
    f21_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f21_entry3.place(
    x = 147.0, y = 211,
    width = 229.0,
    height = 47)


#endregion


'''
FRAMES FOR FIGURES AMB VOLUM
'''
#region
#======== FRAME 30 (Cub)
f30_canvas = Canvas( 
    f30_cub,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f30_canvas.place(x = 0, y = 0)

f30_background_img = PhotoImage(file = f"resources/f30_background.png")
f30_background = f30_canvas.create_image(
    612.5, 357.0,
    image=f30_background_img)

f30_img0 = PhotoImage(file = f"resources/f30_img0.png")
f30_b0 = Button(
    f30_cub,
    image = f30_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f3_figuresAmbVolum),
    relief = "flat")

f30_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f30_img1 = PhotoImage(file = f"resources/f30_img1.png")
f30_b1 = Button(
    f30_cub,
    image = f30_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f30_calculate,
    relief = "flat")

f30_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f30_entry0_img = PhotoImage(file = f"resources/f30_img_textBox0.png")
f30_entry0_bg = f30_canvas.create_image(
    344.0, 235.5,
    image = f30_entry0_img)

f30_entry0 = Entry(
    f30_cub,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f30_entry0.place(
    x = 218.0, y = 211,
    width = 252.0,
    height = 47)


f30_canvas.create_text(
    866.0, 403.5,
    text = "Volum",
    fill = "#ffffff",
    font = ("ArchivoVFBeta-Regular", int(40.0)))


f30_canvas.create_rectangle(
    740, 431, 740+251, 431+49,
    fill = "#c1da37",
    outline = "")



#======== FRAME 31 (Prisme)
f31_canvas = Canvas(
    f31_prisme,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f31_canvas.place(x = 0, y = 0)

f31_background_img = PhotoImage(file = f"resources/f31_background.png")
f31_background = f31_canvas.create_image(
    611.5, 357.0,
    image=f31_background_img)

f31_img0 = PhotoImage(file = f"resources/f31_img0.png")
f31_b0 = Button(
    f31_canvas,
    image = f31_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f3_figuresAmbVolum),
    relief = "flat")

f31_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f31_img1 = PhotoImage(file = f"resources/f31_img1.png")
f31_b1 = Button(
    f31_canvas,
    image = f31_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f31_calculate,
    relief = "flat")

f31_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f31_entry0_img = PhotoImage(file = f"resources/f31_img_textBox0.png")
f31_entry0_bg = f31_canvas.create_image(
    355.5, 235.5,
    image = f31_entry0_img)

f31_entry0 = Entry(
    f31_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f31_entry0.place(
    x = 241.0, y = 211,
    width = 229.0,
    height = 47)

f31_entry1_img = PhotoImage(file = f"resources/f31_img_textBox1.png")
f31_entry1_bg = f31_canvas.create_image(
    355.5, 373.5,
    image = f31_entry1_img)

f31_entry1 = Entry(
    f31_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f31_entry1.place(
    x = 241.0, y = 349,
    width = 229.0,
    height = 47)

f31_entry2_img = PhotoImage(file = f"resources/f31_img_textBox2.png")
f31_entry2_bg = f31_canvas.create_image(
    355.5, 304.5,
    image = f31_entry2_img)

f31_entry2 = Entry(
    f31_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f31_entry2.place(
    x = 241.0, y = 280,
    width = 229.0,
    height = 47)


#======== FRAME 32 (Con Chose)
f32_conChose.configure(bg = "#36bd6d")
f32_canvas = Canvas(
    f32_conChose,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f32_canvas.place(x = 0, y = 0)

f32_background_img = PhotoImage(file = f"resources/f32_background.png")
f32_background = f32_canvas.create_image(
    616.0, 357.0,
    image=f32_background_img)

f32_img0 = PhotoImage(file = f"resources/f32_img0.png")
f32_b0 = Button(
    f32_canvas,
    image = f32_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f3_figuresAmbVolum),
    relief = "flat")

f32_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f32_img1 = PhotoImage(file = f"resources/f32_img1.png")
f32_b1 = Button(
    f32_canvas,
    image = f32_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

f32_b1.place(
    x = 362, y = 291,
    width = 241,
    height = 82)

f32_img2 = PhotoImage(file = f"resources/f32_img2.png")
f32_b2 = Button(
    f32_canvas,
    image = f32_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f34_alturaIgeneratriu),
    relief = "flat")

f32_b2.place(
    x = 226, y = 459,
    width = 243,
    height = 94)


f32_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f32_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

f32_canvas.create_text(
    863.0, 170.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f32_canvas.create_text(
    866.0, 311.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f32_canvas.create_text(
    866.0, 405.5,
    text = "Volum",
    fill = "#ffffff",
    font = ("ArchivoVFBeta-Regular", int(40.0)))


f32_canvas.create_rectangle(
    740, 433, 740+251, 433+49,
    fill = "#c1da37",
    outline = "")

f32_canvas.create_text(
    866.0, 457.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f32_img3 = PhotoImage(file = f"resources/f32_img3.png")
f32_b3 = Button(
    f32_canvas,
    image = f32_img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f35_diametreIgeneratriu),
    relief = "flat")

f32_b3.place(
    x = 354, y = 374,
    width = 249,
    height = 84)

f32_img4 = PhotoImage(file = f"resources/f32_img4.png")
f32_b4 = Button(
    f32_canvas,
    image = f32_img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f36_radiIgeneratriu),
    relief = "flat")

f32_b4.place(
    x = 99, y = 370,
    width = 248,
    height = 88)

f32_img5 = PhotoImage(file = f"resources/f32_img5.png")
f32_b5 = Button(
    f32_canvas,
    image = f32_img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f33_diametreIaltura),
    relief = "flat")

f32_b5.place(
    x = 359, y = 287,
    width = 241,
    height = 86)

f32_img6 = PhotoImage(file = f"resources/f32_img6.png")
f32_b6 = Button(
    f32_canvas,
    image = f32_img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f37_radiIaltura),
    relief = "flat")

f32_b6.place(
    x = 106, y = 291,
    width = 241,
    height = 82)

#======== FRAME 33 (Diàmetre I Altura)
f33_canvas = Canvas(
    f33_diametreIaltura,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f33_canvas.place(x = 0, y = 0)

f33_background_img = PhotoImage(file = f"resources/f33_background.png")
f33_background = f33_canvas.create_image(
    612.5, 357.0,
    image=f33_background_img)

f33_img0 = PhotoImage(file = f"resources/f33_img0.png")
f33_b0 = Button(
    f33_canvas,
    image = f33_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f32_conChose),
    relief = "flat")

f33_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f33_img1 = PhotoImage(file = f"resources/f33_img1.png")
f33_b1 = Button(
    f33_canvas,
    image = f33_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f33_calculate,
    relief = "flat")

f33_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f33_entry0_img = PhotoImage(file = f"resources/f33_img_textBox0.png")
f33_entry0_bg = f33_canvas.create_image(
    369.0, 235.5,
    image = f33_entry0_img)

f33_entry0 = Entry(
    f33_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f33_entry0.place(
    x = 268.0, y = 211,
    width = 202.0,
    height = 47)

f33_entry1_img = PhotoImage(file = f"resources/f33_img_textBox1.png")
f33_entry1_bg = f33_canvas.create_image(
    355.5, 304.5,
    image = f33_entry1_img)

f33_entry1 = Entry(
    f33_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f33_entry1.place(
    x = 241.0, y = 280,
    width = 229.0,
    height = 47)

#======== FRAME 34 (Altura I Generatriu)
f34_canvas = Canvas(
    f34_alturaIgeneratriu,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f34_canvas.place(x = 0, y = 0)

f34_background_img = PhotoImage(file = f"resources/f34_background.png")
f34_background = f34_canvas.create_image(
    612.5, 357.0,
    image=f34_background_img)

f34_img0 = PhotoImage(file = f"resources/f34_img0.png")
f34_b0 = Button(
    f34_canvas,
    image = f34_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f32_conChose),
    relief = "flat")

f34_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f34_img1 = PhotoImage(file = f"resources/f34_img1.png")
f34_b1 = Button(
    f34_canvas,
    image = f34_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f34_calculate,
    relief = "flat")

f34_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f34_entry0_img = PhotoImage(file = f"resources/f34_img_textBox0.png")
f34_entry0_bg = f34_canvas.create_image(
    377.0, 235.5,
    image = f34_entry0_img)

f34_entry0 = Entry(
    f34_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f34_entry0.place(
    x = 284.0, y = 211,
    width = 186.0,
    height = 47)

f34_entry1_img = PhotoImage(file = f"resources/f34_img_textBox1.png")
f34_entry1_bg = f34_canvas.create_image(
    367.0, 304.5,
    image = f34_entry1_img)

f34_entry1 = Entry(
    f34_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f34_entry1.place(
    x = 264.0, y = 280,
    width = 206.0,
    height = 47)



#======== FRAME 35 (Diàmetre i Generatriu)
f35_canvas = Canvas(
    f35_diametreIgeneratriu,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f35_canvas.place(x = 0, y = 0)

f35_background_img = PhotoImage(file = f"resources/f35_background.png")
f35_background = f35_canvas.create_image(
    612.5, 357.0,
    image=f35_background_img)

f35_img0 = PhotoImage(file = f"resources/f35_img0.png")
f35_b0 = Button(
    f35_canvas,
    image = f35_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f32_conChose),
    relief = "flat")

f35_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f35_img1 = PhotoImage(file = f"resources/f35_img1.png")
f35_b1 = Button(
    f35_canvas,
    image = f35_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f35_calculate,
    relief = "flat")

f35_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f35_entry0_img = PhotoImage(file = f"resources/f35_img_textBox0.png")
f35_entry0_bg = f35_canvas.create_image(
    377.0, 235.5,
    image = f35_entry0_img)

f35_entry0 = Entry(
    f35_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f35_entry0.place(
    x = 284.0, y = 211,
    width = 186.0,
    height = 47)

f35_entry1_img = PhotoImage(file = f"resources/f35_img_textBox1.png")
f35_entry1_bg = f35_canvas.create_image(
    367.0, 304.5,
    image = f35_entry1_img)

f35_entry1 = Entry(
    f35_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f35_entry1.place(
    x = 264.0, y = 280,
    width = 206.0,
    height = 47)


#======== FRAME 36 (Radi i Generatriu)
f36_canvas = Canvas(
    f36_radiIgeneratriu,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f36_canvas.place(x = 0, y = 0)

f36_background_img = PhotoImage(file = f"resources/f36_background.png")
f36_background = f36_canvas.create_image(
    612.5, 357.0,
    image=f36_background_img)

f36_img0 = PhotoImage(file = f"resources/f36_img0.png")
f36_b0 = Button(
    f36_canvas,
    image = f36_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f32_conChose),
    relief = "flat")

f36_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f36_img1 = PhotoImage(file = f"resources/f36_img1.png")
f36_b1 = Button(
    f36_canvas,
    image = f36_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f36_calculate,
    relief = "flat")

f36_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f36_entry0_img = PhotoImage(file = f"resources/f36_img_textBox0.png")
f36_entry0_bg = f36_canvas.create_image(
    377.0, 235.5,
    image = f36_entry0_img)

f36_entry0 = Entry(
    f36_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f36_entry0.place(
    x = 284.0, y = 211,
    width = 186.0,
    height = 47)

f36_entry1_img = PhotoImage(file = f"resources/f36_img_textBox1.png")
f36_entry1_bg = f36_canvas.create_image(
    355.5, 304.5,
    image = f36_entry1_img)

f36_entry1 = Entry(
    f36_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f36_entry1.place(
    x = 241.0, y = 280,
    width = 229.0,
    height = 47)

#======== FRAME 37 (Radi i Altura)
f37_canvas = Canvas(
    f37_radiIaltura,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f37_canvas.place(x = 0, y = 0)

f37_background_img = PhotoImage(file = f"resources/f37_background.png")
f37_background = f37_canvas.create_image(
    612.5, 357.0,
    image=f37_background_img)

f37_img0 = PhotoImage(file = f"resources/f37_img0.png")
f37_b0 = Button(
    f37_canvas,
    image = f37_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f32_conChose),
    relief = "flat")

f37_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f37_img1 = PhotoImage(file = f"resources/f37_img1.png")
f37_b1 = Button(
    f37_canvas,
    image = f37_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f37_calculate,
    relief = "flat")

f37_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f37_entry0_img = PhotoImage(file = f"resources/f37_img_textBox0.png")
f37_entry0_bg = f37_canvas.create_image(
    355.5, 235.5,
    image = f37_entry0_img)

f37_entry0 = Entry(
    f37_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f37_entry0.place(
    x = 241.0, y = 211,
    width = 229.0,
    height = 47)

f37_entry1_img = PhotoImage(file = f"resources/f37_img_textBox1.png")
f37_entry1_bg = f37_canvas.create_image(
    355.5, 304.5,
    image = f37_entry1_img)

f37_entry1 = Entry(
    f37_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f37_entry1.place(
    x = 241.0, y = 280,
    width = 229.0,
    height = 47)

#======== FRAME 38 (Cilindre Chose)
f38_canvas = Canvas(
    f38_cilindreChose,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f38_canvas.place(x = 0, y = 0)

f38_background_img = PhotoImage(file = f"resources/f38_background.png")
f38_background = f38_canvas.create_image(
    616.0, 357.0,
    image=f38_background_img)

f38_img0 = PhotoImage(file = f"resources/f38_img0.png")
f38_b0 = Button(
    f38_canvas,
    image = f38_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f3_figuresAmbVolum),
    relief = "flat")

f38_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f38_img1 = PhotoImage(file = f"resources/f38_img1.png")
f38_b1 = Button(
    f38_canvas,
    image = f38_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f39_altIradi),
    relief = "flat")

f38_b1.place(
    x = 106, y = 291,
    width = 241,
    height = 82)

f38_img2 = PhotoImage(file = f"resources/f38_img2.png")
f38_b2 = Button(
    f38_canvas,
    image = f38_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f40_altIdiametre),
    relief = "flat")

f38_b2.place(
    x = 362, y = 291,
    width = 241,
    height = 82)


f38_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f38_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

f38_canvas.create_text(
    863.0, 170.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f38_canvas.create_text(
    866.0, 311.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f38_canvas.create_text(
    866.0, 405.5,
    text = "Volum",
    fill = "#ffffff",
    font = ("ArchivoVFBeta-Regular", int(40.0)))


f38_canvas.create_rectangle(
    740, 433, 740+251, 433+49,
    fill = "#c1da37",
    outline = "")

f38_canvas.create_text(
    866.0, 457.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

#======== FRAME 39 (Alt i Radi)
f39_canvas = Canvas(
    f39_altIradi,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f39_canvas.place(x = 0, y = 0)

f39_background_img = PhotoImage(file = f"resources/f39_background.png")
f39_background = f39_canvas.create_image(
    612.5, 357.0,
    image=f39_background_img)

f39_img0 = PhotoImage(file = f"resources/f39_img0.png")
f39_b0 = Button(
    f39_canvas,
    image = f39_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f38_cilindreChose),
    relief = "flat")

f39_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f39_img1 = PhotoImage(file = f"resources/f39_img1.png")
f39_b1 = Button(
    f39_canvas,
    image = f39_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f39_calculate,
    relief = "flat")

f39_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f39_entry0_img = PhotoImage(file = f"resources/f39_img_textBox0.png")
f39_entry0_bg = f39_canvas.create_image(
    355.5, 235.5,
    image = f39_entry0_img)

f39_entry0 = Entry(
    f39_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f39_entry0.place(
    x = 241.0, y = 211,
    width = 229.0,
    height = 47)

f39_entry1_img = PhotoImage(file = f"resources/f39_img_textBox1.png")
f39_entry1_bg = f39_canvas.create_image(
    355.5, 304.5,
    image = f39_entry1_img)

f39_entry1 = Entry(
    f39_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f39_entry1.place(
    x = 241.0, y = 280,
    width = 229.0,
    height = 47)


#======== FRAME 40 (Alt i Diàmetre)
f40_canvas = Canvas(
    f40_altIdiametre,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f40_canvas.place(x = 0, y = 0)

f40_background_img = PhotoImage(file = f"resources/f40_background.png")
f40_background = f40_canvas.create_image(
    612.5, 357.0,
    image=f40_background_img)

f40_img0 = PhotoImage(file = f"resources/f40_img0.png")
f40_b0 = Button(
    f40_canvas,
    image = f40_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f38_cilindreChose),
    relief = "flat")

f40_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f40_img1 = PhotoImage(file = f"resources/f40_img1.png")
f40_b1 = Button(
    f40_canvas,
    image = f40_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f40_calculate,
    relief = "flat")

f40_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f40_entry0_img = PhotoImage(file = f"resources/f40_img_textBox0.png")
f40_entry0_bg = f40_canvas.create_image(
    367.5, 235.5,
    image = f40_entry0_img)

f40_entry0 = Entry(
    f40_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f40_entry0.place(
    x = 265.0, y = 211,
    width = 205.0,
    height = 47)

f40_entry1_img = PhotoImage(file = f"resources/f40_img_textBox1.png")
f40_entry1_bg = f40_canvas.create_image(
    355.5, 304.5,
    image = f40_entry1_img)

f40_entry1 = Entry(
    f40_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f40_entry1.place(
    x = 241.0, y = 280,
    width = 229.0,
    height = 47)

#======== FRAME 41 (Esfera)
f41_canvas = Canvas(
    f41_esfera,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f41_canvas.place(x = 0, y = 0)

f41_background_img = PhotoImage(file = f"resources/f41_background.png")
f41_background = f41_canvas.create_image(
    612.5, 357.0,
    image=f41_background_img)

f41_img0 = PhotoImage(file = f"resources/f41_img0.png")
f41_b0 = Button(
    f41_canvas,
    image = f41_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f3_figuresAmbVolum),
    relief = "flat")

f41_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f41_img1 = PhotoImage(file = f"resources/f41_img1.png")
f41_b1 = Button(
    f41_canvas,
    image = f41_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f41_calculate,
    relief = "flat")

f41_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f41_entry0_img = PhotoImage(file = f"resources/f41_img_textBox0.png")
f41_entry0_bg = f41_canvas.create_image(
    338.5, 235.5,
    image = f41_entry0_img)

f41_entry0 = Entry(
    f41_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f41_entry0.place(
    x = 224.0, y = 211,
    width = 229.0,
    height = 47)

#======== FRAME 42 (Piràmide Chose)
f42_canvas = Canvas(
    f42_piramChose,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f42_canvas.place(x = 0, y = 0)


f42_canvas.create_rectangle(
    700, 66, 700+411, 66+556,
    fill = "#ee6d33",
    outline = "")

f42_background_img = PhotoImage(file = f"resources/f42_background.png")
f42_background = f42_canvas.create_image(
    612.0, 357.0,
    image=f42_background_img)

f42_img0 = PhotoImage(file = f"resources/f42_img0.png")
f42_b0 = Button(
    f42_canvas,
    image = f42_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f3_figuresAmbVolum),
    relief = "flat")

f42_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)


f42_canvas.create_rectangle(
    740, 147, 740+251, 147+49,
    fill = "#c1da37",
    outline = "")


f42_canvas.create_rectangle(
    740, 287, 740+251, 287+49,
    fill = "#c1da37",
    outline = "")

f42_canvas.create_text(
    863.0, 170.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f42_canvas.create_text(
    866.0, 311.5,
    text = "output",
    fill = "#000000",
    font = ("ArchivoVFBeta-Regular", int(18.0)))

f42_img1 = PhotoImage(file = f"resources/f42_img1.png")
f42_b1 = Button(
    f42_canvas,
    image = f42_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f44_piramOpt2),
    relief = "flat")

f42_b1.place(
    x = 361, y = 277,
    width = 249,
    height = 84)

f42_img2 = PhotoImage(file = f"resources/f42_img2.png")
f42_b2 = Button(
    f42_canvas,
    image = f42_img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f43_piramOpt1),
    relief = "flat")

f42_b2.place(
    x = 106, y = 273,
    width = 248,
    height = 88)

f42_img3 = PhotoImage(file = f"resources/f42_img3.png")
f42_b3 = Button(
    f42_canvas,
    image = f42_img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f45_piramOpt3),
    relief = "flat")

f42_b3.place(
    x = 232, y = 365,
    width = 266,
    height = 95)


#======== FRAME 43 (Piràmide Opt 1)
f43_canvas = Canvas(
    f43_piramOpt1,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f43_canvas.place(x = 0, y = 0)

f43_background_img = PhotoImage(file = f"resources/f43_background.png")
f43_background = f43_canvas.create_image(
    611.5, 357.0,
    image=f43_background_img)

f43_img0 = PhotoImage(file = f"resources/f43_img0.png")
f43_b0 = Button(
    f43_canvas,
    image = f43_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f42_piramChose),
    relief = "flat")

f43_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f43_img1 = PhotoImage(file = f"resources/f43_img1.png")
f43_b1 = Button(
    f43_canvas,
    image = f43_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f43_calculate,
    relief = "flat")

f43_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f43_entry0_img = PhotoImage(file = f"resources/f43_img_textBox0.png")
f43_entry0_bg = f43_canvas.create_image(
    279.0, 442.5,
    image = f43_entry0_img)

f43_entry0 = Entry(
    f43_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f43_entry0.place(
    x = 181.0, y = 418,
    width = 196.0,
    height = 47)

f43_entry1_img = PhotoImage(file = f"resources/f43_img_textBox1.png")
f43_entry1_bg = f43_canvas.create_image(
    278.0, 373.5,
    image = f43_entry1_img)

f43_entry1 = Entry(
    f43_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f43_entry1.place(
    x = 180.0, y = 349,
    width = 196.0,
    height = 47)

f43_entry2_img = PhotoImage(file = f"resources/f43_img_textBox2.png")
f43_entry2_bg = f43_canvas.create_image(
    292.5, 304.5,
    image = f43_entry2_img)

f43_entry2 = Entry(
    f43_canvas,
    bg = "#c1da37",
    highlightthickness = 0)

f43_entry2.place(
    x = 209.0, y = 280,
    width = 167.0,
    height = 47)

f43_entry3_img = PhotoImage(file = f"resources/f43_img_textBox3.png")
entry3_bg = f43_canvas.create_image(
    323.0, 235.5,
    image = f43_entry3_img)

f43_entry3 = Entry(
    f43_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f43_entry3.place(
    x = 270.0, y = 211,
    width = 106.0,
    height = 47)



#======== FRAME 44 (Piràmide Opt 2)
f44_canvas = Canvas(
    f44_piramOpt2,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f44_canvas.place(x = 0, y = 0)

f44_background_img = PhotoImage(file = f"resources/f44_background.png")
f44_background = f44_canvas.create_image(
    611.5, 357.0,
    image=f44_background_img)

f44_img0 = PhotoImage(file = f"resources/f44_img0.png")
f44_b0 = Button(
    f44_canvas,
    image = f44_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f42_piramChose),
    relief = "flat")

f44_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f44_img1 = PhotoImage(file = f"resources/f44_img1.png")
f44_b1 = Button(
    f44_canvas,
    image = f44_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f44_calculate,
    relief = "flat")

f44_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f44_entry0_img = PhotoImage(file = f"resources/f44_img_textBox0.png")
f44_entry0_bg = f44_canvas.create_image(
    279.0, 442.5,
    image = f44_entry0_img)

f44_entry0 = Entry(
    f44_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f44_entry0.place(
    x = 181.0, y = 418,
    width = 196.0,
    height = 47)

f44_entry1_img = PhotoImage(file = f"resources/f44_img_textBox1.png")
f44_entry1_bg = f44_canvas.create_image(
    278.0, 373.5,
    image = f44_entry1_img)

f44_entry1 = Entry(
    f44_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f44_entry1.place(
    x = 180.0, y = 349,
    width = 196.0,
    height = 47)

f44_entry2_img = PhotoImage(file = f"resources/f44_img_textBox2.png")
f44_entry2_bg = f44_canvas.create_image(
    292.5, 304.5,
    image = f44_entry2_img)

f44_entry2 = Entry(
    f44_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f44_entry2.place(
    x = 209.0, y = 280,
    width = 167.0,
    height = 47)

f44_entry3_img = PhotoImage(file = f"resources/f44_img_textBox3.png")
f44_entry3_bg = f44_canvas.create_image(
    323.0, 235.5,
    image = f44_entry3_img)

f44_entry3 = Entry(
    f44_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f44_entry3.place(
    x = 270.0, y = 211,
    width = 106.0,
    height = 47)


#======== FRAME 45 (Piràmide Opt 3)
f45_canvas = Canvas(
    f45_piramOpt3,
    bg = "#36bd6d",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
f45_canvas.place(x = 0, y = 0)

f45_background_img = PhotoImage(file = f"resources/f45_background.png")
f45_background = f45_canvas.create_image(
    611.5, 357.0,
    image=f45_background_img)

f45_img0 = PhotoImage(file = f"resources/f45_img0.png")
f45_b0 = Button(
    f45_canvas,
    image = f45_img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:showFrame(f42_piramChose),
    relief = "flat")

f45_b0.place(
    x = 16, y = 20,
    width = 110,
    height = 60)

f45_img1 = PhotoImage(file = f"resources/f45_img1.png")
f45_b1 = Button(
    f45_canvas,
    image = f45_img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = f45_calculate,
    relief = "flat")

f45_b1.place(
    x = 191, y = 549,
    width = 241,
    height = 82)

f45_entry0_img = PhotoImage(file = f"resources/f45_img_textBox0.png")
f45_entry0_bg = f45_canvas.create_image(
    279.0, 442.5,
    image = f45_entry0_img)

f45_entry0 = Entry(
    f45_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f45_entry0.place(
    x = 181.0, y = 418,
    width = 196.0,
    height = 47)

f45_entry1_img = PhotoImage(file = f"resources/f45_img_textBox1.png")
f45_entry1_bg = f45_canvas.create_image(
    278.0, 373.5,
    image = f45_entry1_img)

f45_entry1 = Entry(
    f45_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f45_entry1.place(
    x = 180.0, y = 349,
    width = 196.0,
    height = 47)

f45_entry2_img = PhotoImage(file = f"resources/f45_img_textBox2.png")
f45_entry2_bg = f45_canvas.create_image(
    292.5, 304.5,
    image = f45_entry2_img)

f45_entry2 = Entry(
    f45_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f45_entry2.place(
    x = 209.0, y = 280,
    width = 167.0,
    height = 47)

f45_entry3_img = PhotoImage(file = f"resources/f45_img_textBox3.png")
f45_entry3_bg = f45_canvas.create_image(
    323.0, 235.5,
    image = f45_entry3_img)

f45_entry3 = Entry(
    f45_canvas,
    bd = 0,
    bg = "#c1da37",
    highlightthickness = 0)

f45_entry3.place(
    x = 270.0, y = 211,
    width = 106.0,
    height = 47)
#endregion




showFrame(f1_main)

window.resizable(False, False)
window.mainloop()
