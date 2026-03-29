"""Tarea 1 Progra Max Q.H"""

import tkinter as tk
import math as mt   #import super util (no hizo nada)
import pygame #Solo para audio
from PIL import Image, ImageTk #Solo para imagenes


def pares(num, salida1=None):
    if num == 0:
        return (0,0)
    elif isinstance(num,int) and num > 0 and num < 9999:
        return pares_aux(abs(num), salida1=salida1)
    else:
        return -1

def pares_aux(num, a=2, Z=(), salida1=None):      #Funcion recursiva (con ayuda de chatgpt) Se excluye el resultado obvio del numero *1 
    if a * a> num:           #a es el divisor que va probando, Z es el resultado que va almacenando cada que se repite el ciclo
        return Z
    if num % a == 0:
        result = (Z+ (a, num//a))
        salida1.insert(tk.END,str(result)+"\n")     
        pares_aux(num // a, a, Z + (a,), salida1)
    
    pares_aux(num, a + 1, Z, salida1)
#print(pares())

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
    
    def calcule():
        salida1.delete("1.0", tk.END)
        
        n = int(entrada.get())      #Sin este int el sistema tira error porque lo lee como un str 
        if n > 1:                   #aquí 
            pares(n, salida1 = salida1)

    canvas_num = tk.Canvas(Ventana2, bg = 'black', width=500, height=500)
    canvas_num.place(x= 50, y= 50)

    #numero = tk.Entry(canvas_num, width= 20)
    #numero.place(x= 200, y= 240)

    entrada = tk.Entry(canvas_num, width= 20)
    entrada.place(x= 200, y= 240)

    Calcular = tk.Button(canvas_num, text = 'Calcular', bg = 'Green', fg = 'White', command = lambda:calcule())
    Calcular.place(x = 200, y= 300)

    salida1 = tk.Text(canvas_num)
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

    
    Ventana3.resizable(width= False, height= False)
    canva_e = tk.Canvas(Ventana3, bg = 'black', width=500, height=500)
    canva_e.place(x= 50, y= 50)
    #canva_e.pack()
    #bola1
    x1 = 50
    y1 = 50
    x2 = 100
    y2 = 100
    dx1 = 4
    dy1 = 4
    #bola2
    x3 = 350
    y3 =  350
    x4 = 400
    y4 = 400
    dx2 = -4
    dy2 = -4

    bola = canva_e.create_oval(x1, y1, x2, y2, fill='red')
    bola2 = canva_e.create_oval(x3, y3, x4, y4, fill='blue')
    
    

    def mover():
        canva_e.move(bola, dx1, dy1)
        canva_e.move(bola2, dx2, dy2)
        canva_e.after(50, mover)
        colision()

    def colision():
        hit1 = canva_e.coords(bola)
        hit2 = canva_e.coords(bola2)
    

        if (hit1[0] < hit2[2] and hit1[2] > hit2[0] and hit1[1] < hit2[3] and hit1[3] > hit2[1]): 
            print ("Colision detectada")
            canva_e.move(bola, dx1,dy1)
            canva_e.move(bola2, dx2,dy2)
            
            
        if (hit1[0] <= 0 or hit1[2] >= 500):
            canva_e.move(bola, dx1,0)
            canva_e.move(bola2, dx2,0)
            
        if (hit1[1] <= 0 or hit1[3] >= 500):
            canva_e.move(bola, 0,-dy1)
            canva_e.move(bola2, 0,-dy2)
            
        if (hit2[0] <= 0 or hit2[2] >= 500):
            canva_e.move(bola2, -dx2,0)
            canva_e.move(bola, -dx1,0)
            
        if (hit2[1] <= 0 or hit2[3] >= 500):
            canva_e.move(bola2, 0,-dy2)
            canva_e.move(bola, 0,-dy1)
            
        
    if colision():
        if abs(x1-x2)<10 or abs(x1-(x2))<10:
            dx1 *= -1
            dx2 *= -1
        if abs(y1-y2) <10 or abs(y1-y2) <10:
            dy1 *= -1
            dy2 *= -1


    #    dx1, dx2 = dx2, dx1
    #    dy1, dy2 = dy2, dy1
        #dx3, dx4 = dx4, dx3
        #dy3, dy4 = dy4, dy3
        
    #    x1 += dx1
    #   y1 += dy1
    #    x2 += dx1
    #    y2 += dy1
        
    


    
    mover()
    
    


    #def colision():
        
    #colision()
    
    Ventana3.grab_set()

    
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
ventana.geometry("700x700")
ventana.configure(
    background= 'gray',
)
imagen = Image.open("1534718_1028.jpg")     #Abre la imagen que se usará para fondo
imagen = imagen.resize((700, 700))          #tamaño de la imagen
img = ImageTk.PhotoImage(imagen)
label_img = tk.Label(ventana, image=img)
label_img.pack()


def cerrarVentana():                #Función que cierra la ventana principal
    print("cerrar esta ventana") 
    ventana.destroy()

ventana.resizable(width= False, height= False)

canva1 = tk.Canvas(ventana, bg = 'black', width=300, height=600)
canva1.place(x= 125, y= 50)


tk.Label(canva1, text = 'Max Andrés Quirós Hernández',background= 'black' ,foreground= 'white', font = ('Times New Roman', 12)).place(x= 25, y= 15)
tk.Label(canva1, text = 'Edad: 18 años', background= 'black' ,foreground= 'white', font = ('Times New Roman', 12)).place(x= 25, y= 40)   
tk.Label(canva1, text = 'Carnet: 2026125772', background= 'black' ,foreground= 'white', font = ('Times New Roman', 12)).place(x= 25, y= 65)  #carnet estudiantil

biografia = "Soy Max, nací en Moravia pero desde hace unos años vivo aquí, me gusta hacer atletismo y jugar Valorant aunque soy malísimo"   #Se crea la variable que tenga la biografía
canva1.create_text(25, 90, text=biografia, fill='white', font=('Times New Roman', 12), anchor='nw', width=250)  #parametros de la bio 
#foto = Image.open("Foto.png") 
#canva1.image = ImageTk.PhotoImage(foto)
#canva1.create_image(25, 50, image=canva1.image, anchor='nw')

    #Abre la imagen que se usará para el perfil

grupo = "Aerosmith"
canva1.create_text(25, 500, text=grupo, fill='white', font=('Times New Roman', 12), anchor='nw', width=250)  #parametros del grupo musical favorito
aero = Image.open("Grupo.png")
canva1.aero = ImageTk.PhotoImage(aero)
canva1.create_image(25, 650, image=canva1.aero, anchor='sw')

botonM = tk.Button(ventana, text = 'Cerrar la Ventana', bg = 'Red', command = lambda:cerrarVentana())
botonM.place(x = 300, y= 650)

#boton1 = tk.Button(canva1, text = 'Perfil', bg = 'purple', command = lambda:Nombre())
#boton1.place(x= 50, y= 100)

boton2 = tk.Button(ventana, text = 'Funcion Pares', bg = 'lime', command = lambda:abre_funcion())
boton2.place(x= 50, y= 650)

boton3 = tk.Button(ventana, text = 'Animacion Esferas', bg = 'cyan', command = lambda:abre_animacion())
boton3.place(x= 165, y= 650)


ventana.mainloop()