from tkinter import *
import random
#---------------------
# VARIABLES GLOBALES
#--------------------

BASE = 660
ALTURA = 220
RADIO = 10
desplazamiento_x = 1
desplazamiento_y = 1
intervalo = 2
centro_x = random.randint(RADIO, BASE)
centro_y = random.randint(RADIO, ALTURA)

X=-500
Y=0

def mover_carro():
    global desplazamiento_x, desplazamiento_y

    x0, y0,= c.coords(carro_1)
    x1, y2,= c.coords(carro_2)
    if x0 < 0 or y0 > X: 
        desplazamiento_x = -desplazamiento_x
    if y0 < 0 or x0 > Y: 
        desplazamiento_y = -desplazamiento_y
        
    c.move(carro_1, desplazamiento_x, desplazamiento_y)
    c.move(carro_2, desplazamiento_x, desplazamiento_y)  
    
    
      
    ventana_principal.after(intervalo, mover_carro)




#--------------------
# VENTANA PRINCIPAL
#--------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("700x450")
ventana_principal.config(bg="black")

#----------------------
# Frame de graficacion
 #----------------------

frame_graficacion = Frame(ventana_principal)    
frame_graficacion.config(bg="white", width=680, height=240)
frame_graficacion.place(x=10, y=10)

 # creacion canvas 

c = Canvas(frame_graficacion, width=BASE-2, height=ALTURA)
c.config(bg="cyan4")
c.place(x=10, y=10)


carretera = c.create_rectangle(BASE/2-350,ALTURA/2+60,BASE/2+330,ALTURA/2-50, fill="bisque4")
linea_carretera = c.create_line(0,ALTURA/2-5,BASE,ALTURA/2-5, fill="yellow")
linea_carretera_2 = c.create_line(0,ALTURA/2,BASE,ALTURA/2, fill="yellow")
linea_inicial = c.create_line(BASE/2-250,ALTURA/2+60,BASE/2-250,ALTURA-160,width=20, fill="white")
linea_inicial = c.create_line(BASE/2-260,ALTURA/2+60,BASE/2-260,ALTURA-160,width=15, fill="black")



img_carro_1 = PhotoImage(file="img/png-transparent-luxury-car-sports-car-ford-mustang-lamborghini-ferrari-spa-cartoon-red-removebg-preview (3) (1).png")
carro_1 = c.create_image(BASE/2+250,ALTURA/2+30,image=img_carro_1)

img_carro_2 = PhotoImage(file="img/descarga__1_-removebg-preview.png")
carro_2 = c.create_image(BASE/2+250,ALTURA/2-20,image=img_carro_2)

boton = Button(ventana_principal, command=mover_carro)
boton.config(bg="white", fg="green",text = "arrancan",font=("Arial", 10),width=5)
boton.place(x=350, y=300)





ventana_principal.mainloop()