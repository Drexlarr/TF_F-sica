from tkinter.ttk import *
from random import randint
import time
import math
from tkinter import *
from PIL import ImageTk, Image

densidad = 0
diametro = 0
velocidad = 0
viscocidad = 0
imagen = ''
tipo  = ''
nreynolds = 0
Objeto = True


def Interfaz():
    window = Tk()
    window.title("Numero de Reynolds")
    window.geometry('580x200')

    def main1():
        lbl.place_forget()
        lbl1.place(x=130,y= 30)
        lbl2.place(x=130,y= 50)
        lbl3.place(x=130,y= 70)
        lbl4.place(x=130,y= 90)
        d.place(x=310,y= 30)
        D.place(x=310,y= 50)
        v.place(x=310,y= 70)
        V.place(x=310,y= 90)
        btn.place(x=250,y=130)
        btn1.place_forget()
        btn2.place_forget()

    def main2():
        lbl.place_forget()
        lbl1.place(x=60,y= 30)
        lbl2.place(x=60,y= 50)
        lbl3.place(x=60,y= 70)
        lbl4.place(x=60,y= 90)
        d.place(x=310,y= 30)
        D.place(x=310,y= 50)
        v.place(x=310,y= 70)
        V.place(x=310,y= 90)
        Objeto = True
        lbl2.configure(text = "Longitud del objeto: ")
        btn.place(x=250,y=130)
        btn1.place_forget()
        btn2.place_forget()
    def Main2():
        main2()

    def main3():
        den = int(d.get())
        dim = int(D.get())
        vel = int(v.get())
        vis = int(V.get())
        t1 = False
        t2 = False
        l1 = False
        l2 = False
        r1 = False
        r2 = False
        n = (den*dim*vel)/vis
        lbl5.place(x=50,y= 30)
        lbl6.place(x=350,y= 30)
        lbl5.configure(text = "Número de Reynolds: " + str(n))
        if n > 3000:
            tipo ="Turbulento"
            if Objeto:
                t1 = True
            else:
                t2 = True
        elif n < 2000:
            tipo ="Laminar"
            if Objeto:
                l1 = True
            else:
                l2 = True
            
        elif n > 3000 and n < 200:
            tipo ="Real"
            if Objeto:
                r1 = True
            else:
                r2 = True

        lbl6.configure(text = "El Fluído es: " + tipo)
        lbl1.place_forget()
        lbl2.place_forget()
        lbl3.place_forget()
        lbl4.place_forget()
        d.place_forget()
        D.place_forget()
        V.place_forget()
        v.place_forget()
        btn.place_forget()
        if t1:
            f2 = Label(window, image = im1).place(x=60,y= 50)
        if t2:
            f2 = Label(window, image = im2).place(x=60,y= 50)
        if l1:
            f2 = Label(window, image = im3).place(x=60,y= 50)
        if l2:
            f2 = Label(window, image = im4).place(x=60,y= 50)
        if r1:
            f2 = Label(window, image = im5).place(x=60,y= 50)
        if r2:
            f2 = Label(window, image = im6).place(x=60,y= 50)
        
        

    def Main():
        main3()

    

    lbl = Label(window, text="Elija si quiere simular un objeto en la tubería o solo el fluído", font='Helvetica 15 bold', fg = "orange")
    lbl.place(x=0,y= 10)
    lbl1 = Label(window, text="Densidad: ", font='Helvetica 12 bold', fg = "orange")
    lbl2 = Label(window, text="Diametro de la tubería: ", font='Helvetica 12 bold', fg = "orange")  
    lbl3 = Label(window, text="Velocidad: ", font='Helvetica 12 bold', fg = "orange")
    lbl4 = Label(window, text="Viscocidad: ", font='Helvetica 12 bold', fg = "orange")
    lbl5 = Label(window, text="", font='Helvetica 12 bold', fg = "orange")
    lbl6 = Label(window, text="", font='Helvetica 12 bold', fg = "orange")
    var = StringVar(window)
    var.set("0")
    var1 = StringVar(window)
    var1.set("0")
    var2 = StringVar(window)
    var2.set("0")
    var3 = StringVar(window)
    var3.set("0")
    d = Spinbox(window,from_=-10000000000, to=100000000000, textvariable=var)
    D = Spinbox(window,from_=-10000000000, to=100000000000, textvariable=var1) 
    v = Spinbox(window,from_=-10000000000, to=100000000000, textvariable=var2)
    V = Spinbox(window,from_=-10000000000, to=100000000000, textvariable=var3)
    im1 = ImageTk.PhotoImage(file="Turbulento.png")
    im2 = ImageTk.PhotoImage(file="TurbulentoObjeto.png")
    im3 = ImageTk.PhotoImage(file="Laminar.png")
    im4 = ImageTk.PhotoImage(file="LaminarObjeto.png")
    im5 = ImageTk.PhotoImage(file="Real.png")
    im6 = ImageTk.PhotoImage(file="RealObjeto.png")
    
    btn = Button(window, text="Calcular", bg="orange", fg="white", font =(20), command=Main)
    btn1 = Button(window, text="Fluido", bg="orange", fg="white", font =(20), command=main1)
    btn2 = Button(window, text="Objeto", bg="orange", fg="white", font =(20), command=Main2)
    btn1.place(x= 150, y = 80)
    btn2.place(x= 330, y = 80)
    #btn.grid(column = 0, row = 5)
    window.mainloop()
    print(Objeto)

Interfaz()
