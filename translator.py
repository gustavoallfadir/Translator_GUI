from tkinter import *
from tkinter import scrolledtext, messagebox
from googletrans import Translator

font="'courier',10"

def menu_rclick(w):
    global the_menu
    the_menu = Menu(w, tearoff=0)
    the_menu.add_command(label="Cortar  ")
    the_menu.add_command(label="Copiar  ")
    the_menu.add_command(label="Pegar  ")
    

def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("Cortar  ",
    command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copiar  ",
    command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Pegar  ",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)


def traducir(x):
    ventana_traduccion()

    T = Translator()

    #numero_caracteres=len(caja_texto.get(1.0,END))
    #print(numero_caracteres)
    rangos= [(1.0, 150.0),(150.0,300.0),(300.0,450.0),(450.0,600.0),(600.0,750.0),(750.0,900.0),(900.0,1050.0),
        (1050.0,1200.0),(1200.0,1350.0),(1350.0,1500.0),(1500.0,1650.0),(1650.0,1800.0),(1800.0,1950.0),
        (1950.0,2100.0),(2100.0,2250.0),(2250.0,2400.0),(2400.0,2550.0),(2550.0,2700.0),(2700.0,2850.0),
        (2850.0,3000.0),(3000.0,3150.0),(3150.0,3300.0),(3300.0,3450.0),(3450.0,3600.0),(3600.0,3750.0),
        (3750.0,3900.0),(3900.0,4050.0),(4050.0,4200.0),(4200.0,4350.0),(4350.0,4500.0),(4500.0,4650.0),
        (4650.0,4800.0),(4800.0,4950.0),(4950.0,5100.0),(5100.0,5250.0),(5250.0,5400.0),(5400.0,5550.0)]

    for i in rangos:
        texto=caja_texto.get(i[0],i[1]) 
        traduccion=T.translate(texto,dest='es').text
        caja_texto2.insert(END,traduccion)



    sub.mainloop()


def main():
    global root 
    global caja_texto

    root=Tk()
    root.title('Traductor')
    root.geometry('600x600+200+80')
    root.minsize(200,200)
    
    caja_texto = scrolledtext.ScrolledText(root,width=5,height='2',font=font)
    caja_texto.config(selectforeground='white',selectbackground='navy',wrap=WORD)
    caja_texto.pack(fill='both',expand=True,padx=3,pady=3)
    caja_texto.bind("<Button-3><ButtonRelease-3>", show_menu)
    #caja_texto.bind('<Return>',traducir)

    boton_traducir= Button(root,text='Traducir',command=lambda:traducir(''),font=font)  
    boton_traducir.pack(pady=10)

    menu_rclick(root)

    root.mainloop()

def ventana_traduccion():
    global caja_texto2
    global sub

    sub=Tk()
    sub.title('Texto traducido')
    sub.geometry('600x600+700+80')
    sub.minsize(200,200)

    caja_texto2 = scrolledtext.ScrolledText(sub,width=5,height='2',font=font)
    caja_texto2.config(selectforeground='white',selectbackground='navy',wrap=WORD)
    caja_texto2.pack(fill='both',expand=True,padx=3,pady=3)
    caja_texto2.bind("<Button-3><ButtonRelease-3>", show_menu)

    




main()

