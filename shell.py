import basic
import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import basic
from tkinter import *
from tkinter import messagebox as MessageBox

def validar_linea(text,cuadro_text):

	result, error = basic.run('<stdin>', text)
	if error:  MessageBox.showerror("Compilador",error.as_string()+"en la  linea")
	if result: cuadro_text.insert (END, result)

class Aplicacion:
    
    def __init__(self):
        self.ventana1=tk.Tk()
        self.agregar_menu()
        self.ventana1.title("Chawala compiler")
        self.ventana1.geometry("730x380")
        self.ventana1.resizable(0,0)
        self.ventana1.config(bg="#2e466d")
        self.scrolledtext1=st.ScrolledText(self.ventana1, width=50, height=20)
        self.scrolledtext2=st.ScrolledText(self.ventana1, width=30, height=20)
        
        self.scrolledtext1.config(bg="#1F304A",fg="white")
        self.scrolledtext2.config(state=DISABLED,bg="#1F304A",fg="white")
        
        self.scrolledtext1.grid(column=0,row=0, padx=20, pady=10)     
        self.scrolledtext2.grid(column=0,row=0, padx=20, pady=10,sticky=N+E)

        self.scrolledtext2.place(x=450,y=40)
        self.scrolledtext1.place(x=10,y=40)
        
        texto = Label(self.ventana1, text="Editor",font=("Helvetica", 12))
        texto.pack()
        texto.place(x=180,y=10)
        texto.config(relief="raised",bg="#6BA4FF")

        compilador = Label(self.ventana1, text="Compilador",font=("Helvetica", 12))
        compilador.pack()
        compilador.place(x=530,y=10)
        compilador.config(relief="raised",bg="#6BA4FF")
        self.nombrearch = ""
        
        self.ventana1.mainloop()
        

    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Guardar archivo", command=self.guardar)
        opciones1.add_command(label="Abrir archivo", command=self.cargar)
        opciones1.add_separator()
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)

        opciones2 = tk.Menu(menubar1, tearoff=0)
        opciones2.add_command(label="Compilar Programa", command=self.compilar)
        
        menubar1.add_cascade(label="Compilador", menu=opciones2)
            
    
    def salir(self):
        sys.exit()

    def guardar(self):
        self.nombrearch=fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("dan files",".dan"),("todos los archivos","*.*")))
        if self.nombrearch!='':
            archi1=open(self.nombrearch, "w", encoding="utf-8")
            archi1.write(self.scrolledtext1.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")

    def cargar(self):
        self.nombrearch=fd.askopenfilename(initialdir = "/",title = "Seleccione archivo",filetypes = (("dan files","*.dan"),("todos los archivos","*.*")))
        if self.nombrearch!='':
            archi1=open(self.nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END) 
            self.scrolledtext1.insert("1.0", contenido)

    def compilar(self):
        
        if self.nombrearch!='':

            ruta=self.nombrearch
            ruta=ruta.replace("C:/","/")
            archi1=open(ruta, "r")
            
            contenido=""
            self.scrolledtext2.config(state=NORMAL)
            
            for linea in archi1.readlines():
                if(linea !="\n"):
                    validar_linea(linea,self.scrolledtext2)
                    contenido=contenido+linea
                    self.scrolledtext2.insert(END,'\n')
            
            self.scrolledtext2.config(state=DISABLED)
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END) 
            self.scrolledtext1.insert("1.0", contenido)

aplicacion1=Aplicacion()