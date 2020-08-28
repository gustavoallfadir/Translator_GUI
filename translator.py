from tkinter import *
from tkinter import scrolledtext
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

    texto_a_traducir = caja_texto.get(1.0,END)
    
    texto_traducido = T.translate(texto_a_traducir, dest='es').text
    
    caja_texto2.insert(END,texto_traducido)

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
    sub.title('Textro traducido')
    sub.geometry('600x600+700+80')
    sub.minsize(200,200)

    caja_texto2 = scrolledtext.ScrolledText(sub,width=5,height='2',font=font)
    caja_texto2.config(selectforeground='white',selectbackground='navy',wrap=WORD)
    caja_texto2.pack(fill='both',expand=True,padx=3,pady=3)
    caja_texto2.bind("<Button-3><ButtonRelease-3>", show_menu)

    




main()

