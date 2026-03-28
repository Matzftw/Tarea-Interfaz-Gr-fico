
"""Tarea 1 Progra Max Q.H"""

import tkinter as tk
import math as mt   #import super util (no hizo nada)
import pygame #Solo para audio
from PIL import Image, ImageTk #Solo para imagenes


def pares(num):
    if num == 0:
        return (0,0)
    elif isinstance(num,int) and num > 0 and num < 9999:
        return pares_aux(abs(num))
    else:
        return -1

def pares_aux(num):
    if num == 0:
        b = num // a
        if a <= b:
            return ({a}, {b})
    else:
        return -1

def abre_funcion():
    Ventana2 = tk.Toplevel(ventana)
    Ventana2.title("Funcion pares")
    Ventana2.geometry("600x600")
    Ventana2.configure(
        background= 'gray',
    )

    imagen2 = Image.open("Fondo int_num.jpg")     #Abre la imagen que se usará para fondo aqui
    imagen2 = imagen2.resize((600, 600))          #tamaño de la imagen
    img2 = ImageTk.PhotoImage(imagen2)
    label_img2 = tk.Label(Ventana2, image=img2)
    label_img2.pack()

    canvas_num = tk.Canvas(Ventana2, bg = 'black', width=500, height=500)
    canvas_num.place(x= 50, y= 50)

    numero = tk.Entry(canvas_num, width= 20)
    numero.place(x= 200, y= 240)

    entrada = numero.get()


    salida1 = tk.Label(canvas_num, text = 'pares_aux.get()', background= 'white' ,foreground= 'white', font = ('Times New Roman', 12))
    salida1.place(x= 200, y= 420)


    Ventana2.grab_set()
    Ventana2.resizable(width= False, height= False)
    
    
    Vuelve = tk.Button(Ventana2, text = 'Volver a la Ventana Principal', bg = 'Red', fg = 'White', command = lambda:Ventana2.destroy())
    Vuelve.place(x = 300, y= 400)

    Ventana2.mainloop()

def abre_animacion():
    Ventana3 = tk.Toplevel(ventana)
    Ventana3.title("Animacion esferas")
    Ventana3.geometry("600x600")
    Ventana3.configure(
        background= 'gray',
    ) 
    imagen3 = Image.open("galaxian-galaga-nintendo.jpg")     #Abre la imagen que se usará para fondo aqui
    imagen3 = imagen3.resize((600, 600))          #tamaño de la imagen
    img3 = ImageTk.PhotoImage(imagen3)
    label_img3 = tk.Label(Ventana3, image=img3)
    label_img3.pack()

    Ventana3.grab_set()
    Ventana3.resizable(width= False, height= False)
    canva_e = tk.Canvas(Ventana3, bg = 'black', width=500, height=500)
    canva_e.place(x= 50, y= 50)
    #canva_e.pack()
    bola = canva_e.create_oval(50, 50, 100, 100, fill='red')
    bola2 = canva_e.create_oval(350, 350, 400, 400, fill='blue')
    
    
    #img4 = imagen4 = Image.open("galaxian-galaga-nintendo.jpg")     #Abre la imagen que se usará para fondo de la animación
    #imagen3 = Image.open("Fondo_int_anima.jpg")     #Abre la imagen que se usará para fondo aqui
    #imagen4 = imagen4.resize((500, 500))                     #tamaño de la imagen
    #img4 = ImageTk.PhotoImage(imagen4)
    #label_img4 = tk.Label(canva_e, image=img4)
    #label_img4.pack()
    

    vx = 5
    vy = 5
    def mover_bola():
        global vx, vy
        x1, y1, x2, y2 = canva_e.coords(bola)
        if x1 <= 0 or x2 >= 500:
            vx = -vx
        if y1 <= 0 or y2 >= 500:
            vy = -vy
        canva_e.move(bola, vx, vy)

    origen = tk.Button(Ventana3, text = 'Volver a la Ventana Principal', bg = 'Red', fg = 'White', command = lambda:Ventana3.destroy())
    origen.place(x = 300, y= 550)
    Ventana3.mainloop()





ventana = tk.Tk()

ventana.title("Perfil")
ventana.geometry("600x600")
ventana.configure(
    background= 'gray',
)
imagen = Image.open("1534718_1028.jpg")     #Abre la imagen que se usará para fondo
imagen = imagen.resize((600, 600))          #tamaño de la imagen
img = ImageTk.PhotoImage(imagen)
label_img = tk.Label(ventana, image=img)
label_img.pack()


def cerrarVentana():                #Función que cierra la ventana principal
    print("cerrar esta ventana") 
    ventana.destroy()

ventana.resizable(width= False, height= False)

canva1 = tk.Canvas(ventana, bg = 'gray', width=300, height=300)
canva1.place(x= 125, y= 50)
#canva1.pack(side= 'top')

tk.Label(canva1, text = 'Max Andrés Quirós Hernández',background= 'gray' ,foreground= 'white', font = ('Times New Roman', 12)).place(x= 25, y= 15)
tk.Label(canva1, text = 'Edad: 18 años', background= 'gray' ,foreground= 'white', font = ('Times New Roman', 12)).place(x= 25, y= 40)
tk.Label(canva1, text = 'Carnet: 2026125772', background= 'gray' ,foreground= 'white', font = ('Times New Roman', 12)).place(x= 25, y= 65)
tk.Label(canva1, text = 'Biografía: Soy Max, nací en Moravia pero desde hace unos años vivo aquí, me gusta hacer atletismo y jugar Valorant aunque soy malísimo', width=300,justify='left',background= 'gray' ,foreground= 'white', font = ('Times New Roman', 12)).place(x= 25, y= 90)
#tk.Label(canva1, image = '', background= 'gray' ,foreground= 'white', font = ('Times New Roman', 12)).place(x= 25, y= 115)




botonM = tk.Button(ventana, text = 'Cerrar la Ventana', bg = 'Red', command = lambda:cerrarVentana())
botonM.place(x = 300, y= 400)

#boton1 = tk.Button(canva1, text = 'Perfil', bg = 'purple', command = lambda:Nombre())
#boton1.place(x= 50, y= 100)

boton2 = tk.Button(ventana, text = 'Funcion Pares', bg = 'lime', command = lambda:abre_funcion())
boton2.place(x= 50, y= 400)

boton3 = tk.Button(ventana, text = 'Animacion Esferas', bg = 'cyan', command = lambda:abre_animacion())
boton3.place(x= 165, y= 400)


ventana.mainloop()