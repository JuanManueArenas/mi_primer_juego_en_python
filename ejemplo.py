from tkinter import *
import random

# -------------------
# variables globales
# -------------------
BASE = 460
ALTURA = 220
radio = 10
desplazamiento_x = 1
desplazamiento_y = 1
intervalo = 2

centro_x = random.randint(radio, BASE)
centro_y = random.randint(radio, ALTURA)

def mover_pelota():
    global desplazamiento_x, desplazamiento_y
    
    x0, y0, x1, y1 = c.coords(pelota)
    if x0 < 0 or x1 > BASE: 
        desplazamiento_x = -desplazamiento_x
    if y0 < 0 or y1 > ALTURA: 
        desplazamiento_y = -desplazamiento_y
    c.move(pelota, desplazamiento_x, desplazamiento_y)
    ventana_principal.after(intervalo, mover_pelota)

# -------------------
# ventana principal
# -------------------
ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

# -------------------
# frame de graficacion
# -------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10,y=10)

# creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

pelota = c.create_oval(centro_x-radio, centro_y-radio, centro_x+radio, centro_y+radio, fill="green", outline="white")

mover_pelota()
# -------------------
# frame de controles
# -------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10,y=260)

# desplegar ventana
ventana_principal.mainloop()